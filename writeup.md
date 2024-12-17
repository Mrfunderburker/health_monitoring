## Question 1

Take a look at the file labeled `data/data2.txt`. Why might we have missing values or values that state "NO SIGNAL" in this dataset? While we are currently ignoring these values, what might be the risk of filtering these values out?

[The values that state "NO SIGNAL" could indicate issues with recording the data or potentially some type of signal or software issues. The risk of filtering these values out is that the results may be biased or ignore important issues that were faced during the data tracking. This can make a more innacurate study.]

## Question 2

While the "averages.png" and "maximums.png" graphs visualize typical values in our time-series data of heart rates and subsequently describe similar trends, the "stdevs.png" graph visualizes the standard deviations, which results in a graph with less apparent trends. In the context of heart rate, what does the standard deviation describe?

[In the context of heart rate, standard deviation can describe variability. If it where to have a lower standard deviation this can indicate heart rates that are relatively stable. An example of this could be when the person is at rest or doing more leisurely activities. However, bigger differences or higher standard deviations indicate greater variability which can be a result of intensive activities, high stress, or other factors.]

## Question 3

Run your `main.py` module and look at the graph labeled "averages.png." Roughly speaking, where do you see the time series experience a significant difference in values along the x-axis? Point out all x-values where you notice a drastic difference in future values.

[I used averages1.png as a reference. If we take a look at the x values we notice the first major drop from 0 to 1 when it goes from around 75bpm to about 62bpm. Then there is a major increase from 10 to 11. it goes from 55bpm to almost 90bpm. At 27, it goes from about 89bpm to 53bpm when it reaches 30. Between 35-40 the heart rate drops, spikes, and drops signifcantly. Going from 50bpm to 80bpm to 55bpm.]

## Question 4

Do you also notice a corresponding difference in values in the "stdevs.png" graph? If so, do these differences align with the "averages.png" graph? 

[I used stdevs1.png as a reference. In the stddevs.png graph, the heart rate is much more erratic having massive drops and spikes in short amounts of time. For the averages.png graph we do see some drops and spikes but not nearly as many as the stdevs graph. The stddevs graph having about 26 major spikes and drops while the averages graph has aproximatly 16 major drops and spikes.]
