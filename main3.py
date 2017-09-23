import random

random.seed()

def generate_question():
    generated = False
    question_string = ""
    while not generated:
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        result = a * b
        question_string = "{0:1d} * {1:1d} =".format(a, b)
        generated = True
    return question_string

f = open("questions3.txt", "w")
for i in range(1,59):
    q = generate_question()
    f.write("{1}\n".format(i, q))
f.close()
