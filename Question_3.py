#Make a code for tokenization using regex?

import re

# Sample text
text = "Hello everyone. I am Abdullah Al Mamun. I am 23 years old. Currently I am writing a code to tokenize this string."

# Find all tokens using the regex pattern
tokens = re.findall(r'\b\w+\b', text)

print("Original Text:")
print(text)
print("\nTokens:")
print(tokens)
