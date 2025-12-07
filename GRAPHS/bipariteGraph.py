#dfs implementation
graph = {
    1: [2, 3],
    2: [1, 5, 6],
    3: [1, 4, 7],
    4: [3],
    5: [2],
    6: [2],
    7: [3, 8],
    8: [7]
}
n = len(graph)
