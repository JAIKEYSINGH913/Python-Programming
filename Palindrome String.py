# Q15.
# Write a function to check whether a given string is a palindrome.

def is_palindrome(text):
    # Convert text to lowercase to ignore capitalization issues
    clean_text = text.lower()

    # Reverse string using slicing
    reversed_text = clean_text[::-1]

    # Check equality
    return clean_text == reversed_text


word = "Radar"
if is_palindrome(word):
    print(f"'{word}' is a palindrome!")
else:
    print(f"'{word}' is not a palindrome.")
