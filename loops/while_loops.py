# while_loops.py
# Practice examples for mastering Python while loops

# Example 1: Basic while loop
count = 0
while count < 5:
    print("Count is:", count)
    count += 1

print("--------")

# Example 2: Countdown
num = 5
while num > 0:
    print("Countdown:", num)
    num -= 1

print("Blastoff!")
print("--------")

# Example 3: While loop with break
i = 0
while True:
    print("i is:", i)
    i += 1
    if i == 3:
        break

print("--------")

# Example 4: While loop with condition
x = 10
while x >= 0:
    if x % 2 == 0:
        print(x, "is even")
    x -= 1
