import random
import os

class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    END = '\033[0m'

quiz_questions = [
    {
        "question": "Which type of Programming does Python support??",
        "choices": ["A) object-oriented programming" , "B)structured programming" , " C)functional programming" , "D)all of the mentioned"],
        "correct_answer": "D"
    },
    {
        "question": "Which of the following is the correct extension of the Python file??",
        "choices": ["A).python ", "B).pl", "C).py ", "D).p "],
        "correct_answer": "C"
    },
    {
        "question": " Which keyword is used for function in Python language??",
        "choices": ["A)Function ", "B)def", "C)Fun ", "D.Define) "],
        "correct_answer": "B"
    }
]

score = 0

def ask_question(question_data):
    global score

    os.system('clear') 
    
    print(Colors.BLUE + "Quiz Game" + Colors.END)
    print("\n" + question_data["question"])
    for choice in question_data["choices"]:
        print(choice)
    user_answer = input(Colors.YELLOW + "Enter the letter of your answer: " + Colors.END).upper()

    if user_answer == question_data["correct_answer"]:
        score += 1
        print(Colors.GREEN + "Correct!" + Colors.END)
    else:
        print(Colors.RED + f"Incorrect. The correct answer is {question_data['correct_answer']}." + Colors.END)

def display_results():
    os.system('clear')  

    print(Colors.BLUE + "Quiz Game - Final Results" + Colors.END)
    print(f"You scored {Colors.GREEN}{score}{Colors.END} out of {len(quiz_questions)} questions.")
    if score == len(quiz_questions):
        print(Colors.GREEN + "Congratulations! You got all the questions correct!" + Colors.END)
    elif score >= len(quiz_questions) // 2:
        print(Colors.YELLOW + "Good job! You did well." + Colors.END)
    else:
        print(Colors.RED + "Keep practicing. You can do better!" + Colors.END)


for question_data in quiz_questions:
    ask_question(question_data)

display_results()
