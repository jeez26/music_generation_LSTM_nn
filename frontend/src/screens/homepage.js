import * as React from "react";
import {Button, Col, Row} from "react-bootstrap";
import {Link} from "react-router-dom";

export const Homepage = () => {
    return <React.Fragment>
        <Row>
            <Col style={{marginTop: '10rem'}}>
                <div className={'h1 display-1'}>
                    <div className={'main-title'}>
                        AI MUSIC
                    </div>
                    <div>
                        GENERATOR
                    </div>
                </div>
                <div className={'h4'} style={{fontWeight: 300}}>
                    <p>
                        Welcome to our site where the magic of music comes to life! We present you with a unique
                        opportunity
                        to immerse yourself in the world of endless musical possibilities with our innovative music
                        generator.
                    </p>
                    <p>
                        Our music generator is a powerful tool built with advanced technology and artificial
                        intelligence
                        that allows you to create your own music with just a few clicks. You no longer need musical
                        knowledge or experience to become a composer. Our generator will automatically create unique
                        music
                        compositions based on your preferences and mood.
                    </p>
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