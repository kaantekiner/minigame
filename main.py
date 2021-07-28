# -*- coding: utf-8 -*-
import random
import time

"""
ACM 373 - Scripting Languages Midterm Project

## author: { Kaan Tekiner - 20141314063 - MIS }
## about author: { Jr.Cyber Security Analyst/seniority:2year, Jr.Application Developer/4year }
## contact: { kaan.tekiner@std.yeditepe.edu.tr }
## website: { http://kaantekiner.com }


---------------------------------------------------------------
Explanation:                                                  |
                                                              |
TheApp! project is a simple game developed in                 |
Python3 language, the main purpose of the                     |
game is being fun. Its generally for kids, especially         |
to make them love the code-based games, also motivating       |
them to write projects like this. It offers 3 different       |
funny game options and cute conversations...                  |
                                                              |
In this project consisting of a single script;                |
there are dictionary structures, functions,                   |
data type conversions, interactive menu,                      |
conversations, if conditions, string                          |
mixing and similar technical features.                        |
---------------------------------------------------------------


---------------------------------------------------------------
Pros:                                                         |
                                                              |
The application works in a dynamic structure and actions      |
have been taken for error management. When the user enters    |
data that is different than expected, the application         |
indicates the necessary warning instead of giving an          |
error and terminating itself.                                 |
                                                              |
UX issue has been taken into account. The application has     |
interactive dialogs with the user and gives as cute           |
answers as possible with its own decision mechanism.          |
                                                              |
It works with performance management in mind; inefficient     |
variable generation is not made and thus it does not          |
create unnecessary load on RAM.                               |
---------------------------------------------------------------


---------------------------------------------------------------
Cons / Developable Aspects:                                   |
                                                              |
The application runs on terminal (CLI) systems. Lack of UI    |
support can result in users disliking visually. UI support    |
can be added for easier usage management.                     |
                                                              |
The application runs in a single script internal.             |
Not having a Class structure due to the lack of               |
OOP is inefficient in terms of improvability.                 |
This may reduce the developer's time / efficiency             |
in the future.                                                |
---------------------------------------------------------------
"""


def main_menu():  #
    print("-" * 10, "Welcome to TheApp!", "-" * 10)  # welcome banner
    print("\nWUT IS DIS?")  # funny header
    print("TheGame is an app that you can play interactive "  # information messages
          "games with it.\nJust choice an option from main "
          "menu and go through. Have fun!!!\n")
    print("1: Play a game.\n"  # game options
          "2: Want Random number?\n"
          "3: Play Up&Down.\n"
          "4: quit...\n")
    try:
        switch_demo(int(input("your choice:")))  # this block tries to get input from user,
        # and pass it to game decision function part. Also, conversion of string input to
        # integer is important, because function is a switch/case which accepts integers only.

    except ValueError:  # If a problem occurs while that 'data conversion', especially
        # this block detects this, and generates the required information message.
        print("just integers from list please....")
        print("bye......")
    except Exception:  # If an error occurs in the runtime part, this block
        # ensures that app is terminated correctly.
        print("an other error accrued :( bye....")


def quit_game():  # quit game function.
    print("If you're going to shut me down, why did you start :'(, bye........")
    exit(0)  # exits properly


