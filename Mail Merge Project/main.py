#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    

with open("./Input/Names/invited_names.txt", 'r') as invited_name:
    names = invited_name.readlines()

with open("./Input/Letters/starting_letter.txt", 'r') as letter:
    letter_template = letter.read()

for name in names:  
    actual_name = name.strip('\n')        
    final_letter = letter_template.replace("[name]", actual_name)
    
    
    with open(f"./Output/ReadyToSend/letter_for_{actual_name}.txt", 'w') as individual_letter:
        separate_letter = individual_letter.write(final_letter)
        


    


