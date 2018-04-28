import random as random
import Individuo
CANT_GENES=8
MAX_FITNESS=[1 for x in range(0,CANT_GENES)]
POB_INICIAL=10




class Population:
    
    genAnterior=None
    genActual=None
    tamanioMax=None
    
    numGen=None
    probOffSprings=None
    primerMejor=None
    mejorHastaAhora=None
    def __init__(self,pobInicial=POB_INICIAL):
        self.genAnterior=[]
        self.genActual=[]
        self.tamanioMax=pobInicial
       
        self.numGen=0
        
        for x in range(0,pobInicial):
            self.genActual.append(Individuo.Individuo(CANT_GENES))
            
        self.genAnterior=self.genActual[:]
            
        self.primerMejor=self.genActual[0]
        self.mejorHastaAhora=self.primerMejor
        for x in self.genActual:
            if(not self.primerMejor.esMejor(x)):
                self.primerMejor=x
        self.mostrarPoblacionActual()
    
    
    def actualizarGeneracion(self,nuevaGen=[]):
        self.genAnterior=self.genActual[:]
        
        self.genActual=nuevaGen[:]
        
        for x in self.genActual:
            if(not self.mejorHastaAhora.esMejor(x)):
                self.mejorHastaAhora=x
        self.numGen+=1
        
    def getNumeroGeneraciones(self):
        return (self.numGen)
        
    def getMejorIndividuo(self):
       
       
                
        return self.mejorHastaAhora
            
        
    def getPrimerMejorIndividuo(self):
        return (self.primerMejor)
    def mostrarPoblacionActual(self):
        for x in self.genActual:
            
            print (x.getCromosomas(),x.getFitness())
        
        
    def getGeneracionActual(self):
        return self.genActual
    
    '''
    def seleccionarIndividuos(self):
        
        sumFitness=0
        seleccionados=[]
        probSeleccion=[]
        nuevaGen=[]
        for x in self.genActual: #array de individuos
            sumFitness+=x.getFitness() 
            
        
        for x in self.genActual:
          
            prob=x.getFitness()/sumFitness if(sumFitness is not 0) else 0
            
            probSeleccion.append(prob) 
        
        while (len(nuevaGen)<self.tamanioMax):
            seleccionados=[]
            for i in range(0,2):
                seleccionar=random.random() #aca esta la probabilidad de seleccion
                for x in self.genActual: #quizas en este paso tendria que randomizar el vector de gen para diversificar opciones
                    
                    if(seleccionar<probSeleccion[self.genActual.index(x)]): #es obvio que esto se ejecuta desde 0 hasta len(self.genActual) igual
                        seleccionados.append(x)
                
            if(len(seleccionados)>1):
                x=0
                while(x<len(seleccionados) and x+1<len(seleccionados)):
                   
                        crossOver=random.random()
                        if(crossOver<self.probCrossoverMin):
                            listaOffsprings=seleccionados[x].crearOffSprings(seleccionados[x+1])
                            for y in listaOffsprings:
                                nuevaGen.append(y)
                                
                                
                        else: #no hubo crossover entonces mando los parents directos
                             nuevaGen.append(seleccionados[x]) 
                             nuevaGen.append(seleccionados[x+1])
                            
                             
                        x=x+2
                        
                        if(len(nuevaGen)>self.tamanioMax):
                            break
                    #voy haciendo hijos de a pares
            
            
            
                
        nuevaGen=nuevaGen[:self.tamanioMax]
        for x in nuevaGen:
            x.mutar()
            
        for x in nuevaGen:
            print (x.getCromosomas())
        print('Fin Gen: ', self.numGen, len(nuevaGen) )
        return nuevaGen
    '''
    def seleccionarParents(self):
        #la idea de esto es que se selecciones pares de individuos para su reproduccion
        #este es un esquema elitista se eligirian los dos mejores y toda la poblacion se rellenaria con los descendientes
        
        sumFitness=0
        seleccionados=[]
        probSeleccion=[]
        
        for x in self.genActual: #array de individuos
            sumFitness+=x.getFitness() 
            
        if(sumFitness is 0):
            raise ValueError('la sumFitness no debiera ser nunca 0, elegir otra poblacion inicial')
        probAcum=0 #los de mayor fittest van a tener una proporcion mayor (analizar cada caso de getFitness())
        for x in self.genActual:
          
            probAcum+=x.getFitness()/sumFitness 
            
            probSeleccion.append(probAcum) 
            
        seleccionados=[]
        yaSeleccionados=[]
        while(len(seleccionados)<2): #se toman dos padres nomas (y se espera que sean los mas fittest, o con mucha leche)
                #hay dos formas de hacer esto, con chances o directamente elitista
                #es decir, selecciono los mejores parents de una o doy posibilidad a la probabilidad de ir permutando
                
                seleccionar=random.random() #aca esta la probabilidad de seleccion
            
                for valor in probSeleccion:
                    
                    if(seleccionar<valor):#el indice del valor es el indice del individuo en self.genActual
                        if(valor not in yaSeleccionados):
                            seleccionados.append(self.genActual[probSeleccion.index(valor)])
                            yaSeleccionados.append(valor)
                        
                        
        return seleccionados
        
        