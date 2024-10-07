import string
from collections import Counter


def clean_text(text):
    """
    Removes punctuation from text and converts it to lowercase.
    """
    # Remove all punctuation characters
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator)

    # Convert all text to lowercase to ensure case-insensitive counting
    cleaned_text = cleaned_text.lower()

    return cleaned_text


def count_words(cleaned_text):
    """
    Splits the cleaned text into words and counts the occurrences of each word.
    """
    words = cleaned_text.split()

    # Count the occurrences of each word
    word_count = Counter(words)

    return word_count


def main():
    # Step 1: Read the entire file
    with open('story.txt', 'r') as file:
        text = file.read()

    # Step 2: Clean the text (remove punctuation and convert to lowercase)
    cleaned_text = clean_text(text)

    # Step 3: Count the occurrences of words
    word_count = count_words(cleaned_text)

    print(word_count)

    # Step 4: Get the 100 most common words
    most_common_words = word_count.most_common(100)

    # Step 5: Print the top 100 words along with their frequency
    for word, count in most_common_words:
        print(f"{word}: {count}")


# Ensure the script runs the main function
if __name__ == "__main__":
    main()
