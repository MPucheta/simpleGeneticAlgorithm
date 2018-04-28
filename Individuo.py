import random as random


PROB_MUTAR=0.01

class Individuo():
    
    chromosomas=None
    cantGenes=None
    probMutar=None
    
    def __init__(self, cantGenes,probMutar=PROB_MUTAR,cromosomas=None):
        self.chromosomas=[]
        self.cantGenes=cantGenes
        self.probMutar=probMutar
        
        if (cromosomas is None):
            for x in range(0,cantGenes):
                gen=random.random()
                gen=0 if gen<0.8 else 1 #ternario python
                self.chromosomas.append(gen)
        else:
            self.setCromosomas(cromosomas)

        #print (self.chromosomas)
    
    def setCromosomas(self,nuevoSet=[]):
        self.chromosomas=nuevoSet
        
    def getCromosomas(self):
        return self.chromosomas
        
    def getFitness(self):
        #el Fittest es cuando todos sus genes son 1
        suma=0
        for x in self.chromosomas:
            suma+=x
        return suma
    
    def mutar(self):
        #por cada gen me fijo si es elegible para mutar, si lo es, lo muto al valor contrario
        #en esta version se muta cada gen por separado, otra version
        #podria ser seleccionar un gen aleatorio y mutarlo
        for x in self.chromosomas:
            checkMutable=random.random()
            self.chromosomas[x]=self.chromosomas[x] if checkMutable<self.probMutar else int(not self.chromosomas[x]) #sin el casteo a int pasa que 1 se convierte a True
            
            
    def esMejor(self,otroIndividuo):
        return (self.getFitness()>=otroIndividuo.getFitness())
            
    def crearOffSprings_OnePointCrossOver(self, otroIndividuo):
        #debiera retornar una lista con 0...n springs nuevos (que sean combinacion, en general van a ser 2 en este caso)
        #se define el metodo de forma general por si cambio la forma de cruzar individuos
        nuevo=[]
        
        CROSS_OVER_POINT=int((random.random()*self.cantGenes)+1) #se elije un punto random por el cual segmentar los genes
        cromosomasA=self.getCromosomas()
        cromosomasB=otroIndividuo.getCromosomas()
        cantGenes=len(cromosomasA)
        offSpring1=[x for x in cromosomasA[:int(cantGenes/CROSS_OVER_POINT)]+cromosomasB[int(cantGenes/CROSS_OVER_POINT):]]
        
        offSpring2=[x for x in cromosomasB[:int(cantGenes/CROSS_OVER_POINT)]+cromosomasA[int(cantGenes/CROSS_OVER_POINT):]]
        
       
        nuevo.append(Individuo(self.cantGenes,cromosomas=offSpring1))
        nuevo.append(Individuo(self.cantGenes,cromosomas=offSpring2))
        return nuevo
    
    def crearOffSprings_UniformCrossOver(self, otroIndividuo):
        
        nuevo=[]
        
  
        cromosomasA=self.getCromosomas()
        cromosomasB=otroIndividuo.getCromosomas()
        offSpring1=[]
        offSpring2=[]
        for x in range(0,len(cromosomasA)): #len(cromosomasA)=len(cromosomasB)
            flipChance1=random.random()
            flipChance2=random.random()
            offSpring1.append(cromosomasA[x] if flipChance1<= 0.5 else cromosomasB[x])
            offSpring2.append(cromosomasB[x] if flipChance2<= 0.5 else cromosomasA[x])
        
       
        nuevo.append(Individuo(self.cantGenes,cromosomas=offSpring1))
        nuevo.append(Individuo(self.cantGenes,cromosomas=offSpring2))
        return nuevo
        