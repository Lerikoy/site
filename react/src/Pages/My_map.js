import React, { Component } from 'react'
import { useJsApiLoader } from '@react-google-maps/api'
import { Map } from '../Components/Map'
import '../App.css'

 const API_KEY=process.env.REACT_APP_API_KEY;
 console.log(API_KEY);

 const defaultCenter = {
   lat: -3.745,
   lng: -38.523
 };

 const libraries = ['places']

 const My_maps = () =>{
   const {isLoaded} = useJsApiLoader({
     id: 'google-map-script',
     googleMapsApiKey: API_KEY,
     libraries
   })
   return(
     <div className='Ma_maps'>
       {isLoaded ? <Map center = {defaultCenter} /> : <h2>Loading</h2>}
     </div>
   );
};


export default My_maps; /*class My_map extends Component {
  render() {
    return (
      <div>My_map</div>
    )
  }
}*/
