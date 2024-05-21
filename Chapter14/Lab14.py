import string

class EmptyStringError(Exception):
    """Exception raised for empty input strings."""
    pass

#This function processes each line, 
# converting it to lowercase and removing punctuation. If the line is empty, it raises the EmptyStringError



def clean_line(line):
    """Changes case and removes punctuation from the input line."""
    # Raise exception if line is empty
    if not line.strip():
        raise EmptyStringError("The input line is empty")
    
    # Make all characters lowercase
    cleaned_line = line.lower()
    
    # Remove punctuation
    punct = str.maketrans('', '', string.punctuation)
    cleaned_line = cleaned_line.translate(punct)
    
    return cleaned_line


def count_words(words):
    """Takes a list of cleaned words and returns a count dictionary."""
    word_count = {}
    
    for word in words:
        try:
            count = word_count.setdefault(word, 0)
        except TypeError:
            # Skip the word if it's not hashable
            continue
        word_count[word] += 1
    
    return word_count


def word_stats(word_count):
    """Takes a word count dictionary and returns the top and bottom five entries."""
    word_list = list(word_count.items())
    word_list.sort(key=lambda x: x[1])
    
    try:
        least_common = word_list[:5]
        most_common = word_list[-1:-6:-1]
    except IndexError as e:
        # If the list is empty or too short, just return the list
        least_common = word_list
        most_common = list(reversed(word_list))
    
    return most_common, least_common



def process_text(text):
    """Processes the input text to count word frequencies and return statistics."""
    lines = text.split('\n')
    all_words = []
    
    for line in lines:
        try:
            cleaned_line = clean_line(line)
            words = cleaned_line.split()
            all_words.extend(words)
        except EmptyStringError as e:
            print(f"Warning: {e}")
    
    word_count = count_words(all_words)
    most_common, least_common = word_stats(word_count)
    
    return most_common, least_common

# Example text input
text = """
This is a test. This test is only a test.
In case of an actual emergency, the test you are taking would be followed by more testing.
"""

# Process the text
most_common, least_common = process_text(text)

# Output the results
print("Most Common Words:", most_common)
print("Least Common Words:", least_common)
