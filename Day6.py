nums = [10, 20, 5, 40]

print("Max:", max(nums))
print("Min:", min(nums))
nums = [10, 20, 5, 40]
nums = list(set(nums))
nums.sort()
print("Second Largest:", nums[-2])
nums = [1, 2, 2, 3, 4, 4]
unique = list(set(nums))
print(unique)
nums = [1, 2, 3, 4, 5, 6]

even = 0
odd = 0

for n in nums:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even:", even)
print("Odd:", odd)
text = "MachineLearning"
print(text[::-1])
text = input("Enter string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
text = "Convolution Neutal Network"
count = {}

for ch in text:
    count[ch] = count.get(ch, 0) + 1

print(count)
text = "Deeplearning"
vowels = "aeiou"

v = 0
c = 0

for ch in text:
    if ch in vowels:
        v += 1
    else:
        c += 1

print("Vowels:", v)
print("Consonants:", c)
students = [
    {"Abhinav": "A", "marks": 70},
    {"Rithika": "B", "marks": 90},
    {"Rohan": "A" , "marks": 93},
    {"kavya": "A", "marks": 75},
]
top = students[0]

for s in students:
    if s["marks"] > top["marks"]:
        top = s

print("Topper:", top)
total = 0

for s in students:
    total += s["marks"]

avg = total / len(students)
print("Average:", avg)
passed = [s for s in students if s["marks"] >= 50]
print(passed)
nums = [10, 20, 5, 40]
nums = list(set(nums))
nums.sort()

print("Second Smallest:", nums[1])
list1 = [1, 2, 3]
list2 = [3, 4, 5]

merged = list(set(list1 + list2))
print(merged)
nums = [1, 2, 2, 3, 3,4,5,5,5,5, 3]
freq = {}

for n in nums:
    freq[n] = freq.get(n, 0) + 1

print(freq)