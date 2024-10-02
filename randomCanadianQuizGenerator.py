#! Python 3.12.5
# randomQuizGenerator.py - Creates quizzes with questions and answers in
# random order, along with the answer key.

import random

# The Quiz data. Keys are states and values are their capitals

capitals = {'Alberta': 'Edmonton', 'British Columbia': 'Victoria', 'Manitoba': 'Winnipeg',
'New Brunswick': 'Fredericton', 'New Foundland and Labrador': 'Saint John\'s', 'Nova Scotia': 'Halifax',
'Ontario': 'Toronto', 'Prince Edward Island': 'Charlottetown', 'Quebec': 'Quebec City',
'Saskatchewan': 'Regina', 'Yukon': 'Whitehorse', 'Nunavut': 'Iqaluit', 'Northwest Territories': 'Yellowknife'}
            

            # Generate 35 quiz files.
for quizNum in range(35):
    # TODO: Create the quiz and answer key files.
    # Create the quix and answer key files.
    quizFile = open(f'capitalsquiz_ca{quizNum + 1}.txt', 'w')
    answerKeyFile = open(f'capitalsquiz_answers_ca{quizNum + 1}.txt', 'w')

    # Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write((' ' * 20) + f'State Capitals Quiz (Form{quizNum + 1})')
    quizFile.write('\n\n')

    # Shuffle the order of the states.
    states = list(capitals.keys())    # get all the states in a list
    random.shuffle(states)    # randomize the order of the states       

    # TODO: Loop through all 50 states, makin the question for each.
    # Loop through all 50 states, making a question for each.
    for questionNum in range(13):

        # Get right or wrong answers.
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())    # get a complete list of answers
        del wrongAnswers[wrongAnswers.index(correctAnswer)]    # remove the right answers
        wrongAnswers = random.sample(wrongAnswers, 3)    # pick 3 random ones

        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)    # randomize the order of the answers.

        # Write the question and the answer options to the quiz file.
        quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')
        for i in range(4):
            quizFile.write(f"    {'ABCD'[i]}.  { answerOptions[i]}\n")
        quizFile.write('\n')

        # Write the answer key to a file.
        answerKeyFile.write(f"{questionNum + 1}. {'ABCD'[answerOptions.index(correctAnswer)]}\n")
    quizFile.close()
    answerKeyFile.close()
                           

            
