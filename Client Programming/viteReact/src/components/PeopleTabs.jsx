import {useState, useEffect} from 'react'
import { TabPane, Tab } from 'semantic-ui-react'
import PeopleGroup from './PeopleGroup'
import getData from '../utils/getData'
import './People.css'



// const PeopleTabs = () =>  <Tab panes={panes} />

const PeopleTabs = () => {

  const [peopleObj, setPeopleObj] = useState();
  const [loaded, setLoaded] = useState(false);

  const panes = [
    { menuItem: 'Faculty', render: () => <TabPane>
      <PeopleGroup title="Faculty" obj={peopleObj.faculty}/>
      </TabPane> },
    { menuItem: 'Staff', render: () => <TabPane>
      <PeopleGroup title="Staff" obj={peopleObj.staff}/>
      </TabPane> },
  ]

  //Go get the Data
  useEffect ( ()=>{
    getData('people/')
      .then((json)=>{
        setPeopleObj(json);
        setLoaded(true);
      })
  }, []);

  if(!loaded) return <h1>Loading People...</h1>

  return (
    <>
    <h1>{peopleObj.title}</h1>
    <h3>{peopleObj.subTitle}</h3>
    <Tab panes={panes}/>
    
    </>
  );
} 


export default PeopleTabs