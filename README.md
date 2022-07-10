# wordleVisualization
My friend and I have texted our Wordle scores to each other every day since January 2022. I decided to collect this data and visualize it. 

I first downloaded our Facebook Messenger conversations as a JSON object, and used regex to extract our scores (since each message has the format "Wordle [Puzzle#] [GuessNumber]/6"). After that, I used SQLite3 to save our data into a database table. I created a csv file from the data, and then copied this csv file into the online editor for p5.js (the index.html and style.css files were provided through the p5.js editor). In the editor, I created the code to draw ellipses that varies in color and width/height. 

The color of each ellipse is based on the month. The width of an ellipse represents my number of guesses for that day's puzzle, and the height of the ellipses represents my friend's number of guesses. 

The "friend1.png" shows the figure that was output based on our data. The recording.mov file shows a video of the animated data visualization for my friend and me. The csv file only has my data. 

According to the program, there were about 82 days where we *both* exchanged scores (for context, there are about ~169 days between January 22 and July 9). As a trend, I noticed that there wasn't a lot of improvement over time for either of us.
