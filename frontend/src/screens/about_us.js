import * as React from 'react';
import {YMaps, Map} from '@pbe/react-yandex-maps';
import {Col, Row} from "react-bootstrap";

import logo from "../assets/img/logo.png"

export const AboutUs = () => {
    return <React.Fragment>
        <YMaps>
            <Row>
                <Col style={{marginTop: '12rem'}}>
                    <div className={'h1 display-1'}>
                        <div className={'main-title'}>
                            AI MUSIC
                        </div>
                    </div>
                    <div className={'h4'} style={{fontWeight: 300}}>
                        AI Music is a project developed by students of Peter the Great St. Petersburg Polytechnic
                        University (SPbPU) as part of the Deep Learning discipline in 2023. This project is not
                        commercial and is a pure demonstration of the work of the implemented neural network.
                    </div>
                    <div className="text-center">
                        <img src={logo}/>
                    </div>
                </Col>
                <Col className={'d-flex justify-content-center align-items-center'} style={{marginTop: '12rem'}}>
                    <Map height={400} width={400}
                         defaultState={{center: [60.00558571505473, 30.374185880429247], zoom: 14}}/>
                </Col>
            </Row>
        </YMaps>
    </React.Fragment>
}