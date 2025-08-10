
import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for index, row in nato_data.iterrows()}


condition = True
while condition:
    user_word = input("Enter the word: ").upper()
    
    try:    
        user_list = [phonetic_dict[letter] for letter in user_word]
    except KeyError:
        print("Sorry! Alphabets only...")
    else:
        condition = False
        
print(user_list) 
