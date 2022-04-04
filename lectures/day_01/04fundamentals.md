
# Composite
---
# Lists
--
```py
fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetables = ['lettuce', 'cucumber', 'carrots']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)
```

```bash
['apple', 'banana', 'orange', 'strawberry', 'lettuce', 'cucumber', 'carrots']
```
<!-- .element: class="fragment" -->

--
```py
fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetables = ['lettuce', 'cucumber', 'carrots']
fruits_and_vegetables = fruits + vegetables
salad = 3 * vegetables
print(salad)
```

```bash
['lettuce', 'cucumber', 'carrots', 'lettuce', 'cucumber', 'carrots', 'lettuce', 'cucumber', 'carrots']
```
<!-- .element: class="fragment" -->

--
```py
my_list = [0,1,2,3,4,5]
```
--
```py
my_list = [0,1,2,3,4,5]
print(my_list[0])
```
## 0    <!-- .element: class="fragment" -->
--
```py
my_list = [0,1,2,3,4,5]
print(my_list[3])
```
## 3    <!-- .element: class="fragment" -->
--
```py
my_list = [0,1,2,3,4,5]
print(my_list[6])
```
`IndexError: list index out of range`    <!-- .element: class="fragment" -->
--
```py
x = [99,4,2,5,-3]
print(x[:])
```
```bash
#the output would be [99,4,2,5,-3]
```
<!-- .element: class="fragment" -->
--
```py
x = [99,4,2,5,-3]
print(x[1:])
```
```
#the output would be [4,2,5,-3];
```
<!-- .element: class="fragment" -->
--
```py
x = [99,4,2,5,-3]
print(x[:4])
```
```
#the output would be [99,4,2,5]
```
<!-- .element: class="fragment" -->
--
```py
nums = [0,1,2,3,4,5,6,7,8,9]
start = 0
stop = 10
step =1

print(nums[start:stop:step])
```
```bash
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
<!-- .element: class="fragment" -->
--
```py
nums = [0,1,2,3,4,5,6,7,8,9]
nums.append(10)
print(nums)
```
```bash
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10]
```
<!-- .element: class="fragment" -->

---
# Tuples
-- 
Python's immutable version of a list.
--
```py
dog = ("Canis Familiaris", "dog", "carnivore", 12)
```
-- 
```py
dog = ("Canis Familiaris", "dog", "carnivore", 12)
dog = dog + ("domestic",)
```
```bash
#("Canis Familiaris", "Dog", "carnivore", 12, "domestic")
```
<!-- .element: class="fragment" -->
-- 
```py
dog = ("Canis Familiaris", "dog", "carnivore", 12)
print(id(dog))
dog = dog + ("domestic",)
print(id(dog))

```
```bash
1744714210480
1744713248944
```
<!-- .element: class="fragment" -->


---
# Hello World (Practice)
---
# Dictionaries
--
>A Dictionary is another mutable set type that can store any number of Python objects, including other set types. Dictionaries consist of pairs (called items) of keys and their corresponding values.
--
```py
person_list = ["Tyler", 39, True, True]
```
```py
person_dict = {'name': "Tyler", 'age': 39}
```
<!-- .element: class="fragment" -->
```py
address = {'street': "123 Main", 'city': 'Santa Clarita', 'state': 'CA', 'zip': 91355}
```

<!-- .element: class="fragment" -->
```py
person_dict['address'] = address
```
<!-- .element: class="fragment" -->

```py
person_dict = {'name': "Tyler", 'age': 39,
'address': {'street': "123 Main", 'city': 'Santa Clarita',
 'state': 'CA', 'zip': 91355}}
```
<!-- .element: class="fragment" -->

note:
break for lunch
or do demo