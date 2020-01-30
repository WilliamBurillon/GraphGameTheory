import networkx as nx
from random import  randint
from random import uniform
import matplotlib.pyplot as plt



def generateSimpleGraph(n,addComplexity=False,withKarma=False):
    firstConnectionDone = False
    maxTimer = 1000
    g = nx.Graph()
    if addComplexity:
        if withKarma:
            for i in range(0, n):
                # showingValue is the value display to neighbor node before connection : [min = 0.5*value, max = 1.5*value]
                g.add_node(i, value=0, rdnTime=randint(0, maxTimer), label=i, showingValue=[0, 0],karma = 0, nbDefect = 0 )
        else:
            for i in range(0, n):
                # showingValue is the value display to neighbor node before connection : [min = 0.5*value, max = 1.5*value]
                g.add_node(i, value=0, rdnTime=randint(0, maxTimer), label=i,showingValue=[0,0])
    else:
        for i in range(0,n):
            g.add_node(i,value = 0, rdnTime =randint(0,maxTimer),label=i)

    for i in range(maxTimer):
        # for each 'Tic' of the time, the function will look at nodes which
        # have the same 'randomTic'

        for j in range(len(g.nodes)):
            # if it's time to the node to play
            if i==g.nodes[j]['rdnTime']:
                #node chosen and function will chose a another node
                # which will maximise its value
                currentNode = g.nodes[j]
                if addComplexity :
                    chosenNeighbor=lookAtNeighbors(g,currentNode,True)
                else:
                    chosenNeighbor = lookAtNeighbors(g,currentNode)

                if not(g.has_edge(currentNode['label'],chosenNeighbor['label'])):
                    if firstConnectionDone :
                        if addComplexity :
                            g.add_edge(currentNode['label'], chosenNeighbor['label'])
                            currentNode['value'] += chosenNeighbor['value']
                            currentNode['showingValue'] = [0.5*currentNode['value'],1.5*currentNode['value']]
                            chosenNeighbor['value'] += currentNode['value']
                            chosenNeighbor['showingValue'] = [0.5*chosenNeighbor['value'],1.5*chosenNeighbor['value']]
                            # print(g.nodes.data())
                        else:
                            g.add_edge(currentNode['label'],chosenNeighbor['label'])
                            currentNode['value'] +=chosenNeighbor['value']
                            chosenNeighbor['value'] += currentNode['value']
                            # currentNode['value'] +=chosenNeighbor['value']

                    else:
                        # if it is the first connection, each nodes value are init.
                        # to 1
                        if addComplexity:
                            g.add_edge(currentNode['label'], chosenNeighbor['label'])
                            currentNode['value'] = 1
                            currentNode['showingValue'] = [0.5 * currentNode['value'], 1.5 * currentNode['value']]
                            # g.nodes[j]
                            chosenNeighbor['value'] = 1
                            chosenNeighbor['showingValue'] = [0.5 * chosenNeighbor['value'],
                                                              1.5 * chosenNeighbor['value']]
                            firstConnectionDone = True
                        else:
                            g.add_edge(currentNode['label'], chosenNeighbor['label'])
                            currentNode['value'] = 1
                            g.nodes[j]

                            chosenNeighbor['value'] = 1
                            chosenNeighbor['showingValue'] = [0.5 * chosenNeighbor['value'], 1.5 * chosenNeighbor['value']]
                            firstConnectionDone = True
    return g

def generateGraphWithKarma(n):
    g = generateSimpleGraph(n,True,True)
    maxTimer = 1000
    nbTour =3
    for a in range(1,nbTour+1):

        denominateur = a

        for i in range(maxTimer):
            # for each 'Tic' of the time, the function will look at nodes which
            # have the same 'randomTic'

            for j in range(len(g.nodes)):
                # if it's time to the node to play
                if i==g.nodes[j]['rdnTime']:
                    #node chosen and function will chose a another node
                    # which will maximise its value
                    currentNode = g.nodes[j]
                    chosenNeighbor = lookAtNeighborsWithKarma(g,currentNode)

                    if chosenNeighbor != None :
                        # A revoir
                        if list(g.neighbors(currentNode['label']))!= [] :
                            weakestNode = getWeakestNode(g,currentNode)
                            g.remove_edge(currentNode['label'],weakestNode['label'])
                            weakestNode['value'] -= currentNode['value']
                            currentNode['value'] -= weakestNode['value']
                            g.add_edge(currentNode['label'],chosenNeighbor['label'])
                            currentNode['value']+=chosenNeighbor['value']
                            chosenNeighbor['value']+=currentNode['value']
                            currentNode['nbDefect']+=1
                            currentNode['karma'] = currentNode['nbDefect']/denominateur
                        else:
                            g.add_edge(currentNode['label'], chosenNeighbor['label'])
                            currentNode['value'] += chosenNeighbor['value']
                            chosenNeighbor['value'] += currentNode['value']

                    else:
                        currentNode['value'] = 2*currentNode['value']

    return g
