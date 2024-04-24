import re
import nltk
from nltk.corpus import stopwords as nltk_stopwords
from collections import Counter

# Confirm that NLTK stopwords have been downloaded
nltk.download('stopwords')

# Define the file location
file_location = "/app/random_paragraphs.txt"

def start():
    # Read the text file
    paragraph = read_file(file_location)
    
    # Remove the stopwords
    words_without_stopwords = remove_stopwords(paragraph)
    
    # Count the word frequency
    word_counts = count_frequency(words_without_stopwords)
    
    # Show the frequency of each word in the text on the console
    show_word_frequency(word_counts)

def read_file(file_location):
    # Read the contents of the file
    with open(file_location, "r", encoding="utf-8") as file:
        text = file.read()
    return text

def remove_stopwords(paragraph):
    # Function to remove stopwords
    # Load NLTK English stopwords
    stop_words = set(nltk_stopwords.words("english"))
    # Split text into words
    words = re.findall(r'\b\w+\b', paragraph.lower())
    # Remove stopwords
    words_filtered = [word for word in words if word not in stop_words]
    return words_filtered

def count_frequency(words):
    # Function to count word frequency
    word_frequency = Counter(words)
    return word_frequency    

def show_word_frequency(word_frequency):
    # Show the frequency distribution of words on the console
    for word, count in word_frequency.most_common():
        print(f"{word}: {count}")

start()  

