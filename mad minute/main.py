from random import randint
from time import sleep
from threading import Thread

# Generate the questions
questions = []
for num in range(2, 10):
  for num2 in range(2, 10):
    questions.append(str(num) + " x " + str(num2))

# Generate the answers for the questions
answers = []
for question in questions:
  words = question.split()
  answers.append(int(words[0]) * int(words[2]))

ans = None
score = [0, 0]

# Create functions for the extra threads
def timer():
  sleep(60)

def math(txt):
  global ans
  ans = input(txt + " = ")

# Create the timer thread and start it
t1 = Thread(target=timer)
t1.start()
# Main game while loop
while True:
  # Grab a random question and the answer to the question
  index = randint(0, (len(questions) - 1))
  question = questions[index]
  answer = answers[index]
  # Create the input thread and start it
  t2 = Thread(target=math, args=(question,))
  t2.start()
  # Loop until either the timer thread has finished or the input thread has finished
  while True:
    # If the timer thread has ended, print the score and exit the game
    if not t1.is_alive():
      print(f"\nGood game! You got {score[0]} correct and {score[1]} wrong!")
      exit()
    # If the input thread has ended, check if the player has gotten the answer correct
    if not t2.is_alive():
      # Try to convert the player's answer into a integer, if an error occurs, run the except code.
      try:
        if int(ans) == answer:
          print("Correct!")
          # Add +1 to the correct answer score count
          score[0] += 1
        else:
          print("Wrong! The answer was:", answer)
          # Add +1 to the incorrect answer score count
          score[1] += 1
      except:
        print("That isn't a number! The answer was:", answer)
        # Add +1 to the incorrect answer score count
        score[1] += 1
      break