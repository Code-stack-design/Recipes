from collections import defaultdict, deque
from typing import List

def findAllRecipes(
    recipes: List[str],
    ingredients: List[List[str]],
    supplies: List[str]
) -> List[str]:
    graph = defaultdict(list)
    in_degree = {recipe: len(reqs) for recipe, reqs in zip(recipes, ingredients)}

    for recipe, reqs in zip(recipes, ingredients):
        for ing in reqs:
            graph[ing].append(recipe)

    queue = deque(supplies)
    result = []

    while queue:
        item = queue.popleft()
        for rec in graph.get(item, []):
            in_degree[rec] -= 1
            if in_degree[rec] == 0:
                result.append(rec)
                queue.append(rec)
    return result

def prompt_user_input():
    recipes = input("Enter recipes separated by commas (e.g., bread, sandwich, burger):\n").strip().split(",")
    recipes = [r.strip() for r in recipes if r.strip()]

    print("\nNow enter ingredients for each recipe, in the same order.")
    print("Use semicolons (;) to separate recipes, and commas to separate ingredients within each.")
    print("Example: yeast, flour; bread, meat; sandwich, cheese, meat")
    raw = input("Ingredients:\n").strip()
    parts = [p.strip() for p in raw.split(";") if p.strip()]
    ingredients = [ [ing.strip() for ing in part.split(",") if ing.strip()] for part in parts ]

    supplies = input("\nEnter your supplies separated by commas (e.g., flour, yeast, meat):\n").strip().split(",")
    supplies = [s.strip() for s in supplies if s.strip()]

    return recipes, ingredients, supplies

if __name__ == "__main__":
    recipes, ingredients, supplies = prompt_user_input()
    result = findAllRecipes(recipes, ingredients, supplies)
    print("\nBased on your inputs, you *can* make these recipes:")
    print(result)
