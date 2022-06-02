import pandas as pd

# read data using pandas
raw_data = pd.read_csv("nato_phonetic_alphabet.csv")
df = pd.DataFrame(raw_data)

# convert data to dataframe
nato_dict = {row["letter"]: row["code"] for (index, row) in df.iterrows()}

def generate_output():
    # ask for user input and print the NATO translation
    user_input = input("Enter a word to be translated: ").upper()
    try:
        nato_letter_list = [nato_dict[letter] for letter in user_input]
        print(nato_letter_list)
    except KeyError:
        print("Sorry! Only alphabetical characters allowed!")
        generate_output()

generate_output()




