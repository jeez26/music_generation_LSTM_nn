import useSound from "use-sound";
import boopSfx from '../screens/music.mp3';
import {useEffect, useState} from "react";

export const MusicPlayer = () => {
    const [is_playing, setPlaying] = useState(false);
    const [currTime, setCurrTime] = useState({
        min: "",
        sec: "",
    });
    const [seconds, setSeconds] = useState();

    const [play, {pause, duration, sound}] = useSound(boopSfx);

    useEffect(() => {
        const sec = duration / 1000;
        const min = Math.floor(sec / 60);
        const secRemain = Math.floor(sec % 60);
        const time = {
            min: min,
            sec: secRemain
        };
        console.log(time);
    }, [currTime, duration])

    useEffect(() => {
        const interval = setInterval(() => {
            if (sound) {
                setSeconds(sound.seek([]));
                const min = Math.floor(sound.seek([]) / 60);
                const sec = Math.floor(sound.seek([]) % 60);
                setCurrTime({
                    min,
                    sec,
                });
            }
        }, 1000);
        return () => clearInterval(interval);
    }, [sound]);

    const playingButton = () => {
        if (is_playing) {
            pause(); // this will pause the audio
            setPlaying(false);
        } else {
            play(); // this will play the audio
            setPlaying(true);
        }
    };

    return <div>
        <button onClick={() => playingButton()}>{is_playing ? 'pause' : 'play'}</button>
    </div>;
}