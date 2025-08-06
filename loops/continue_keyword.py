# continue_keyword.py
# Practice examples using the continue keyword in for and while loops

# Example 1: Skip even numbers
for num in range(1, 6):
    if num % 2 == 0:
        continue
    print("Odd number:", num)

print("--------")

# Example 2: Skip specific item in list
animals = ["cat", "dog", "snake", "elephant"]
for animal in animals:
    if animal == "snake":
        continue
    print("I like", animal)

print("--------")

# Example 3: Continue in while loop
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print("i is", i)

