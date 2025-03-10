import React from 'react';
import Bar from './../Bar/Bar';
import './BarContainer.css';

const BarContainer = ({data, height, width}) => {
    const maxValue = Math.max(...data);
    const barWidth = `${100 / data.length}%`;

    return (
        <div className="bar-container" style={{height: height, width: width}}>
            {data.map((value, index) => {
                const barHeight = (value / maxValue) * 100;
                return (
                    <Bar
                        key={index}
                        height={`${barHeight}%`}
                        width={barWidth}
                    />
                );
            })}
        </div>
    );
};

export default BarContainer;