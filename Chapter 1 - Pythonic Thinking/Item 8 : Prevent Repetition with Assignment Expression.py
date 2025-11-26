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

