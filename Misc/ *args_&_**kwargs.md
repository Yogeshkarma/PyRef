
# 🌟 Understanding `*args` and `**kwargs` in Python

When you don’t know **how many arguments** a function will receive — Python gives you two magic tools:  
👉 `*args` and `**kwargs`

Let’s break them down in the easiest way possible 💡

---

## 🧩 1. What are `*args`?

### ✅ Meaning:
`*args` allows you to pass **any number of positional arguments** (without knowing how many in advance).

### 🧠 Think of it like:
> "I want my function to accept as many values as the user wants to send."

### 🔹 Example:
```python
def show_numbers(*args):
    print(args)

show_numbers(1, 2, 3)
show_numbers(5, 10, 15, 20)
````

### 🧾 Output:

```
(1, 2, 3)
(5, 10, 15, 20)
```

✅ `args` collects all values into a **tuple**.

---

## 🪄 2. You Can Loop Through `*args`

```python
def show_numbers(*args):
    for num in args:
        print(num)

show_numbers(10, 20, 30)
```

Output:

```
10
20
30
```

---

## 🎯 3. `*args` with Other Parameters

You can use normal parameters **before** `*args`.

```python
def greet(greeting, *names):
    for name in names:
        print(f"{greeting}, {name}!")

greet("Hello", "Alice", "Bob", "Charlie")
```

Output:

```
Hello, Alice!
Hello, Bob!
Hello, Charlie!
```

---

## 🧱 4. What are `**kwargs`?

### ✅ Meaning:

`**kwargs` lets you pass **any number of keyword arguments** (like `key=value` pairs).

### 🧠 Think of it like:

> "I want my function to accept as many key-value pairs as needed."

### 🔹 Example:

```python
def show_info(**kwargs):
    print(kwargs)

show_info(name="Alice", age=25, country="India")
```

### 🧾 Output:

```
{'name': 'Alice', 'age': 25, 'country': 'India'}
```

✅ `kwargs` collects all values into a **dictionary**.

---

## 🪄 5. You Can Loop Through `**kwargs`

```python
def show_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

show_info(name="John", age=30, city="Mumbai")
```

Output:

```
name = John
age = 30
city = Mumbai
```

---

## 🧠 6. Using Both `*args` and `**kwargs` Together

Yes! You can use both in the same function 😄

```python
def display_data(*args, **kwargs):
    print("Positional:", args)
    print("Keyword:", kwargs)

display_data(1, 2, 3, name="Alice", age=20)
```

Output:

```
Positional: (1, 2, 3)
Keyword: {'name': 'Alice', 'age': 20}
```

✅ `*args` → stores positional arguments (as a tuple)
✅ `**kwargs` → stores keyword arguments (as a dictionary)

---

## ⚙️ 7. Order of Parameters

When using all types of parameters, follow this order:

```
def function(normal, *args, default, **kwargs):
    pass
```

💡 **Easy rule to remember:**

> Normal → `*args` → Default → `**kwargs`

Example:

```python
def mix_example(a, b, *args, x=10, **kwargs):
    print(a, b)
    print(args)
    print(x)
    print(kwargs)

mix_example(1, 2, 3, 4, 5, x=99, y=100, z=200)
```

Output:

```
1 2
(3, 4, 5)
99
{'y': 100, 'z': 200}
```

---

## 🚀 8. Using `*` and `**` When Calling Functions

You can also **unpack** values when calling a function.

### Example:

```python
def add(a, b, c):
    print(a + b + c)

nums = (1, 2, 3)
add(*nums)   # same as add(1, 2, 3)
```

Output:

```
6
```

### With Dictionary:

```python
def introduce(name, age, country):
    print(f"My name is {name}, I'm {age}, from {country}")

person = {"name": "Alice", "age": 25, "country": "India"}
introduce(**person)
```

Output:

```
My name is Alice, I'm 25, from India
```

---

## 🧾 Summary Table

| Symbol     | Stands For        | Collects          | Type       | Example          |
| ---------- | ----------------- | ----------------- | ---------- | ---------------- |
| `*args`    | Arguments         | Positional values | Tuple      | `show(1, 2, 3)`  |
| `**kwargs` | Keyword Arguments | Key–value pairs   | Dictionary | `show(a=1, b=2)` |

---

## 🎯 In Simple Words

* `*args` → use when you want **many inputs without names**.
* `**kwargs` → use when you want **many inputs with names**.
* You can use **both together** for maximum flexibility!

---

## 💡 Tip

If you’re unsure:

> Use `*args` and `**kwargs` to make your function flexible enough to handle anything!

version 1.0
