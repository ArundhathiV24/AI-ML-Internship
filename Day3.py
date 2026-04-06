numbers = [1,2,3,4,5,6,7,8,9,10]
print("List:", numbers)

# 2. Find sum of list elements
print("Sum:", sum(numbers))

# 3. Find maximum number
print("Max:", max(numbers))

# 4. Print even numbers from list
print("Even numbers:")
for num in numbers:
    if num % 2 == 0:
        print(num)

# 5. Reverse a list
print("Reversed list:", numbers[::-1])
# 1. Create student dictionary
student = {
    "name": "Arundhathi",
    "age": 23,
    "marks": 85
}

print("Student:", student)

# 2. Update marks
student["marks"] = 90

# 3. Add new key (grade)
student["grade"] = "A"

# 4. Print all keys and values
print("\nUpdated Student Details:")
for key, value in student.items():
    print(key, ":", value)
text = "madam"

# 1. Count number of characters
print("Length:", len(text))

# 2. Reverse a string
print("Reversed:", text[::-1])

# 3. Check palindrome
if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# 4. Count vowels
vowels = "aeiou"
count = 0
for char in text:
    if char.lower() in vowels:
        count += 1
print("Vowel count:", count)
# 1. Remove duplicates from list using set
list1 = [1,2,2,3,4,4,5]
unique_list = list(set(list1))
print("Unique list:", unique_list)

# 2. Find common elements between two sets
set1 = {1,2,3,4}
set2 = {3,4,5,6}

common = set1.intersection(set2)
print("Common elements:", common)
# 1. Squares from 1–10
squares = [x*x for x in range(1,11)]
print("Squares:", squares)

# 2. Even numbers from 1–20
even_numbers = [x for x in range(1,21) if x % 2 == 0]
print("Even numbers:", even_numbers)