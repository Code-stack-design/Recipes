How It Works:

User Input: Recipes: Comma-separated list (e.g., "bread, sandwich, burger")
Ingredients: Semicolon-separated lists for each recipe, with ingredients comma-separated (e.g., "yeast, flour; bread, meat; sandwich, cheese").
Supplies: Comma-separated list of what you already have.

Processing:

Builds a dependency graph (ingredient → recipes).
Uses indegree logic (how many ingredients each recipe needs).
Enqueues supplies, and as dependencies are resolved, enqueues recipes that become makeable.

Output:

Displays the final list of recipes you can make, based on chained dependencies.

**#Screenshot of output**

<img width="1007" height="493" alt="image" src="https://github.com/user-attachments/assets/774583f0-7ea5-450f-8053-4ad0d39f3d92" />

#Demo video

https://github.com/user-attachments/assets/386d8460-1ef9-47b6-be1d-3d88402cd519

