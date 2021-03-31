from random import randint
from utils import generateNewValue

class Chromosome:
    def __init__(self, problParam = None):
        self.__problParam = problParam
        self.__repres = generateNewValue(problParam['min'], problParam['max'])
        self.__fitness = 0.0
    
    @property
    def repres(self):
        return self.__repres
    
    @property
    def fitness(self):
        return self.__fitness 
    
    @repres.setter
    def repres(self, l = []):
        self.__repres = l 
    
    @fitness.setter 
    def fitness(self, fit = 0.0):
        self.__fitness = fit

    def findPosition(self,child):
        p=0
        while child[p]!=-1:
            p=p+1
            if p>=len(child):
                break
        return p
    
    def cycle(self, child,parent1,parent2,pozitie):
        nrElemente=0
        while True:
            #print(pozitie)
            #print(parent2)
            pozitie=parent1.index(parent2[pozitie])
            if child[pozitie]!=-1:
                break
            child[pozitie]=parent1[pozitie]
            nrElemente=nrElemente+1
        return nrElemente

    
    def crossover(self, c):
        '''
        r = randint(0, len(self.__repres) - 1)
        newrepres = []
        for i in range(r):
            newrepres.append(self.__repres[i])
        for i in range(r, len(self.__repres)):
            newrepres.append(c.__repres[i])
        for i in range(0,len(self.__repres)):
            if self.__repres[i] == self.__repres[r]:
                newrepres[i]=self.__repres[r]
        offspring = Chromosome(c.__problParam)
        offspring.repres = newrepres
        return offspring
        '''
        '''
        pos1 = randint(-1, self.__problParam['all']['noNodes'] - 1)
        pos2 = randint(-1, self.__problParam['all']['noNodes'] - 1)
        if (pos2 < pos1):
            pos1, pos2 = pos2, pos1 
        k = 0
        newrepres = self.__repres[pos1 : pos2]
        for el in c.__repres[pos2:] +c.__repres[:pos2]:
            if (el not in newrepres):
                if (len(newrepres) < self.__problParam['all']['noNodes'] - pos1):
                    newrepres.append(el)
                else:
                    newrepres.insert(k, el)
                    k += 1

        offspring = Chromosome(self.__problParam)
        offspring.repres = newrepres
        return offspring
        '''
        
        parent1=self.repres
        parent2=c.__repres
        child1=[-1] * len(parent1)
        child2=[-1] * len(parent1)

        nrElemente=1
        child1[0]=parent1[0]
        pozitie=0
        while nrElemente<len(child1):
            nrElemente=nrElemente + self.cycle(child1,parent1,parent2,pozitie)

            pozitie=self.findPosition(child1)
            
            if pozitie<len(child1):
                nrElemente=nrElemente + self.cycle(child1,parent2,parent1,pozitie)
                
        pozitie=0
        nrElemente=1
        child2[0]=parent2[0]
        while nrElemente<len(child2):
            nrElemente=nrElemente + self.cycle(child2,parent2,parent1,pozitie)

            pozitie=self.findPosition(child2)
            
            if pozitie<len(child2):
                nrElemente=nrElemente + self.cycle(child2,parent1,parent2,pozitie)

                    
        offspring1 = Chromosome(self.__problParam)
        offspring1.repres = child1
        offspring2 = Chromosome(self.__problParam)
        offspring2.repres = child2

        if offspring1.fitness < offspring2.fitness:
            return offspring1
        return offspring2  



    def mutation(self):
        '''
        i = randint(self.__problParam["min"],self.__problParam["max"]-1)
        j = randint(self.__problParam["min"],self.__problParam["max"]-1)
        if (i>j):
            i,j = j,i

        while i<j:
            self.__repres[i],self.__repres[j] = self.__repres[j],self.__repres[i]
            i=i+1
            j=j-1
        '''
        '''
        pos1 = randint(0, self.__problParam['all']['noNodes'] - 1)
        pos2 = randint(0, self.__problParam['all']['noNodes'] - 1)
        if (pos2 < pos1):
            pos1, pos2 = pos2, pos1
        el = self.__repres[pos2]
        del self.__repres[pos2]
        self.__repres.insert(pos1 + 1, el)
        '''
        
        n=0.0
        while n<len(self.__repres)*0.05:
            i=randint(0, len(self.__repres) - 1)
            j=randint(0, len(self.__repres) - 1)
            while i==j:
                j=randint(0, len(self.__repres) - 1)
            self.__repres[i],self.__repres[j] = self.__repres[j],self.__repres[i]
            n=n+1
            
            
        
        
        
    def __str__(self):
        return '\nChromo: ' + str(self.__repres) + ' has fit: ' + str(self.__fitness)
    
    def __repr__(self):
        return self.__str__()
    
    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness