import { useState, useEffect } from 'react'; // React hooks for state and lifecycle management
import './Minor.css'; // CSS for styling the Minor component

import CourseModal from './CourseModal'; // Component to display course details in a modal
import getData from '../utils/getData'; // Utility function for API requests

const Minor = () => {
  // State to hold the minors data fetched from the API
  const [minors, setMinorObj] = useState();

  // State to track if the data has finished loading
  const [loaded, setLoaded] = useState(false);

  // Fetch minors data when the component mounts
  useEffect(() => {
    getData('minors/UgMinors/') // API endpoint for undergraduate minors
      .then((data) => {
        setMinorObj(data); // Save fetched data in state
        setLoaded(true); // Mark as loaded
      });
  }, []); // Dependency array is empty, so this runs only once when the component mounts

  // Show a loading message until the data is fetched
  if (!minors || !minors.UgMinors) {
    return <h2>Loading Minors...</h2>;
  }

  return (
    <div id="minorBar" className="Minor"> {/* Main container with id for navigation */}
      <h2>Undergraduate Minors</h2>

      {/* Loop through each minor and display its details */}
      {minors.UgMinors.map((minor, index) => (
        <div key={index} className="minorCard"> {/* Wrapper for each minor */}
          <h3>{minor.title}</h3> {/* Minor title */}
          <p>{minor.description}</p> {/* Minor description */}
          
          {/* List of courses for the minor */}
          <h4>Courses:</h4>
          <ul>
            {minor.courses.map((course, i) => (
              <CourseModal key={i} courseID={course} /> // Render CourseModal for each course
            ))}
          </ul>

          {/* Display additional notes, if available */}
          {minor.note && (
            <div className="minorNote">
              <strong>Note:</strong> {minor.note}
            </div>
          )}
        </div>
      ))}
    </div>
  );
};

export default Minor;