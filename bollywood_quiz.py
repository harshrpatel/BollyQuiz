import time
from questions import QUESTION_LIST
from termcolor import colored


# def generate_problem(problem_no, ques, answer):
#     print(problem_no, ques, answer)
#     response = input(str(ques))
#     if response == answer:
#         print("Right Answer")
#         return True
#     elif len(response) < 1:
#         print("Enter the right answer PLEASE")
#         generate_problem(problem_no, ques, answer)
#     else:
#         print("Wrong Answer!!")
#         return False

# def quiz():
#     total_problems = len(QUESTION_LIST)
#     print(total_problems)
#     for i in range(total_problems):
#         ques_no = i+1
#         result = generate_problem(ques_no, QUESTION_LIST[i][0], QUESTION_LIST[i][1])
#         if result:
#             score += 20
#         else:
#             score -= 10
#             generate_problem(ques_no, QUESTION_LIST[i][0], QUESTION_LIST[i][1])


class Main:
    problem = 1
    first_time_flag = True
    score = 100
    start_time = time.time()

    def get_input_and_verify(ques, answer, score):
        right_answer_not_given = True
        while right_answer_not_given:
            response = input(ques)
            if response.lower() == answer:
                print(colored("Right Answer", 'green'))
                score += 20
                print("Score: ", score)
                right_answer_not_given = False
            elif len(response) < 1:
                print(colored("Please enter the Right Answer!", "magenta"))
            else:
                print(colored("Wrong Answer", "red"))
                score -= 10
                print("Score: ", score)
        return score

    while problem < len(QUESTION_LIST)+1:
        print("This is Problem number: ", problem)
        score = get_input_and_verify(QUESTION_LIST[problem-1][0], QUESTION_LIST[problem - 1][1], score)
        problem += 1

    print("you finished the tasks")
    time_taken = (time.time() - start_time) / 60
    print("score: ", score)
    print("adjusted Score: ", score / time_taken)


if __name__ == '__main__':
    Main()

# if __name__ == '__main__':
#     # main()
#     quiz()
