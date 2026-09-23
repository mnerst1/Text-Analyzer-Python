import re


def read_file(filename):
    """
    Читает текстовый файл и возвращает его содержимое.
    """

    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()

    except FileNotFoundError:
        print(f"Ошибка: файл '{filename}' не найден.")
        return None


def get_words(text):
    """
    Превращает обычный текст в список слов.
    """

    text = text.lower()

    words = re.findall(r"\b[\w'-]+\b", text, flags=re.UNICODE)

    return words


def count_words(words):
    """
    Создаёт словарь частоты слов.
    """

    word_frequency = {}

    for word in words:

        if word in word_frequency:
            word_frequency[word] += 1

        else:
            word_frequency[word] = 1

    return word_frequency


def get_top_words(word_frequency, limit=10):
    """
    Возвращает самые часто встречающиеся слова.
    """
    sorted_words = sorted(
        word_frequency.items(),
        key=lambda item: (-item[1], item[0])
    )
    return sorted_words[:limit]


def print_statistics(text, words, word_frequency):
    """
    Выводит общую статистику текста.
    """
    lines = text.splitlines()

    total_lines = len(lines)
    total_words = len(words)
    total_characters = len(text)
    characters_without_spaces = len(
        re.sub(r"\s", "", text)
    )

    unique_words = len(word_frequency)

    print()
    print("=" * 50)
    print("              TEXT ANALYZER")
    print("=" * 50)

    print(f"Lines:                  {total_lines}")
    print(f"Words:                  {total_words}")
    print(f"Unique words:           {unique_words}")
    print(f"Characters:             {total_characters}")
    print(
        f"Characters without spaces: "
        f"{characters_without_spaces}"
    )

    if word_frequency:

        most_common_word = max(
            word_frequency.items(),
            key=lambda item: item[1]
        )

        print()
        print(
            f"Most common word: "
            f"{most_common_word[0]} "
            f"({most_common_word[1]} times)"
        )


def print_top_words(word_frequency):
    """
    Выводит TOP-10 самых популярных слов.
    """

    top_words = get_top_words(
        word_frequency,
        10
    )

    print()
    print("-" * 50)
    print("TOP 10 WORDS")
    print("-" * 50)

    for position, (word, count) in enumerate(
        top_words,
        start=1
    ):
        print(
            f"{position:>2}. "
            f"{word:<20} "
            f"{count}"
        )


def search_word(word_frequency):
    """
    Позволяет пользователю узнать,
    сколько раз встречается конкретное слово.
    """

    print()
    word = input(
        "Enter a word to search: "
    ).strip().lower()

    count = word_frequency.get(
        word,
        0
    )

    print()

    if count > 0:
        print(
            f"'{word}' appears "
            f"{count} time(s)."
        )

    else:
        print(
            f"'{word}' was not found."
        )


def main():
    """
    Главная функция программы.
    """

    filename = "text.txt"

    print("=" * 50)
    print("TEXT ANALYZER")
    print("=" * 50)

    print()
    print(f"Reading file: {filename}")
    text = read_file(filename)

    if text is None:
        return

    words = get_words(text)
    word_frequency = count_words(words)

    print_statistics(
        text,
        words,
        word_frequency
    )

    print_top_words(
        word_frequency
    )

    search_word(
        word_frequency
    )

    print()
    print("=" * 50)
    print("Analysis completed!")
    print("=" * 50)

if __name__ == "__main__":
    main()