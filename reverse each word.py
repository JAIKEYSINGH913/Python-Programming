# Q22.
# Write a program to reverse each word in a given sentence.

sentence = "Python is fun"
words = sentence.split()
reversed_words = []

for word in words:
    # Reverse string using slicing
    rev = word[::-1]
    reversed_words.append(rev)

# Combine the words back into a single string
final_sentence = " ".join(reversed_words)
print(f"Original: {sentence}")
print(f"Reversed: {final_sentence}")
