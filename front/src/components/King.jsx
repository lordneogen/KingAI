import React, {useState} from 'react';
import Graph from "./Graph";
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
const King = (props) => {

    console.log(props)
    const [kings,setKings] = useState([])
    const objectId=props.post.id
    const handleDelete = () => {
        fetch(`http://127.0.0.1:8000/kings/${objectId}/`, {  // Замените URL на ваш эндпоинт Django
            method: 'DELETE'
        })
            .then(response => {
                if (response.ok) {
                    console.log('Object deleted');
                    fetch('http://127.0.0.1:8000/kings/')  // Замените URL на ваш эндпоинт Django
                        .then(response => response.json())
                        .then(data => setKings(data))
                        .catch(error => console.log(error));
                    // Можно выполнить дополнительные действия после успешного удаления объекта
                } else {
                    throw new Error('Ошибка при удалении объекта');
                }
            })
            .catch(error => console.log(error));
    };
    const handleModel_detail = () => {
        // Действия, которые могут быть выполнены перед перенаправлением

        // Перенаправление на ссылку
        const urlhr=`http://localhost:3000/kings_detail/${objectId}/`

        window.location.href = urlhr;
    };

    return (
        <div className="live-out">
            <div>
                <div>
                    <h4>Номер:{props.post.id}</h4>
                    <h4>Характеристики:</h4>
                    <p>Кол-во карт:{props.post.card_num}</p>
                    <p>Кол-во попыток:{props.post.epo}</p>
                    <p>Сложность денег:{props.post.dif_money}</p>
                    <p>Сложность популярности:{props.post.dif_popularity}</p>
                    <p>Сложность армии:{props.post.dif_army}</p>
                    <p>Сложность земли:{props.post.dif_land}</p>
                </div>
                <Graph title={props.post.id} xData={JSON.parse(props.post.graph_num)} yData={JSON.parse(props.post.graph)}  />
            </div>
            <div>
                <button onClick={handleModel_detail}>Детали</button>
                <button onClick={handleDelete}>Удалить</button>
            </div>
        </div>
    );
};

export default King;