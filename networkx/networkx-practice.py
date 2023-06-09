'''

You are given a file directedGraph.txt corresponding to a directed graph.

You are to read it into a variable G that holds a suitable graph structure
and answer the following questions. Please note that I refer to this graph
G in the questions.


Networkx documentation:
https://networkx.org/documentation/stable/reference/index.html

Netowkrx tutorial:
https://networkx.org/documentation/stable/tutorial.html

'''

import networkx as nx
import matplotlib.pyplot as plt

'''
1. Read the file into an appropriate graph structure (1 point)
'''
g = nx.read_edgelist("directedGraph.txt", create_using=nx.DiGraph)


'''
2. Print out the number of nodes and edges in G. (1 point)
'''
print(g.number_of_nodes())
print(g.number_of_edges())


'''
3. Identify the 5 nodes in G that have the most edges directed outwards.
Print out the node ids and the number of outward edges for these 5 sorted by
number of outward edges  (6 points)
'''

outwards_dict = g.out_degree()
outward_dict_sorted = sorted(outwards_dict, key=lambda t: t[1], reverse=True)
print(outward_dict_sorted[0:5])


'''
4. Identify the 5 nodes in G that have most edges directed inwards.
Print out the node ids and the number of inwards edges for these 5 sorted by
number of inwards edges (6 points)
'''

inwards_dict = g.in_degree()
inwards_dict_sorted = sorted(inwards_dict, key=lambda t: t[1], reverse=True)
print(inwards_dict_sorted[0:5])

'''
5. Print out the number of connected components present in G.
You will need to study the kind of connected component present in
directed graphs which is not the same as for undirected graphs. (3 points)
'''

weak_number = nx.number_weakly_connected_components(g)
strong_number = nx.number_strongly_connected_components(g)
print(weak_number + strong_number)

'''
6. For each connected component in G print out the number of nodes and number of edges,
and the average shortest path. (5 points)
'''

weak_cc = list(nx.weakly_connected_components(g))
strong_cc = list(nx.strongly_connected_components(g))
all_cc = weak_cc + strong_cc

for c in all_cc:
    wg = g.subgraph(c)
    print(wg.number_of_nodes(), wg.number_of_edges(), nx.average_shortest_path_length(wg))


'''
7. Write a function called distancetwo that takes a nodeid N as argument
and that returns the list of nodes in G at distance two to node N.
If A points to B and B points to C then C is at distance 2 from A. (5 points)
'''
 
def distancetwo(N):
    two_path = []
    for node in g.nodes:
        #calculate all simple paths at distance up to 2 from node N
        simple_paths = list(nx.all_simple_paths(g, N, node, cutoff=2))
        for el in simple_paths:
            #filter for nodes at distance 2 from node N only
            if len(el)==3:
                two_path.append(el[-1])
    return two_path


'''           
8. Create a subgraph S containing only the size 2 and 3 weakly connected components
in G. (2 points) # size of 3
'''

G = set()
for cc in weak_cc:
    if len(cc) == 2 or len(cc) == 3:
        #updating set G because without it, it is not possible to do 
        #subgraph S of all weakly connected components of size 2 and 3
        G.update(cc)
S = g.subgraph(G)

'''
9. Plot subgraph S. (1 point)
'''

nx.draw(S)
plt.show()
