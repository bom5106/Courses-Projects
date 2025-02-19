//load stuff
//import React from 'react'
import {useState, useEffect} from 'react'
import About from './components/About.jsx'

import PeopleTabs from './components/PeopleTabs.jsx'
//getData
import getData from './utils/getData.js'

import './App.css'

import Degree from './components/Degree';

import Minor from './components/Minor';
import Employment from './components/Employment.jsx'

import NavbarBar from './components/Navbar.jsx'

import 'bootstrap/dist/css/bootstrap.min.css';

import EmploymentMap from './components/EmploymentMap.jsx'

import Research from './components/Research.jsx'

//my component
  const App=()=>{
    //set up state
    //const[getter, setter] = useState(init);
    //boolean if the data is loaded
    const [loaded, setLoaded] = useState(false);
    //obj that holds data
    const [about, setAbout] = useState();

    //app methods
    useEffect( () =>{
      //go get my data...
        getData('about/').
          then((json)=>{
            setAbout(json);
            setLoaded(true);
          })
    }, [] );



    //app return
    if(!loaded) return(
      <>
        <div className="stick">
          <h1>Welcome to Brandon's iSchool Site</h1>
          <div>Loading...</div>
        </div>
      </>
    );

    return (
      <>
        <div className="stick">
          <h1>Welcome to Brandon's iSchool Site</h1>
          <div>...Menu of some sort...</div>
          <NavbarBar/>
        </div>
        <div className="App">
          {/* Components */}
          <About ad={about}/>
          <hr/>
          <PeopleTabs/>
          
          <h1>Degree Programs</h1>
          <Degree/>
          
          <h1>Minors Offered</h1>
          <Minor/>

          <h1>Employment Opportunities</h1>
          <Employment/>

          <h1>Google Map</h1>
          <EmploymentMap/>

          <h1>Research</h1>
          <Research/>




        </div>
      </>
    );
}

export default App