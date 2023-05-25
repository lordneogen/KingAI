import React from 'react';
import Plot from 'react-plotly.js';

class Graph extends React.Component {
    render() {
        const { title, xData, yData } = this.props;

        const data = [
            {
                x: xData,
                y: yData,
                type: 'scatter',
            },
        ];

        const layout = {
            title: title,
            xaxis: {
                title: 'Попытки',
            },
            yaxis: {
                title: 'Возраст',
            },
        };

        return (
            <div className="gr">
                <Plot   data={data} layout={layout} />
            </div>
        );
    }
}

export default Graph;
