import random

random.seed()

def generate_question():
    generated = False
    question_string = ""
    answer = None
    while not generated:
        a = random.randint(1,19)
        b = random.randint(1,9)
        operator = random.randint(2,2)
        if operator == 1:
            answer = a + b
            question_string = "{0:2d} + {1:2d} = ".format(a, b)
        elif operator == 2:
            answer = a - b
            question_string = "{0:2d} - {1:2d} = ".format(a, b)
        else:
            raise Exception("Unknown error when generating questions!")
        if (answer >= 0) and (answer < 10):
            generated = True
    return (question_string, answer)

if __name__ == "__main__":
    f = open("questions.txt", "w")
    for i in range(1,59):
        (q, answer) = generate_question()
        f.write("{0:2d}: {1} {2:2d}\n".format(i, q, answer))
    f.close()
