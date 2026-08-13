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

```
### July 29 — Finishing tracking

**Goal today:** Track the remaining runs (7, 9, 10, 12-14)

**What worked:** I had no issues tracking the remaining runs. I plotted the data of runs 1-4 in working_with_data.py. I used a for loop this time since there were 4 dataframes rather than 2, which made the code much more condensed and scalable. It also matched the theory that paddles increase drag and therfore damp the motion. Run 2, despite having a paddle, didn't seem to damp that much, though I think it is because the paddle was small. Run 3, with a 4x4 paddle, had a significantly more visible damping, and run 4 was even more damped. 

**Data / files I created:** experiment/data/run07_M2_P2.csv, experiment/data/run09_M2_P6.csv, experiment/data/run10_M2_P2.csv, experiment/data/run12_M3_P2.csv, experiment/data/run13_M3_P4.csv, experiment/data/run14_M3_P6.csv
```

```
### July 30 — Combining Runs

**Goal today:** Combine all the runs

**What worked:** I successfully used a list of all the files along with a for loop to create pandas dataframes, extract the run#, paddle key, and mass key, of all the runs. The only thing that took me a second was figuring out how to get all the dataframes into a list, but I realized I had just used the wrong bracket and I quickly fixed the code. I noticed that the pd.concat code uses a list, hence why I used a list to combine all the files in this case. It took me about 10 minutes total, and I worked in working_with_data.py

**Data / files I created:** all_runs.csv
```

```
### July 31 — Fitting my own Data

**Goal today:** Fit my own data for run 4

**What worked:** I had no problem using my older code but slightly updated to makes guesses for my period, plotting, and creating functions. The only issue I had was an indexing error because pulling run04 kept the entire indeces, but using the head command didn't but I realized that entire step was uneccessary quite quickly and realized I could just use the dataframe for all the data instead anyways. I got a pretty good prediction for omega, so I ran that and the fit had no issues getting the period perfect. Here are the numbers it got [1.37350787e+00  8.52685833e+00 -8.08605110e-03 -3.36909913e+00]. The graph of the residual appeared to follow asymptotes similar to hyperbolas, slightly rotated. There is a moment in the middle where the swap between the predictions having a magnitude too low and too high is visible. 

**What failed / surprised me:** The function does not have a damping factor, so the graph was completely unable to damp. I didn't have any ways to change this without completely rewriting the function, so I compared what I could: the location of the peaks, which matched up.

**Data / files I created:** experiment/fitting_my_own_data.py
```

```
### August 3 — Fitting the Damped Model

**Goal today:** Using the damped equation to fit my data.

**What worked:** I mostly used the old data code, but added a new term as well as a gamma input for the function. I had no issues doing this, and got a really good fit line. The predicted values I had were already pretty good, so this worked fine. The only one that was different from the values given by the function last time was the A0 value. I believe the code gave a lower value for A0 as it is a measure of the amplitude, and without damping it is better to use the average amplitude. That fits the curve better than the starting amplitude because the error isn't as large towards the end than it would otherwise be. This is why the value after adding damping is much higher, as it is able to actually shrink and reduce error. I was a little surprised that A was lower than the number I calculated, but perhaps the rate of damping is just barely not constant enough that this slightly lower number fits better.

**Observations/Predictions:** I printed popt and got these values. [ 2.97221638  0.05275184  8.52389841  0.02432687 -3.36850759]. The old valeus were [1.37350787e+00 (0) 8.52685833e+00 -8.08605110e-03 -3.36909913e+00] I noticed that the values for omega and C are basically the same as before, though phi and A are different. A makes sense for the reason explained above, though I don't know why phi would differ between name and before. It was already very small, however, so this could just be a slight change due to omega also changing ever so slightly. I plotted the residual today and it looked like basically random noise that's only pattern was having highs and lows on somewhat regular intervals, though with almost random (small) magnitudes. I plotted Friday's residuals against today's residuals and noticed something strange. Between 10 and 15 seconds, Friday's had a little portion that looked like a heartbeat because the magnitude of the amplitude of the curve from the fit switched from being too low to too high. Interestingly, in this timeframe, the values for residual for the new curve lined up almost perfectly. My only guess as to why this could've happened was that this happened due to the magnitudes being similar. This is where the magnitudes of the amplitudes should line up, so the residuals should be caused by the imperfections in the way something bounces on a spring. Perhaps the curves fit well enough that those bounces were the only problem there. This also makes sense because it seemed the residuals lined up on the same period most of the time, though this wasn't always true. Other than that, the residuals look completely different because Friday's were just way larger.
For my predictions, I imagine gamma will be much higher with larger paddles and much lower with smaller paddles. There should be more damping, so therefore a higher value for gamma. For the run with no paddle, there should be a near 0 value for gamma as it should theoretically almost not dampen at all.

**About the springs:** I tried a few springs before settling on the final ones, each which had their own problem. The first few springs were problematic because they were super small and super powerful. I could immediately tell they wouldn't work because I could barely stretch them, and even the heaviest of the weights we had wouldn't do enough. Additionally, them being extremely small meant it was hard to put things on them, which made actually using the weights hard. Sometimes they would just fling off as well in our testing, which was definitely not good. Then, we found weaker springs. The problem with some of them was that they couldn't handle the near 300g weight of some of the builds, meaning they would be broken by the time all the trials were done. The spring I settled on was the best of the weaker springs, allowing me to easily stretch it, record it, and not worry about it breaking from all the weight.

**Data / files I created:** experiment/fitting_the_damped_model.py
```