def play_a_game():  # main executer function of this game
    print("Wanna play a game? okay...")
    total_hp = 3  # local variable for total health point of user, while playing this game
    print("Now, i will give you some chars --and cool hints sure:)--, and you will "
          "try to find the original word from them:)\nremember! you just have 3 shot:))))")  # Explaining game scenario
    answer = input("yes or noi:\x20")  # get answer from user
    if answer != "yes" and answer != "noi":  # checks if unwanted answer come
        print("bad answer!!! bye.")  # unsuitable answer, exiting.
        exit(0)
    elif answer == "yes":  # checks answer
        pass  # keep going on runtime
        print("okay! lets go...")
    else:  # else, detects player do not want to play the game
        print("okay...bye.")
        exit(0)
    # answer is yes, keep going.
    # dict number 1 for storing hardcoded original words
    dictionary_1 = \
        {
            1: "congratulations",
            2: "necessary",
            3: "honorable",
            4: "solution",
            5: "excalibur",
            6: "overrated",
            7: "rhythm",
            8: "entrepreneur",
            9: "psychologist",
            10: "misunderstanding",
        }
    # dict number 2 for storing hints of related original words - foreign key is the index of element.
    dictionary_2 = \
        {
            1: "we say it, when someone achieve something hard, or mary with his/her love?",
            2: "has same meaning with 'being essential'",
            3: "deserving of respect or high regard. - dictionaries say so...",
            4: "the way of solve something:)",
            5: "sword of king Arthur, also a pc from Casper...'",
            6: "rated or valued too highly - generally uses for movies or video games nowadays",
            7: "dum tıs dum tıs dum dum tıs...",
            8: "people who shoot video and post vlogs in social media......",
            9: "after years of hard-work, people who interest with human minds an thinking types",
            10: "'you got it wrong' situation....",
        }
    random_number = random.randint(1, 10)  # generates a random integer for randomize selection
    # from the dictionary_1, and also have to keep this variable locally, so it can be used to
    # show related hint from dictionary_2.
    selected = dictionary_1[random_number]
    print("your word is >>>>", mixer(selected), " --" + dictionary_2[random_number] + "-- ")  # as seen, it uses
    # random_number variable for foreign key. Also, the selected string for question sent to mixer function.
    # With this, mixed version of string will be return to print function.

    for i in range(total_hp):  # a for loop, per 1 health point.
        players_guess = input("try it: ")  # get guess from user
        if players_guess == selected:  # if user answer correctly, application congrats him and quit.
            print("Wow... you found it... congratulations!!!:), bye!!!")
            exit(0)
        else:  # if player fail, application decrease 1 health point from local(functions global) health point variable
            total_hp -= 1  # reduce 1 from total_hp variable
            print("you can't... you lost 1 health point, " + str(total_hp) + " left...")  # warn user.
            if total_hp == 0:  # while for loop goes on, if total_hp be 0 after decreasing, player lose
                # the game. This algorithm can also be developed by no total_hp reducing, because the for loop
                # works related to the health point integer. Sure, if player cannot guess correct
                # answer for total_hp value times, loop wil be done and developer can show 'you loose' message there.
                # If player won, this can be determined while game in loop, and developer can break the loop
                # with 'you won' message and run exit(). Also in this type, if user won and app do not exit
                # in that moment, user will also receive 'you loose' message, which can decrease game experience.
                print("and you loose :'( ...", "bye.....")
                exit(0)


def mixer(selected):  # function for mixing 'randomly selected string' for the question.
    new_one = ""  # a local variable for store new(mixed) string.
    for i in range(len(selected)):  # all strings is a char list in Python, this loop
        # runs throughout length of determined string, for begin mixing.
        picked = random.randint(0, len(selected) - 1)  # because first index of lists is 0; while string
        # have x length, app has to choose a random integer between 'zero and (x -1)' or '1 and x'.
        # Sure with this, random integer can define random char's index in string(char list)
        new_one += selected[picked]  # append the selected random char from string, to store variable.
        temp_string = selected[:picked] + selected[picked + 1:]  # the temp_string variable is sum of
        # two parts. First part is the starting of selected string just ends before selected
        # random char, other part is the rest of selected string without first letter, which is
        # selected random char in selected string. To sum up, temp_string is the remaining
        # part of selected string, after random selected char taken from it.
        selected = temp_string  # equaling selected string to temp_string. With these, new  version of selected
        # string can be processed in loop again, until no char left in it.
    return new_one  # return the mixed string back to question.


