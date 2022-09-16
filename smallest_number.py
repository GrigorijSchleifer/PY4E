# find smallest number
lst = [78, 56, -2, 12, 8, -33]


smallest_number = max(lst)
# if smaller than maximal number 
for itm in lst:
    if itm < smallest_number:
        smallest_number = itm

print(smallest_number)