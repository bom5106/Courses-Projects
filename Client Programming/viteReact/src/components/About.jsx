//let's make an About component!

const About = ({ad})=>{
    return(
        <div id = "aboutBar" className="About">
            <h2>{ad.title}</h2>
            <h3>{ad.description}</h3>
            <div className="aboutQuote">
              <h4 className="quote">{ad.quote}</h4>
              <h4>--{ad.quoteAuthor}</h4>
            </div>
          </div>
    );
}
export default About