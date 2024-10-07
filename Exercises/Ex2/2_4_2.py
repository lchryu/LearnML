import re
from collections import Counter


def clean_text(text):
    # Remove punctuation using regex and convert to lowercase
    cleaned_text = re.sub(r'[^\w\s]', '', text).lower()
    return cleaned_text.split()


def main():
    # Step 1: Read the entire file
    with open('story.txt', 'r') as file:
        text = file.read()

    # Step 2: Clean and process the text
    words = clean_text(text)

    # Step 3: Count the occurrences of words using Counter
    word_count = Counter(words)

    # Step 4: Sort and print the top 100 most common words
    for word, count in word_count.most_common(100):
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
