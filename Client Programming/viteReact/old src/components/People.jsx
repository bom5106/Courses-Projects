import {useState, useEffect} from 'react'
import getData from '../utils/getData'
import './People.css'



const People=()=>{

    const [peopleObj, setPeopleObj] = useState();
    const [loaded, setLoaded] = useState(false);

    useEffect( ()=>{
        getData('people/')
            .then((json)=>{
                    setPeopleObj(json);
                    setLoaded(true);
            })
    }, [] );

    if(!loaded) return <><h1>Hello</h1></>

    return (
        <>
            <h1>{peopleObj.title}</h1>
            <h3>{peopleObj.subTitle}</h3>
            <h3>Faculty</h3>
            <div className="peopleList">
                {/*Loop*/}
                {peopleObj.staff.map((p) =>
                    <div className = "peopleListItem">
                        <h3>{p.name}</h3>
                        <img src={p.imagePath} alt='pic person' />
                    </div>
                )};
            </div>
            <h3>Staff</h3>
            <div className="peopleList">
                {/*Loop*/}
                {peopleObj.staff.map((p) =>
                    <div className = "peopleListItem">
                        <h3>{p.name}</h3>
                        <img src={p.imagePath} alt='pic person' />
                    </div>
                )};
            </div>
        </>
    );
}
export default People