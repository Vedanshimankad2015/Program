lst = ['cycling','coding','eating','sleeping','studying']

print("length of list:",len(lst))
print("first element", lst[0])
print("Last Element:", lst[-1])

lst.remove('cycling')
print("Updated List :", lst)

lst.sort()
print("Sorted List:", lst)

lst.pop(1)
print("Updated List :", lst)

lst.reverse()
print("Reversed List :", lst)

print("Multiplication on List :", lst*2)

lst = lst[:4]
print("Sliced List :", lst)

lst.clear()