def getWeakestNode(g,currentNode):
    idNeighors = list(g.neighbors(currentNode['label']))

    resNode= g.nodes[idNeighors[0]]
    resNodeValue = g.nodes[idNeighors[0]]['value']
    idNeighors.pop(0)
    for id in idNeighors:
        if g.nodes[id]['value'] < resNodeValue:
            resNodeValue = g.nodes[id]['value']
            resNode = g.nodes[id]

    return resNode
def checkEqualIvo(lst):
    return not lst or lst.count(lst[0]) == len(lst)
def lookAtNeighborsWithKarma(g,currentNode):
    possibleNeighbors = []
    possibleNeighborsValue = []
    possibleNeighborsKarma = []
    # currentValue = currentNode['value'] * (1-currentNode['karma'])
    currentValue = currentNode['value']
    for i in range(0,len(g.nodes)):
        if currentNode!=g.nodes[i]:
            tempValue=g.nodes[i]['value']
            if currentValue < tempValue:
                possibleNeighbors.append(g.nodes[i])
                possibleNeighborsValue.append(tempValue)
                possibleNeighborsKarma.append(g.nodes[i]['karma'])


    if len(possibleNeighbors)== 0 :
        res = None

    else:
        if checkEqualIvo(possibleNeighborsKarma):
            res = possibleNeighbors[randint(0,len(possibleNeighbors)-1)]
        else:
            res = possibleNeighbors[possibleNeighborsKarma.index(min(possibleNeighborsKarma))]


    return res

def lookAtNeighbors(g,currentNode,hiddenValue=False):
    """
    reste jsute a checker qu'il ne retourne pas le current node
    :param currentNode: the current node which is playing
    :param hiddenValue: boolean which for the second part of the question
    :param g:
    :return: the best node related to the rules
    """
    if currentNode != g.nodes[0]:
        neighbors = [g.nodes[0]]
        step = 1
        second = False
    else:
        neighbors = [g.nodes[1]]
        step = 0
        second = True

    # for i in range(1,g.nodes):
    #     if neighbors[len(neighbors)-1]['value']>=g.nodes[i]['value'] and g.nodes!=currentNode:
    #         neighbors.append(g.nodes[i])
    if hiddenValue :
        # think to the fact we have a problem
        currentMaxValue = uniform(neighbors[len(neighbors)-1]['showingValue'][0],neighbors[len(neighbors)-1]['showingValue'][1])
        for i in range(step, len(g.nodes)):
            if second:
                # start from 0 and don't chpose the second
                currentValue = uniform(g.nodes[i]['showingValue'][0],g.nodes[i]['showingValue'][1])
                if g.nodes[i] != currentNode and currentMaxValue==currentValue and i != 1:
                    neighbors.append(g.nodes[i])
                elif g.nodes[i] != currentNode and currentMaxValue < currentValue   and i != 1:
                    neighbors.clear()
                    neighbors.append(g.nodes[i])
                    currentMaxValue=currentValue
            else:
                currentValue = uniform(g.nodes[i]['showingValue'][0], g.nodes[i]['showingValue'][1])
                if g.nodes[i] != currentNode and currentMaxValue == currentValue :
                    neighbors.append(g.nodes[i])
                elif g.nodes[i] != currentNode and currentMaxValue < currentValue :
                    neighbors.clear()
                    neighbors.append(g.nodes[i])
                    currentMaxValue=currentValue
    else:
        for i in range(step,len(g.nodes)):
            if second:
                # start from 0 and don't chpose the second
                if g.nodes[i]!=currentNode and neighbors[len(neighbors)-1]['value']==g.nodes[i]['value'] and i!=1:
                    neighbors.append(g.nodes[i])
                elif g.nodes[i]!=currentNode and neighbors[len(neighbors)-1]['value']< g.nodes[i]['value'] and i!=1:
                    neighbors.clear()
                    neighbors.append(g.nodes[i])
            else:
                if g.nodes[i]!=currentNode and neighbors[len(neighbors)-1]['value']==g.nodes[i]['value'] :
                    neighbors.append(g.nodes[i])
                elif g.nodes[i]!=currentNode and neighbors[len(neighbors)-1]['value']< g.nodes[i]['value'] :
                    neighbors.clear()
                    neighbors.append(g.nodes[i])

    if len(neighbors) == 1:
        res = neighbors[0]
    else :
        res = neighbors[randint(0,len(neighbors)-1)]

    return  res


