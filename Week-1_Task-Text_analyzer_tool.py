from collections import Counter

text = """A text analyzer tool is software that processes and examines textual data to extract meaningful information.
It converts unstructured text into structured data using techniques like tokenization, normalization, and keyword extraction.
Text analyzer tools are widely used in natural language processing for tasks such as sentiment analysis and text classification.
They help organizations analyze large volumes of text efficiently for better decision-making."""

text = text.lower()
text = text.replace(".", "")
text = text.replace(",", "")

words = text.split()

stop_words = ["is", "it", "in", "are", "the", "and", "to"]

clean_words = []
for w in words:
    if w not in stop_words:
        clean_words.append(w)

total_words = len(clean_words)

freq = Counter(clean_words)
top_words = freq.most_common(5)

sentences = text.split(".")
sentence_lengths = []

for sentence in sentences:
    if sentence.strip() != "":
        sentence_lengths.append(len(sentence.split()))

print("Total Words:", total_words)
print("Top 5 Frequent Words:", top_words)
print("Sentence Lengths:", sentence_lengths)

file = open("output.txt", "w")
file.write("Total Words: " + str(total_words) + "\n")
file.write("Top 5 Words: " + str(top_words) + "\n")
file.write("Sentence Lengths: " + str(sentence_lengths))
file.close()

print("Results saved in output.txt")