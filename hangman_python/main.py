# Hangman
# Nov 17, 2021
# Colby Campbell

from random import randint

# All the possible words that could be used!
words = [
    "abruptly",
    "absurd",
    "abyss",
    "affix",
    "askew",
    "avenue",
    "awkward",
    "axiom",
    "azure",
    "bagpipes",
    "bandwagon",
    "banjo",
    "bayou",
    "beekeeper",
    "bikini",
    "blitz",
    "blizzard",
    "boggle",
    "bookworm",
    "boxcar",
    "boxful",
    "buckaroo",
    "buffalo",
    "buffoon",
    "buxom",
    "buzzard",
    "buzzing",
    "buzzwords",
    "caliph",
    "cobweb",
    "cockiness",
    "croquet",
    "crypt",
    "curacao",
    "cycle",
    "daiquiri",
    "dirndl",
    "disavow",
    "dizzying",
    "duplex",
    "dwarf",
    "embezzle",
    "equip",
    "espionage",
    "ebola",
    "exodus",
    "faking",
    "fishhook",
    "fixable",
    "fjord",
    "flapjack",
    "flopping",
    "fluffiness",
    "flyby",
    "foxglove",
    "frazzled",
    "frizzled",
    "fuchsia",
    "funny",
    "gabby",
    "galaxy",
    "galvanize",
    "gazebo",
    "gizmo",
    "glowworm",
    "glyph",
    "gnarly",
    "gnostic",
    "gossip",
    "grogginess",
    "haphazard",
    "hyphen",
    "iatrogenic",
    "icebox",
    "injury",
    "ivory",
    "ivy",
    "jackpot",
    "jaundice",
    "jawbreaker",
    "jaywalk",
    "jazziest",
    "jazzy",
    "jelly",
    "jigsaw",
    "jinx",
    "jujitsu",
    "jockey",
    "jogging",
    "joking",
    "jovial",
    "joyful",
    "juicy",
    "jukebox",
    "jumbo",
    "kayak",
    "kazoo",
    "keyhole",
    "khaki",
    "kilobyte",
    "kiosk",
    "kitsch",
    "kiwifruit",
    "klutz",
    "knapsack",
    "larynx",
    "lengths",
    "lucky",
    "luxury",
    "lymph",
    "marquis",
    "matrix",
    "megahertz",
    "microwave",
    "mnemonic",
    "mystify",
    "nowadays",
    "ovary",
    "oxidize",
    "oxygen",
    "pajama",
    "peekaboo",
    "phlegm",
    "pixel",
    "pizazz",
    "pneumonia",
    "polka",
    "pshaw",
    "psyche",
    "puppy",
    "puzzling",
    "quartz",
    "queue",
    "quips",
    "quixotic",
    "quiz",
    "quizzes",
    "quorum",
    "razzmatazz",
    "rhubarb",
    "rhythm",
    "rickshaw",
    "schnapps",
    "scratch",
    "shiv",
    "snazzy",
    "sphinx",
    "spritz",
    "squawk",
    "staff",
    "strength",
    "strengths",
    "stretch",
    "stronghold",
    "stymied",
    "subway",
    "swivel",
    "syndrome",
    "thriftless",
    "thumbscrew",
    "topaz",
    "transcript",
    "transgress",
    "transplant",
    "triathlon",
    "twelfth",
    "twelfths",
    "unknown",
    "unworthy",
    "unzip",
    "uptown",
    "vaporize",
    "vixen",
    "vodka",
    "voodoo",
    "vortex",
    "voyeurism",
    "walkway",
    "waltz",
    "wave",
    "wavy",
    "waxy",
    "wellspring",
    "wheezy",
    "whiskey",
    "whizzing",
    "whomever",
    "wimpy",
    "witchcraft",
    "wizard",
    "woozy",
    "wristwatch",
    "wyvern",
    "xylophone",
    "yachtsman",
    "yippee",
    "yoked",
    "youthful",
    "yummy",
    "zephyr",
    "zigzag",
    "zigzagging",
    "zilch",
    "zipper",
    "zodiac",
    "zombie"
]

# Chooses the secret word
secret_word = words[randint(0, len(words))]

# Makes the variables that will be used for the program
guess = ""
wrong_letters = ""
correct_letters = ""
guess_count = 0

# Gets how many guesses the player wants
guess_limit = input("How many guesses do you want? Press \"Enter\" to go to the default (6): ")
if str.isdigit(guess_limit):
    guess_limit = int(guess_limit)
else:
    guess_limit = 6
out_of_guesses = False

# If the player hasn't guess the secret word or the player still has guesses, loop
while guess != secret_word and not out_of_guesses:
  if guess_count < guess_limit:
    print("**********")
    print("You have " + str(guess_limit - guess_count) + " guesses left.")
    print("Incorrect letters: " + wrong_letters)
    word_line = str(len(secret_word)) + ": "
    for letter in secret_word:
      if letter in correct_letters:
        word_line += letter + " "
      else:
        word_line += "_ "
    print(word_line)
    guess = input("Guess a letter, or the word: ").lower()
    # If the guess is one letter
    if len(guess) == 1:
      # If the guess is correct
      if guess in secret_word:
        print("Correct! There is an " + guess + "!")
        correct_letters += guess
      else:
        # If the guess has already been guessed before
        if guess in wrong_letters:
          print("You have already tried an " + guess + "! Try a different letter!")
        # If the guess is guess!
        else:
          print("There is no " + guess + "! Try again!")
          wrong_letters += guess + ", "
          guess_count = guess_count + 1
    # If the guess is not one letter
    else:
      # If guess is blank
      if guess == "":
        print("This is just a blank, did you make a mistake?")
      # If guess is the secret word
      elif guess == secret_word:
        print("Correct!")
      # If the guess is incorrect
      else:
        print("That isn't the word!")
        guess_count = guess_count + 1
  # If the person is out of guesses
  else:
    out_of_guesses = True

# If the player is out of guesses, they lose, but if they aren't they win!
if out_of_guesses:
  print("You lose! Your word was " + secret_word + "!")
else:
  print("Congratulations! You win!")