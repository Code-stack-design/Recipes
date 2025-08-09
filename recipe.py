from collections import defaultdict, deque
from typing import List

def findAllRecipes(
    recipes: List[str],
    ingredients: List[List[str]],
    supplies: List[str]
) -> List[str]:
    # Build graph: ingredient → list of recipes that need it
    graph = defaultdict(list)
    # Track number of required ingredients (in-degree) per recipe
    in_degree = {recipe: len(reqs) for recipe, reqs in zip(recipes, ingredients)}

    # Populate graph
    for recipe, reqs in zip(recipes, ingredients):
        for ing in reqs:
            graph[ing].append(recipe)

    # Start with what's immediately available
    queue = deque(supplies)
    result = []

    # BFS / Topological sort logic
    while queue:
        item = queue.popleft()
        for rec in graph.get(item, []):
            in_degree[rec] -= 1
            if in_degree[rec] == 0:
                result.append(rec)
                queue.append(rec)

    return result

# Example use case:
if __name__ == "__main__":
    recipes = ["bread"]
    ingredients = [["flour", "salt"]]
    supplies = ["flour", "salt"]
    print(findAllRecipes(recipes, ingredients, supplies))
    # Expected output: ["bread"]
