## In this and course and scripts, we will be learn how to use data visualization
## to communicate data insights and explain them through story telling.


## Introduction To The Data.
#In this script , we will use datset on percentage of bachelor's degrees gratnted
# to women from 1970 to 2012.

import pandas as pd
import matplotlib.pyplot as plt

women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
x_values = women_degrees["Year"]
y_values = women_degrees["Biology"]

plt.plot(x_values, y_values) # line chart for biology degrees in data for all years
plt.show()


## Visualizing The Gender Gap. Visualizing multiple line charts for gender gap

x_values = women_degrees["Year"]
y_women = women_degrees["Biology"]
y_men = 100 - women_degrees["Biology"]


fig = plt.figure()
plt.plot(x_values, y_women, c = "blue", label = "Women")
plt.plot(x_values, y_men,c = "green", label = "Men")
plt.title("Percentage of Biology Degrees Awarded By Gender")
plt.legend(loc = 'upper right') # added legend
plt.show()


## Data-Ink Ratio. It is the fractional amount of the plotting area dedicated to displaying the data
## Hiding Tick Marks

x_values = women_degrees["Year"]
y_women = women_degrees["Biology"]
y_men = 100 - women_degrees["Biology"]


fig = plt.figure()
plt.plot(x_values, y_women, c = "blue", label = "Women")
plt.plot(x_values, y_men,c = "green", label = "Men")
plt.tick_params(bottom="off", top="off", left= "off", right= "off")
plt.title("Percentage of Biology Degrees Awarded By Gender")
plt.legend(loc = 'upper right') # added legend
plt.show()


## Hiding Spines. 

fig, ax = plt.subplots()
ax.plot(women_degrees['Year'], women_degrees['Biology'], label='Women')
ax.plot(women_degrees['Year'], 100-women_degrees['Biology'], label='Men')
ax.tick_params(bottom="off", top="off", left="off", right="off")
# Add your code here

ax.spines["right"].set_visible(False)
ax.spines["bottom"].set_visible(False)
ax.spines["top"].set_visible(False)
ax.spines["left"].set_visible(False)


ax.legend(loc='upper right')
ax.set_title('Percentage of Biology Degrees Awarded By Gender')
plt.show()


## Comparing Gender Gap Across Degree Categories. 

major_cats = ['Biology', 'Computer Science', 'Engineering', 'Math and Statistics']
fig = plt.figure(figsize=(12, 12))

for sp in range(0,4):
    ax = fig.add_subplot(2,2,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[major_cats[sp]], c='blue', label='Women')
    ax.plot(women_degrees['Year'], 100-women_degrees[major_cats[sp]], c='green', label='Men')
    # Add your code here.
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.tick_params(bottom="off", top="off", left="off", right="off")
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["left"].set_visible(False)
    ax.set_title(major_cats[sp])
    

# Calling pyplot.legend() here will add the legend to the last subplot that was created.
plt.legend(loc='upper right')
plt.show()

## In this script, we explored how to enhance a chart's storytelling capabilities by minimizing chartjunk and encouraging comparison


## END
