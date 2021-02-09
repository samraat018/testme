_____________________________________________________ZIP FUNCTIONS___________________________________________________

zip() function returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, 
 and then the second item in each passed iterator are paired together etc.

If the passed iterators have different lengths, the iterator with the least items decides the length of the new iterator.

SYNTAX:-
    zip(iterator1, iterator2, iterator3 ...)

________________________________________________________EXAMPLES_____________________________________________________

a = ("John","peter")
b = ("Jenny","ashwin")

x = list(zip(b,a))
x



number_list = [1, 2, 3,3]
str_list = ['one', 'two', 'three',"three"]

# No iterables are passed
result = list(zip())
result
# Converting itertor to list
result_list = list(result)
print(result_list)

# Two iterables are passed
result = zip(number_list, str_list)

# Converting itertor to set
result_set = set(result)
result_set[0]

__________________________________________Different number of iterable elements____________________________________________________________________________

numbersList = [1, 2, 3]
str_list = ['one', 'two']
numbers_tuple = ('ONE', 'TWO', 'THREE', 'FOUR')

result = zip(numbersList, numbers_tuple)
list(result)


result1 = zip(numbersList, str_list, numbers_tuple)
list(result1)


____________________________________________Unzipping the Value Using zip()_________________________________________

 
coordinate = ['x', 'y', 'z']
value = [3, 4, 5]

result = zip(coordinate, value)
result_list = list(result)
result_list

c, v = zip(*result_list)
c
v

a=["ashwin","jyoti","ashish"]
b=[90,70,60]


for i,j in zip(a,b):
    if j==90:
        print(i,j,"good")



a=input("enter a number: ")
a+=1
type(a)
    












