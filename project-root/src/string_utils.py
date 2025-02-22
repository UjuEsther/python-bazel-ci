"""
string_utils.py
Provides string manipulation utilities.
"""

def reverse_string(s):
    """Returns the reverse of a string."""
    return s[::-1]

def is_palindrome(s):
    """Checks if a string is a palindrome."""
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def count_vowels(s):
    """Counts the number of vowels in a string."""
    return sum(1 for char in s.lower() if char in "aeiou")
