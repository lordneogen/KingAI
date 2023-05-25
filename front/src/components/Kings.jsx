import React, {useEffect, useState} from 'react';
import Model from "./Model";
import King from "./King";
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
const Kings = (props) => {

    const [kings,setKings] = useState([])

    const [money, setMoney] = useState(7500);
    const [popularity, setPopularity] = useState(7500);
    const [army, setArmy] = useState(7500);
    const [land, setLand] = useState(7500);
    const [epo, setEpo] = useState(1000);
    const [models, setModels] = useState(0);
    useEffect(() => {
        fetch('http://127.0.0.1:8000/kings/')  // Замените URL на ваш эндпоинт Django
            .then(response => response.json())
            .then(data => setKings(data))
            .catch(error => console.log(error));
    }, []);


    const handleSubmit = (e) => {
        e.preventDefault();

        const newObject = {
            epo:epo,
            num:models,
            dif_money:money,
            dif_popularity:popularity,
            dif_army:army,
            dif_land:land

        };

        console.log(newObject)
        fetch('http://127.0.0.1:8000/kings/', {  // Замените URL на ваш эндпоинт Django
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(newObject)
        })
            .then(response => response.json())
            .then(data => {
                console.log('Object created:', data);
                fetch('http://127.0.0.1:8000/kings/')  // Замените URL на ваш эндпоинт Django
                    .then(response => response.json())
                    .then(data => setKings(data))
                    .catch(error => console.log(error));
                // Можно выполнить дополнительные действия после успешного создания объекта
            })
            .catch(error => console.log(error));



    };
    const handleModels = () => {
        // Действия, которые могут быть выполнены перед перенаправлением

        // Перенаправление на ссылку
        window.location.href = 'http://localhost:3000/models';
    };

    const handleKings = () => {
        // Действия, которые могут быть выполнены перед перенаправлением

        // Перенаправление на ссылку
        window.location.href = 'http://localhost:3000/kings';
    };

    const handleCards = () => {
        // Действия, которые могут быть выполнены перед перенаправлением

        // Перенаправление на ссылку
        window.location.href = 'http://localhost:3000/';
    };


    console.log(kings)
    return (
        <div className="App">
            <div className="live-out">
                <div>
                    <p className="marg">Количество попыток и моедль</p>
                    <input onChange={e => setEpo(e.target.value)} type="number" value={epo} defaultValue="1000" className="marg" placeholder="Кол-во попыток"/>
                    <input onChange={e => setModels(e.target.value)} type="number" value={models} defaultValue="0" className="marg" placeholder="Модель"/>
                    <p className="marg">Характеристики сложности теста</p>
                    <input onChange={e => setMoney(e.target.value)} type="number" value={money} defaultValue="1000" className="marg" placeholder="Деньги"/>
                    <input onChange={e => setPopularity(e.target.value)} type="number" value={popularity} defaultValue="1000" className="marg" placeholder="Популярность"/>
                    <input onChange={e => setArmy(e.target.value)} type="number" value={army} defaultValue="1000" className="marg" placeholder="Армия"/>
                    <input onChange={e => setLand(e.target.value)} type="number" value={land} defaultValue="1000" className="marg" placeholder="Земля"/>
                </div>
                <button onClick={handleSubmit}>Создать королей</button>
                <button  onClick={handleModels}>Вернутся к моделям</button>
                <button  onClick={handleCards}>Вернутся к картам</button>
            </div>
            {kings.map(post=>
                <King post={post} key={post.id}/>
            )}
        </div>
    );
};

export default Kings;