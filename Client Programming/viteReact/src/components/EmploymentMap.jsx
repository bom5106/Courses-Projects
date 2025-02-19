import React from 'react';
import './EmploymentMap.css'

const EmploymentMap = () => {
  return (
    <div id = "employmentMapBar" className="EmploymentMap">
      <h2>Employment Locations</h2>
      <iframe
        src="https://ischool.gccis.rit.edu/api/map/"
        title="Employment Map"
        width="100%"
        height="600px"
        style={{ border: 0 }}
        allowFullScreen=""
        loading="lazy"
      ></iframe>
    </div>
  );
};

export default EmploymentMap;


// import {useState, useEffect} from 'react'
// import { GoogleMap, LoadScript, Marker } from '@react-google-maps/api';
// import getData from '../utils/getData';
// import './EmploymentMap.css'

// const EmploymentMap = () => {

//   const [locations, setLocationsObj] = useState();
//   const [loaded, setLoaded] = useState(false);

//   useEffect(() => {
//     getData('map/').then((data) => {
//       setLocationsObj(data);
//       setLoaded(true);
//     });
//   }, []);

//   if(!loaded){
//     return <h2>Loading Map...</h2>
//   }

// };
// export default EmploymentMap;
