Format
```
### [Date] — [one-line title]

**Goal today:**
(What am I trying to do or find out?)

**What I tried:**
(Steps, in order. Be specific enough to repeat.)

**What worked:**

**What failed / surprised me:**

**What I changed:**

**Data / files I created:**
(filenames, where they live)

**AI help today:**
(What I used AI for, if anything — see AI Use Rules)

**Questions for Gaurav:**

**Next step:**
```

```
### June 29 — Can an AI actually reason the laws of nature with enough data, or is it simply using what it already knows?

**Goal today:** Set up what I need for this project.

**Data / files I created:** research_notebook.md, notes

**Questions for Gaurav:** None

**Next step:** Begin learning to code and pushing my files to github.
```

```
### June 30 — Basics of coding

**Goal today:** Learn basic Python and push files to githup

**What I tried:** I went through the code academy hello world lesson for learning python in order.

**What worked:** I was successfully able to use commands such as print(), str(), and I could variables.

**What failed / surprised me:** It took me a few attempts to put enough spaces in my message.

**Data / files I created:** code_basics.py, internship folder

**AI help today:** None

**Questions for Gaurav:** "Do I need to fill out all the categories in the notebook, or only ones that apply?" and "Should I do check ins every night, or only nights where I still had work to get through?"

**Next step:** Complete my assignments on Wednesday.
```

```
### July 1 — Learning functions

**Goal today:** Today's goal was to learn and apply functions.

**What I tried:** The main thing I did was learning, but I also created a function that calculates the area and perimeter of a rectangle

**What worked:** I was able to create rectangles and print out the area and perimeter using the str() command.

**What failed / surprised me:** I was struggling to find a way to neatly print out the area and perimeter, but settled on just using the coordinate-like output.



**Data / files I created:** more_basics.py, internship folder

**Questions for Gaurav:** None

**Next step:** Set up for the actual experiment.
```

```
### July 2 — Practice run

**Goal today:** Install tracker and do a practice run of the experiment with house keys and a rubber band.

**Predictions:** Over time the bounces will die out due to drag forces. Theoretically, I believe objects with lower masses will experience their bounces dying out faster. They will have to traverse through more air due to moving faster (because T=2pisqrt(m/k)). I also feel like ive seen a similar things happen with pendulums dying out based on string length, which should be the equivalent to mass according to the equations for simple harmonic motion. Additionally, I think the paddles will accelerate the dying out of the bounces because they also catch air.

**What I tried:** I took a loop of keys and tied a rubber band around them such that if the keys moved at all, so would the band, and vice versa. I then put the rubber band on a ring stand and pulled a key while recording.

**What worked:** After a few attempts, I was able to successfully get the keys to move following harmonic motion.

**What failed / surprised me:** At first, after the first bounce the keys would immediately freeze. I think this was due to the keys going so high that the rubber band no longer had tension, making the elastic potential energy fall to 0, completely ruining the motion. 

**What I changed:** I realized adding more mass should work as that would pull the rubber band down, meaning after moving a bit, there would still be tension. Adding more keys did the trick.

**Data / files I created:** Keys_test_run.MOV, internship folder
(filenames, where they live)

**Next step:** Assignments for Friday and using the tracker
```

```
### July 3 — First Run of Tracker

**Goal today:** Using tracker to see what happens as the from yesterday keys bounce

**Predictions:** I predict that the height of the keys over time will move in a sinusoidal motion, that is diminishing. Over time, both the low and high points will be brought closer to 0, yet theoretically the period will remain consistent. Eventually the bounces will seem more stable when the keys switch to a more pendulum-like motion rather than up and down bounces. I predict it will take roughly 15 bounces for this to happen.

**Results:** The keys bounced roughly 10 times before the motion became minimal, but seemed to even have some motion up to 20 bounces. I thought that the motion by the time of 10 bounces is roughly what would be seen at 15, though, so I was incorrect on my prediction in that.

**What failed / surprised me:** The data was surprisingly clean, up until around after 10 bounces. I also noticed while doing the tracking that later on, the keys started moving left and right in the frame, rather than just up and down. This does support my hypothesis that the keys would move more like a pendulum, as I noticed in real life during the recording. The data also got messier around this time. 

**What I would change for next time:** During the real run, I will need to make the ruler more level in the plane, and I should try to ensure the spring cant swing side to side. This is both to prevent a switch to more pendulum-like motion, which would mess up energy calculations as the amount the spring is stretched would be higher and mess with the results. I also saw the keys rotate. I don't think this would happen with a spring, but either way I should try to insure the massses are connected in a way that prevents rotation from happening as that transfers some energy and may mess with the calculations

**Data / files I created:** Tracker_First_Run_Data.csv and Tracker_First_Run_Graph.pdf, internship folder

```

