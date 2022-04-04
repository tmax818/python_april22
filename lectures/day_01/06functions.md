# Functions
--
>A function is a named block of code that we can execute to perform a specific task.
--
see [functions.py](./files/functions.py)
and [functions.js](./files/functions.js)
--
## syntax
--
- use the `def` keyword and end the function signature with a colon:
--
## parameters and arguments
- define the function with optional parameters
- `parameter` is the variable that will hold or reference the argument(s) passed in when the function is invoked/called.
--
```py
#function declaration:
def function_name(parameter):
    print(parameter)
```
<!-- .element: class="fragment" -->
```py
#function invocation: invoke or call
function_name('argument')
```
<!-- .element: class="fragment" -->
```bash
argument
```
<!-- .element: class="fragment" -->
--
## returning values
--
```py
def seven(lucky_number):
    print(lucky_number)
    return 6 + 1
```
<!-- .element: class="fragment" -->
```py
return_value = seven(42)
```
<!-- .element: class="fragment" -->
```bash
# => print to terminal the argument: 42
# => returns 7
```
<!-- .element: class="fragment" -->
```py
print(return_value)
# print function prints the return value to the terminal
```
<!-- .element: class="fragment" -->
--
>**a function is what it returns**
--
## compare to JavaScript

```javascript
// functions.js

function functionName(parameter) {
    console.log("inside function:", parameter)
    return parameter
}

console.log("value of the function: ", functionName('argument'))
```
---
# Default Parameters & Named Arguments
--
>default parameters allow optional arguments and named arguments allow different order of arguments
--

```py
def divide(a,b):
    return a/b
```
<!-- .element: class="fragment" -->
```py
divide(10,2):
```
<!-- .element: class="fragment" -->

---
# Debugging
---
# Functions Basic I (Practice)
--
```py
#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
```

```bash
5
```
<!-- .element: class="fragment" -->
--
```py
#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
```
```bash
NameError: name 'number_of_days_in_a_week_silicon_or_triangle_sides' is not defined
```
<!-- .element: class="fragment" -->
--
```py
#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
```
```bash
5
```
<!-- .element: class="fragment" -->
--
```py
#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())

```
```bash
5
```
<!-- .element: class="fragment" -->
--
```py
#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
```
```bash
None
```
<!-- .element: class="fragment" -->

--
```py
#6
def add(b,c):
    print(b+c)
print(add(1,2) + add(2,3))
```
```bash
TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
```
<!-- .element: class="fragment" -->


---
# Functions Basic II (Practice)
---
# Functions Intermediate I (Core)