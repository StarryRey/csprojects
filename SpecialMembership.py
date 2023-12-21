

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

def overlap(list1, list2):
    for num1 in list1:
        for num2 in list2:
            if num1 == num2:
                return True
    return False

if overlap(list1, list2):
    print("They overlap")
else:
    print("They do not overlap")
