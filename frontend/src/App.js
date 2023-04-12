import * as React from 'react';
import './utils/fontawesome';

import SiteRoutes from "./utils/routes/routes";
import {CookiesProvider} from "react-cookie";

import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap';
import "./assets/css/styles.css"


export const App = () => {
    return (
        <CookiesProvider>
            <div id={'background'}>
                <div id={'background_image'}/>
            </div>
            <SiteRoutes/>
        </CookiesProvider>)
}

export default App;