```
### July 6 — Control Flow

**Goal today:** Go through the control flow lesson in codecadamey and push a project to the repo.

**What worked:** I was able to get through the lesson with no problems

**What surprised me:** I noticed you could input multiple checks into an expression, though I didnt use this. (For example, you could put "if 10 >= age >= 20:" and it would work)
```

```
### July 7 — Basics of Lists

**Goal today:** Learning the basics of using lists

**What surprised me:** I was a little surprised by the using 2D lists, but I got the hang of it pretty quickly.

**Data / files I created:** I moved all the coding practice to a new folder called Learning Coding and Practice. I also created list_basics.py
```

```
### July 8 — Finishing lists and Data

**Goal today:** Learning more about using lists in python, but also working with the data for my first tracker run.

**Spreadsheet notes:** I noticed in the data that each points contained 3 pieces of information, but for a lot of points only one piece of information was present. This is confusing, but I think what happened was that the data included every frame, but not points as I did not actually use the tracker for those frames. This makes the data messier and in need of cleaning. Its still possible to follow, but it does bury the bulk of the actually relevant information. Removing those points would help. Also, a lot of the points I did put data for look random in the spreadsheet. Some of them are just super far from other data points. Perhaps some of those should also be removed to make it easier to work with.

**What I tried:** It took me a bit to understand it, but eventually I made a python file to run code involving my first tracker run.

**What worked:** I successfully imported pandas, and was able to eventually get my code working. I also had no issues with finding the file path as right clicking the file in vs code let me copy the path. I had no issues with learning how to use lists.

**What failed / surprised me:** It took me a few attempts to get my code working, but I realized I missed some quotation mark and I got it to work.

**Data / files I created:** tracker_first_run.py, internship folder.
```

```
### July 9 — Learning Loops

**Goal today:** Complete the Codecadamey loops lesson and find the max height of the keys on my first tracker run

**What worked:** I had no problems creating a function to convert from centimeters to meters nor with printing. It took a bit of time to get the code to find the max height working, but I eventually got it to work. 

**What failed / surprised me:** I struggled a bit to get the max value for the data file. When using the function initially, it was printing the max values for every column, but eventually I figured out how to limit to only the column I needed with enough research.

**What I changed:** I updated tracker_first_run.py as mentioned above.
```

```
### July 10 — Plotting Data 

**Goal today:** Using matplotlib to plot my data

**What worked:** I imported matplotlib with no issues. It took a few minutes of researching, but eventually I found the information I needed to plot my data. It was a much quicker process today than trying to get function code during the previous days. There is not much to comment on today as it was only a few lines of code. I did notice that I find it easiest to get my code from websites that specifically tackle the problem I have, such as using matplotlib to read python columns. Google's overviews may not always understand the question nor how to answer it, and stack overflow typically has more complicated questions that contain information that doesn't actually help me.
```

```
### July 13 — Assembling and more code practice

**Goal today:** Assembling the masses and foam paddles as well as practicing cleaning my data myself

**What worked:** I had no issues with making the foam paddles. I also was able to clean my data quite quickly, with the biggest struggle being trying to drop the lines containing missing data. I also modified the relative paths of my code to account for the fact the files are in a folder. Thankfully VScode makes finding the relative paths easier

**What failed / surprised me:** There were a few issues with assembling the masses, so I couldn't make those yet. Also the spring seems to be too small, as pulling it down would require it to go upwards too far, meaning tension is lost. I noticed in my coding that stack overflow was much more helpful today, and I think I overall got better at using google to research what I need to do. I struggled removing the lines with missing data not because I didn't know the command, but rather simply because I didn't know I needed to assign that data to a variable. I eventually figured it out, though.

**Data / files I created:** tracker_first_run_cleaning.py and My_Tracker_First_Run_Data_Cleaned.csv, which were both put in a new folder containing all the first run information: Tracker First Run
```

