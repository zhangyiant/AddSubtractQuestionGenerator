import random

random.seed()


def generate_question():
    generated = False
    question_string = ""
    result = 0
    while not generated:
        a = random.randint(1, 1000)
        b = random.randint(1, 1000)
        c = random.randint(1, 1000)
        operator = random.randint(1, 2)
        if operator == 1:
            result = a + b
            question_string = "{0:3d} + {1:3d}".format(a, b)
        elif operator == 2:
            result = a - b
            question_string = "{0:3d} - {1:3d}".format(a, b)
        else:
            raise Exception("Unknown error when generating questions!")
        if (result >= 0) and (result <= 1000):
            pass
        else:
            continue
        operator = random.randint(1, 2)
        if operator == 1:
            result = result + c
            question_string += " + {0:3d} =".format(c)
        elif operator == 2:
            result = result - c
            question_string += " - {0:3d} =".format(c)
        else:
            raise Exception("Unknown error when generating questions!")
        if (result >= 0) and (result <= 1000):
            generated = True
        else:
            continue
    return question_string


f = open("questions2.txt", "w")
for i in range(1, 59):
    q = generate_question()
    f.write("{1}\n".format(i, q))
f.close()