```
### August 4 — Fitting all Runs

**Goal today:** Fit all 15 runs and create a file with the numbers needed for the fitted curve

**What worked:** I had no issues using a for loop to get all the information necessary to get the fitted numbers, nor make the lists. I completed most things quickly with minimal issues. Most of the graphs looked right, but there were some odd things I noticed. I compared the values I got this time around to last time for run04, and they were almost identical, suggesting it went well. I wasn't entirely sure if I should've separated each value before converting the dataframe into a csv file or just kept them together, but I decided to keep all the values together as it would be easier to plug into a function and also quite easy to separate.

**What failed / surprised me:** It took me a bit to understand certain errors, like why I had issues filtering by mass keys, but then I understood I needed to use .all in some way, did some research along with error checking, and managed to figure out how to get it to actually filter. I did notice I could've also just filtered by the run number, knowing the mass keys of each run, but decided it would be better to actually learn how to filter the way I did

**Observations:** I noticed when doing the plots that almost all the plots looked extremely good, except run 15 which looked incredibly wacky. I don't know for sure why specifically run 15 had this happen, but I noticed that sometimes its peaks would be significantly higher or lower than the previous ones, so the fit line looked much more random. Other than that, though, the fit lines were really good. I checked the gamma values, and in each mass group, a larger paddle meant a higher gamma value, supporting my prediction. Additionally, I noticed that the larger masses experienced slightly less damping than their lower mass counterparts, supporting one of my earlier theories that the larger masses should dampen, which I predicted would be due to them going through the air slower (because of the period equation), hence reducing drag. Interestingly, their omega values were also lower, suggesting that the period is indeed lower (matching the period equation). This explains why run 4 damped the most, as it was the lowest mass and highest paddle, whereas run 11 damped the least as it was the opposite.

**Data / files I created:** experiment/fitting_all_runs.py, and experiment/data/fitted_params.csv
```

```
### August 5 — Using scatterplots

**Goal today:** using scatterplots to compare mass and omega, as well as paddle size and gamma.

**What worked:** I first fixed the table from yesterday, with the hardest part being getting the paddle sizes, as it took a few attempts to actually get the keys. I made the new lists and updated fitted_params.csv. I used this file when making my scatter plots, and had no issues doing so.

**Observations:** Omega decreased as masses increased, matching my earlier predictions. Omega decreasing, means a longer period (I misstyped this yesterday). This follows the period equation (which predicts that mass increases period). The omega values valued a decent bit in each mass group, but there is still a very clear trend line showing omega decreasing with mass. In the gamma verse paddle_size plot, it appears gamma increases with paddle sizes. It too varies a lot in each paddle group, with the sort of following a power curve, but it is unclear due to the fact there are only 4 sizes. Sizes 0 and 2 are pretty similar to each other, but by paddle size of 6, it becomes significantly clearer that paddles have a huge impact on gamma, meaning they increase decay rate as predicted.
The twin runs have similar numbers in some aspects, and very different numbers in others. Both pairs have A values that are opposites, but that makes sense because the amplitude hasn't changed, only the sign. They have differing phi values, which just means the phase is different (which basically means they don't start at exactly the same times). The C values are surprisingly similar, but similar to phase shifts, they can easily change with the smallest of differences in conditions. The gamma and omega values should be similar, and they indeed are quite close. They aren't perfect, however, as the gamma values in run 1 vs run 5 are 0.0014 away, and omega values are 0.06 away. These aren't the largest differences, but they are relatively big still. Run 7 and 10 have closer gamma and omega values, though.

**Data / files I created:** experiment/scatter_plots.py
```

