# infinite_loop_demo.py
# Examples of infinite loops (commented out for safety)

# Example 1: Basic infinite loop (DO NOT UNCOMMENT UNLESS YOU KNOW HOW TO STOP IT!)
# while True:
#     print("I'm stuck forever!")

print("--------")

# Example 2: Infinite loop with break
i = 0
while True:
    print("i =", i)
    i += 1
    if i > 3:
        break

