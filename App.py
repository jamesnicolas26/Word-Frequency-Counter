from collections import Counter

def word_count(text):
    words = text.split()
    return Counter(words)

text = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Pellentesque eu erat lacus, vehicula eu tincidunt ac, pulvinar et urna. 
Curabitur vehicula justo eget diam posuere sollicitudin eu tincidunt nulla. 
Curabitur eleifend, arcu a dictum varius, risus neque venenatis arcu, a semper massa urna sit amet eros. 
"""

word_frequencies = word_count(text.lower())
for word, count in word_frequencies.most_common():
    print(f"{word}: {count}")
