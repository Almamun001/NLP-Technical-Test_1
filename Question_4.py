#How to fetch email and phone from a text using regex? Implement

import re

# Sample text
text = """
 I am 23 years old. Currently I am writing a code to tokenize this string.
Contact me at al.mamun@gmail.com or mamun001@iubat.edu.bd. 
For phone, you can reach me at +88 01724592883 or +88 01612255225 
My secondary contact is 123 456 7890. Email me@my-domain.com for assistance.
"""

# Regex patterns
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
phone_pattern = r'\+?\d[\d -]{8,}\d'

# Find all emails and phone numbers
emails = re.findall(email_pattern, text)
phones = re.findall(phone_pattern, text)

print("Original Text:")
print(text)
print("\nEmails:")
print(emails)
print("\nPhone Numbers:")
print(phones)
