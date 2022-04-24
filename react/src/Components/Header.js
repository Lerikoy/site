import { Button } from 'react-bootstrap'
import React, { Component, useState} from 'react'
import {
    Container,
    Form,
    FormControl,
    Nav,
    Navbar,
    Modal
} from 'react-bootstrap'
import logo from './logo192.svg'
import {
    BrowserRouter as Router,
    Route,
    Routes,
    Link
} from 'react-router-dom';

import Home from '../Pages/Home'
import Blog from '../Pages/Blog'
import Agences_tours from '../Pages/Agences_tours'
import My_map from '../Pages/My_map'



export default function Navibar() {

        const[show, setShow] = useState(false);

        const handleClose = () => setShow(false);
        const handleShow = () => setShow(true);


        const[show_register, setShow_register] = useState(false);
        
        const handleClose_register = () => setShow_register(false);
        const handleShow_register = () => setShow_register(true); 

        return (
            <>
                <Navbar className='navbar' sticky='top' collapseOnSelect expand="lg" variant="light" bg="none">
                    <Container>
                        <Navbar.Brand href="/">
                            <img
                                src={logo}
                                height="40"
                                width="40"
                                className="d-inline-block align-top"
                                alt="Logo" />
                        </Navbar.Brand>
                        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
                        <Navbar.Collapse id="responsive-navbar-nav">
                            <Nav className="me-auto">
                                <Nav.Link href="/" active> Главная </Nav.Link>
                                <Nav.Link href="/blog"> Блог </Nav.Link>
                                <Nav.Link href="/agencies_tours"> Туры и агенства </Nav.Link>
                                <Nav.Link href="/my_map"> Карта </Nav.Link>
                            </Nav>
                            
                            <Button className='register ms-0 me-2 rounded-pill'  variant="outline-primary" onClick={handleShow}>Вход</Button>
                            <Button className='login ms-0 rounded-pill' onClick={handleShow_register}>Регистрация</Button>
                            
                        </Navbar.Collapse>
                    </Container>
                </Navbar>

                <Modal show={show} onHide={handleClose}>
                    <Modal.Header closeButton>
                        <Modal.Title>Вход</Modal.Title>
                    </Modal.Header>
                    <Modal.Body>
                            <Form>
                                <Form.Group controlId="formBasicEmail">
                                    <Form.Label className="text-muted">Адрес электронной почты</Form.Label>
                                    <Form.Control type="email" placeholder="@"/>
                                </Form.Group>

                                <Form.Group controlId="formBasicPassword">
                                    <Form.Label className="text-muted">Пароль</Form.Label>
                                    <Form.Control type="password" placeholder=""/>
                                </Form.Group>

                                <Form.Group>
                                    <Form.Check type="checkbox" label="Запомнить меня" />
                                </Form.Group>
                            </Form>
                    </Modal.Body>
                    <Modal.Footer>
                        <Button variant="secondary" onClick={handleClose}>
                            Close
                        </Button>
                        <Button variant="primary" onClick={handleClose}> 
                        {/* поменять здесь ссылку для авторизации */}
                            Войти
                        </Button>
                    </Modal.Footer>
                </Modal>

                <Modal show={show_register} onHide={handleClose_register}>
                    <Modal.Header closeButton>
                        <Modal.Title>Регистрация</Modal.Title>
                    </Modal.Header>
                    <Modal.Body>
                            <Form>
                                <Form.Group controlId="formBasicEmail">
                                    <Form.Label className="text-muted">Адрес электронной почты</Form.Label>
                                    <Form.Control type="email" placeholder="@"/>
                                </Form.Group>

                                <Form.Group controlId="formBasicPassword">
                                    <Form.Label className="text-muted">Пароль</Form.Label>
                                    <Form.Control type="password" placeholder=""/>
                                </Form.Group>

                                <Form.Group>
                                    <Form.Check type="checkbox" label="Запомнить меня" />
                                </Form.Group>
                            </Form>
                    </Modal.Body>
                    <Modal.Footer>
                        <Button variant="secondary" onClick={handleClose_register}>
                            Close
                        </Button>
                        <Button variant="primary" onClick={handleClose_register}> 
                        {/* поменять здесь ссылку для авторизации */}
                            Войти
                        </Button>
                    </Modal.Footer>
                </Modal>

                {/* <Navbar >
                <Form className='d-flex'>
                                <FormControl
                                    type="text"
                                    placeholder="Search"
                                    className="d-inline mx-2" />
                                <Button variant="outline-info">Search</Button>
                            </Form>
                </Navbar> */}

                <Router>
                    <Routes>
                        <Route path='/' element={<Home />} />
                        <Route path='/blog' element={<Blog />} />
                        <Route path='/agencies_tours' element={<Agences_tours />} />
                        <Route path='/my_map' element={<My_map />} />

                    </Routes>
                </Router>
            </>
        )
    
}

