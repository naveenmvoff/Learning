
def user_input(word,letter):
	return word.count(letter)


input_word, input_letter = input("Enter the word and , then eneter the letter: ").split(",")

result = user_input(input_word, input_letter)
print(result)