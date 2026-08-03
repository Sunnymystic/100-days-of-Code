import pandas
from turtle import Turtle, Screen
student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
#{"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (index, row) in df.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
screen = Screen()
screen.title("Nato Phenotic Alphabet")
user_input = screen.textinput(
    title="Nato Phenotic Alphabet",
    prompt="Enter a word."
)
user_input = user_input.upper()
phonetic_code = [phonetic_dict[word] for word in user_input if word in list(phonetic_dict.keys())]
print(phonetic_code)