def random_number_game():  # game executer function
    try:
        print("wwwwwaaaannnna random number??????? okay....<3<3<3<3<3<3<3")
        # user selects two integer for min and max for game.
        choice_list = [int(input("Pick the first num: "))]
        # user selects other one
        second_input = int(input("Pick second one!!!!!!!!: "))
        choice_list.append(second_input)  # append second one to number list.
        # because of execution structure of random.randint function, if the second value is lower than first one,
        # ValueError exception will be raised. App checks this for running smooth.
        if choice_list[0] > choice_list[1]:
            print("hey... please pick a greater num for the second one...")
            exit(0)
        if second_input >= 65535:  # max value of an integer can be 65535 in theory.
            # Python can process bigger ones, but while application this, it do not let use for this.
            print("this one is veeery big... choice another............ bye.....")
            exit(0)
            pass
        if second_input > 100:  # if user picks big one, app acts like its hard to determine.
            print("oh.. this one is hard... whatever:(........")
            time.sleep(1)
        for i in range(1, 5):  # cute output with loop for UX, app acts like its thinking.
            print("searching it", "." * i)
            time.sleep(0.5)  # waits between 'thinking'.
        time.sleep(1)  # last searching will be 2 secons.
        # generates random integer between range which user determines, and print it.
        print("okay found it!!!!!!!!\nyour random one is >>>>>>>> ",
              str(random.randint(choice_list[0], choice_list[1])) + "\x20!!!\nhappy 2 see you again. bye:')...")
        # game done.
    except ValueError:  # If a problem occurs while that 'data conversion', especially this
        # block detects this, and generates the required information message.
        print("hey! please enter an integer!!!")
        print("bye......")
        exit(0)
    except Exception:  # If an error occurs in the runtime part, this block
        # ensures that app is terminated correctly.
        print("an other error accrued :( bye....")


def play_up_or_down():  # game executer function
    print("Now, i will pick a number and you will try to guess it...\nAre you ready?")
    answer = None  # empty answer variable, will be determined with users answer.
    while answer != "yes":  # while users answer become 'yes', app will ask the 'wanna play' question.
        answer = input("yes or no: ")
        if answer != "yes" and answer != "no":  # application do not like the answer, because it is not suitable.
            print(">:( type yes or no!!!")
        if answer == "no":  # answer is suitable for conditions, but application wants to force user to play.
            print(":( don't you want to play?")
    print("you said yes:'))))))) lets go!!!!!!!!!")  # if user inputs and say 'yes', while loop will break itself
    # because the answer provides 'False' condition for while loop, similar to 'do-while' in PHP.
    think_array = ['thinking.', 'thinking..', 'thinking...', 'Find it!']  # UX messages array, for being
    # cute and realistic.
    for word in think_array:  # prints items in think_array.
        print(word)
        time.sleep(0.5)  # waiting like app is thinking.
    target = random.randint(1, 100)  # select a random integer, this value also will be the target of user.
    # print("--", target, "--") # for debug purposes. commented out for production.
    while True:  # starting the while loop, it will be loop again and again until some code breaks it.
        try:
            guess = int(input("okay, make a guess: "))  # get users guess from input.
            # Converts the string input to integer, because the randomly selected target is integer too.
            if guess == target:  # if user guess the target integer correctly, condition successes and game will end.
                print("Congrats!!! you found it... bye.")
                exit(0)
            elif guess > target:  # if users guess is greater than target, app will notify him.
                print("go down!")
            else:  # the last condition is that; users guess is smaller than target. Sure, app will notify him to go up.
                if isinstance(guess, int):  # check the input type again with not conversion trying
                    # this time, using isinstance function.
                    print("go up!")

        except ValueError:  # If a problem occurs while that 'data conversion', especially this
            # block detects this, and generates the required information message.
            print("hey! please enter an integer!!!")
            print("bye......")
            exit(0)
        except Exception:  # If an error occurs in the runtime part, this block
            # ensures that app is terminated correctly.
            print("an other error accrued :( bye....")


def switch_demo(number):  # Python do not have built-in switch:case function, but it can be done with dicts.
    # This function gets an integer value, which is the users choice for play pointed game.
    switcher = \
        {
            1: play_a_game,  # these are the game executer or quit functions.
            2: random_number_game,
            3: play_up_or_down,
            4: quit_game
        }
    if number not in switcher:  # if users selection not in list, app notifies user and exits.
        print("just integers from list please....")
        print("bye......")
    func = switcher.get(number, lambda: "bad choice... Pick again!!!")  # if user select a valid
    # option, the related function name is taken from dict and 'func's value will be that.
    func()  # func will be executed and sure, with it; the related function will be executed too.


print("\nstarting...")  # this is where the application starts
main_menu()  # the relevant function is called and the menu is shown to the player
# EOF
