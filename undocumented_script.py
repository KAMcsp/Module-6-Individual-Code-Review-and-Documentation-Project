"""Transform sample lists of numbers and words, then print the results.

Numbers are scaled by parity (even numbers doubled, odd numbers tripled),
and words are re-cased by length (long words uppercased, short words
lowercased).
"""

# Named constants keep the transformation rules in one place, so they can
# be changed without hunting through the logic.
EVEN_MULTIPLIER = 2
ODD_MULTIPLIER = 3
LONG_WORD_MIN_LENGTH = 6  # Words of this length or more count as "long".


def process_numbers(numbers):
    """Double even numbers and triple odd numbers.

    Args:
        numbers: An iterable of integers.

    Returns:
        A new list of integers, in the same order as the input.
    """
    return [
        number * (EVEN_MULTIPLIER if number % 2 == 0 else ODD_MULTIPLIER)
        for number in numbers
    ]


def format_words_by_length(words):
    """Uppercase long words, lowercase short ones, and join them with spaces.

    Args:
        words: An iterable of strings.

    Returns:
        A single string with the re-cased words separated by single spaces.
    """
    return " ".join(
        word.upper() if len(word) >= LONG_WORD_MIN_LENGTH else word.lower()
        for word in words
    )


def main():
    """Run the transformations on sample data and print the results."""
    numbers = [1, 2, 3, 4, 5, 6, 7]
    fruits = ["apple", "banana", "kiwi", "grapefruit", "cherry"]

    print("Processed Numbers:", process_numbers(numbers))
    print("Processed Strings:", format_words_by_length(fruits))


if __name__ == "__main__":
    main()
