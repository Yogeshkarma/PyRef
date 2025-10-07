# ⚙️ Python Generators — The Easiest Guide Ever!

## 🧠 What is a Generator?

A **generator** is a special type of function in Python that lets you **generate values one at a time** instead of returning them all at once.

Think of it like a **lazy worker** — it gives you one item at a time **only when you ask for it** 👷‍♂️

---

## 🧩 Normal Function vs Generator Function

### 🧾 Normal Function:
```python
def get_numbers():
    return [1, 2, 3, 4, 5]

print(get_numbers())
````

Output:

```
[1, 2, 3, 4, 5]
```

👉 It returns the whole list at once.

---

### ⚙️ Generator Function:

```python
def get_numbers():
    for i in range(1, 6):
        yield i
```

Here we used the keyword **`yield`** instead of **`return`**.

Output:

```python
nums = get_numbers()
print(nums)
```

You’ll get:

```
<generator object get_numbers at 0x000001>
```

Because it **doesn’t run immediately**, it just **creates a generator object**.

---

## 🌀 Getting Values from a Generator

You can get values **one by one** using the `next()` function:

```python
nums = get_numbers()

print(next(nums))  # 1
print(next(nums))  # 2
print(next(nums))  # 3
```

When there are no more values, Python raises a `StopIteration` error.

---

## 🔁 Looping Through a Generator

Instead of calling `next()` manually, use a `for` loop:

```python
for num in get_numbers():
    print(num)
```

Output:

```
1
2
3
4
5
```

---

## 🚀 Why Use Generators?

| Normal Function            | Generator                 |
| -------------------------- | ------------------------- |
| Stores all data in memory  | Generates data one by one |
| Can be slow for large data | Very memory efficient     |
| Uses `return`              | Uses `yield`              |

---

## 🧮 Example: Large Range

```python
def big_numbers():
    for i in range(1, 1000000):
        yield i
```

Even though it can produce **10 lakh numbers**, it doesn’t store them all — it generates them **on the go!**

---

## ⚙️ Example: Generator for Even Numbers

```python
def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

for num in even_numbers(10):
    print(num)
```

Output:

```
0
2
4
6
8
```

---

## 🧩 Generator Expressions (Shortcut)

Just like list comprehensions, but with **()`** instead of **[]**.

```python
squares = (x*x for x in range(5))
print(next(squares))  # 0
print(next(squares))  # 1
```

---

## 🎯 When to Use Generators

✅ When working with **large data** (like files or big lists)
✅ When you want to **save memory**
✅ When you need **streaming or lazy loading** (like reading lines from a file)

---

## 📂 Real Example: Reading a Large File

```python
def read_file_line_by_line(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()
```

This reads one line at a time — perfect for **huge files**!

---

## 🧩 Summary

| Keyword              | Meaning                                 |
| -------------------- | --------------------------------------- |
| `yield`              | Used instead of `return` in a generator |
| `next()`             | Gets the next value from the generator  |
| `StopIteration`      | Raised when generator is exhausted      |
| Generator Expression | `(x for x in range(...))`               |

---

## 🚀 In One Line:

**Generators = Functions that remember where they left off and give you values one by one!**

---
