i = 7
x = "even" if i % 2 == 0 else "odd"
print(x)


numbers = [1,2,3,4,5,6,7,8,9,10,11,12]

square_times_2_greater_than_100 = [x for x in numbers if x * x * 2 > 100]

print(square_times_2_greater_than_100)