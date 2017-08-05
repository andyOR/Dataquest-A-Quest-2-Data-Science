## In this script, we'll see few examples of what an algorithm looks like, and introduce some methods for evaluating their efficiency


## Implementing An Algorithm

# When the algorithm finds Kobe in the data set, store his position in Kobe_position
kobe_position = ""

# Find Kobe in the data set
for r in nba:
    player = r[0]
    if player=="Kobe Bryant":
        kobe_position = r[1]
        

## The Importance Of Modularity And Abstraction

