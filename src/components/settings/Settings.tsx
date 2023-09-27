import React from 'react';
import './Settings.css';

export default function Settings() {
    return (
        <div className={"setting-container"}>
            <div>Enter your data to sort separated by a ','</div>
            <input className={"data-input"} placeholder={"e.g. 37, 28, 68, 26"}/>
        </div>
    );
}
