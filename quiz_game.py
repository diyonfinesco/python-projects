import random
from termcolor import cprint


def ask_question(index, question, options):
    print(f'{index}: {question}\n')
    print(options)

    return input("\nAnswer: ").upper().strip()

def run_quiz(questions):

    random.shuffle(questions)
    score = 0

    for index, item in enumerate(questions, 1):

        user_answer = ask_question(index, item["question"], item["options"])

        if user_answer == item["answer"]:
            cprint('\nCorrect\n', 'green')
            score += 1
        else:
            cprint(f'\nWrong! correct answer is {item["answer"]}\n', 'red')


    print(f'Quiz over!. Your score is {score} out of {len(questions)}')

def main():
    questions = [
        {
            'question': 'What is the capital of France?',
            'options': 'A. Berlin\nB. Madrid\nC. Paris\nD.Rome',
            'answer': 'C'
        },
        {
            'question': 'Which planet is the known as the red planet?',
            'options': 'A. Earth\nB. Mars\nC. Jupiter\nD. Saturn',
            'answer': 'B'
        },
        {
            'question': 'What is the largest ocean on Earth?',
            'options': 'A. Atlantic\nB. Indian\nC. Arctic\nD. Pacific',
            'answer': 'D'
        },
    ]

    run_quiz(questions)

if __name__ == '__main__':
    main()