import random as random

import Population

CANT_GENES=8
MAX_FITNESS=[1 for x in range(0,CANT_GENES)]
POB_INICIAL=5
PROB_CROSSOVER=0.9
ERROR_ACEPTABLE=int(sum(MAX_FITNESS)*0.25) #ACEPTO hasta un porcentaje, ej si MAX_FITNESS=-10 acepto que haya un acercamiento hasta 9
MAX_GENERACIONES=10000

class GeneticAlgorithm:
    poblacion=None
    
  
    def __init__(self):
        pass

    def seleccionarSobrevivientes(self,poblacionBase,nuevosMiembros):
        #se pretende analizar si los nuevosMiembros reemplazan a miembros anteriores
        #concretamente miembros mas fuertes reemplazaran a los mas debiles para asegurar una poblacion con mas fitness
        if(len(nuevosMiembros) <1):
            pass
        nuevosMiembros.sort(key=lambda x: x.getFitness(), reverse=True)
        nuevaGen=poblacionBase[:]
        nuevaGen.sort(key=lambda x:x.getFitness()) #quiero los meimbros con menos fitness primero
        offSpringAComparar=0 #0 es el primero
        
        it=0
        while(it<len(nuevaGen) and offSpringAComparar<len(nuevosMiembros)):
            item=nuevaGen[it]
            
            if(nuevosMiembros[offSpringAComparar].getFitness()>=item.getFitness()):
                nuevaGen[it]=nuevosMiembros[offSpringAComparar]
                offSpringAComparar+=1
    
                
            it+=1
        return nuevaGen
            
    def encontrarSolucion(self):
        self.poblacion=Population.Population(POB_INICIAL)
        while((self.poblacion.getMejorIndividuo().getFitness() < sum(MAX_FITNESS)-ERROR_ACEPTABLE) and (self.poblacion.getNumeroGeneraciones()<MAX_GENERACIONES)):
            for x in self.poblacion.getGeneracionActual():
                print( x.getCromosomas(),x.getFitness())
                
            print('Fin GEN ',self.poblacion.getNumeroGeneraciones())
            #PARENT SELECION
            parents=self.poblacion.seleccionarParents()
            #CROSSOVER
            cruzar=random.random()
            offSprings=[]
            if(cruzar<PROB_CROSSOVER):
                offSprings=parents[0].crearOffSprings_UniformCrossOver(parents[1]) #dos nuevos miembros
                #offSprings=parents[0].crearOffSprings_OnePointCrossOver(parents[1]) #dos nuevos miembros
            #MUTATION
            #Se puede decidir si mutar todos los descendientes o toda la poblacion entera
            poblacionBase=self.poblacion.getGeneracionActual()
            for x in poblacionBase:
                x.mutar()
            #SURVIVOR SELECTION
            nuevaGen=self.seleccionarSobrevivientes(poblacionBase,offSprings)
            self.poblacion.actualizarGeneracion(nuevaGen)
            
    
    
    
        print('Fin en generacion numero:  ', self.poblacion.getNumeroGeneraciones())
        print('primer mejor individuo: ', self.poblacion.getPrimerMejorIndividuo().getCromosomas(),self.poblacion.getPrimerMejorIndividuo().getFitness())
     
        print(' mejor individuo: ', self.poblacion.getMejorIndividuo().getCromosomas(),self.poblacion.getMejorIndividuo().getFitness())
        
if (__name__ == "__main__"):
    '''
    I= Individuo(cromosomas=[1,1,1,1,1])
    I2=Individuo(cromosomas=[0,0,0,0,0])
    
    nuevo=I.crearOffSprings(I2)
    I3=Individuo(cromosomas=nuevo[0])
    print ("nuevo individuo hijo:", I3.getCromosomas())
    
     test=[I,I2]
    test.sort(key=lambda x: x.getFitness(), reverse=True)
    for x in test:
        print (x.getCromosomas())
     
    '''
   
    g=GeneticAlgorithm()
    g.encontrarSolucion()
    
   