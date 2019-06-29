import random

random.seed()

def generate_question():
    generated = False
    question_string = ""
    result = 0
    while not generated:
        a = random.randint(1,19)
        b = random.randint(1,9)
        operator = random.randint(2,2)
        if operator == 1:
            result = a + b
            question_string = "{0:2d} + {1:2d} = {2:2d}".format(a, b, a+b)
        elif operator == 2:
            result = a - b
            question_string = "{0:2d} - {1:2d} = {2:2d}".format(a, b, a-b)
        else:
            raise Exception("Unknown error when generating questions!")
        if (result >= 0) and (result < 10):
            generated = True
    return question_string

if __name__ == "__main__":
    f = open("questions.txt", "w")
    for i in range(1,59):
        q = generate_question()
        f.write("{0:2d}: {1}\n".format(i, q))
    f.close()
