import random

random.seed()


def generate_question():
    generated = False
    question_string = ""
    result = 0
    while not generated:
        a = random.randint(1, 10000)
        b = random.randint(1, 10000)
        operator = random.randint(1, 2)
        if operator == 1:
            result = a + b
            question_string = "{0:4d} + {1:4d}\t={2:5d}".format(a, b, a + b)
        elif operator == 2:
            result = a - b
            question_string = "{0:4d} - {1:4d}\t={2:5d}".format(a, b, a - b)
        else:
            raise Exception("Unknown error when generating questions!")
        if (result >= 0) and (result <= 10000):
            generated = True
        else:
            continue
    return question_string


f = open("questions_3d_add.txt", "w")
for i in range(1, 24):
    q = generate_question()
    f.write("{1}\n".format(i, q))
f.close()
