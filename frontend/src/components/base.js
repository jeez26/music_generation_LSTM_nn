import {Header} from './header';
import * as React from "react";
import {Container} from "react-bootstrap";

export function BaseLayout({children}) {
    return (
        <React.Fragment>
            <Header/>
            <main className={"py-2 ps-4 pe-4"}>
                <Container fluid>
                    {children}
                </Container>
            </main>
        </React.Fragment>
    )
}
