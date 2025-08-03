
import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {}
answer_list = []
for (index, row) in nato_data.iterrows():
    phonetic_dict[row.letter] = row.code

user_word = input("Enter the word: ").upper()

user_list = [phonetic_dict[letter] for letter in user_word]
print(user_list) 
