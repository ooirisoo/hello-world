var n = 0;
var c = 3;

function setup() {
  createCanvas(windowWidth, windowHeight);
  background(0);
  color(HSB);
}

function draw() {
  
  var a = n * 137.5;
  var r = c * sqrt(n);
  
  var x = r * cos(a) + mouseX;
  var y = r * sin(a) + mouseY;
  

  fill(a % 256, 180, 255);
  noStroke();
  ellipse(x, y, 4, 4);
  

/*  function mousePressed(){
    if (n = 0, n < width, n++){
      var n = 0;
    }
  }
I tried to make some interaction with the mouse,
When mousepressed, the pattern will rebuild from the click point,
rather than a big hollow like what it shows now,
but I failed...
*/
  n++;
  
}
