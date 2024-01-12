const canvas = document.getElementById("canvas"); // Replace "canvas" with your canvas element's ID
const ctx = canvas.getContext("2d");

const logo = new Image();
logo.src = "idan_logo.png"; // Replace with your image file path

let logoX = canvas.width / 2 - logo.width / 4;
let logoY = canvas.height / 2 - logo.height / 4;
let speedX = 2;
let speedY = 2;

function changeColor() {
  // Implement your color change logic here
}

function draw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);

  // Move the image
  logoX += speedX;
  logoY += speedY;

  // Bounce off the edges and change logo color
  if (logoX < 0 || logoX + logo.width / 2 > canvas.width) {
    speedX = -speedX;
    logo.src = changeColor();
  }
  if (logoY < 0 || logoY + logo.height / 2 > canvas.height) {
    speedY = -speedY;
    logo.src = changeColor();
  }

  ctx.drawImage(logo, logoX, logoY, logo.width / 2, logo.height / 2);

  requestAnimationFrame(draw);
}

draw();
