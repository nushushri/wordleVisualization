let table;
let monthColor = "blue";
let rowNum = 81;
let rate = 3;

function preload()
{
  table = loadTable('wordle1.csv', 'csv', 'header');
}
function setup() {
  createCanvas(500,500);
  background('black');
  frameRate(rate);
  // stroke("white");
  // noFill();
  // ellipse(250, 250, 350,350);
  // text("X", 425, 250);
  // ellipse(250, 250, 300,300);
  // text("6", 400, 250);
  // ellipse(250, 250, 250,250);
  // text("5", 375, 250);
  // ellipse(250, 250, 200,200);
  // text("4", 350, 250);
  // ellipse(250, 250, 150,150);
  // text("3", 325, 250);
  // ellipse(250, 250, 100,100);
  // text("2", 300, 250);
  // ellipse(250, 250, 50,50);
  // text("1", 275, 250);
}

function draw() {
    fill("black");
    stroke("black");
    rect(0, 0, 150, 50);
    if(rowNum > -1)
    {
      monthColorFun(table.getString(rowNum,0));
      stroke(monthColor);
      strokeWeight(1);
      noFill();
      textSize(16);
      text(table.getString(rowNum,1), 30, 30);
      ellipse(250, 250, int(table.getString(rowNum,2))*50,int(table.getString(rowNum, 3))*50);
      rowNum = rowNum - 1;
    }
  
}

function monthColorFun(month){
  if(month == "July")
    {
      monthColor = color(200,0, 255);
    }
  if(month == "June")
    {
      monthColor=color(0, 60, 255);
    }
  if(month == "May")
    {
      monthColor = color(0, 255, 229);
    }
  if(month == "April")
    {
      monthColor = color(119, 255, 0);
    }
  if(month == "March")
    {
      monthColor = color(242, 255, 0);
    }
  if(month == "Feb")
    {
      monthColor = color(255, 145, 0);
    }
  if(month == "Jan")
    {
      monthColor = color(255, 34, 0);
    }
}