import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import Graph from "./Graph";

const Model_detail = () => {
    const { id } = useParams();
    const [models, setModels] = useState(null);

    useEffect(() => {
        fetch(`http://127.0.0.1:8000/models/${id}/`)  // Замените URL на ваш эндпоинт Django
            .then(response => response.json())
            .then(data => {
                if (Array.isArray(data) && data.length > 0) {
                    setModels(data[0]);
                }
            })
            .catch(error => console.log(error));
    }, [id]);


    const handleDelete = () => {
        console.log(models);
        fetch(`http://127.0.0.1:8000/models/${id}/`, {  // Замените URL на ваш эндпоинт Django
            method: 'DELETE'
        })
            .then(response => {
                if (response.ok) {
                    console.log('Object deleted');
                    // Можно выполнить дополнительные действия после успешного удаления объекта
                } else {
                    throw new Error('Ошибка при удалении объекта');
                }
            })
            .catch(error => console.log(error));
    };

    return (
        <div className="live-out">
            {models ? (
                <div>
                    <div>
                        <h4>Номер:{models.id}</h4>
                        <p>Кол-во карт:{models.card_num}</p>
                        <p>Кол-во попыток:{models.epo}</p>
                        <p>Сложность денег:{models.dif_money}</p>
                        <p>Сложность популярности:{models.dif_popularity}</p>
                        <p>Сложность армии:{models.dif_army}</p>
                        <p>Сложность земли:{models.dif_land}</p>
                    </div>

                    {/*const { title, xData, yData } = this.props;*/}
                    <Graph title={id} xData={JSON.parse(models.graph_num)} yData={JSON.parse(models.graph)}  />
                    <div>
                        {models.desc.split(',').map((str, index) => (
                            <p key={index}>{str}</p>
                        ))}
                    </div>
                </div>
            ) : (
                <p>Loading...</p>
            )}

            <div>
                <button onClick={handleDelete}>Удалить</button>
            </div>
        </div>
    );
};

export default Model_detail;
