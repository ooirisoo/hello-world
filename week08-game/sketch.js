let spritesheet;
let spritedata;

let animation = [];

let bread = [];

function preload() {
  spritedata = loadJSON('bread.json');
  spritesheet = loadImage('bread.png');
}


function setup() {
  createCanvas(640, 480);
  let frames = spritedata.frames;
  for (let i = 0; i < frames.length; i++) {
    let pos = frames[i].position;
    let img = spritesheet.get(pos.x, pos.y, pos.w, pos.h);
    animation.push(img);
  }

  for (let i = 0; i < 5; i++) {
    bread[i] = new Sprite(animation, 0, i * 75, random(0.1, 0.4));
  }
}

function draw() {
  background(0);

  for (let bread of breads) {
    horse.show();
    horse.animate();
  }

  // image(animation[frameCount % animation.length], 0, 0);
}