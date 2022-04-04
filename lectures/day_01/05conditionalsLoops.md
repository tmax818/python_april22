# Conditionals
--
>Conditional statements allow us to run certain lines of code depending on whether certain conditions are met. 
--
```py
condition = True
if condition:
    print("this is true")
```

```bash
this is true
```
<!-- .element: class="fragment" -->
--
```py
expression = "Something that returns a value."
if expression:
    print("Will this print?")
print("...or will this?")
```

```bash
Will this print?
...or will this?
```
<!-- .element: class="fragment" -->
--
```py
if not True:
    print("this ran...")
print("no this ran!!!")
```

```bash
no this ran!!!
```
<!-- .element: class="fragment" -->
--
```py
if not False:
    print("this ran...")
print("no this ran!!!")
```
```bash
this ran...
no this ran!!!
```
<!-- .element: class="fragment" -->
--
```py
if not True:
    print("this ran...")
else:
    print("no this ran!!!")
print("of course this ran, it's outside the conditional!!!")
```
```bash
this ran!!!
of course this ran, it's outside the conditional!!!
```
<!-- .element: class="fragment" -->
--
```py
if not True:
    print("this ran...")
elif True:
    print("the elif ran...")
else:
    print("no this ran!!!")
print("of course this ran, it's outside the conditional!!!")
```
```bash
the elif ran...
of course this ran, it's outside the conditional!!!
```
<!-- .element: class="fragment" -->
---
# Loops
--
## `for` loops with range
--
compare with JavaScript
```javascript
for(var i = 0; i < 10; i++) {
    console.log(i)
}
```
```bash
0
1
2
3
4
5
6
7
8
9
```
<!-- .element: class="fragment" -->
--
same code in Python:
```py
for i in range(10):
    print(i)
```
```bash
0
1
2
3
4
5
6
7
8
9
```
<!-- .element: class="fragment" -->
--
### range with 2 args:
```py
start = 0 # inclusive
stop = 10 # exclusive
step = 2
for i in range(start, stop, step):
    print(i)
```
```bash
0
2
4
6
8
```
<!-- .element: class="fragment" -->

---
# For Loop Basic I (Core)

