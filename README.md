# GraphGameTheory 

This project was made for my graph theory course. The project goal is to understand the formation of graph with more than 100 nodes. 
Moreover, this project shows how nodes deal when you adding some rules to make the formation more realistic. 

## Getting Started 

These instructions will allow you to understand how to use the project

### Prerequisites

You have to install some packages : 
  
'''
  - NetworkX (2.4 version)
  - MatPlotLib (Last version) 
'''


## How to run some tests 

This section will show you how to run some test. In fact, there is four kind of test in this project

### 1° Random Binomial Graph

With this test, we can see the evolution of the node connection percentage of the taller cluster according to the probability and the 
ditribution of need also according to the probability
'''
statistics = statsForGraphs(100,1000) 
plotRes(statistics)
'''
Here, the algorithm will the statistics related to a graph with 100 nodes, and a probability variation between 0.0 and 0.1 with a step of
0.01

### 2° Simple Graph Game

Here, we can create a graph where a node will chose another node among all node to maximise its value according a rule :
the node value is the sum of the value of these neighbours

In the project there are two kinds of graph according to this rule.
'''
g = gF.generateSimpleGraph(100)
plotGraph(g)
'''
This line will create a graph related to the previous rule

But we can add more complexity with the fact that each neighbour can't know the value of other nodes, it just know that the value is
in the interval : [0.5*realValue, 1.5*realValue] 
'''
g = gF.generateSimpleGraph(100,True)
plotGraph(g)
'''

### 3° More Complex Graph Game

Finally, the last verison of the graph game is more realistic. Indeed, the game is played more than one round. And the node can defect and 
severed the link between an other node if it find a best node. In this case, the node will have a punishment : its value karma 
will increase (formula : times number where it defect / round number). Moreover, a node will prefere a node with a low karma value.

'''
g= gF.generateGraphWithKarma(100)
plotGraph(g)
'''
