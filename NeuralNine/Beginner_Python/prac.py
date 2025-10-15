# By default all the inputs are stored as strings
# We have to convert them into ints and etc if we have to use them as such
#x = input("Enter value: ")
#print(type(x))

#y = int(x)
#print(type(y))

#z = 0
#while (z < 10):
#    z += 1
#    print("hello", end=' 2')

#for i in range(1,20):
#    print("Whazzz up! - i = ", i)

#i = 0
#for i in range(4):
#    i += 1
#    if i == 5:
#        break 
#    print(i)

# break - immediately terminates the loop in which it is contained.
# continue - skips the rest of the current iteration of the loop.
# pass - is a null operation which serves as a placeholder in situations where a statement is syntactically required, but no action needs to be performed.
# E.g.  if x == 5:
#           pass
#       print("123")
# Without the pass operation python interpreter will give us Indentation error

#mylist = ["hello","someone","he","she","him"]
# The slicing works on index, not elements. so here we are saying slice index 0 to 2. basically 3 elements

# List Comprehensions
#squares = [n**2 for n in range(10)]
#print(squares)
#if "someone" in mylist:
#    mylist.pop(mylist.index("someone"))

#print(mylist)

#a = [1,5,2,44,54,12]
#a.sort() # use a method or a function sorted()
#print(a)

#print(sorted(a))

# Making a tuple a list using typecasting

tu = (1,2,3,0,23,11)
print("Original Tuple \n", tu)
x = list(tu)
print("Converted to List \n", x)
x.insert(2,88)
print("Updated List \n", x)
y = tuple(x)
print("Converting the list into tuple after converting tuple into list and adding 88 \n", y)
