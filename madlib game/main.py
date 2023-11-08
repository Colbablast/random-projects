# Variable Practice
# CS 20 - Nov 2
# Colby Campbell

print("Mad-Lib Game!")

# With the seperate mad_lib_choices.txt file, it is very easy to add new mad-libs! Just use the symbol
# ~ before typing the script as well as before typing the name of the script!

# The mad-lib choices are taken from the mad_lib_choices.txt file
mad_lib_choices = []
final_line = ""
text_file = open('mad_lib_choices.txt', 'r')
text = text_file.readlines()
for line in text:
    if line[0] == "~":
        mad_lib_choices.append(final_line[:len(final_line) - 1])
        final_line = ""
        final_line += line[1:]
    else:
        final_line += line
mad_lib_choices.append(final_line)

# Printing all of the mad-lib choices for the player
for num, mad_lib in enumerate(mad_lib_choices):
    if num % 2 == 0:
        continue
    print(str((num + 1) // 2) + ": " + mad_lib)

# Asking what mad-lib the person wants to use and checking to make sure the choice is usable
while True:
    choice = input(
        "What mad-lib would you like to use? Use the numbers to choose!: ")
    try:
        if int(choice) > len(mad_lib_choices) // 2 or int(choice) < 1:
            print("That number is not an integer in the range of 1-" +
                  str(len(mad_lib_choices) // 2))
        else:
            break
    except:
        print("That isn't an integer buddy...")

# Takes the choice and sets it to one of the mad-libs
for num, mad_lib in enumerate(mad_lib_choices):
    if num % 2 == 1:
        continue
    if int(choice) - 1 == num // 2:
        mad_lib_script = mad_lib
        break

# Decodes the mad_lib_script from one string into two seperate lists for the script and the word_prompts
new_script = []
line = ""
word_prompts = []
word = ""
square_bracket = False
for letter in mad_lib_script:
    if letter == "[":
        square_bracket = True
        new_script.append(line)
        line = ""
    elif letter == "]":
        square_bracket = False
        word_prompts.append(word)
        word = ""
    else:
        if square_bracket:
            word += letter
        else:
            line += letter
new_script.append(line)

# Asks to choose a word for each of the word prompts, then puts the answers in the words list
words = []
for word in word_prompts:
    if word[0] == "!":
        new_word = input(word[1:] + ": ")
    else:
        new_word = input(word + ": ")
    if word[0] == "!":
        new_word = new_word[0].upper() + new_word[1:]
    words.append(new_word.strip())

# Puts the script back together with the new words now replacing the [Blanks]
end_script = ""
loop_num = len(new_script)
if len(words) > loop_num:
    loop_num = len(words)
for num in range(loop_num):
    if num < len(new_script):
        end_script += new_script[num]
    if num < len(words):
        end_script += words[num]

# Prints the final script!
print("*****\n" + end_script + "\n*****")
