def main7():
    new_score = int(input("enter new score "))
    register = str
    if 19 <= new_score <= 20:
        register = "the score is A"
    elif 16 <= new_score <= 18:
        register = "the score is B"
    elif 13 <= new_score <= 15:
        register = "the score is C"
    elif 10 <= new_score <= 12:
        register = "the score is D"
    elif 1 <= new_score <= 9:
        register = "the score is B"
    print(register)
    main7()
main7()