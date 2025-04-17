def dotA2(value):
    new_score = int(input("enter new score "))
    register = str
    match value:
        case 1:
            new_score = int(input("enter new score "))
            register = str
        case 2:
            if 19 <= new_score <= 20:
                register = "the score is A"
        case 3:
            if 16 <= new_score <= 18:
                register = "the score is B"
        case 4:
            if 13 <= new_score <= 15:
                register = "the score is C"
        case 5:
            if 10 <= new_score <= 12:
                register = "the score is D"
        case 6:
            if 1 <= new_score <= 9:
                register = "the score is B"
    print(register)
dotA2(2)

