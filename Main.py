from random import randint
from utils import generateNewValue
from GA import GA
import networkx as nx
import numpy


def fitnessFunction(path, mat):
    n=0
    l=[]
    l.append(0)
    i=0
    j=0
    while len(l)<len(mat):
        j=path[i]
        n=n+mat[i][j]
        if j in l and len(l)<len(mat):
            n=n+999999.0
            break
        else:
            l.append(j)
        i=j
    i=j
    while len(l)<len(mat):
        j=path[i]
        n=n+mat[i][j]
        i=j
        l.append(j)
    n=n+mat[0][j]
    return n


def Citire(fileName):
    f = open(fileName, "r")
    net = {}
    n = int(f.readline())
    net['noNodes'] = n
    mat = []
    for i in range(n):
        mat.append([])
        line = f.readline()
        elems = line.split(",")
        for j in range(n):
            mat[-1].append(float(elems[j]))
    net["mat"] = mat 
    degrees = []
    noEdges = 0
    for i in range(n):
        d = 0
        for j in range(n):
            if (mat[i][j] == 1):
                d += 1
            if (j > i):
                noEdges += mat[i][j]
        degrees.append(d)
    net["noEdges"] = noEdges
    net["degrees"] = degrees
    f.close()
    return net


def Main():
    c = Citire("newinput.txt")
    

    param = {'popSize' : 200, 'noGen': 1000, 'tour' : 0.33}
    problParam= {'min':0,'max' : c["noNodes"], 'function' : fitnessFunction, 'mat': c['mat'], 'all' : c}

    ga=GA(param,problParam)
    ga.initialisation()
    ga.evaluation()

    fit=9999999
    gen=0
    for g in range(int(param['noGen'])):
        ga.oneGenerationElitism()
        #ga.oneGeneration()
        #ga.oneGenerationSteadyState()
        bestChromo = ga.bestChromosome()
        if fit > bestChromo.fitness:
            fit = bestChromo.fitness
            gen = g
        print(bestChromo.fitness)
        #print('Best solution in generation ' + str(g) + ' is: x = ' + str(bestChromo.repres) + ' f(x) = ' + str(bestChromo.fitness))
    #print(fit)
    #print(gen)


Main()
