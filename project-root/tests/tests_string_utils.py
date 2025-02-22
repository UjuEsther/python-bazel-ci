import pytest
from src.string_utils import reverse_string, is_palindrome, count_vowels

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Python") == "nohtyP"

def test_is_palindrome():
    assert is_palindrome("madam") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("Racecar") == True

def test_count_vowels():
    assert count_vowels("hello") == 2
    assert count_vowels("AEIOU") == 5
    assert count_vowels("xyz") == 0
