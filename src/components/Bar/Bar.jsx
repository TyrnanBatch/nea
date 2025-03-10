import React from 'react';
import './Bar.css';

const Bar = ({width, height}) => {
    const barStyle = {
        width: width,
        height: height,
    };

    return <div className="bar" style={barStyle}></div>;
};

export default Bar;