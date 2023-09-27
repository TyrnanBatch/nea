import React from 'react';
import './App.css';
import Bars from "./components/bars/Bars";
import Settings from "./components/settings/Settings";

export default function App() {
  return (
      <div className={'main-container'}>
        <Bars/><Settings/>
      </div>
  );
}