```
### August 6 — Writing the prompts

**Goal today:** Write the prompts for the AIs.

**Prompts:** 
I did an experiment where I pulled down and released a mass hanging from a spring with a paddle adding air resistance. The first column is time in seconds, and the second is vertical displacement. What equation describes this motion and what does each part of it mean?

I did an experiment, and here is the data that came from it. The first column is time in seconds, and the second is a measurement. What processes could produce this data and what equations would fit it?

I have this data with 2 columns, column 1 and column 2. Find some equation that can relate the data in these columns and explain how you got to it.

I did an experiment, and here is the data that came from it. The first column is time in seconds, and the second is a measurement. What processes could produce this data and what equations would fit it? How confident are you in your answer and what in the data supports it?


**What worked:** I had no issues with the code portion for today, and I spent some time on writing the prompts.

**Predictions:** The models should have no issues with the first rung. I think they will struggle on the second rung, and can probably figure out that its oscillations, but maybe not where the oscillations came from. I think they will be able to figure out time on the third rung, but not the fact that its oscillations nor what the equation is. I think on the fourth rung, they will not be able to come up with the equation nor that its oscillations specifically, but they should be able to figure out that its an oscillation-like motion.

**Other notes:** Some other interesting ways to challenge the AIs I thought of are to move around the columns so that time isn't always increasing linearly, and perhaps even organize it by height. That could force them to think about how to look at the data differently. Another interesting trick would be to do some transformation to the data, such as give it in seconds squared, so that the AIs would have to figure out the equation using data like a human would, without knowing what the final units would be. This approach would be similar to something like measuring gravity, which is in meters/second squared, but realistically you would be recording that in meters vs seconds (so reasoning would be needed.)
To answer the question from last check in, I assume damping grows faster than paddle side length because what matters is not the length nor perimeter, but rather surface area, especially in the direction of motion (up and down). This means that the damping should theoretically change with side length squared (since the paddles are squares).

**Data / files I created:** experiment/separating_runs.py
```

```
### August 7 — Strings

**Goal today:** Finish the Codecademy strings module.

**What worked:** I completed the rest of the strings module with no issues. I did both projects, and was able to get them to work successfully. I already had experience working with both ciphers used in the project, so they were familiar in that aspect.

**Predictions:** I do not think AIs will describe run04 and run11 differently. From my experiencing with them, they typically do not point out differences unless prompted and instead focus on patterns. For example, I have given ChatGPT an answer key with errors before, and told it was from an answer key. It immediately assumed that everything was correct, until I pointed out the errors, after which it agreed that there were 3 errors in the problem on the key. I imagine a similar case would happen the second it sees oscillations, not commenting on the damping but rather the equation. The only possible difference I imagine is that they might default to using the simple equation for run11 and the damped equation for run04 just because run11 may be closer to the simple patterns. 
```

```
### August 10 — Modules in Codecademy

**Goal today:** Complete the lesson and video for pythonn modules in Codecademy

**What worked:** I completed the lesson quickly with no issues. I am already quite familiar with modules as I have been using them frequently throughout the internship. The lesson mainly focused on the datetime and random modules, which I had no issues using.

**For tomorrow:** It will be important to pay attention to the wording of how AIs talk about things. Using different equations for differnt runs, or using different adjectives, is a sign that the AIs view the runs differently.
```

