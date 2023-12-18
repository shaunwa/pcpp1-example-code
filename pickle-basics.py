import pickle

try:
    with open('pickle-basics-storage.pkl', 'rb') as file:
        words = pickle.load(file)
except FileNotFoundError:
    words = []

print('Here are the words that you entered previously: ')
for word in words:
    print(word)

new_word = input('Please enter a new word: ')
words.append(new_word)

with open('pickle-basics-storage.pkl', 'wb') as file:
    pickle.dump(words, file)