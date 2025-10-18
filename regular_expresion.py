import re

# -------------------------------
# 1. re.search() → finds FIRST match
# -------------------------------
text = "I love Python"
match = re.search("Python", text)  # Looks for 'Python'
if match:
    print("Found:", match.group())   # Output: Found: Python

# -------------------------------
# 2. re.findall() → finds ALL matches
# -------------------------------
text = "apple, banana, apple, mango"
matches = re.findall("apple", text)
print(matches)   # Output: ['apple', 'apple']

# -------------------------------
# 3. re.split() → split string by pattern
# -------------------------------
text = "one,two;three four"
parts = re.split("[,; ]", text)  # split by , or ; or space
print(parts)   # Output: ['one', 'two', 'three', 'four']

# -------------------------------
# 4. re.sub() → replace text
# -------------------------------
text = "I like java, java is good"
new_text = re.sub("java", "python", text)
print(new_text)  # Output: I like python, python is good

# -------------------------------
# 5. Common Meta Characters
# -------------------------------
# .  → any char
# ^  → start of string
# $  → end of string
# *  → 0 or more
# +  → 1 or more
# ?  → 0 or 1
# {m,n} → between m and n times
# [] → set of chars
# |  → OR
# \d → digit
# \w → word (letters, digits, _)
# \s → whitespace

# -------------------------------
# 6. Example: Match digits
# -------------------------------
text = "My phone number is 9876543210"
digits = re.findall(r"\d+", text)   # \d+ → one or more digits
print(digits)  # Output: ['9876543210']

# -------------------------------
# 7. Example: Validate Email
# -------------------------------
email = "test@example.com"
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"  # Regex for simple email
if re.match(pattern, email):
    print("Valid Email")  # Output: Valid Email
else:
    print("Invalid Email")

# -------------------------------
# 8. Example: Extract Capitalized Words
# -------------------------------
text = "Python is Great and Powerful"
words = re.findall(r"\b[A-Z][a-z]*\b", text)
print(words)  # Output: ['Python', 'Great', 'Powerful']
