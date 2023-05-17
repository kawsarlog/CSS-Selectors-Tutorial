// Get the custom cursor element
const customCursor = document.getElementById('custom-cursor');

// Add an event listener to the document for mousemove event
document.addEventListener('mousemove', (event) => {
  // Update the position of the custom cursor element to follow the mouse cursor
  customCursor.style.transform = `translate(${event.clientX}px, ${event.clientY}px)`;
});