```
### August 11 — Prompting GPT

**Goal today:** Prompt ChatGPT and read analyze its answers

**What worked:** I quite quickly grasped the code and filled in what I needed to run it.

**What I changed:** I know that AIs like ChatGPT use markdown and LaTeX. The answers were hard to read, so I put them into a .md file and modified them slightly so that I could see what they said in the VScode view mode. 

**Answer observations:**

Rung 1, Run04: The AI was able to correctly get to the equation for damped harmonic oscillators, and did work off the actual data. It correctly explains each portion of the equation.

Rung 2, Run04: The AI once again got the correct equation and thought it was a damped harmonic oscillator, but showed signs of less confidence. It also lists physical processes that could've been responsible, but doesn't know which it was. It gave a second equation with a sine function as well, suggesting there is another process that might be confusing it. It also considers the possibility the oscillation does not fully decay. It created an equation using the actual data.

Rung 3, Run04: The AI got a slightly different equation this time, guessing that a portion of the amplitude does not dampen. It still guessed that it was a decaying oscillation, but didn't know what the measurements were so used x instead of t. It created an equation using the actual data.

Rung 4, Run04: The AI got the corect general equation, and made a rough equation for the data it was fed, even using a round function to account for the added messiness in the data. It again listed a few things that could cause this data, but wasn't sure on which. It claimed high confidence of the data being oscillations, but more moderate confidence in its numbers and low confidence in the physical mechanism, which makes sense based off the data.

Rung 1, Run11: It correctly guessed the governing equation, though used beta instead of gamma. It commented on how there was "weak decay", showing a difference to run04. It also comments on how it "only slowly los[es] amplitude."

Rung 2, Run11: It got the general equation, but used a noise factor of epsilon of time. The big important thing is that it did NOT have a decay factor at all this time, and had a first guess of simple harmonic motion. The equations contain numbers guessed from the data as well, like in all other runs. There were a lot of interesting equations that the AI came up with, but it even says the data does "not show a decaying envelope" and says that if there is damping, the system is likely "being driven or is in a steady-state oscillation."

Rung 3, Run11: Once again, it got the general equation but did not put in a damping factor. Again, it uses x instead of t, and even uses an x_0 for a shift instead of phi. It says the difference between the data and the guessed equation probably comes from noise, rounding, and slight irregularities. The AI does not guess what process caused this.

Rung 4, Run11: Once again, the equation contains no damping. It says that the equation was nearly sinusoidal and comments on how the data is periodic and rounded. It comments on no obvious growth, decay, or drift, unless gamma is very small, but it did at least adress the damped harmonic motion equation. It says that possible processes could've been simple harmonic motion as well as other things, though doesn't seem to ever apply it could've been from a spring moving up and down. The AI said it was very confident (in fact it appears to be near certain) that the data is from a periodic oscillatory process that has some noise, but is significantly less confident on the exact process.

**Other notes:** I haven't tested the guessed equation, so I don't know if they are actually good guesses or completely stray away from the actual data the AI was fed. I was right about the AI starting to struggle at rung 2 onwards, though am somewhat surprised it mostly still got that the equations were from harmonic motion. There were some differences between the guesses the AI had in run04 verse run11, and I was right that the biggest difference came from the potential to use the simple equation rather than the damped one, which seems to have happened for most rungs. I am surprised it specifically mentioned the weak decay in rung 1, though.

**Data / files I created:** experiment/all_answers_readable.md, experiment/read_answer.py

**AI help today:** No AI help, just prompting.
```

