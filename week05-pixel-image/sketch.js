let img;
function preload(){
  img = loadImage("dino.png");
}

function setup() {
  //img.resize(400, 300)
  createCanvas(img.width, img.height);
}

function draw() {
  background(0);
  let gap = 10;
  img.loadPixels();
  for (let y = floor(gap/2); y < height; y += gap){
    for (let x = floor(gap/2); x < width; x += gap){
      let pixelIndex = floor((x + y * width) * 4);
      let r = img.pixels[pixelIndex];
      let g = 255 - img.pixels[pixelIndex + 1];
      let b = img.pixels[pixelIndex + 2];
      
      fill(r, g, b);
      let distance = dist(mouseX, mouseY, x, y)/(width/2);
      let wave = sin(distance * TWO_PI + millis() * 0.003);
      let amp = 20;
      let newX = x + wave * amp;
      let newY = y + wave * amp;
      ellipse(newX, newY, gap * 1);
    }
  }
//  image(img, 0, 0);
}