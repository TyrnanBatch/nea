import React from 'react';
import './Settings.css';

export default function Settings() {
    return (
        <div className={"setting-container"}>
            <div className={"data-input"}>
                <div className={"data-input-text"}>
                    Enter your data to sort separated by a ','
                </div>
                <input placeholder={"e.g. 37, 28, 68, 26"}/>
            </div>
        </div>
    );
}
