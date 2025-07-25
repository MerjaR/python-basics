# List comprehension with max two lines including def
def begin_with_vowel(words: list):
    return [word for word in words if word[0] in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]]

if __name__ == "__main__":
    word_list = ["automobile","motorbike","Animal","cat","Dog","APPLE","orange"]
    for vowelled in begin_with_vowel(word_list):
        print(vowelled)
