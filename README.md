# Text Analysis Tool

This Python module provides a simple yet effective text analysis tool that computes basic statistics about a given text. It can be used to determine the total number of words, the number of unique words, the average word length, and the frequency of each word in the text.

## Features

- **Word Count**: Total number of words in the text.
- **Unique Words**: Total number of unique words.
- **Average Word Length**: Average length of the words.
- **Word Frequency**: Frequency of each word in the text.

## Getting Started

### Prerequisites

Ensure you have Python installed on your machine. You can download Python from [here](https://www.python.org/downloads/).

### Installation

Clone this repository to your local machine using:

```bash
git clone https://github.com/Deathbringer98/analyze_text_statistics.git


```
### Usage 
To use the tool, simply import the function from the module and pass the text you want to analyze:
from text_analysis import analyze_text_statistics

# Example text
text = "Hello world! Welcome to the world of Python programming."

# Get statistics
stats = analyze_text_statistics(text)
print(stats)

