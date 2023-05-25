import React, {useEffect, useState} from "react";
import ReactDOM from "react-dom";
import King_live from "./components/Card";
import '../src/styles/main.css'
import Card from "./components/Card";
import Cards from "./components/Cards";
import {
    BrowserRouter as Router,
    Switch,
    Route,
    Link, Routes
} from "react-router-dom";
import Models from "./components/Models";
import Model_detail from "./components/Model_detail";
import Kings from "./components/Kings";
import King_detail from "./components/King_detail";
// {
//     "id": 1,
//     "description": "Ваше королевство столкнулось с наводнением.",
//     "option": "Выделить деньги на восстановление инфраструктуры.",
//     "option_effect": {
//     "money": -8000,
//         "popularity": 5,
//         "army": 0,
//         "land": 0
// }
// },
function App() {
   return (
       <Router>
           <div>
               <Routes>
                   <Route path="/" element={<Cards />} />
                   <Route path="/models" element={<Models />} />
                   <Route path="/models_detail/:id" element={<Model_detail />} />
                   <Route path="/kings" element={<Kings />} />
                   <Route path="/kings_detail/:id" element={<King_detail />} />
               </Routes>
           </div>
       </Router>
   );
}

export default App;
