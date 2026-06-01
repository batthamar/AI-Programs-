from collections import deque
graph = {             
    "amar":["rajpartap"],
    "rajpartap": ["inder"],
    "inder": ["shagan","maninder"],
    "maninder": ["harika"],
    "shagan": ["harika"],
    "harika": ["adda PU"]
}
def bfs(startlookingfrom,lookingfor):
    queue=deque()
    visited=set()
    queue.append(startlookingfrom)
    visited.add(startlookingfrom)
    while queue:
        if len(graph.get(queue[0], [])) > 0:
            for nodes in graph[queue[0]]:
                   if (nodes==lookingfor):
                       print(nodes+" it's here")
                       queue.append(nodes)
                       return True
                   if nodes not in visited:
                       queue.append(nodes)
                       visited.add(nodes)
            queue.popleft()
            print(queue)
        else:
            queue.popleft()
    print(visited)
bfs("amar","harika")
