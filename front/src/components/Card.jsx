import React, {useState} from 'react';
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
const Card = (props) => {
    console.log(props)
    const [cards,setCards] = useState([])
    const objectId=props.post.id
    const handleDelete = () => {
        fetch(`http://127.0.0.1:8000/cards/${objectId}/`, {  // Замените URL на ваш эндпоинт Django
            method: 'DELETE'
        })
            .then(response => {
                if (response.ok) {
                    console.log('Object deleted');
                    fetch('http://127.0.0.1:8000/cards/')  // Замените URL на ваш эндпоинт Django
                        .then(response => response.json())
                        .then(data => setCards(data))
                        .catch(error => console.log(error));
                    // Можно выполнить дополнительные действия после успешного удаления объекта
                } else {
                    throw new Error('Ошибка при удалении объекта');
                }
            })
            .catch(error => console.log(error));
    };
    return (
        <div className="live-out">
        <div>
            <div>
                <h4>Номер:{props.post.id}</h4>
                <h4>Название:</h4>
                <p>{props.post.name}</p>
                <h4>Описание:</h4>
                <p>{props.post.title}</p>
                <h4>Характеристики:</h4>

                <p>Деньги:{props.post.money}</p>
                <p>Популярность:{props.post.popularity}</p>
                <p>Армия:{props.post.army}</p>
                <p>Земля:{props.post.land}</p>
                {props.post.is_learn ? <h4>Для обучения</h4> : <h4>Для теста</h4>}
            </div>
        </div>
            <div>
                <button onClick={handleDelete}>Удалить</button>
            </div>
        </div>
    );
};

export default Card;