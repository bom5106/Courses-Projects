import { useState, useEffect } from 'react'; // React hooks for state and lifecycle management
import './Degree.css'; // CSS for styling the Degree component
import Accordion from '@mui/material/Accordion'; // Material-UI Accordion component for collapsible sections
import AccordionSummary from '@mui/material/AccordionSummary'; // Summary section for Accordion (header)
import AccordionDetails from '@mui/material/AccordionDetails'; // Details section for Accordion (body)
import ExpandMoreIcon from '@mui/icons-material/ExpandMore'; // Icon for expandable Accordions

import getData from '../utils/getData'; // Utility function for API requests

const Degree = () => {
  // State to hold the degrees data fetched from the API
  const [degrees, setDegreeObj] = useState();

  // State to track if data has been loaded
  const [loaded, setLoaded] = useState(false);

  // Fetch degrees data when the component mounts
  useEffect(() => {
    getData('degrees/') // Call API to fetch degrees data
      .then((data) => {
        setDegreeObj(data); // Set the fetched data in state
        setLoaded(true); // Mark as loaded
      });
  }, []); // Dependency array is empty, so this runs only once when the component mounts

  // Show a loading message until the data is fetched
  if (!loaded) {
    return <h2>Loading Degrees...</h2>;
  }

  return (
    <div id="degreeBar" className="Degree"> {/* Main container with id for navigation */}
      
      {/* Undergraduate Degrees */}
      <section>
        <h2>Undergraduate Degrees</h2>
        {/* Loop through undergraduate degrees and create an Accordion for each */}
        {degrees.undergraduate.map((degree, index) => (
          <div key={index} className="degreeCard"> {/* Wrapper for individual degree */}
            <Accordion>
              {/* Summary section of the Accordion */}
              <AccordionSummary
                expandIcon={<ExpandMoreIcon />} // Expand/collapse icon
                aria-controls={`panel-${index}-content`} // Accessibility attribute for content
                id={`panel-${index}-header`} // Accessibility attribute for header
              >
                <h3>{degree.title}</h3> {/* Degree title */}
              </AccordionSummary>

              {/* Details section of the Accordion */}
              <AccordionDetails>
                <p>{degree.description}</p> {/* Degree description */}
                <h4>Concentrations:</h4>
                <ul>
                  {/* List of concentrations */}
                  {degree.concentrations.map((concentration, i) => (
                    <li key={i}>{concentration}</li>
                  ))}
                </ul>
              </AccordionDetails>
            </Accordion>
          </div>
        ))}
      </section>

      {/* Graduate Degrees */}
      <section>
        <h2>Graduate Degrees</h2>
        {/* Loop through graduate degrees and create an Accordion for each */}
        {degrees.graduate.map((degree, index) => (
          <div key={index} className="degreeCard"> {/* Wrapper for individual degree */}
            <Accordion>
              {/* Summary section of the Accordion */}
              <AccordionSummary
                expandIcon={<ExpandMoreIcon />} // Expand/collapse icon
                aria-controls={`panel-${index + degrees.undergraduate.length}-content`} // Accessibility attribute for content
                id={`panel-${index + degrees.undergraduate.length}-header`} // Accessibility attribute for header
              >
                {/* Title handling for advanced certificates */}
                <h3>
                  {degree.degreeName !== "graduate advanced certificates"
                    ? degree.title
                    : "Graduate Advanced Certificates"}
                </h3>
              </AccordionSummary>

              {/* Details section of the Accordion */}
              <AccordionDetails>
                {degree.degreeName !== "graduate advanced certificates" ? (
                  <>
                    <p>{degree.description}</p> {/* Degree description */}
                    <h4>Concentrations:</h4>
                    <ul>
                      {/* List of concentrations */}
                      {degree.concentrations.map((concentration, i) => (
                        <li key={i}>{concentration}</li>
                      ))}
                    </ul>
                  </>
                ) : (
                  <ul>
                    {/* List of available certificates for advanced certificates */}
                    {degree.availableCertificates.map((certificate, i) => (
                      <li key={i}>{certificate}</li>
                    ))}
                  </ul>
                )}
              </AccordionDetails>
            </Accordion>
          </div>
        ))}
      </section>
    </div>
  );
};

export default Degree;