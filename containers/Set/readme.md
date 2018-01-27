#!/usr/bin/env python
 
x = set(["Postcard", "Radio", "Telegram"])
print(x)
 
y = {"Postcard","Radio","Telegram"}
print(y)
************************************************
Set Methods
************************************************

1)Clear elements from set
To remove all elements from sets:
ex:
x = set(["Postcard", "Radio", "Telegram"])
x.clear()
print(x)

2)Add elements to a set
To add elements to a set:
ex:
x = set(["Postcard", "Radio", "Telegram"])
x.add("Telephone")
print(x)

3)Remove elements to a set
To remove elements to a set:
ex:
x = set(["Postcard", "Radio", "Telegram"])
x.remove("Radio")
print(x)

4)Difference between two sets
To find the difference between two sets use:
ex:
x = set(["Postcard", "Radio", "Telegram"])
y = set(["Radio","Television"])
>>>print( x.difference(y) )
set(['Postcard', 'Telegram'])
>>>print( y.difference(x) )
set(['Television'])
>>> print x
set(['Postcard', 'Telegram', 'Radio'])
>>> print y
set(['Television', 'Radio'])

Be aware that x.difference(y) is different from y.difference(x).


Here we can see that values in x and y do not change. If we want the values to change in them then use
differece_update() function.
>>> x.difference_update(y)
>>> print x
set(['Postcard', 'Telegram'])

5)Subset
To test if a set is a subset use:
ex:
x = set(["a","b","c","d"])
y = set(["c","d"])
print( x.issubset(y) )<b>
</b>

6)Super-set
To test if a set is a super-set:
ex:
x = set(["a","b","c","d"])
y = set(["c","d"])
print( x.issuperset(y) )

7)Intersection
To test for intersection, use:
ex:
x = set(["a","b","c","d"])
y = set(["c","d"])
print( x.intersection(y) )

We also have function to change the values of set x.intersection_update(y)