```
### August 12 — Prompting Claude

**Goal today:** Prompt claude and compares its answers to GPT.

**What worked:** I had no issue getting the code to prompt claude working nor any issues with printing it. Thankfully this time I didn't have to do many adjustments and the raw answers are almost all readable in a markdown file.

**Answer observations:**

Rung 1, Run04: Claude was able to get the correct equation, though used a fractional form rather than gamma * t. It also gave an equation using my numbers, and worked off of them. It thoroughly even used the numbers to claim that the data shows light damping.

Rung 2, Run04: Claude came to a nearly identical equation as last time, this time immediately giving fitted numbers rather than the general equation. It very confidently calls it a lighty damped "high-Q resonator". I don't know what those are, so can't easily comment on accuracy. It does later mention that a mass-spring-damer is such an example, and claude doesn't claim to know the exact process.

Rung 3, Run04: This itme claude used the standard gamma * t style equation, and again decided to immediately skip to actual numbers instead of giving a general equation. The equation comes from actually analyizing and pattern matching as Claude says that if you look at the shape, you can see the swing size getting smaller, which is typically that general equation.

Rung 4, Run04: "NO TEXT RETURNED (stop_reason: max_tokens)"

Rung 1, Run11: Claude gave the correct general equation, including damping, then fits it to the numbers, assuming the units are centimeters. It assumes that the center being below 0 is because of gravity, not because of the way the tracking works. Claude specifically calls out how the damping is very tiny and almost so small that the noise over powers it.

Rung 2, Run11: Claude gave an equation that fits to the numbers with no damping included. It correctly states taht a process that could produce the equation is an undamped or lightly damped oscillator, and specifically calls out how the damping factor might've just been too small in my data. Claude seems to be also saying that if you look at the residuals after doing more math, you could get more precision on the processes involved.

Rung 3, Run11: Again, Claude gave an equation that fits the numbers with no damping included. It again suggests looking at the shape to see the 'pure periodic signal'. It seems to miss the chance of a very light decay entirely.

Rung 4, Run11: Claude first explained prtions of the data before giving the equation that fits. It calls out how the noise in the data is coming from integer rounding, and says there is no evidence of measurement noise. iT does at least consider the possibility of a damped oscillator, but thinks it is unlikely. It is very confident the only noise is integer rounding and is not confident on what the process is, matching up with its guesses (as mass-spring was one of its last guesses).

| rung | run | gpt | claude |
|---|---|---|---|
| rung1 | run04 | recognized | recognized |
| rung2 | run04 | recognized | recognized |
| rung3 | run04 | reasoned | reasoned |
| rung4 | run04 | recognized | N/A |
| rung1 | run11 | recognized | recognized |
| rung2 | run11 | reasoned | reasoned |
| rung3 | run11 | failed | failed |
| rung4 | run11 | reasoned | reasoned |

**Other notes:** Once again, I didn't check how well the numbers fit. I noticed Claude was more thoroughly checking for errors in the data than GPT was, and gave many suggestions to make the data clearer. Claude also noticed some oddity in the data it seems GPT missed.

I gave models "failed" only if they both didn't get the damped equation nor even considered the possibility of damping. I also gave "failed" if there was not even a mention of a spring-mass oscillator.
I gave "recognized" unless there is actually some sort of explanation how the equation was gotten to, rather than just an explanation of the equation itself.
This was the best approach I could come up with, but GPT implied, and Claude basically stated, that when they see the up and down swinging of oscillations, they assume it follows the sinusoidal model of C + A * cos(2pi/T(x-x0)) or something similar.
For rung 3 run 11, both AIs seemed to reason well, but didn't offer any real processes that could have been involved. Claude seemed to be focused on AC singals, voltage, and DC offsets.

**Answers to the 5 questions:**
1) Both models handled the ladder the same according to the table, though I did notice Claude gave more detail. They both approached things differently, with GPT being more explanatory and Claude focusing more on searching for errors.
2) Claude was a little better with telling run04 and run11 apart as it gave significantly more details about the decay factors. Overall, they both mainly gave differences behaviorally by focusing more heavily on the undamped equation for run11, except for in rung 1.
3) Both models on rung 4 run11 gave high confidence (using the same 95% number) that it was oscillatory, and they both were not confident on the exact process. They both were very confident in rung 1, and less so confident in later rungs, but all throughout seemed mostly confident in the equation being oscillations. They were both very confident that there was no damping in run 11, despite the fact that basically any physical process is going to have (very light) damping because of entropy.
4) The twin runs were good at showing error. The AIs reaching the same conclusion suggests that the data does have a pretty concrete pattern. The similarities suggest those equations are actually quite good guesses, but it could also mean the AIs were trained similarly and therefore see the same patterns, even if the patterns are wrong.
5) The AIs behaving differently because they assumed different equations for run11 and run04 seems to haev held up as I predicted. The AIs did both consider damping a few times in run11, which means there is a little more going on than I thought there would be.

What surprised me the most across this experiment was the actual damping itself, which eventually determined the runs that we would use. I did originally predict that the runs with larger masses and smallest paddles would damp the least (that run was run 11, which matches up), but it still felt counter intuitive. This only made sense to me because of the physics equations, but it sounds insane to say. The friction force, for example, increases with mass (mu*mg*costheta,most of the time.) 
Designing the questions was an interesting challenge because it required carefully saying enough to get the AIs to discuss what I wanted them to without even hinting as to what I was doing. I couldn't even really say "experiment" as that could suggest what I did was measure controlled variables and almost completely eliminates possibilities like measuring the distribution of random numbers. Physics is concrete, writing is not.
I don't think I would change how I use AIs in schoolwork. I have always tried to give them as much context as possible, and I have generally been good at catching their errors (which I have seen them make a few times). It seems newer models are better at doing this work, which makes them even better at what I use AIs for -- checking and understanding the process to get to my answers.

**Data / files I created:** experiment/all_answers_readable_claude.md, experiment/data/claude_answers.csv

**AI help today:** No AI help, just prompting.
```

