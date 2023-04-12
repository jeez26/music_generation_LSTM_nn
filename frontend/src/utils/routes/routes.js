import {BrowserRouter, Route, Routes} from "react-router-dom";
import * as React from "react";
import {Homepage} from "../../screens/homepage";
import {BaseLayout} from "../../components/base";
import {GenerateMusic} from "../../screens/generate";
import {AboutUs} from "../../screens/about_us";

const SiteRoutes = () => {

    return (
        <React.Fragment>
            <BrowserRouter>
                <Routes>
                    <Route path="/" element={<BaseLayout><Homepage/></BaseLayout>}/>
                    <Route path="/generate" element={<BaseLayout><GenerateMusic/></BaseLayout>}/>
                    <Route path="/about-us" element={<BaseLayout><AboutUs/></BaseLayout>}/>
                </Routes>
            </BrowserRouter>
        </React.Fragment>
    );
}

export default SiteRoutes;