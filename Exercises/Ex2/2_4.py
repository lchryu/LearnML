import string
from collections import Counter


def clean_text(text):
    translator = str.maketrans('', '', string.punctuation)
    cleaned_text = text.translate(translator)

    cleaned_text = cleaned_text.lower()

    return cleaned_text


def count_words(cleaned_text):
    words = cleaned_text.split()

    word_count = Counter(words)

    return word_count


def main():
    with open('story.txt', 'r') as file:
        text = file.read()

    cleaned_text = clean_text(text)

    word_count = count_words(cleaned_text)

    print(word_count)

    most_common_words = word_count.most_common(100)

    for word, count in most_common_words:
        print(f"{word}: {count}")


if __name__ == "__main__":
    main()