```
### July 14 — Practicing merging data and reading it

**Goal today:** Merging sample data with my tracker data and plotting it

**What worked:** I quite quickly managed to combine all the data into 1 column and turned it into a csv file. I had no issues renaming columns or locating columns as I was able to figure it out quite quickly with google.

**Observations:** I noticed that the line that has more damping has the larger paddles. This makes sense as those paddles are catching air and likely causing drag forces, which supports my earlier predictions. The damping seems to make a huge difference early on as the mass with the small paddles oscilates much more, yet still on the same period. Eventually, the bounces of both die down though.

**Data / files I created:** merging_sample_data_and_comparing.py and sample_data_merged_with_my_data.csv
```

```
### July 15 — Codecademy review

**Goal today:** Review a lot of what I learned with Codecademy

**What worked:** I was able to work with most of the functions. Today took me longer than most days with Codecademy relative to their estimated time (though it still went at roughly the estimated pace). This is probably because the code is less fresh in my head and took more effort to get working. I noticed loops took me the longest to grasp, probably because theres just so many ways to do loops (especially considering for loops, while loops, and if statements),

**Data / files I created:** code_challenges.py in the Learning Coding and Practice folder
```

```
### July 16 — Explaining code

**Goal today:** Write a walkthrough of my code

**Code explanation:** The first few lines of code are just to grab the necessary data. The usecols input allows me to remove the x column, which was not included in the other data and not necessary. I used a rename function to change the column names for my tracker data before getting the columns for the other data. I did this because renaming the columns for my tracker data is only 1 line of code, but it would be 3 if I wanted to rename the columns for all of the other data instead. The next bunch of lines just added in some columns that would be useful for data, such as mass and paddles. I then had some commented out print commands just to view that the data did indeed get converted properly. The next line of code combined all of the data into one. I found a few different functions that would do this, but .concat allowed me to input all 4 datasets at once rather than 2 at a time. I decided it would be clean if ordered them by putting my tracker data first, then did least paddle size to greatest. It was one of the last lines of code in the first part because I needed to ensure all the data was complete and organized properly before I could combine it. I again used a print command to check the data. The to_csv line turned that combined data into a csv file. Index is set to false because otherwise that data would be numbered by an index, which would be unnecessary. 
I imported matplotlib.pyplot at the start of the second part as it was not needed earlier. The first line following that command just took the data from the new file. The 2 following lines found the specific data I was searching for, the data with large and small paddles. I specifically chose large and small paddles because that allowed me to locate using the same column for both datasets. If I chose none, I would also end up locating my tracker data, so I would need to use a different column or perhaps multiple pieces of information in order to get it work. I had print commands to ensure I actually got the correct datasets. The first 2 lines after that tell matplotlib what I wanted to plot (both the data sets and the actual columns to pay attention to). The next 3 lines labeled the graph, and the line after that created a grid. The .legend function tells matplotlib to label the first line 'small paddles' and the second line 'large paddles'. The last line of code is what actually shows the graph of the data.
```

```
### July 20 — experiment setup

**Goal today:** Build and test the masses

**What failed / surprised me:** The eye bolt was way more heavy than expected, so I had to modify the numbers in order for the experiment to actually work. The masses were a little inconsistent, but I managed to find working numbers. My dad and I modified a few things to accomidate for the materials we had.
```

```
### July 21 — Doing the runs

**Goal today:** Recording all the runs.

**What worked:** My set up allowed me to record the videos well.

**What failed / surprised me:** I couldn't actually get through all the runs, especially because they took much longer than expected (4 minutes for a lot of the runs, rather than the expected, 10 seconds to a minute). I had to end the videos early to ensure that the files could even be moved, and most of them are too large to be pushed to github. In fact, the motion could've probably continued for 10+ minutes with a lot of the runs, especially based on the data from the tracker run. I also had to end that early, as it was taking really long and there may need to be some changes to the set up for it to be viable to do 15 runs. This wen't unnoticed in the test run because I used the 6 inch paddle as I wanted to ensure that the spring could withstand the weight.

**What I changed:** Since I am using a yardstick, My data will be collected in inches. There is a direct conversion from inches to meters, which I can use if necessary.

**Data / files I created:** run1_M1_P0.mov, run2_M1_P2.mov, run3_M1_P4.mov, run4_M1_P6.mov, run5_M1_P0.mov, run1_M1_P0.csv, run1_M1_P0pdf.pdf. Most are not accessible due to being too large.
```

