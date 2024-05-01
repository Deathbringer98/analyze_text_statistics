def analyze_text_statistics(text):
    """
    Analyze text and return its statistics including word count, unique word count,
    average word length, and word frequency.

    :param text: str - the text to analyze
    :return: dict - dictionary with text statistics
    """
    words = text.split()
    word_count = len(words)
    unique_words = set(words)
    unique_word_count = len(unique_words)
    avg_word_length = sum(len(word) for word in words) / word_count
    word_frequency = {word: words.count(word) for word in unique_words}

    return {
        "Total words": word_count,
        "Unique words": unique_word_count,
        "Average word length": avg_word_length,
        "Word frequency": word_frequency
    }

# Example usage
example_text = "Hello world! Welcome to the world of Python programming."
stats = analyze_text_statistics(example_text)
print(stats)
