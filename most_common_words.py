# Finding how many times a word appears in text, returning a dictionary with words that appear more times than lower_limit
import string

def most_common_words(filename: str, lower_limit: int):
    with open(filename, 'r') as file:
        text = file.read()
    
    words = text.split()
    cleaned_words = [word.strip(string.punctuation) for word in words]

    word_counts = {}

    for word in cleaned_words:
        if word:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
    
    filtered_counts = {word: count for word, count in word_counts.items() if count >= lower_limit}

    return filtered_counts

if __name__ == "__main__":

    print(most_common_words("comprehensions.txt", 3))

