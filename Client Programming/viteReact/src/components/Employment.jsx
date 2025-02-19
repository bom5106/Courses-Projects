import React, { useState, useEffect } from 'react'; // React hooks for state and lifecycle management
import Box from '@mui/material/Box'; // Material-UI component for layout and styling
import { DataGrid } from '@mui/x-data-grid'; // Material-UI DataGrid for displaying tabular data with pagination
import getData from '../utils/getData'; // Utility function to fetch data from the API

const Employment = () => {
  // State to hold the employment data fetched from the API
  const [employments, setEmployments] = useState(null);

  // State to track if the data has finished loading
  const [loadedEmployment, setLoadedEmployment] = useState(false);

  // Fetch employment data when the component mounts
  useEffect(() => {
    getData('employment/').then((data) => {
      setEmployments(data); // Save fetched data in state
      setLoadedEmployment(true); // Mark as loaded
    });
  }, []); // Dependency array is empty, so this runs only once when the component mounts

  // Show a loading message until the data is fetched
  if (!loadedEmployment) {
    return <h2>Loading Employments...</h2>;
  }

  // Columns for Co-op Table
  // Define column headers for the DataGrid displaying co-op information
  const coopColumns = [
    { field: 'employer', headerName: 'Employer', flex: 1 }, // Column for employer
    { field: 'degree', headerName: 'Degree', flex: 1 }, // Column for degree
    { field: 'city', headerName: 'City', flex: 1 }, // Column for city
    { field: 'term', headerName: 'Term', flex: 1 }, // Column for term
  ];

  // Rows for Co-op Table
  // Map the co-op data into a format suitable for the DataGrid
  const coopRows = employments.coopTable.coopInformation.map((item, index) => ({
    id: index + 1, // Add a unique ID for each row
    ...item, // Spread the remaining data from the item
  }));

  // Columns for Professional Employment Table
  // Define column headers for the DataGrid displaying professional employment information
  const employmentColumns = [
    { field: 'employer', headerName: 'Employer', flex: 1 }, // Column for employer
    { field: 'degree', headerName: 'Degree', flex: 1 }, // Column for degree
    { field: 'city', headerName: 'City', flex: 1 }, // Column for city
    { field: 'title', headerName: 'Title', flex: 1 }, // Column for job title
    { field: 'startDate', headerName: 'Start Date', flex: 1 }, // Column for start date
  ];

  // Rows for Professional Employment Table
  // Map the professional employment data into a format suitable for the DataGrid
  const employmentRows = employments.employmentTable.professionalEmploymentInformation.map(
    (item, index) => ({
      id: index + 1, // Add a unique ID for each row
      ...item, // Spread the remaining data from the item
    })
  );

  return (
    <div id="employmentBar" className="Employment"> {/* Main container with id for navigation */}
      <h2>Employment Section</h2>

      {/* Co-op Table */}
      <section>
        <h3>{employments.coopTable.title}</h3> {/* Display the title for the Co-op Table */}
        <Box sx={{ height: 400, width: '100%', marginBottom: 4 }}>
          <DataGrid
            rows={coopRows} // Rows of data for the Co-op Table
            columns={coopColumns} // Columns for the Co-op Table
            pageSizeOptions={[10, 25, 50, 100]} // Options for rows per page
            initialState={{
              pagination: {
                paginationModel: { pageSize: 10 }, // Default rows per page
              },
            }}
            disableRowSelectionOnClick // Prevent rows from being selectable on click
            checkboxSelection={false} // Disable checkbox selection
          />
        </Box>
      </section>

      {/* Professional Employment Table */}
      <section>
        <h3>{employments.employmentTable.title}</h3> {/* Display the title for the Professional Employment Table */}
        <Box sx={{ height: 400, width: '100%' }}>
          <DataGrid
            rows={employmentRows} // Rows of data for the Professional Employment Table
            columns={employmentColumns} // Columns for the Professional Employment Table
            pageSizeOptions={[10, 25, 50, 100]} // Options for rows per page
            initialState={{
              pagination: {
                paginationModel: { pageSize: 10 }, // Default rows per page
              },
            }}
            disableRowSelectionOnClick // Prevent rows from being selectable on click
            checkboxSelection={false} // Disable checkbox selection
          />
        </Box>
      </section>
    </div>
  );
};

export default Employment;