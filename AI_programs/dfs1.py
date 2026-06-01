graph = {
    "A": ["B","D","C"],
    "B": ["C"],
    "C": [],
    "D": ["E"],
    "E": []
}

visited = set()

def dfs(node, target):
    if node == target:
        return True 
    
    visited.add(node)
    print(f"visiting {node}")
    if graph[node]:
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, target):  
                    return True  
    
    else:return False  

print(dfs("A", "E"))  
