fresh_fruit = {
    "apple":10,
    "banana":2,
    "lemon":5,
}

def make_lemonade(count):

    print(f"{count} lemonade is ready.")

def out_of_stock():
    print(f"There are no lemon to make a lemonade.")

# ----------------------------- TRADITIONAL ----------------------------
count = fresh_fruit.get("lemon", 0)

if count > 0:
    make_lemonade(count)
else:
    out_of_stock()

# ----------------------------- TRADITIONAL ----------------------------

# -------------------- ASSIGNMENT OPERATOR --------------

if lemonade_count := fresh_fruit.get("lemon",0) > 0:
    make_lemonade(count)
else:
    out_of_stock()




# -------------

# making cider with the assignment operator

def make_cider(count):
    print(f"Making sider with {count} apples")

if (apple_count := fresh_fruit.get("apple",0)) >= 4:
    make_cider(apple_count)
else:
    print("Out of apple to make a cider")


# ------------------------------
def pick_fruit():
    if not fresh_fruit: # stops the while loop naturally when dictionary is empty
        return None

    fruit, count = fresh_fruit.popitem() # returns and removes on pair.
    return {fruit : count}

def make_juice(fruit: str, count : int):
    juices = []
    for _ in range(count):
        juices.append(fruit + " Juice")

    return juices



bottles = []

while available_fruit := pick_fruit():
    for fruit, count in available_fruit.items():
        juice = make_juice(fruit, count)
        bottles.extend(juice)


print(bottles)

# ---------------- Challenge Exercise (Harder, Realistic, Forces understanding)

# Problem:
# You have a function,
# def read_log_entry():
#   returns the next log entry as a string
#   return "" (empty string) when no more log exists.

# Your task:
#
# Write a loop using assignment expression that:
# 	1.	Reads log entries until empty string ("")
# 	2.	Counts:
# 	•	how many entries contain "ERROR"
# 	•	how many contain "WARNING"
# 	3.	Stops automatically when there are no more entries
# 	4.	Prints the final counts
#
# Rules:
# 	•	You must use while entry := read_log_entry():
# 	•	You must NOT:
# 	•	repeat function calls
# 	•	use break
# 	•	use infinite loops like while True

logs = [
    "INFO Starting system",
    "WARNING Low disk space",
    "ERROR Failed to load module",
    "INFO User login",
    "ERROR Crash detected",
    ""
]

test = type(logs.pop())

def read_log_entry(logs):
    return logs.pop(0) if logs else ""
    # return first element of logs, if the list is empty return empty string.

errors = 0
infos = 0
warnings_count = 0
while entry := read_log_entry(logs):

    if entry.startswith("INFO"):
        infos += 1
    elif entry.startswith("ERROR"):
        errors += 1
    elif entry.startswith("WARNING"):
        warnings_count  += 1


print(f"Errors : {errors}")
print(f"Infos : {infos}")
print(f"Warnings :{warnings_count}")



