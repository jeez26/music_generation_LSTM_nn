import {MusicPlayer} from "../components/music_player";
import {FontAwesomeIcon} from "@fortawesome/react-fontawesome";
import {Button, Col, Form, Row} from "react-bootstrap";
import * as React from "react";
import {useState} from "react";

export const GenerateMusic = () => {
    const [audio, setAudio] = useState(null);
    const [count_notes, setCountNotes] = useState(10);
    const [type, setType] = useState('classic_piano');

    return <div className={'d-flex justify-content-center align-items-center'}
                style={{height: 'calc(100vh - 100px)'}}>
        {!audio ? <React.Fragment>
                <div>
                    <Row>
                        <Col md={6}>
                            <Form.Label>Количество нот</Form.Label>
                            <Form.Control type={'number'} min={10} max={500}
                                          value={count_notes}
                                          onChange={(e) => {
                                              setCountNotes(e.target.value)
                                          }}/>
                        </Col>
                        <Col md={6}>
                            <Form.Label>Тип музыки</Form.Label>
                            <Form.Select
                                value={type}
                                onChange={(e) => {
                                    setType(e.target.value)
                                }}>
                                <option value={'classic_piano'}>Классическое Пианино</option>
                                <option value={'electro_piano'}>Электро Пианино</option>
                                <option value={'guitar'}>Гитара</option>
                                <option value={'super_game_boy'}>SuperGameBoy</option>
                            </Form.Select>
                        </Col>
                        <Button className={'d-block mt-3 main-button display-4 ps-5 pe-5'} onClick={() => {
                            if (!audio) {
                                setAudio(new Audio(
                                    `http://localhost:4000/generate_music?notes_count=${count_notes}&music_type=${type}`));
                            }
                        }}>Сгенерировать</Button>
                    </Row>
                </div>
                <div>
                </div>
            </React.Fragment>
            : null}
        <div>
            {audio ?
                <div>
                    {audio[0]}
                    <Button className={'play_button'} onClick={() => {
                        if (audio) {
                            audio.play()
                        }
                    }}>
                        <FontAwesomeIcon icon={'play'}/>
                    </Button>
                </div>
                : null}
        </div>
    </div>
}