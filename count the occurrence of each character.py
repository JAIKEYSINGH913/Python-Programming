# Q19.
# Write a program to count the occurrence of each character in a given string using a dictionary.

text = "hello"
char_counts = {}

for char in text:
    if char in char_counts:
        char_counts[char] += 1
    else:
        char_counts[char] = 1

print(f"Character occurrences in '{text}':")
print(char_counts)
