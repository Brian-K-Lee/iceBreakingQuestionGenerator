####################################################
##Ice Breaking Activity For a New Team Or a Member##
#################Author: Brian Lee##################
#############Last Updated On 3/5/2023###############
####################################################

# This program pulls a random question from the ice breaking question list I put together
# There are 20 questions and you can pick a number from 1 to 20 to generate a question
# If you are shy, a program will pick a number; therefore, a random question for you.
# It is a replacement of my ice breaking activity for a new team or a member
# That is available on Quizlet.com as only five picks are now allowed with the free account.
# https://quizlet.com/601356634/data-quality-team-flash-cards/?x=1jqt
# It uses pandas and numpy libraries.

### Load Libraries
import pandas as pd
import numpy as np

### Import 20 Ice Breaking Questions
questions = pd.read_csv('C:/Users/KT/Documents/Python/ForFun/IceBreaking/iceBreakingQuestions.csv')

### Generate 3 Questions (can change using range()) From Someone's Drawing
for i in range(3):
    randomNumber = input("Choose a Number Between 0-20: ")
    randomNumber = int(randomNumber)
    print("You picked:\n", questions.iloc[randomNumber,0],"\n")

### Generate a Random Question From The Question List
print("You picked:\n", questions.iloc[np.random.choice(questions.index), 0], "\n")

print('Hope it was fun! I believe in the quote, "Teamwork makes the dream work!"')