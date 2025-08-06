# list_methods.py
# Practice examples using .append(), .pop(), .insert(), and negative indices

# Example 1: Append
tasks = ["eat", "sleep"]
tasks.append("code")
print("Tasks after append:", tasks)

print("--------")

# Example 2: Pop last item
movies = ["Titanic", "Avatar", "Inception"]
last = movies.pop()
print("Removed:", last)
print("Now:", movies)

print("--------")

# Example 3: Pop first item
first = movies.pop(0)
print("Removed first:", first)
print("Now:", movies)

print("--------")

# Example 4: Insert at index
colors = ["red", "blue", "yellow"]
colors.insert(1, "green")
print("Colors:", colors)

print("--------")

# Example 5: Negative index
fruits = ["apple", "banana", "cherry", "date"]
print("Last fruit:", fruits[-1])
print("Second last:", fruits[-2])

