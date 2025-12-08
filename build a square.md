### build a square
```
def generate_shape(n):
    square ="+"*n
    return "\n".join(square for i in range(n))
```
# Step-by-step explanation of `generate_shape(n)`

## 1️⃣ **Create the first variable**
It creates a variable **`square`** that takes the value of **`<n>`** and multiplies the **`'+'`** character by **`<n>`** to form a single line of the square.

## 2️⃣ **Repeat the line**
It repeats the **`square`** variable **`<n>`** times using a loop or comprehension, creating multiple lines. 

## 3️⃣ **Join the lines**
It joins all the repeated lines with **`"\n"`** to form a full square and returns the result.

![flowchart](make_square_flowchart.png)