```
### July 22 — Finding the period with actual data

**Goal today:** Using the actual data to find and check the period.

**What worked:** I had no issues cleaning the file or plotting it, which makes sense considering that I have already done that. I copied the code over and changed the information in them to match the new information, but I would not have any issues manually writing something like usecols=range(3), and I frequently used the pd.read_csv function anyways. I wrote the model function and numpy worked fine. I successfully guessed that np.pi would give the value of pi, so writing the code to find omega was no problem. I decided to use code to find the first peak in my data, and after some lines, I managed to plot 10 seconds and count the number of peaks from the first to 10 seconds later. I used this period along with a for loop to create grid lines at exactly where each future peak should be in a plt plot. The peaks almost perfectly lined up with the grid lines, suggesting that period indeed is constant.

**What I changed:** I decided to turn the plotting and cleaning into functions, so that in the future I can run my already written functions to complete the necessary tasks. It took me a bit of research and thought, but I managed to even automatically change the name of the files so that I could create a new clean one.

**Data / files I created:** run1_M1_P0_clean.csv, under the data folder in experiment, and fitting_data.py in the experiment folder.
```

```
### July 23 — All 15 runs

**Goal today:** Record the 15 runs

**What I tried:** I recorded them the same way as last time, but with 90 second recordings. I had to change this, however. I had no issues pulling the masses down 4 inches (using inches instead of centimeters due to it being a yard stick), though the bounces weren't perfectly straight. The paddles didn't seem to have any effect on how straight up and down the bounces were, though, so it seemed to be based on my release angle and how precisely I hooked the eyebolt to the spring. If any run veered off too much, I decided to just restart them, so all the swinging is small or not even noticeable. Recording took about an hour, and I was able to multitask. (I renamed and pushed files from each batch while recording the next).

**What failed / surprised me and what I changed:** The first few runs all ended up being close to 100 mb, one of which went over. We decided it would be best to decrease the recording time as I was already recording 30 fps HD. Some of the files for the last few runs were 40 mb larger than the others, so I decided, so I decided to put them into a google drive as even with my dad's help, we couldn't easily compress them.

**Data / files I created:** 15 files for the videos, and runs.csv, all in the data folder. experiment/data/videos/run01_M1_P0.mov, experiment/data/videos/run02_M1_P2.mov, experiment/data/videos/run03_M1_P4.mov, experiment/data/videos/run04_M1_P6.mov, experiment/data/videos/run05_M1_P0.mov, experiment/data/videos/run06_M2_P0.mov, experiment/data/videos/run07_M2_P2.mov, experiment/data/videos/run08_M2_P4.mov, experiment/data/videos/run09_M2_P6.mov, experiment/data/videos/run10_M2_P2.mov, experiment/data/videos/run11_M3_P0.mov, experiment/data/videos/run12_M3_P2.mov, experiment/data/videos/run13_M3_P4.mov, experiment/data/videos/run14_M3_P6.mov, experiment/data/videos/run15_M3_P6.mov runs 11-15 are also in a google drive.
```

```
### July 24 — Basics with strings

**Goal today:** Start the Codecadamey lesson strings.

**What worked:** I completed the lessons in strings with no problems. It was very useful to learn that strings are basically lists of characters, which made it much more intuitive how things like indexes work with them. The course asked me to use a few for loops and functions, which I had no issues doing as I have gotten quite familiar with them.
```

```
### July 27 — Beginning tracking

**Goal today:** Begin tracking the videos

**What worked:** I tracked runs 11, 15, and 08 successfully and made their corresponding .csv files. It took about an hour to do, some of which was just spent familiarizing myself with the tracking process. The sideways swings made it slightly harder to track them, but it overall went well.

**What I changed:** I decided to go by every 3 frames rather than every 5 to make the data less random and to increase the number of clear peaks. Based on how few points are between each peak and trough, I think this was the right decision.

**Data / files I created:** experiment/data/run08_M2_P4.csv, experiment/data/run11_M3_P0.csv, experiment/data/run15_M3_P6.csv
```

```
### July 28 — Tracking the first 6 runs

**Goal today:** Track runs 1-6.

**What worked:** I had no issues tracking runs 1-6 and plotting the data of runs 11 vs 15. It seems run 15 died down quicker according to the graph, matching with the theory that paddles increase drag and therefore increase damping. I continued tracking these runs going 3 frames at a time and it took about an hour to complete. I used working_with_data.py to do the plotting, and I used the code I had used when working with sample data, though slightly modified since the data was not combined.

**Data / files I created:** experiment/data/run01_M1_P0.csv experiment/data/run02_M1_P2.csv experiment/data/run03_M1_P4.csv experiment/data/run04_M1_P6.csv experiment/data/run05_M1_P0.csv experiment/data/run06_M2_P0.csv experiment/working_with_data.py
```

