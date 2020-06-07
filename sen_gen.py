import numpy as np
import random
import re
from collections import defaultdict
from os import listdir

target_path = 'books/'

def choose_file(source_path = target_path):
    my_files = listdir(source_path)
    return random.choice(my_files)


# Read text from file and tokenize.

def read_book(book):
    print(book)
    with open(f'{target_path}{book}') as f:
        text = f.read()
    tokenized_text = [
        word
        for word in re.split('\W+', text)
        if word != ''
    ]
    return tokenized_text

# Create graph.
def create_graph(text):
    markov_graph = defaultdict(lambda: defaultdict(int))

    last_word = text[0].lower()
    for word in text[1:]:
        word = word.lower()
        markov_graph[last_word][word] += 1
        last_word = word
    return markov_graph

# Preview graph.
def preview_graph(graph, words : list, limit_: int = 3):
    for first_word in words:
        next_words = list(graph[first_word].keys())[:limit_]
        for next_word in next_words:
            print(first_word, next_word)


def walk_graph(graph, distance=5, start_node=None):
    """Returns a list of words from a randomly weighted walk."""
    if distance <= 0:
        return []

    # If not given, pick a start node at random.
    if not start_node:
        start_node = random.choice(list(graph.keys()))

    weights = np.array(
        list(graph[start_node].values()),
        dtype=np.float64)

    # Normalize word counts to sum to 1.
    weights /= weights.sum()

    # Pick a destination using weighted distribution.
    choices = list(graph[start_node].keys())
    chosen_word = np.random.choice(choices, None, p=weights)

    return [chosen_word] + walk_graph(
        graph, distance=distance - 1,
        start_node=chosen_word)

def build_sentense():
    markov_graph = create_graph(read_book(choose_file(target_path)))
    preview_graph(markov_graph, ("który",), 3 )
    sentence = ' '.join(walk_graph(markov_graph, distance=30)).capitalize() + '.'
    return sentence

print(build_sentense())