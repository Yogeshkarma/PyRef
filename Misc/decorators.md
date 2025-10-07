
# 🧩 Python Decorators — The Easiest Guide Ever!

## 🌟 What is a Decorator?

A **decorator** is just a way to **add extra features or behavior to a function** — without changing its original code!

Think of it like a **sticker** you put on something to make it look or act cooler 😎  
You “decorate” the function with some extra power!

---

## 🧠 Basic Example

Let’s start simple 👇

```python
def greet():
    print("Hello!")

# calling normally
greet()
````

Output:

```
Hello!
```

Now let’s say we want to **add** something before or after `greet()` runs.
We can do that using a **decorator**.

---

## 🪄 Creating a Decorator

A decorator is a **function that takes another function as input**, adds something to it, and returns it.

```python
def my_decorator(func):
    def wrapper():
        print("✨ Something before the function runs")
        func()  # calling the original function
        print("✅ Something after the function runs")
    return wrapper
```

Now, use it to decorate another function:

```python
@my_decorator
def greet():
    print("Hello!")

greet()
```

Output:

```
✨ Something before the function runs
Hello!
✅ Something after the function runs
```

---

## 🧩 How It Works Behind the Scenes

When you write:

```python
@my_decorator
def greet():
    print("Hello!")
```

It is the same as writing:

```python
def greet():
    print("Hello!")

greet = my_decorator(greet)
```

So, `greet` becomes the **wrapper function** returned by the decorator!

---

## 💡 Decorator with Arguments

Let’s say your function takes arguments:

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function runs")
        func(*args, **kwargs)
        print("After function runs")
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Python")
```

Output:

```
Before function runs
Hello, Python!
After function runs
```

---

## ⚙️ Real-Life Uses of Decorators

Decorators are used everywhere in Python!
Here are some **real uses**:

✅ **Logging** — Track when a function runs
✅ **Authentication** — Check login before accessing data
✅ **Timing** — Measure how long a function takes
✅ **Validation** — Automatically check inputs

---

## ⏱ Example: Timing a Function

```python
import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        end = time.time()
        print(f"⏰ Time taken: {end - start} seconds")
    return wrapper

@timer
def slow_function():
    time.sleep(2)
    print("Done!")

slow_function()
```

Output:

```
Done!
⏰ Time taken: 2.0 seconds
```

---

## 🎀 Summary

| Concept           | Meaning                                       |
| ----------------- | --------------------------------------------- |
| `@decorator`      | Adds extra behavior to a function             |
| `wrapper()`       | Inner function that runs extra code           |
| `*args, **kwargs` | Helps decorator handle any function arguments |
| Real uses         | Logging, timing, validation, access control   |

---

## 🚀 In One Line:

**Decorators = Functions that modify other functions (without touching their code)!**

