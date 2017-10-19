# Hierholzer's Algorithm
Implementation to solve Eulerian Paths on undirected graphs. Detecting if it's an eulerian graph, it's cycles and circuits.

Input - File with the following structure
   
    9                     #number of vertixes
    0 1 0 1 0 0 0 0 0     #Adjacency Matrix
    1 0 1 1 1 0 0 0 0 
    0 1 0 0 1 0 0 0 0 
    1 1 0 0 1 0 0 1 0 
    0 1 1 1 0 1 1 1 0 
    0 0 0 0 1 0 0 0 1 
    0 0 0 0 1 0 0 1 0 
    0 0 0 1 1 0 1 0 1 
    0 0 0 0 0 1 0 1 0

Output - * Abort and inform if it's not an Eulerian Graph
         * The final Eulerian path
         
Contribuitors: Victor Medeiros(@medeirosvictor), Diogo Lopes (@cirddan)
Later on this repository will have more implementations regarding Graph Theory.
Useful references to best practices when developing in Python:
http://docs.python-guide.org/en/latest/writing/structure/
