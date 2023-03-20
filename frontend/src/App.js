import * as React from 'react';
import './utils/fontawesome';

import SiteRoutes from "./utils/routes/routes";
import {CookiesProvider} from "react-cookie";


export const App = () => {
    return (
        <CookiesProvider>
            <SiteRoutes/>
        </CookiesProvider>)
}

export default App;




