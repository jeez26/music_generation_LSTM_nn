from backend.core.config.app_config import AppConfig
from backend.request_models.generate_music_request import GenerateMusicRequest, MusicType

import os
import pickle
import numpy
import uuid

from fastapi.responses import FileResponse
from music21 import instrument, note, stream, chord
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.layers import BatchNormalization as BatchNorm
from keras.layers import Activation
from midi2audio import FluidSynth


class LSTMMusicGeneratorService:

    def __init__(
        self,
        config: AppConfig,
    ):
        self.config = config

    def generate_music(self, request_data: GenerateMusicRequest) -> FileResponse:
        music_file_response = self._generate_music_by_type(
            music_type=request_data.music_type,
            notes_count=request_data.notes_count,
        )
        return FileResponse(
            path=music_file_response,
            filename=music_file_response,
        )

    def _generate_music_by_type(self, music_type: str, notes_count: int) -> str:
        """
        Generate a piano midi file
        Return path to generated file
        """

        # load the notes used to train the model
        with open(self.config.notes_path, 'rb') as filepath:
            notes = pickle.load(filepath)

        # Get all pitch names
        pitchnames = sorted(set(item for item in notes))

        # Get all pitch names
        n_vocab = len(set(notes))

        network_input, normalized_input = self._prepare_sequences(notes, pitchnames, n_vocab)
        model = self._create_network(normalized_input, n_vocab)
        prediction_output = self._generate_notes(model, network_input, pitchnames, n_vocab, notes_count)
        return self._create_midi(prediction_output, music_type=music_type)

    def _prepare_sequences(self, notes, pitchnames, n_vocab) -> tuple:
        """ Prepare the sequences used by the Neural Network """
        # map between notes and integers and back
        note_to_int = dict((note, number) for number, note in enumerate(pitchnames))

        sequence_length = 100
        network_input = []
        output = []
        for i in range(0, len(notes) - sequence_length, 1):
            sequence_in = notes[i:i + sequence_length]
            sequence_out = notes[i + sequence_length]
            network_input.append([note_to_int[char] for char in sequence_in])
            output.append(note_to_int[sequence_out])

        n_patterns = len(network_input)

        # reshape the input into a format compatible with LSTM layers
        normalized_input = numpy.reshape(network_input, (n_patterns, sequence_length, 1))
        # normalize input
        normalized_input = normalized_input / float(n_vocab)

        return network_input, normalized_input

    def _create_network(self, network_input, n_vocab):
        """ create the structure of the neural network """
        model = Sequential()
        model.add(LSTM(
            512,
            input_shape=(network_input.shape[1], network_input.shape[2]),
            recurrent_dropout=0.3,
            return_sequences=True
        ))
        model.add(LSTM(512, return_sequences=True, recurrent_dropout=0.3, ))
        model.add(LSTM(512))
        model.add(BatchNorm())
        model.add(Dropout(0.3))
        model.add(Dense(256))
        model.add(Activation('relu'))
        model.add(BatchNorm())
        model.add(Dropout(0.3))
        model.add(Dense(n_vocab))
        model.add(Activation('softmax'))
        model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

        # Load the weights to each node
        model.load_weights(self.config.weights_path)

        return model

    def _generate_notes(self, model, network_input, pitchnames, n_vocab, notes_count: int):
        """
        Generate notes from the neural network based on a sequence of notes
        """

        # pick a random sequence from the input as a starting point for the prediction
        start = numpy.random.randint(0, len(network_input) - 1)

        int_to_note = dict((number, note) for number, note in enumerate(pitchnames))

        pattern = network_input[start]
        prediction_output = []

        # generate notes
        for note_index in range(notes_count):
            print(f'| STEP {note_index}/{notes_count} |')
            prediction_input = numpy.reshape(pattern, (1, len(pattern), 1))
            prediction_input = prediction_input / float(n_vocab)

            prediction = model.predict(prediction_input, verbose=0)

            index = numpy.argmax(prediction)
            result = int_to_note[index]
            prediction_output.append(result)

            pattern.append(index)
            pattern = pattern[1:len(pattern)]

        return prediction_output

    def _create_midi(self, prediction_output, music_type: str) -> str:
        """
        convert the output from the prediction to notes and create a midi file
        from the notes
        """
        offset = 0
        output_notes = []

        # create note and chord objects based on the values generated by the model
        for pattern in prediction_output:
            # pattern is a chord
            if ('.' in pattern) or pattern.isdigit():
                notes_in_chord = pattern.split('.')
                notes = []
                for current_note in notes_in_chord:
                    new_note = note.Note(int(current_note))
                    new_note.storedInstrument = instrument.Piano()
                    notes.append(new_note)
                new_chord = chord.Chord(notes)
                new_chord.offset = offset
                output_notes.append(new_chord)
            # pattern is a note
            else:
                new_note = note.Note(pattern)
                new_note.offset = offset
                new_note.storedInstrument = instrument.Piano()
                output_notes.append(new_note)

            # increase offset each iteration so that notes do not stack
            offset += 0.5

        midi_stream = stream.Stream(output_notes)
        unique_name = f'result_{uuid.uuid4()}'
        midi_stream.write('midi', fp=f'{self.config.results_file_path}/{unique_name}.mid')

        FluidSynth(
            sound_font=self._get_sound_font_path_by_type(music_type=music_type)
        ).midi_to_audio(
            f'{self.config.results_file_path}/{unique_name}.mid',
            f'{self.config.results_file_path}/{unique_name}.wav'
        )

        return f'{self.config.results_file_path}/{unique_name}.wav'

    def _get_sound_font_path_by_type(self, music_type: str) -> str:
        match music_type:
            case MusicType.GUITAR:
                return os.path.abspath('fluidsynth/guitar_sound_font.sf2')
            case MusicType.ELECTRO_PIANO:
                return os.path.abspath('fluidsynth/electro_piano_sound_font.sf2')
            case MusicType.CLASSIC_PIANO:
                return os.path.abspath('fluidsynth/classic_piano_sound_font.sf2')
            case MusicType.SUPER_GAME_BOY:
                return os.path.abspath('fluidsynth/super_game_boy_sound_font.sf2')
            case _:
                raise ValueError
