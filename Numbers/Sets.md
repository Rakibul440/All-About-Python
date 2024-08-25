# Python Sets
In Python, a set is an unordered collection of unique elements. Sets are defined by values separated by commas inside curly brackets {}. Here are some key features and operations:

## Creating Sets

- my_set = {1, 2, 3, 4, 5}

## Set Operations

- Union: ```my_set1 | my_set2``` (combines elements from both sets)
- Intersection: ```my_set1 & my_set2``` (returns elements common to both sets)
- Difference: ```my_set1 - my_set2``` (returns elements in my_set1 not in my_set2)
- Symmetric Difference: ```my_set1 ^ my_set2``` (returns elements in either set, but not both)

## Set Methods

- add():``` my_set.add(6)``` (adds an element to the set)
- remove(): ```my_set.remove(4)``` (removes an element from the set)
- discard():``` my_set.discard(4)``` (removes an element if it exists)
- pop(): ```my_set.pop()``` (removes and returns an arbitrary element)
- clear(): ```my_set.clear()``` (removes all elements)

## Set Properties

- len(): ```len(my_set)``` (returns the number of elements)
- in: ```4 in my_set``` (checks if an element is in the set)

## Creating Sets


### Create a set using curly brackets {}
```
my_set = {1, 2, 3, 4, 5}
print(my_set)  # {1, 2, 3, 4, 5}
```
### Create a set using the set() function
```
my_set = set([1, 2, 3, 4, 5])
print(my_set)  # {1, 2, 3, 4, 5}
```

## Set Operations

### Union (combines elements from both sets)
```
my_set1 = {1, 2, 3}
my_set2 = {3, 4, 5}
print(my_set1 | my_set2)  # {1, 2, 3, 4, 5}
```
### Intersection (returns elements common to both sets)
```
print(my_set1 & my_set2)  # {3}
```
### Difference (returns elements in my_set1 not in my_set2)
```
print(my_set1 - my_set2)  # {1, 2}
```
### Symmetric Difference (returns elements in either set, but not both)
```
print(my_set1 ^ my_set2)  # {1, 2, 4, 5}
```

## Set Methods


### Add an element to the set
```
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # {1, 2, 3, 4}
```
### Remove an element from the set
```
my_set.remove(2)
print(my_set)  # {1, 3, 4}
```
### Discard an element (removes if exists, otherwise does nothing)
```
my_set.discard(3)
print(my_set)  # {1, 4}
```
### Pop an arbitrary element from the set
```
print(my_set.pop())  # 1 (or 4, since sets are unordered)
```
### Clear the set
```
my_set.clear()
print(my_set)  # set()
```

## Set Properties


### Check if an element is in the set
```
my_set = {1, 2, 3}
print(2 in my_set)  # True
```
### Get the number of elements in the set
```
print(len(my_set))  # 3
```

These examples demonstrate the basics of Python sets, including creation, operations, methods, and properties. Sets are useful for storing unique elements and performing set operations.
