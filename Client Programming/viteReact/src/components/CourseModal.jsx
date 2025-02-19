import * as React from 'react'; // Import React for using components, hooks, and JSX
import Box from '@mui/material/Box'; // Material-UI component for layout and styling
import Button from '@mui/material/Button'; // Material-UI button component
import Typography from '@mui/material/Typography'; // Material-UI component for text
import Modal from '@mui/material/Modal'; // Material-UI component for creating modals

import getData from '../utils/getData'; // Utility function to fetch data from the API

// Inline style for the modal box
const style = {
  position: 'absolute',
  top: '50%',
  left: '50%',
  transform: 'translate(-50%, -50%)',
  width: 400,
  bgcolor: 'background.paper',
  border: '2px solid #000',
  boxShadow: 24,
  p: 4,
};

// Component to display course details in a modal
export default function CourseModal(courseID) {
  // State to hold the course data fetched from the API
  const [courses, setCoursesObj] = React.useState();

  // State to track whether the data has finished loading
  const [loaded, setLoaded] = React.useState(false);

  // State to handle the modal's open/close state
  const [open, setOpen] = React.useState(false);

  // Function to open the modal
  const handleOpen = () => {
    setOpen(true);
  };

  // Function to close the modal
  const handleClose = () => {
    setOpen(false);
  };

  // Fetch course data when the component mounts
  React.useEffect(() => {
    getData('course/courseID=' + courseID.courseID) // Fetch data using courseID passed as a prop
      .then((data) => {
        setCoursesObj(data); // Save the fetched data to state
        setLoaded(true); // Mark as loaded
      });
  }, [courseID.courseID]); // Only refetch if courseID changes

  // Display a loading message until the data is fetched
  if (!loaded) return <h1>Loading...</h1>;

  return (
    <div>
      {/* Button to trigger the modal */}
      <Button onClick={() => handleOpen(courseID)}> {courseID.courseID} </Button>

      {/* Modal to display course details */}
      <Modal open={open} onClose={handleClose}>
        <Box sx={style}>
          {/* Display course information */}
          <Typography>
            CourseID: {courseID.courseID}
          </Typography>
          <Typography>
            Title: {courses.title}
          </Typography>
          <Typography>
            Description: {courses.description}
          </Typography>
        </Box>
      </Modal>
    </div>
  );
}