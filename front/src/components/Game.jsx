import React, {useEffect, useState} from 'react';
import Graph from "./Graph";

const Game = ({ item }) => {
    const [isFlipped, setIsFlipped] = useState(false);
    const [id1,setId1]=useState(0);

    const [isLoading, setIsLoading] = useState(true);

    const handleCardClick = () => {
        setIsFlipped(!isFlipped);
        if(isFlipped) {
            setId1(id1 + 1);
        }
    };

    useEffect(() => {
        setTimeout(() => {
            setIsLoading(false);
        }, 1000); // Задержка в 3 секунды
    }, []);


    const handleCardClickinv = () => {
        setIsFlipped(!isFlipped);
        if(isFlipped) {
            setId1(id1 - 1);
        }
    };

    if (isLoading) {
        // Здесь можно отобразить компоненты загрузки или анимацию
        return <div>Loading...</div>;
    }

    return (
                <div>{item ?  (
                    <div className={`card ${isFlipped ? 'flipped' : ''}`}>
                        <div className="card-inner">
                            <div className="card-front">
                                <div className="card-suit"><p className="pp">Номер жизни:{item[id1][0]} Возраст:{item[id1][7]}</p></div>
                                <div className="card-suit" className="pp">Вы выбрали-{item[id1][1]}</div>
                                <div className="card-value">⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡤⠤⠤⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠊⢀⣀⣀⡈⠳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⣀⣸⠟⠁⣠⠏⠁⠈⠉⠉⠳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                    ⠀⠀⠀⠀⠀⠀⣠⡞⠟⣠⠞⠁⣠⠁⠀⠀⠀⠀⢠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                    ⠀⠀⠀⠀⢠⣾⠟⣁⣠⠞⠓⢠⠏⠁⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                    ⠀⠀⢀⣴⡿⠁⢀⣾⠟⠋⢀⠎⠀⠀⠂⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                    ⠀⢠⣾⣿⡟⠐⣠⠟⠓⢁⠁⠀⠀⠀⠀⠀⠀⠀⠀⣿⣷⣦⣄⡀⠀⠀⠀⠀⠀
                                    ⠰⣿⣿⡟⠡⠔⠊⠙⠳⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡇⠀⠈⢿⡄⠀⠀⠀⠀
                                    ⠀⠈⠻⣿⣦⡀⠀⠀⣤⠤⠴⠶⢶⣶⣤⣤⣤⣄⠈⠻⡇⠀⠈⢿⡇⠀⠀⠀⠀
                                    ⠀⠀⠀⠈⠻⣿⣧⠀⠀⠉⠙⠓⠚⠛⠛⠛⠛⠋⠁⠀⣰⠃⠀⠈⢿⡄⠀⠀⠀
                                    ⠀⠀⠀⠀⠀⠙⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠏⠀⠀⠀⠈⢿⡀⠀⠀
                                    ⠀⠀⠀⠀⠀⠀⢻⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⠁⠀⠀⠀⠀⠀⢈⣷⠀⠀
                                    ⠀⠀⠀⠀⠀⠀⠀⠻⣿⣦⡀⠀⠀⠀⠀⠀⣰⠟⠀⠀⠀⠀⠀⠀⠀⣼⣿⠀⠀
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣦⣤⣤⣤⠞⠁⠀⠀⠀⠀⠀⠀⢀⣾⣿⠏⠀⠀
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠠⣿⡟⠁⠀⠀⠀
                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠟⠁⠀⠀⠀⠀⠀⠀⠀⠋⠁⠀⠀⠀⠀
                                </div>
                                <div className="card-suit" className="pp">Вы не выбрали-{item[id1][2]}</div>
                            </div>
                            <div className="card-back"></div>
                        </div>
                        <div className="bt_div">
                            <button onClick={handleCardClickinv} className="bt y">Предыдущий</button>
                        <button onClick={handleCardClick} className="bt g">Следующий</button>
                        </div>
                    <div className="progress-bar ">
                        <p>Денег</p>
                        <div className="progress-back y-b"></div>
                        <div className="progress y" style={{ width: `${item[id1][3]}%` }}></div>
                    </div>
                        <div className="progress-bar ">
                            <p>Популярность</p>
                            <div className="progress-back p-b"></div>
                            <div className="progress p" style={{ width: `${item[id1][4]}%` }}></div>
                        </div>
                        <div className="progress-bar ">
                            <p>Армия</p>
                            <div className="progress-back r-b"></div>
                            <div className="progress r" style={{ width: `${item[id1][5]}%` }}></div>
                        </div>
                        <div className="progress-bar ">
                            <p>Земля</p>
                            <div className="progress-back g-b"></div>
                            <div className="progress g" style={{ width: `${item[id1][6]}%` }}></div>
                        </div>

                        {/*# {id: 1, name: 'Имя', title: 'Бла-Бла', money: 1000, popularity: 0, army: 0, land: -10},*/}
                    {/**/}
                    </div>
                ) : (
                    <p>Loading...</p>
                )}</div>
    );
};

export default Game;
