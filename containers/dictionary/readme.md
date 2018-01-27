There are two important points to remember about dictionary keys −

(a) More than one entry per key not allowed. Which means no duplicate key is allowed. When duplicate keys encountered during assignment, the last assignment wins. For example −
ex:
dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
print "dict['Name']: ", dict['Name']

(b) Keys must be immutable. Which means you can use strings, numbers or tuples as dictionary keys but something like ['key'] is not allowed. Following is a simple example −
ex:
dict = {['Name']: 'Zara', 'Age': 7}
print "dict['Name']: ", dict['Name']

When the above code is executed, it produces the following result −

Traceback (most recent call last):
   File "test.py", line 3, in <module>
      dict = {['Name']: 'Zara', 'Age': 7};
TypeError: list objects are unhashable

Dictionary and Set uses hashing technique whereas list does not use hashing.

Python includes following dictionary methods −
1 	dict.clear()
Removes all elements of dictionary dict

2 	dict.copy()
Returns a shallow copy of dictionary dict

3 	dict.fromkeys()
Create a new dictionary with keys from seq and values set to value.

4 	dict.get(key, default=None)
For key key, returns value or default if key not in dictionary

5 	dict.has_key(key)
Returns true if key in dictionary dict, false otherwise

6 	dict.items()
Returns a list of dict's (key, value) tuple pairs

7 	dict.keys()
Returns list of dictionary dict's keys

8 	dict.setdefault(key, default=None)
Similar to get(), but will set dict[key]=default if key is not already in dict

9 	dict.update(dict2)
Adds dictionary dict2's key-values pairs to dict

10 	dict.values()
Returns list of dictionary dict's values
