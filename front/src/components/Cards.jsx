import React, {useEffect, useState} from 'react';
import Card from "./Card";
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
const Cards = (props) => {

    const [cards,setCards] = useState([])

    const [name, setName] = useState('');
    const [title, setTitle] = useState('');
    const [money, setMoney] = useState(0);
    const [popularity, setPopularity] = useState(0);
    const [army, setArmy] = useState(0);
    const [land, setLand] = useState(0);
    const [learn, setLearn] = useState(true);

    useEffect(() => {
        fetch('http://127.0.0.1:8000/cards/')  // Замените URL на ваш эндпоинт Django
            .then(response => response.json())
            .then(data => setCards(data))
            .catch(error => console.log(error));
    }, []);

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

    const handleCheckboxChange = () => {
        setLearn(!learn);
    };

    const handleSubmit = (e) => {
        e.preventDefault();

        const newObject = {
            name: name,
            title:title,
            money:money,
            popularity:popularity,
            army:army,
            land:land,
            is_learn:learn

        };

        fetch('http://127.0.0.1:8000/cards/', {  // Замените URL на ваш эндпоинт Django
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(newObject)
        })
            .then(response => response.json())
            .then(data => {
                console.log('Object created:', data);
                fetch('http://127.0.0.1:8000/cards/')  // Замените URL на ваш эндпоинт Django
                    .then(response => response.json())
                    .then(data => setCards(data))
                    .catch(error => console.log(error));
                // Можно выполнить дополнительные действия после успешного создания объекта
            })
            .catch(error => console.log(error));



    };
    console.log(cards)
    return (
        <div className="App">
            <div className="live-out">
                <input type="text" placeholder="Название" onChange={e => setName(e.target.value)} value={name}/>
                <input type="text" placeholder="Описание" onChange={e => setTitle(e.target.value)} value={title}/>
                <div>
                    <p className="marg">Характеристики</p>
                    <input onChange={e => setMoney(e.target.value)} type="number" value={money} defaultValue="0" className="marg" placeholder="Деньги"/>
                    <input onChange={e => setPopularity(e.target.value)} type="number" value={popularity} defaultValue="0" className="marg" placeholder="Популярность"/>
                    <input onChange={e => setArmy(e.target.value)} type="number" value={army} defaultValue="0" className="marg" placeholder="Армия"/>
                    <input onChange={e => setLand(e.target.value)} type="number" value={land} defaultValue="0" className="marg" placeholder="Земля"/>
                    <p className="marg">Это не для обучения:</p>
                    <input className="marg" onClick={handleCheckboxChange} type="checkbox"/>

                </div>
                <button onClick={handleSubmit}>Создать карту</button>
                <button onClick={handleModels}>Вернутся к обучению</button>
                <button onClick={handleKings}>Вернутся к королям</button>
            </div>
            {cards.map(post=>
                <Card post={post} key={post.id}/>
            )}
        </div>
    );
};

export default Cards;
