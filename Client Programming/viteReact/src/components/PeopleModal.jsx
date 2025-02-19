import * as React from 'react';
import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import Typography from '@mui/material/Typography';
import Modal from '@mui/material/Modal';

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

export default function BasicModal(prop) {
  const [open, setOpen] = React.useState(false);
  const handleOpen = () => setOpen(true);
  const handleClose = () => setOpen(false);

  return (
    <div>
      <Button onClick={handleOpen}>{prop.name || 'Open Modal'}</Button>
      <Modal
        open={open}
        onClose={handleClose}
        aria-labelledby="modal-modal-title"
        aria-describedby="modal-modal-description"
      >
        
        <Box sx={style}>
          {/* Flexbox Container */}
          
          <Box sx = {{ display: 'flex', gap: 2}}>
            <img src={prop.imagePath} alt="pic person" style={{ width: '300px', height: '300px' }}/>
          </Box>

          <Box>
          <Typography id="modal-modal-name" variant="h6" component="h2">
            Name: {prop.name || 'No Name'}
          </Typography>

          <Typography id="modal-modal-title" variant="h6" component="h2">
            Title: {prop.tagline || 'No Title'}
          </Typography>

          <Typography id="modal-modal-email" variant='h6' component="h2">
            Email: {prop.email || 'No Email'}
          </Typography>

          <Typography id="modal-modal-interest" variant='h6' component="h2">
            Interest Area: {prop.interestArea || "No Interest Area"}
          </Typography>

          <Typography id="modal-modal-office" variant='h6' component="h2">
            Office: {prop.office || "No Office"}
          </Typography>

          <Typography id="modal-modal-website" variant='h6' component="h2">
            Website: {prop.website || "No Website"}
          </Typography>

          <Typography id="modal-modal-phone" variant='h6' component="h2">
            Phone: {prop.phone || "No Phone Number"}
          </Typography>

          <Typography id="modal-modal-twitter" variant='h6' component="h2">
            Twitter: {prop.twitter || "No Twitter"}
          </Typography>

          <Typography id="modal-modal-facebook" variant='h6' component="h2">
            Facebook: {prop.facebook || "No Facebook"}
          </Typography>

          {/* <Typography id="modal-modal-description" sx={{ mt: 2 }}>
            Duis mollis, est non commodo luctus, nisi erat porttitor ligula.
          </Typography> */}
          </Box>
        </Box>
      </Modal>
    </div>
  );
}