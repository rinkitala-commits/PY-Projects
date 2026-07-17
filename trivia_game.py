import random

python_qna = {
    "Who created Python?": "Guido",
    "How do you write a comment?": "#",
    "What is the extension of Python files?": "py",
    "Name some basic data types.": "int",
    "How do you check a variable type?": "type",
    "Difference between list and tuple?": "Mutability",
    "How do you create a dictionary?": "Braces",
    "What is None in Python?": "Null",
    "How do you write an if statement?": "Condition",
    "How do you break a loop?": "break",
    "How do you skip an iteration?": "continue",
    "How do you define a function?": "def",
    "What is a module?": "File",
    "How do you import a module?": "import",
    "What is indentation in Python?": "Spaces",
    "How do you take user input?": "input"
}

def pyhton_trivia_game():
    python_qna_list = list(python_qna.keys())
    total_questions = 5
    score = 0

    selected_questions = random.sample(python_qna_list, total_questions)

    for idx, question in enumerate(selected_questions):
        print(f"{idx + 1}.{question}")
        user_answer = input("Your answer: ").lower().strip()
        correct_answer = python_qna[question]

        if user_answer == correct_answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong. The correct answer is {correct_answer}.\n")

    print(f"Game over! Your total score is {score}/{total_questions}.")

pyhton_trivia_game()