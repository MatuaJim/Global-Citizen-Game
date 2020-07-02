import time


easy = ["What is the ingredient that causes bread to rise?","__1__",
        "\nWhat is the highest mountain in the world? Mount","__2__",
        "\nWhat planet bears the name of the Roman god of war?","__3__",
        "\nWhich world ocean has a name that means peace?", "The", "__4__","Ocean\n"]
easy_answers = ["Yeast","Everest","Mars","Pacific"]
medium = ["Which planet has the most moons?", "__1__",
          "\nA Corona is another word for the atmosphere of what celestial body? ","The","__2__",
          "\nWhat common household product is otherwise known as Sodium Chloride? ","__3__",
          "\n186,282 miles per second is the speed of what in a vacuum?","__4__","\n"]
medium_answers = ["Jupiter","Sun","Salt","Light"]
hard = ["Which galaxy is the closest to the Milky Way?", "The", "__1__", "Galaxy",
        "\nWhat is the unit of power that is roughly equal to 746 watts?","__2__",
        "\nWhat planet do the moons Titan, Enceladus, Mimas, and Iapetus orbit?", "__3__",
        "\nWhat was the name of the first U.S. space station?","__4__","\n"]
hard_answers = ["Andromeda","Horsepower","Saturn","Skylab"]

print("\    /\    /  __  |  __  _   _ _   __  ")
print(" \  /  \  /  /__\ | /   / \ | | | /__\ ")
print("  \/    \/   \__  | \__ \_/ |   | \__  ")
print("       _____    _____                  ")
print("         |  _     |  |    __           ")
print("         | / \    |  |_  /__\          ")
print("         | \_/    |  | | \__           ")
print("       ___                             ")
print("      |   \    __ __ |   __  __        ")
print("      |__ /| | \   / |  /__\ | |       ")
print("      |    \_/ _\ /_ |  \__  |         ")
print("                                       ")
print("      Please select a difficulty       ")
print("        Easy, Medium, or Hard          ")
print("                                       ")
players_choice = input("    Please type in your selection: ")

def dif_selection(players_choice):
    """ Takes the players difficulty selection and then loads the proper conditions for the gameself.
    input;
    players_choice: STR input from user selecting a difficulty level
    output:
    questions: the questions corresponding to the players difficulty choice.
    answers: the answers to the questions.
    """
    if players_choice.lower() == "easy":
        questions,answers = easy,easy_answers
        print("       Easy mode selected")
        time.sleep(1.1)
        return (questions,answers)
    elif players_choice.lower() == "medium":
        questions,answers = medium,medium_answers
        print("     Medium mode selected")
        time.sleep(.05)
        return (questions,answers)
    elif players_choice.lower() == "hard":
        questions,answers = hard,hard_answers
        print("     Hard mode selected")
        time.sleep(.05)
        return (questions,answers)
    else:
        print(" \n     Selection not recognized, easy difficulty selected by default\n\n\n")
        questions,answers = easy,easy_answers
        return (questions,answers)
questions,answers = dif_selection(players_choice)
spaces_5 = """
./\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\.
.                                                              .
.                                                              .
.______________________________________________________________.
"""
print(spaces_5)

def attempt_check(ques_num,questions,answers):
    """
    Prompts the user to fill in the first blank. Displays the updated
    fill-in-the-blank when the user inputs the correct answer and prompts them
    to fill in the next blank. Prompts the user to try again when their guess
    is incorrect.
    input:
    ques_num: INT The current blank number.
    questions: STR The questions to be answered
    answers: list of STR The answers for the questions.
    output:
    ques_num: the current question number
    """
    space = " "
    print(space.join(questions))
    blank = "__" + str(ques_num) + "__"
    guess = str(input("What word should replace? " + "__" + str(ques_num) + "__"))
    answer = answers[ques_num-1]
    if guess.lower() == answer.lower():
        questions[questions.index(blank)] = answer
        print("\n\nCORRECT!\n\n")
        ques_num += 1
        return ques_num
    else:
        print("Incorrect. Please try again.\n")
        return attempt_check(ques_num, questions, answers)

def play_game(questions,answers,spaces_5):
    """
    This takes in the parameters of the game and runs the game under the set conditions.
    input:
    questions: the questions that pertain to the difficulty level selected
    answers: a list of answers to the given questions
    spaces_5: a variable containing a string meant for visual formating of appearance
    """
    space = " "
    ques_num = 1
    print("     Welcome to puzzler, a science themed trivia game!\n\n\n")
    for answer in answers:
        ques_num = attempt_check(ques_num, questions, answers)
        print(spaces_5)
        time.sleep(1.5)
    print(space.join(questions))
    print("Congratulations you have WON!!!!!!!!!!!!!!!!!!!!")
    
play_game(questions,answers,spaces_5,)
