# WebSurfing
A (relatively) small random walk over the web network.

## Functioning
1) The program contains the 'webSurfing' function, which will perform a random walk over the web network. 
2) The function accepts five arguments namely, url, base, filePath, depth, and teleportationProbability.
3) The program begins at the given 'url'. 'base' is the domain of the current link.
4) It then extracts all the links present on the current page.
5) The program then with a probability of 'teleportationProbability', teleports to a random link (selected from the already explored links), or with a probability 1 - 'teleportationProbability' surfs to a random adjacent link (selected from the links present on the current page).
6) The program does this for 'depth' number of iterations.
7) The program writes all the newly encountered links to a file with the path 'filePath'. \
&emsp; Links extracted from a sample random walk are provided in 'Links.txt' \
&emsp; Walk initialised at: https://iitrpr.ac.in \
&emsp; Depth: 30
8) The program also simultaneously generates a graph with an edge between the current page and all the links present on that page.
9) The program finally ouputs the generated graph.

## How To Use
1) Open the Terminal.
2) Navigate to the folder containing the program.
3) Use the command 'python .\webSurfing.py' to execute the program.
