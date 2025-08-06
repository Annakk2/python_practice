# nested_loops.py
# Practice examples of nested loops

# Example 1: Outfit combinations
shirts = ["red", "blue"]
pants = ["jeans", "shorts"]

for shirt in shirts:
    for pant in pants:
        print("Outfit:", shirt, "shirt with", pant)

print("--------")

# Example 2: Multiplication table (1 to 3)
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i * j}")
    print("--------")

