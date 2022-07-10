# wordleVisualization
My friend and I text our Wordle times to each other every day since January 2022. I decided to collect this data and visualize it. 

I first downloaded our Facebook Messenger conversations as a JSON object, and used regex to extract our times (since each message has the format "Wordle [Puzzle#] [GuessNumber]/6"). After that, I used SQLite3 to save our data into a database table. I created a csv file from the data, and then copied this csv file into the online editor for p5.js (the index.html and style.css files were provided through the p5.js editor). In the editor, I created the code to draw an ellipse that varies in color and width/height. 

The color of the ellipses is based on the month. The width of the ellipses represents my number of guesses, and the height of the ellipses represents my friend's number of guesses. 

The "friend1.png" shows the figure that was output based on our data. The recording.mov file shows a video of the animated data visualization for my friend and me. The csv file only has my data. 

The program was able to extract about 83 days worth of data--not bad considering that there were ~169 days between January 22 and July 9 (when we played) and sometimes we missed exchanging times (we also took a break for about a month). As a trend, I noticed that there wasn't a lot of improvement over time for either of us.
