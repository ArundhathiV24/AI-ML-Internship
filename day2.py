# =========================
# TASK 1: THEORY (PRINT)
# =========================
print("1. Python is used in AI because it is simple and has powerful libraries.")
print("2. Variables store data values.")
print("3. Data type defines type of data (int, float, string, boolean).")
print("4. If is for decision making, loop is for repetition.")
print("5. Function is a reusable block of code.\n")


# =========================
# TASK 2: BASIC CODING
# =========================

# 1. Print details
print("---- Details ----")
name = "Arundhathi"
age = 23
course = "M.Tech Data Science"
print(name, age, course)

# 2. Arithmetic operations
print("\n---- Arithmetic ----")
a = 10
b = 5
print("Add:", a + b)
print("Subtract:", a - b)
print("Multiply:", a * b)

# 3. Even or Odd
num = int(input("\nEnter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 4. Largest of two numbers
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
if x > y:
    print("Largest:", x)
else:
    print("Largest:", y)

# 5. Input and display
user_name = input("Enter your name: ")
print("Hello", user_name)


# =========================
# TASK 3: LOGIC BUILDING
# =========================

# 1. Positive, negative, zero
num = int(input("\nEnter number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 2. Largest of 3 numbers
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)

# 3. Grade system
marks = int(input("Enter marks: "))
if marks > 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
else:
    print("Grade C")


# =========================
# TASK 4: LOOPS
# =========================

print("\nNumbers 1 to 20:")
for i in range(1, 21):
    print(i)

print("\nEven numbers:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

n = int(input("\nEnter N: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum:", total)

print("\nReverse 10 to 1:")
for i in range(10, 0, -1):
    print(i)


# =========================
# TASK 5: FUNCTIONS
# =========================

def add(a, b):
    return a + b

print("\nAddition using function:", add(5, 3))


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print("Is 7 prime?", is_prime(7))


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print("Factorial of 5:", factorial(5))


# =========================
# BONUS TASKS
# =========================

print("\nPattern:")
for i in range(1, 5):
    print("*" * i)

# Reverse number
num = int(input("\nEnter number: "))
rev = 0
temp = num

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

print("Reversed:", rev)

# Count digits
num = int(input("Enter number: "))
count = 0

while num > 0:
    num //= 10
    count += 1

print("Number of digits:", count)