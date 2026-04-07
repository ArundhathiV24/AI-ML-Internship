#!/usr/bin/env python
# coding: utf-8

# In[1]:


with open("data.txt", "w") as file:
    file.write("Name: Arundhathi\n")
    file.write("Course: M.Tech Data Science\n")
    file.write("Location: Kerala\n")


# In[3]:


with open("data.txt", "r") as file:
    content = file.read()
    print(content)


# In[5]:


with open("data.txt", "a") as file:
    file.write("\nNew Entry: AI/ML Intern")


# In[7]:


with open("data.txt", "r") as file:
    lines = file.readlines()
    print("Number of lines:", len(lines))


# In[9]:


with open("data.txt", "r") as file:
    text = file.read()
    words = text.split()
    print("Number of words:", len(words))


# In[11]:


try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)
except ZeroDivisionError:
    print("Cannot divide by zero!")


# In[15]:


try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter a number.")


# In[17]:


try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter a number.")


# In[19]:


try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Division by zero error!")
except ValueError:
    print("Invalid input!")
else:
    print("Result is:", result)
finally:
    print("Execution completed.")


# In[21]:


try:
    with open("data.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found!")


# In[23]:


with open("data.txt", "r") as file:
    words = file.read().split()
    longest = max(words, key=len)
    print("Longest word:", longest)


# In[25]:


with open("data.txt", "r") as file:
    text = file.read().lower()
    vowels = "aeiou"
    count = sum(1 for char in text if char in vowels)
    print("Number of vowels:", count)


# In[27]:


with open("data.txt", "r") as file:
    lines = file.readlines()

unique_lines = list(set(lines))

with open("data.txt", "w") as file:
    file.writelines(unique_lines)

print("Duplicate lines removed.")

