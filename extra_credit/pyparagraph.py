
import os




file_to_open = os.path.join("raw_data", "paragraph_1.txt")
num_words=0
num_sentences=0

with open(file_to_open, "r") as this_file:
    this_text=this_file.read()

print(this_text)

this_text2=this_text




print(this_text2)
words=this_text2.split()
total_char=0
for word in words:
    num_words+=1
    total_char=total_char+len(word)

average_word_length=total_char/num_words

for char in "!?.":
    num_sentences=this_text2.count(char)

for char in "!.->\n":
    this_text2=this_text2.replace(char, " ") 

print(words)

average_sentence_length=num_words/num_sentences


print("Number of words: " + str(num_words))  
print("Average word length: %2.1f"%(average_word_length))
print("Number of sentences: " + str(num_sentences))
print("Average sentence length in words: " + str(average_sentence_length))


