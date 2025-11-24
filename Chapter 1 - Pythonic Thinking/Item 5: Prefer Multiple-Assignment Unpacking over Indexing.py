item = ("Peanut butter", "Jelly")
first,second = item #Unpacking

print(first , " and " , second)



'''
Newcomers to Python may be surprised to learn that 
unpacking can even be used to swap values in place without the need to create temporary variables. 
Here I use typical syntax 
with indexes to swap ther values between two positions in a list as part of 
an ascending-order sorting algorithm
'''

def bubble_sort(arr: list):

    for _ in range(len(arr)):
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                tmp = arr[i]
                arr[i] = arr[i-1]
                arr[i-1] = tmp


my_arr = [4,3,1,5,6,7,0]
bubble_sort(my_arr)
print(my_arr)

'''
However, with unpacking syntax, it's possible to swap indexes in a single line:
'''
def unpacking_bubble_sort(arr:list):

    for _ in range(len(arr)):
        for i in range(1,len(arr)):
            if arr[i] < arr[i-1]:
                arr[i-1], arr[i] = arr[i] , arr[i-1]

my_arr = [5,6,7,3,1,2,3,4,0,-12,4,0]
unpacking_bubble_sort(my_arr)
print(my_arr)


# Another valuable application of unpacking is in the target lists of for loops and similar constructs.


snacks = [("bacon",350), ("donut",240), ("muffin",190)]

for rank, (name,calories) in enumerate(snacks,1):
    print(f"#{rank}: {name} has {calories} calories.")