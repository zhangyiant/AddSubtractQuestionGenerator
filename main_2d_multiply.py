import random

random.seed()


def generate_question():
    generated = False
    question_string = ""
    result = 0
    while not generated:
        a = random.randint(1, 99)
        b = random.randint(1, 9)
        result = a * b
        question_string = "{0:2d} * {1:2}\t={2:3d}".format(a, b, a * b)
        generated = True
    return question_string


f = open("questions_2d_multiply.txt", "w")
for i in range(1, 10):
    q = generate_question()
    f.write("{1}\n".format(i, q))
f.close()
