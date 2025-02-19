import PeopleModal from './PeopleModal'

const PeopleGroup=({title, obj})=>{

    return (
        <>
            <div className="peopleList">
                {/*loop */}
                {obj.map((p)=>
                    <div className="peopleListItem" key={p.username}>
                        <h3>{p.name}</h3>
                        <img src={p.imagePath} alt="pic person" />
                        <PeopleModal {...p} />
                    </div>
                )};
            </div>
        </>
    )
}
export default PeopleGroup