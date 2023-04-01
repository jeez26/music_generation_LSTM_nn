import * as React from "react";
import {Button, Col, Row} from "react-bootstrap";
import {Link} from "react-router-dom";

export const Homepage = () => {
    return <React.Fragment>
        <Row>
            <Col style={{marginTop: '12rem'}}>
                <div className={'h1 display-1'}>
                    <div className={'main-title'}>
                        AI MUSIC
                    </div>
                    <div>
                        GENERATOR
                    </div>
                </div>
                <div className={'h4'} style={{fontWeight: 300}}>
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse pulvinar neque non lacus
                    vehicula ornare eu ac lorem. Integer eget tempor enim, sed malesuada felis. Praesent eu auctor elit,
                    eget scelerisque dolor. Vestibulum sodales ipsum in odio fringilla, ac viverra elit porta.
                </div>
            </Col>
            <Col className={'d-flex justify-content-center align-items-center'} style={{marginTop: '12rem'}}>
                <Link to={'/generate'}>
                    <Button className={'main-button display-4 ps-5 pe-5'}>
                        GENERATE
                    </Button>
                </Link>
            </Col>
        </Row>
    </React.Fragment>
}