# for_loops.py
# Practice examples for mastering Python for loops

# Example 1: Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("I like", fruit)

print("--------")

# Example 2: Loop through a range
for i in range(5):
    print("Counting:", i)

print("--------")

# Example 3: Print squares
for num in range(1, 6):
    print("Square of", num, "is", num ** 2)

print("--------")

# Example 4: Loop through a string
word = "Ana"
for char in word:
    print("Letter:", char)

print("--------")

# Example 5: Loop with condition
numbers = [5, 12, 3, 21, 8]
for num in numbers:
    if num > 10:
        print(num, "is greater than 10")
