import networkx as nx
import matplotlib.pyplot as plt
import graphFormation as gF
from random import random



def statsForGraphs(probaAccuracy=100,nbTestPerProba=100):
    proba=[]
    # Represents the largest clusters related to p
    maxiSizeCluster = []
    degreePerProb=  []
    for i in range(1, 100):
        p = i/probaAccuracy
        maxiSizeClusterTemp=0
        degreeMoy= 0
        for j in range(nbTestPerProba):
            degreeMoyPerG = 0
            print(j)
            g = nx.binomial_graph(100 , p)
            lstDegre = g.degree
            temp = len(max(nx.connected_component_subgraphs(g), key=len).nodes)
            maxiSizeClusterTemp += temp

            for tuple in lstDegre:
                degreeMoyPerG+= tuple[1]
            degreeMoyPerG = degreeMoyPerG / len(lstDegre)
            degreeMoy+= degreeMoyPerG
            g.clear()

        degreePerProb.append(degreeMoy/nbTestPerProba)
        maxiSizeCluster.append( maxiSizeClusterTemp/nbTestPerProba)
        proba.append(p)

    return [proba,maxiSizeCluster,degreePerProb]


def plotRes(resultsArray):
    plt.figure()
    plt.plot(resultsArray[0],resultsArray[1])
    plt.xlabel("Probability")
    plt.ylabel("Nodes Connectivity")
    plt.title("Nodes Connectivity ")
    plt.figure()
    plt.plot(resultsArray[0],resultsArray[2])
    plt.xlabel("Probability")
    plt.ylabel("degree")
    plt.show()


def plotGraph(g):
    pos = nx.spring_layout(g)
    nx.draw_networkx_nodes(g, pos)
    nx.draw_networkx_labels(g, pos)
    nx.draw_networkx_edges(g, pos)
    plt.show()


if __name__ == '__main__':

    # Statistic related to the formation of a binomial graph
    # statistics = statsForGraphs(100) # this params is the precision of the probability
    # plotRes(statistics)

    # (2) simple graph formation
    # g = gF.generateSimpleGraph(100)

    # (2) simple graph with some complexity ( hidden node value during the game)

    # g = gF.generateSimpleGraph(100,True)

    # (3) Realistic graph with karma behavior

    g= gF.generateGraphWithKarma(100)

    plotGraph(g)




