// SCROLL TO TOP FUNCTION
// gets the button by ID and storing it in a constant
const scrollTopBtn = document.getElementById("btnScrollUp");

// shows the button when a user scrolls down 100px from top
window.onscroll = function() {
  var top = window.scrollY;
  console.log(top);
  if (top >= 100) {
    scrollTopBtn.style.display = "block";
  } else {
    scrollTopBtn.style.display = "none";
  }
}

// event listener for the button
scrollTopBtn.addEventListener("click", scrollUp);

// scrolls to top of the document on click
function scrollUp() {
  document.body.scrollTop = 0;
  document.documentElement.scrollTop = 0;
}

