

# recursive dfs function. DFS is a quick way to check IF there is a route between A and B
def dfs(graph, current_vertex, target_value, visited=None):
    if visited is None:
        visited = []
    # creates path of visited vertices
    visited.append(current_vertex)
    # base case
    if current_vertex is target_value:
        return visited

    # randomly works through neighbors connected to current vertex
    for neighbor in graph[current_vertex]:
        # only visits unvisited vertices
        if neighbor not in visited:
            # recursive call of itself
            path = dfs(graph, neighbor, target_value, visited)
            if path:
                return path


# iterative bfs function. BFS is for shortest route calculation
def bfs(graph, start_vertex, target_value):
    # beginning of path building. For now path is just starting point
    path = [start_vertex]
    vertex_and_path = [start_vertex, path]
    bfs_queue = [vertex_and_path]
    visited = set()
    while bfs_queue:
        # set current vertex and path to front queue value
        current_vertex, path = bfs_queue.pop(0)
        # adds current vertex to visited checklist
        visited.add(current_vertex)
        # iterates through neighbor of current vertex
        for neighbor in graph[current_vertex]:
            # if it is not visited yet. Visit it.
            if neighbor not in visited:
                # if the new visit is the target value stop and return path + neighbor
                if neighbor is target_value:
                    return path + [neighbor]
                # if the new visit is not target value. Enqueue the neighbour to BFS queue
                else:
                    bfs_queue.append([neighbor, path + [neighbor]])


some_hazardous_graph = {
    # set([1, 2, 3]) is same as {1, 2, 3}. Only an empty set needs to be defined with set() to disambiguate it from an
    # empty dictionary which is {}. Note: dictionary syntax is {key1:value1, key2:value2} and set syntax is {1, 2, 3}
    # both set and {} syntax is used below
    'lava': {'sharks', 'piranhas'},
    'sharks': {'piranhas', 'bees'},
    'piranhas': set(['bees']),
    'bees': set(['lasers']),
    'lasers': set([])
}
print('Breadth first search path:')
print(bfs(some_hazardous_graph, 'sharks', 'bees'))
print('\nDepth first search path:')
print(dfs(some_hazardous_graph, 'sharks', 'bees'))
print('\n---------------------------------------------------------\nRun multiple times to see difference between '
      'algorithms!!')
