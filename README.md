# simpleGeneticAlgorithm
Primer acercamiento a los algoritmos geneticos

Planteo:
Se empieza la poblacion con un numero de individuos totalmentes al azar.
Un Individuo tiene su propio Cromosoma/su propia coleccion de genes: [1,0,1,1,0]
Se intenta hacer evolucionar la poblacion hasta conseguir un individuo cercano al mayor fitness (mayor sum(genes)). Los genes pueden tomar valor 0 o 1.

Funcion Fitness: Suma simple de los genes de los individuos

Selection: parent selectiond estilo ruleta. Solo dos padres pueden ser elegidos (a futuro, ver de hacer distintas camadas)
CrossOver: estan implementados OnePoint y Uniform

Mutation: bit-flip. Hay probabilidad de que cada gen cambie
SurvivorSelection: Los offsprings reemplazan los miembros con menos fitness de la generacion pasada.



