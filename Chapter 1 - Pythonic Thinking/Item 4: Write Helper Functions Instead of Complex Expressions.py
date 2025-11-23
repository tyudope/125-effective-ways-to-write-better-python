from urllib.parse import parse_qs


my_values = parse_qs("red=5&blue=0&green=", keep_blank_values = True)

print(repr(my_values))


print("Red:  ", my_values.get("red"))
print("green: ", my_values.get("green"))
print("opacity:  ", my_values.get("opacity"))

# let's assign default value 0 when parameter isn't supplied or is blank.

red = my_values.get("red")[0] or 0
green = my_values.get("green")[0] or 0

# Now that this logic is spread across multiple lines, it's a bit harder to copy and paste for assigning other variables (e.g. red). If I want to reuse this functionality repeatedly even just two
# or three times, as in this example then writing a helpe function is the way to go

def get_first_int(values, key, default = 0):

    found = values.get(key, [""])
    if found[0]:
        return int(found[0])

    return default

print("-------\n")
red = get_first_int(my_values, "red")
green = get_first_int(my_values,"green")
opacity = get_first_int(my_values, "opacity")
print(f"Red: {red}")
print(f"Green: {green}")
print(f"Opacity: {opacity}")


'''
Things to remember:

- Python's syntax makes it all too easy to write single-line expressions that are overly complicated and difficult to read.
- Move complex expressions into helper functions, especially if you need to use the same logic repeatedly.

'''