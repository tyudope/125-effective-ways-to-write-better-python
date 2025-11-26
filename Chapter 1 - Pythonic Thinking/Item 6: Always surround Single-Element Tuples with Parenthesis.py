def find_user(username) -> tuple:

    if username == "selim":
        return ("found", ) # -> consistent : always a tuple
    return ("not found", ) # same


print(type(find_user("selim"))) # -> return tuple.
print(find_user("selim")[0]) # -> found.



# Follow-up question.

'''
REAL USE CASES - Unpacking values consistently

Imagine you parse some config or ML model infor and return either:

- a single result, or
- multiple results

If you don't return a tuple, code breaks.

wrong design
def get_layers(model):
    if model.num_layers == 1:
        return 'dense'
    return ('dense', 'relu)
    
l1, l2 = get_layers(model)
# BOOM, ValueError: not enough values to unpack (expected 2, got 1)
'''

#correct design
def get_layers(model):
    if model.num_layers == 1:
        return ("dense",)
    return ("dense", "relu")

#l1, l2 = get_layers(model)
# always a tuple, never crashes