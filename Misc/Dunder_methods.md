
# ✨ Python Dunder (Magic) Methods — The Easiest Guide

In Python, **dunder methods** (also called **magic methods**) are **special methods with double underscores** at the beginning and end, like `__init__` or `__str__`.

They allow you to **define how objects behave** with built-in operations like printing, adding, or comparing.  

---

## 🧩 What are Dunder Methods?

- Start and end with **double underscores**: `__method__`
- Python automatically calls them in certain situations
- You **don’t call them directly** most of the time

### Examples:

| Dunder Method | Triggered When |
|---------------|----------------|
| `__init__` | When creating an object |
| `__str__` | When printing an object |
| `__add__` | When using `+` operator |
| `__len__` | When using `len()` |
| `__eq__` | When comparing objects with `==` |

---

## 🏗️ 1. `__init__` — The Constructor

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 25)
print(p.name, p.age)
````

Output:

```
Alice 25
```

✅ Runs automatically when a new object is created.

---

## 🖨️ 2. `__str__` — How to Print Objects Nicely

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

p = Person("Bob", 30)
print(p)
```

Output:

```
Bob is 30 years old
```

Without `__str__`, Python prints something like `<__main__.Person object at 0x000>` 😅

---

## ➕ 3. `__add__` — Customize Addition

```python
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

a = Number(5)
b = Number(10)
print(a + b)
```

Output:

```
15
```

✅ Lets you **define how `+` works** for your objects.

---

## ⚖️ 4. `__eq__` — Customize Equality Check

```python
class Person:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return self.name == other.name

p1 = Person("Alice")
p2 = Person("Alice")
print(p1 == p2)
```

Output:

```
True
```

✅ Compares objects **based on your rules** instead of memory address.

---

## 📏 5. `__len__` — Customize Length

```python
class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

lst = MyList([1,2,3,4])
print(len(lst))
```

Output:

```
4
```

✅ Lets `len()` work with your custom objects.

---

## 🔄 6. Other Common Dunder Methods

| Method        | Triggered When                         |
| ------------- | -------------------------------------- |
| `__sub__`     | `-` operator                           |
| `__mul__`     | `*` operator                           |
| `__gt__`      | `>` operator                           |
| `__lt__`      | `<` operator                           |
| `__getitem__` | Accessing item like `obj[key]`         |
| `__setitem__` | Assigning item like `obj[key] = value` |
| `__call__`    | Calling object like a function         |

---

## 🚀 7. Example: Combining Multiple Dunder Methods

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(2, 3)
p2 = Point(5, 7)
p3 = p1 + p2
print(p3)
```

Output:

```
Point(7, 10)
```

✅ We can **add points** and **print them nicely**.

---

## 🧩 Summary

| Dunder Method                   | Purpose                                     |
| ------------------------------- | ------------------------------------------- |
| `__init__`                      | Constructor, runs when creating object      |
| `__str__`                       | Defines string representation for `print()` |
| `__repr__`                      | Defines official representation (`repr()`)  |
| `__add__`, `__sub__`, `__mul__` | Define `+`, `-`, `*` operations             |
| `__eq__`, `__lt__`, `__gt__`    | Comparisons (`==`, `<`, `>`)                |
| `__len__`                       | Defines behavior for `len()`                |
| `__getitem__`, `__setitem__`    | Access and assign items using `[]`          |
| `__call__`                      | Make objects callable like a function       |

---

## 💡 Tip:

* **Dunder methods = special methods that Python calls automatically**
* They let you **customize the behavior of your objects**
* Start using `__str__`, `__add__`, and `__eq__` for fun and practical OOP coding!

