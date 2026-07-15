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

