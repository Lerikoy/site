import React from 'react'
import '../App.css'
import { YMaps, Map, GeolocationControl, Placemark} from 'react-yandex-maps';

const Yandex_Map = () => (
  <YMaps>
    <div>
      <Map className='Y_Map'
        defaultState={{
            center: [62.027221, 129.732178],
            zoom: 9,
            controls: [],
        }}>
        <GeolocationControl options={{ float: 'left' }} />
        {/* <Placemark>
          https://cdn-icons.flaticon.com/png/512/2776/premium/2776067.png?token=exp=1653556352~hmac=41e2b0258cfba7290d3f925b66f8b348
        </Placemark> */}
        </Map>
    </div>
  </YMaps>
);

export default Yandex_Map;