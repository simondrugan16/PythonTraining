from question_list import QuestionList

def start_quiz():
    my_question_list = QuestionList()
    questions_answered = 0
    correct_answers = 0
    for question in my_question_list.questions:
        user_answer = str(input(f"True of False, {question.question} "))
        if user_answer == str(question.answer):
            correct_answers += 1
        questions_answered += 1
        print(f"Current score: {correct_answers}/{questions_answered}")
    
    print(f"Quiz over! You scored: {correct_answers}/{questions_answered}")
    

start_quiz()