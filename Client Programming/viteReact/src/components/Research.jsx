import React, { useState, useEffect } from 'react'; // React hooks for state and lifecycle management
import Accordion from '@mui/material/Accordion'; // Material-UI Accordion for collapsible sections
import AccordionSummary from '@mui/material/AccordionSummary'; // Accordion header
import AccordionDetails from '@mui/material/AccordionDetails'; // Accordion body
import Typography from '@mui/material/Typography'; // Material-UI Typography for consistent text styling
import ExpandMoreIcon from '@mui/icons-material/ExpandMore'; // Icon for expand/collapse functionality
import getData from '../utils/getData'; // Utility function to fetch data from the API
import './Research.css'; // CSS for styling the Research component


const Research = () => {
  // State to hold the fetched research data
  const [researchData, setResearchData] = useState(null);
  // State to track if the data has finished loading
  const [loaded, setLoaded] = useState(false);

  // Fetch research data from the API when the component mounts
  useEffect(() => {
    getData('research/').then((data) => {
      setResearchData(data); // Save fetched data in state
      setLoaded(true); // Mark as loaded
    }); 
  }, []); // Dependency array is empty, so this runs only once when the component mounts

  // If the data is still loading, display a loading message
  if (!loaded) {
    return <h2>Loading Research...</h2>;
  }

  return (
    <div id='researchBar' className="Research"> {/* Main container with an id for navigation */}
      <h2>Research Section</h2>

      {/* Research by Interest Area */}
      <section>
        <h3>Research by Interest Area</h3>
        {researchData.byInterestArea && researchData.byInterestArea.length > 0 ? (
          // Loop through each research interest area and render an Accordion
          researchData.byInterestArea.map((area, index) => (
            <Accordion key={index}>
              <AccordionSummary expandIcon={<ExpandMoreIcon />}>
                <Typography>{area.areaName}</Typography>
              </AccordionSummary>
              <AccordionDetails>
                <ul>
                  {area.citations.map((citation, i) => (
                    <li key={i}>{citation}</li>
                  ))}
                </ul>
              </AccordionDetails>
            </Accordion>
          ))
        ) : (
          <p>No research data available for Interest Areas.</p>
        )}
      </section>

      {/* Research by Faculty */}
      <section>
        <h3>Research by Faculty</h3>
        {researchData.byFaculty && researchData.byFaculty.length > 0 ? (
          researchData.byFaculty.map((faculty, index) => (
            <Accordion key={index}>
              <AccordionSummary expandIcon={<ExpandMoreIcon/>}>
                <Typography>{faculty.facultyName}</Typography>
              </AccordionSummary>
              <AccordionDetails>
                <Typography>Username: {faculty.username}</Typography>
                <ul>
                  {faculty.citations.map((citation, i) => (
                    <li key={i}>{citation}</li>
                  ))}
                </ul>
              </AccordionDetails>
            </Accordion>
          ))
        ) : (
          <p>No research data available for Faculty.</p>
        )}
      </section>
    </div>
  );
};

export default Research;