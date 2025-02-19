import Container from 'react-bootstrap/Container'; // Bootstrap container for responsive layouts
import Nav from 'react-bootstrap/Nav'; // Bootstrap Nav component for navigation items
import Navbar from 'react-bootstrap/Navbar'; // Bootstrap Navbar component for creating a navigation bar
import NavDropdown from 'react-bootstrap/NavDropdown'; // Bootstrap NavDropdown for dropdown menus (optional, not used here)

// Functional component for the navigation bar
function NavbarBar() {
  return (
    <Navbar expand="lg" className="bg-body-tertiary"> {/* Navbar with a background class */}
      <Container> {/* Bootstrap container to align content properly */}
        <Nav className="me-auto"> {/* Align navigation items to the left */}
          {/* Navigation Links */}
          <Nav.Link href="#degreeBar">Degree</Nav.Link> {/* Links to the Degree section */}
          <Nav.Link href="#minorBar">Minor</Nav.Link> {/* Links to the Minor section */}
          <Nav.Link href="#employmentBar">Employment</Nav.Link> {/* Links to the Employment section */}
          <Nav.Link href="#employmentMapBar">Google Map</Nav.Link> {/* Links to the Google Map section */}
          <Nav.Link href="#researchBar">Research</Nav.Link> {/* Links to the Research section */}
          <Nav.Link href="#aboutBar">About</Nav.Link> {/* Links to the About section */}
        </Nav>
      </Container>
    </Navbar>
  );
}

export default NavbarBar; // Export the NavbarBar component for use in other parts of the app