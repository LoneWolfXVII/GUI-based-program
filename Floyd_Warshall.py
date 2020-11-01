INF = 99999

graph = []

#graph = [[int(int(j))  for j in i] for i in graph]

#result = []


def floyd_warshall(graph, n):
    #print("no. of vertices:",n)
    distance_matrix = graph
    for k in range(n):
        next_distance_matrix = [list(row) for row in distance_matrix] # make a copy of distance matrix
        for i in range(n):
            for j in range(n):
                # Choose if the k vertex can work as a path with shorter distance
                next_distance_matrix[i][j] = min(distance_matrix[i][j], distance_matrix[i][k] + distance_matrix[k][j])
                distance_matrix = next_distance_matrix # update
    return distance_matrix

n=len(graph)

#print('Shortest distance matrix:',floyd_warshall(graph,n))
