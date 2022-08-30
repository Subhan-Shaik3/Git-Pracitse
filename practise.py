#This program tells about the word of frequency
#how are you
words = "what is this how are you"
frequency_of_words = {}
for word in words.split():
    if word not in frequency_of_words:
        frequency_of_words[word] = 1
    else:
        frequency_of_words[word] += 1
print(frequency_of_words)