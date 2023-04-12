import {Container, Nav, Navbar} from "react-bootstrap";
import {Link} from "react-router-dom";

export const Header = () => {
    return <Navbar bg="dark" variant="dark" expand="md" style={{color: 'white'}} className={"pt-2 pb-2 ps-4 pe-4"}>
        <Container fluid>
            <Link to={'/'}>
                <div className={'h3'} style={{margin: 0, fontWeight: 'bolder'}}>AiMusic</div>
            </Link>
            <Nav className="ml-auto" variant={"dark"}>
                <Link to={'/about-us'} role={'button'} className={'nav-item me-3'}>
                    About Us
                </Link>
                <Link to={'/generate'} role={'button'} className={'nav-item me-5'}>
                    Generate
                </Link>
            </Nav>
        </Container>
    </Navbar>
}