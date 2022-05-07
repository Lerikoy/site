import React, { Component } from 'react'
import '../App.css'
import { YMaps, Map } from 'react-yandex-maps';

const Yandex_Map = () => (
  <YMaps>
    <div>
      <Map className='Y_Map'
        defaultState={{
            center: [62.027221, 129.732178],
            zoom: 9
        }} />
    </div>
  </YMaps>
);

export default Yandex_Map;