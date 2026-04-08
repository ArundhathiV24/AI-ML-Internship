# 1. Reverse a string
text = "python"
print(text[::-1])

# 2. Count number of words
sentence = "AI ML Python"
print(len(sentence.split()))

# 3. Check palindrome
word = "madam"
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# 4. Replace words
text = "hello ai"
print(text.replace("ai", "ml"))

# 5. Count vowels
text = "machine learning"
vowels = "aeiou"
count = 0
for char in text:
    if char in vowels:
        count += 1
print(count)
students = [
    {"name": "A", "marks": 70},
    {"name": "B", "marks": 85},
    {"name": "C", "marks": 90},
    {"name": "D", "marks": 60},
    {"name": "E", "marks": 75}
]
# 2. Print all students
for s in students:
    print(s)
# 3. Find average marks
total = 0
for s in students:
    total += s["marks"]
avg = total / len(students)
print("Average:", avg)
# 4. Find highest marks
max_marks = max(s["marks"] for s in students)
print("Highest:", max_marks)
# 5. Print students with marks > 75
for s in students:
    if s["marks"] > 75:
        print(s["name"])

# Using Math Module        
import math

print("Square root of 25:", math.sqrt(25))
print("2 raised to power 3:", math.pow(2, 3))

# 2. Using random module
import random

print("Random number between 1 and 10:", random.randint(1, 10))
print("Random choice from list:", random.choice([1, 2, 3, 4]))


# 3. Creating your own module logic (function)
def greet(name):
    return "Hello " + name

print(greet("AI Student"))
print(greet("AI Student"))
# 1. Second highest number
nums = [10, 20, 4, 45, 99]
nums = list(set(nums))
nums.sort()
print(nums[-2])

# 2. Count frequency of characters
text = "hello"
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1
print(freq)

# 3. Remove duplicates
nums = [1, 2, 2, 3, 4, 4]
unique = list(set(nums))
print(unique)