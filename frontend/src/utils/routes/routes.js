import {BrowserRouter, Route, Routes} from "react-router-dom";
import * as React from "react";
import {Homepage} from "../../screens/homepage";

const SiteRoutes = () => {

    return (
        <React.Fragment>
            <BrowserRouter>
                <Routes>
                    <Route path="/" element={<Homepage/>}/>
                </Routes>
            </BrowserRouter>
        </React.Fragment>
    );
}

export default SiteRoutes;