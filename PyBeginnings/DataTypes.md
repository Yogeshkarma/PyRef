
# 🐍 Python Data Types – Complete Guide

Understanding **data types** is one of the most important parts of learning Python.  
A **data type** defines the type of value a variable holds — such as numbers, text, or sequences.

---

## 📘 What are Data Types?

Every value in Python has a **data type**.  
It tells the interpreter what kind of operations can be performed on that value.

For example:
```python
a = 10       # Integer
b = "Hello"  # String
c = 3.14     # Float
````

---

## 🧮 1. Numeric Data Types

Numeric data types store numbers of different kinds.

| Type        | Description                                   | Example       |
| ----------- | --------------------------------------------- | ------------- |
| **int**     | Integer values without decimals               | `x = 42`      |
| **float**   | Floating-point numbers (decimal values)       | `y = 3.14159` |
| **complex** | Complex numbers with real and imaginary parts | `z = 2 + 3j`  |

### 🔹 Example:

```python
a = 5          # int
b = 2.5        # float
c = 3 + 4j     # complex

print(type(a)) # <class 'int'>
print(type(b)) # <class 'float'>
print(type(c)) # <class 'complex'>
```

---

## 🔤 2. String Data Type (`str`)

A **string** represents a sequence of characters enclosed in quotes.

### 🔹 Example:

```python
name = "Python"
message = 'Hello, World!'
```

### 🔹 String Operations:

```python
text = "Python"
print(text.upper())     # PYTHON
print(text.lower())     # python
print(text[0])          # P
print(text[1:4])        # yth
print(len(text))        # 6
```

---

## 📋 3. Sequence Data Types

### ➤ (a) **List**

A list is an **ordered**, **mutable** (changeable) collection of items.

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[1])         # banana
fruits.append("mango")   # add new item
```

✅ Lists can hold different data types:

```python
mixed = [10, "hello", 3.14, True]
```

---

### ➤ (b) **Tuple**

A tuple is an **ordered**, **immutable** collection of items.

```python
numbers = (1, 2, 3)
print(numbers[0])        # 1
# numbers[1] = 5 → ❌ Error (tuples are immutable)
```

✅ Used when you don’t want data to change.

---

### ➤ (c) **Range**

Represents a sequence of numbers, often used in loops.

```python
for i in range(5):
    print(i)
```

Output:

```
0
1
2
3
4
```

---

## 🧰 4. Mapping Data Type – `dict`

A **dictionary** stores data as key–value pairs.
It’s **unordered**, **mutable**, and **indexed** by keys.

```python
student = {
    "name": "Alice",
    "age": 20,
    "course": "Python"
}
```

### 🔹 Accessing values:

```python
print(student["name"])        # Alice
student["age"] = 21           # modify value
```

---

## 🧩 5. Set Data Types

### ➤ (a) **set**

A **set** is an **unordered**, **mutable** collection of unique items.

```python
nums = {1, 2, 3, 3, 2}
print(nums)     # {1, 2, 3} → duplicates removed
```

### ➤ (b) **frozenset**

An **immutable** version of a set.

```python
fnums = frozenset([1, 2, 3])
```

---

## ⚙️ 6. Boolean Data Type (`bool`)

Represents **True** or **False** values.

```python
is_active = True
is_greater = 10 > 5   # True
```

✅ Used in conditional statements:

```python
if is_greater:
    print("Yes, 10 is greater than 5!")
```

---

## ⚗️ 7. None Type (`NoneType`)

`None` represents the **absence of a value**.

```python
data = None
print(type(data))   # <class 'NoneType'>
```

Used as a placeholder for variables that are not yet assigned a value.

---

## 🧠 8. Type Conversion

You can convert between compatible data types using built-in functions.

| Function  | Description         | Example                      |
| --------- | ------------------- | ---------------------------- |
| `int()`   | Converts to integer | `int(3.14)` → `3`            |
| `float()` | Converts to float   | `float(5)` → `5.0`           |
| `str()`   | Converts to string  | `str(10)` → `'10'`           |
| `list()`  | Converts to list    | `list((1,2,3))` → `[1,2,3]`  |
| `tuple()` | Converts to tuple   | `tuple([1,2,3])` → `(1,2,3)` |
| `set()`   | Converts to set     | `set([1,2,2])` → `{1,2}`     |

---

## 🧾 Summary Table

| Category | Data Type                 | Mutable | Ordered | Example             |
| -------- | ------------------------- | ------- | ------- | ------------------- |
| Numeric  | `int`, `float`, `complex` | ❌       | ✅       | `10`, `3.5`, `2+3j` |
| Sequence | `str`                     | ❌       | ✅       | `"hello"`           |
| Sequence | `list`                    | ✅       | ✅       | `[1, 2, 3]`         |
| Sequence | `tuple`                   | ❌       | ✅       | `(1, 2, 3)`         |
| Mapping  | `dict`                    | ✅       | ❌       | `{"a":1}`           |
| Set      | `set`                     | ✅       | ❌       | `{1, 2, 3}`         |
| Set      | `frozenset`               | ❌       | ❌       | `frozenset({1,2})`  |
| Boolean  | `bool`                    | ❌       | ❌       | `True`, `False`     |
| None     | `NoneType`                | ❌       | ❌       | `None`              |

---

## 🎯 Conclusion

Python provides a wide range of **data types** to handle different kinds of data easily.
Knowing them helps you write more **efficient**, **readable**, and **error-free** programs.

> 🧩 Tip: You can always check a variable’s data type using the built-in `type()` function.

```python
x = [1, 2, 3]
print(type(x))   # <class 'list'>
```

Version 1.0

