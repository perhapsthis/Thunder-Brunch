#! python3
# This is a text adventure I'm working on to help me get some basic Python skills understood.

import random
import time
import sys

finalScore = ([1])  ## This is the tally of ENERGY DRINKS
finalName = ([])  ##This is a list containing the user's name
percentage_played = ([]) ## This is a metric of how much of the game the player plays.
def DelayPrint(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(0.02)

while True: ## The whole game exists within this while loop, so it can be played again and again.

    def straightAnswer():  # This is a recursive introduction that only lets the player continue with an affirmative response.
        ans = input('\nAre you a true player for real? \nIs your heart free, \nlike a free-roaming caribou? "yes" or "no". :').lower()
        if ans == ('yes'):  # The only answer
            time.sleep(1)
            percentage_played.append(1)
            DelayPrint('I love you.')
            time.sleep(1)
            DelayPrint('''
    I am a minor god from a parallel dimension.

    (For reference you can think of Q from Star Trek TNG...
    ...but less given to singing and dancing...)

    (...Slightly less given to singing and dancing.)


    I was created to tell stories that involve a bit of random chaos.''')

            time.sleep(1)
            DelayPrint('\nI like chaos.')
            time.sleep(1)
            DelayPrint("\nWe are going to have a fucking adventure...")
            time.sleep(2)
            print ('')

        elif ans == ('no'):  # For sassy people
            DelayPrint('\nScuttle on then. \nSally forth! \mGit!')
            percentage_played.append(1)
            straightAnswer()
        else:
            time.sleep(2)
            percentage_played.append(1)
            DelayPrint("\nI need a 'yes' or 'no'.")
            straightAnswer()

    straightAnswer()

    def TheirName():
        userName = input('What is your name?')
        if userName.isprintable():
            time.sleep(1)
            percentage_played.append(1)
            DelayPrint("""\nIt's good to meet you """ + userName + ". Gimmie a sec.")
            DelayPrint('\nI will pick from my list of adventures...')
            finalName.append(userName)
        else:
            DelayPrint("\nThat's not an acceptable choice. \nYou stand judged.")
            percentage_played.append(1)
            TheirName()

    TheirName()

    def check_phone(): #These are things that you see on your phone. Random chaos.
        print ('\n...')
        DelayPrint('\nYou get an alert on your phone')
        print ('')
        rand_phone = ['"Baby, I miss you!"', '"Your phone bill is due"', '"You are delicious"', '"Update 10.03 is now available"', '"The International Space Station is above you right now"', '""Groucho" wants to be friends with you"', '"You have six new likes!"']
        DelayPrint('\nYour Phone says: ' + (random.choice(rand_phone)))
        print ('')


    def RandomThought(): #These are weird thoughts the player has randomly during the game
        print ('\n...')
        DelayPrint('\nYou have a random thought... ')
        ans = random.randint(0,13)
        if ans == 1:
            DelayPrint('...')
            DelayPrint('\n"I wonder what Magnum PI would have been like in space?')
            DelayPrint('...\n')
        elif ans == 2:
            DelayPrint('...')
            DelayPrint('\n"Who are YOU calling a psycho!?"')
            DelayPrint('...\n')
        elif ans == 3:
            DelayPrint('...')
            DelayPrint('\n"I must not fear. \nFear is the mind killer"')
            DelayPrint('...\n')
        elif ans == 4:
            DelayPrint('...')
            DelayPrint('\n"Two noodles in the dark"')
            DelayPrint('...\n')
        elif ans == 5:
            DelayPrint('...')
            DelayPrint('\n"Five sparrows sing Mozart"')
            DelayPrint('...\n')
        elif ans == 6:
            DelayPrint('...')
            DelayPrint('\n"I am NOT a Merry Man!"')
            DelayPrint('...\n')
        elif ans == 7:
            DelayPrint('...')
            DelayPrint('\n"Yeah...\nFarscape holds up."')
            DelayPrint('...\n')
        elif ans == 8:
            DelayPrint('...')
            DelayPrint('\n"I am a happy monkey..."')
            DelayPrint('...\n')
        elif ans == 9:
            DelayPrint('...')
            DelayPrint('\n"Set professionalism to full-on!"')
            DelayPrint('...\n')
        elif ans == 10:
            DelayPrint('...')
            DelayPrint('''\n"Sand dollars and dolphins make love under the sun''')
            DelayPrint('...\n')
        elif ans == 11:
            DelayPrint('...')
            DelayPrint('\nMy feet hurt.')
            DelayPrint('...\n')
        elif ans == 12:
            DelayPrint('...\n')
            DelayPrint('''\n"I flip you. \nI flip you for real."''')
            DelayPrint('...\n')
        elif ans == 13:
            DelayPrint('...')
            DelayPrint('\nMy energy is not at peak levels.')
            DelayPrint('...\n')
        time.sleep(2)


    def lineSetup():  # Line Setup. This must be done to move on. This is recursive.
        check_phone()
        percentage_played.append(1)
        DelayPrint('''
    You just got here. You are opening, and you are by yourself.
    All you have is your sense of personal freedom, your knives, and one ENERGY DRINK
    If something goes wrong you have nobody but yourself to deal with it.
    You are going to need to set up the line.''')

        ans = input('''
    Do you:
    a: Turn on all the equipment
    b: Go smoke a bowl
    c: Do inventory
    d: Put on your work shoes

    (Pick a letter.) :''').lower()

        if ans == ('a'):
            DelayPrint('\nThis was the most responsible choice. \nYou are awarded one ENERGY DRINK')  # This is the best option as far as energy drinks go, but I'm a chaos god...
            finalScore.append(1)
            time.sleep(2)
            percentage_played.append(1)
            RandomThought()
            challengeOne()

        elif ans == ('b'):  # This is a weirder path, but can turn out well.
            DelayPrint('Hey pal, \nnot at work, ok?')
            time.sleep(2)
            percentage_played.append(1)
            RandomThought()
            challengeTwo()
        elif ans == ('c'):  # I don't like people who pick this one. They lose a drink.
            DelayPrint("\nI know you're trying to get ahead, but that's not what should be on your mind right now. You forfeit. an ENERGY DRINK.")
            time.sleep(2)
            del finalScore[-1]
            percentage_played.append(1)
            RandomThought()
            challengeOne()
        elif ans == ('d'):  #Slackers
            DelayPrint("\nSafety first, but now you're three minutes behind. \nService starts in 57 minutes.")
            time.sleep(2)
            percentage_played.append(1)
            RandomThought()
            challengeOne()
        else:
            print('/nWRONG ANSWER' * 50)
            percentage_played.append(1)
            lineSetup()


    def challengeOne():  # A monkey wrench in an otherwise fine morning.
        ans = input('\nYou have many challenges ahead. \nPick a number between 1 and 5')
        if ans == ('1'):
            check_phone()
            percentage_played.append(1)
            DelayPrint("\nThere isn't any bacon!")
            RandomThought()
            responseOne()
        elif ans == ('3'):
            check_phone()
            DelayPrint('\nYour nephew is in jail')
            DelayPrint('\nYou have to talk to your sister on the phone for ten minutes, \na bail bondsman for another ten.')
            time.sleep(2)
            percentage_played.append(1)
            responseTwo()
        elif ans == ('5'):
            check_phone()
            DelayPrint('\nYou have been unhappy for weeks. Unhappy with your life. You just realized why.')
            DelayPrint('\nYou quit, right then, all of a sudden.')
            DelayPrint('\nYou throw your apron in the laundry bag and forfeit all of your ENERGY DRINKS')
            DelayPrint('\nYou go to the bus stop, and call home.')
            DelayPrint('\n"Baby...I did something rash..."')
            time.sleep(2)
            del finalScore[:]
            percentage_played.append(1)
            endGame()
        elif ans == ('2'):
            check_phone()
            percentage_played.append(1)
            responseOne()
        elif ans == ('4'):
            check_phone()
            percentage_played.append(1)
            responseOne()
        else:
            DelayPrint('You were disobedient. \nYou just missed out on some good shit.')
            DelayPrint("Don't tempt a minor god from a parallel dimension...")
            percentage_played.append(1)
            beginService()


    def challengeTwo():  ## This is what happens if you smoke a bowl
        ans = random.randint(0, 4)
        if ans == 1:
            DelayPrint("\nYou think 'Ahhhhhhh!!!! Fuck! What was I just doing??'")
            RandomThought()
            check_phone()
            percentage_played.append(1)
            responseOne()
        elif ans == 3:
            DelayPrint("\nYou decide to make yourself some breakfast. \nYou just lost ten minutes of prep time, and forget where you put your ENERGY DRINK.")
            del finalScore[-1]
            percentage_played.append(1)
            responseTwo()
        else:
            DelayPrint("\nYou smoked just the right amount. \nEverything is perfect. \nYou are awarded one ENERGY DRINK.")
            finalScore.append(1)
            RandomThought()
            percentage_played.append(1)
            check_phone()
            response_three()


    def responseOne():  # Your state of mind if you are freaked out, angry, or too high.
        ans = input('\nYou have been dealt a bit of stress. \nRoll for State of Mind! \n(Choose a number between 1 and 5)')
        if ans == ('1'):
            DelayPrint('\nYou are surrounded on all sides by chaos.')
            time.sleep(3)
            percentage_played.append(1)
            DelayPrint('\nYou can feel your pulse in your ear, in your wrists....')
            time.sleep(2)
            DelayPrint('\nYou turned the grill up all the way when you started, and now the heat is filling the line with a feeling of danger.')
            time.sleep(7)
            DelayPrint('\nYou get over it.')
            time.sleep(2)
            check_phone()
            CurrentTally()
            beginService()
        elif ans == ('2'):
            DelayPrint("\nYou got your shit together.")
            time.sleep(5)
            RandomThought()
            percentage_played.append(1)
            CurrentTally()
            beginService()
        elif ans == ('4'):
            DelayPrint("\nYou become obsessed with wanting to know why \nnobody can take care of any number of tasks except for you")
            time.sleep(2)
            percentage_played.append(1)
            DelayPrint("\nYou get bummed out.")
            negativeSpiral()
        else:
            time.sleep(2)
            DelayPrint("\nYou are feeling grouchy as shit.")
            time.sleep(2)
            CurrentTally()
            percentage_played.append(1)
            beginService()

    def negativeSpiral(): ## Serious grumps go here.
        time.sleep(2)
        DelayPrint('\nShit man...You go dark there for a minute.')
        DelayPrint('\nFor a minute there, you think you might flee!')
        DelayPrint('\nYou snap out of it.')
        time.sleep(2)
        RandomThought()
        percentage_played.append(1)
        check_phone()
        CurrentTally()
        beginService()

    def CurrentTally(): ## This function returns a string containing the numbner of ENERGY DRINKS
        print ('')
        DelayPrint(finalName[0] + ' , you currently have ' + str(len(finalScore)) + ' ENERGY DRINKS!')


    def responseTwo():  # If you got behind before opening.
        ans = input('''
    You are behind on your pre-open checklist. Something will have to not get done.
    Do you:
    a: Not make hashbrowns
    b: Not heat up the gravy
    c: Not make the fruit bowls
    Pick a letter.''').lower()
        if ans == ('a'):
            DelayPrint("Are you serious??? \nNo hashbrowns? \nGood luck \nThat'll cost an ENERGY DRINK!")
            del finalScore[-1]
            CurrentTally()
            percentage_played.append(1)
            beginService()
        elif ans == ("b"):
            DelayPrint("You are not going to be able to sell many menu items without gravy. You better get it going ASAP!")
            CurrentTally()
            percentage_played.append(1)
            beginService()
        elif ans == ("c"):
            DelayPrint("That's okay, someone else will cover for you, and resent you.")
            CurrentTally()
            percentage_played.append(1)
            beginService()
        else:
            time.sleep(2)
            percentage_played.append(1)
            DelayPrint("That's not an option " + (finalName[0]))
            responseTwo()

    def response_three(): # The luckiest of all the smoke-a-bowl paths.
        DelayPrint('\nYou meander through your list of opening tasks...')
        percentage_played.append(1)
        DelayPrint("\nStars explode like dynamite in your brain...")
        time.sleep(5)
        print("""
                       **      o   *              * +              **               *
         *     +
              *      **          *        **  **             **    *    *   . .            ,   .         . *   .  .  ,
          **     +    .    .  .     .             .     .    *         '    '   .   ..     *   *    . **    *    *   . .  **    *    *   . .  **    *    *   . .      +   .  '*  +                       **      o   *              * +              **               *
            **  **             **    *    *   . .        **    *    *   . .  **    *    *   . .  **    *    *   . .  **    *    *   . .      ,   .         . *   .  .  ,
          **     +    .    .  .     .             .     .    *         '    '   .       ,   .         . *   .  .  ,
          **     +    .    .  .     .             .     .    *         '    '   .   ..     *   *    .     +   .  '*  +                       **      o   *              * +              **               *
         *     +
              *      **          *        **  **             **    *    *   . .            ,   .         . *   .  .  ,
          **     +    .    .  .     .             .     .    *         '    '   .   ..     *   *    .     +   .  '*  +                       **      o   *              * +              **               *
         *     +*   *    .     +   .  '*  +                       **      **    *    *   . .  **    *    *   . .  **    *    *   . .  **    *    *   . .  o   *              * +  ..   **    *    *   . .  **    *    *   . .  **    *    *   . .  **    *    *   . .  **    *    *   . .    *   *    .     +   .  '*  +                       **      o   *              * +              **               *

              *      **          *        **  **             **    *    *   . .            ,   .         . *   .  .  ,
          **     +    .    .  .     .             .     .    *         '    '   .   ..     *   *    .     +   .  '*  +                       **      o   *              * +              **               *
         *     +
              *      **          *       ____ **    *    *   . .  **    *    *   . .  **    *    *   . .  **    *    *   . .  **    *    *   . .  **    *    *   . .  **    *    *   . .
                               __...---~'    `~~~----...__ **    *    *   . .  **    *    *   . .  **    *    *   . .  **    *    *   . .  **    *    *   . .  **    *    *   . .
                            _=============================== **    *    *   . .  **    *    *   . .  **    *    *   . .  **    *    *   . .
       ,----------------._/'      `---..._______...---' **    *    *   . .  **    *    *   . .  **    *    *   . .  **    *    *   . .  **    *    *   . .  **    *    *   . .
       (_______________||_) . .  ,--' **    *    *   . .  **    *    *   . .  **    *    *   . .  **    *    *   . .  **    *    *   . .
           /    /.---'         `/ **    *    *   . .  **    *    *   . .  **    *    *   . .  **    *    *   . .  **    *    *   . .  **    *    *   . .
          '--------_- - - - - _/ **    *    *   . .  **    *    *   . .  **    *    *   . .  **    *    *   . .  **    *    *   . .  **    *    *   . .  **    *    *   . .
                    `--------' **    *    *   . .  **    *    *   . .  **    *    *   . .  **    *    *   . .  **    *    *   . .  **    *    *   . .

              *      **          *        **  **             **    *    *   . .            ,   .         . *   .  .  ,
          **     +    .    .  .     .             .     .    *         '    '   .   ..     *   *    .     +   .  '*  +                       **      o   *              * +              **               *
         *     + **    *    *   . .  **    *    *   . .  **    *    *   . .  **    *    *   . .
              *      **          *        **  **             **    *    *   . .            ,   .         . *   .  .  ,
          **     +    .    .  .      **    *    *   . .  **    *    *   . .  **    *    *   . .  **    *    *   . . .             .     .    *         '    '   .   ..     *   *    .     +   .  '*  +                       **      o   *              * +              **               *
         *     +
              *      **          *        **  **             **    *    *   . .            ,   .         . *   .  .  ,
          **     +    .    .  .     . **    *    *   . .  **    *    *   . .  **    *    *   . .  **    *    *   . .  **    *    *   . .  **    *    *   . .  **    *    *   . .              .     .    *         '    '   .   ..     *   *    .     +   .  '*  +                       **      o   *              * +              **               *
         *     +
              *      **          *        **  **             **    *    *   . .            ,   .         . *   .  .  ,
          **     +    .    .  .     .             .     .    *         '    '   .   ..     *   *    .     +   .  '*  +                       **      o   *              * +              **               *
         *     +
              *      **          *        **  **             **    *    *   . .            ,   .         . *   .  .  , **    *    *   . .  **    *    *   . .  **    *    *   . .
          **     +    .    .  .     .             .     .    *         '    '   .   ..     *   *    .     +   .  '

     **    *    *   . .  **    *    *   . .

              """)
        time.sleep(2)
        beginService()

    def beginService():  # The foodening begins...
        time.sleep(5)
        percentage_played.append(1)
        DelayPrint('''

    It is 7:00AM ''' + (finalName[0]) + '''. Brunch service has just begun and you are no longer alone.
    Your rouge's gallery of comrades are with you.
    You made it through your first hour. You are awarded ONE ENERGY DRINK.

    Now is time to begin to food people.

    ALL HAIL FOOD!
    ''')
        finalScore.append(1)
        RandomThought()
        time.sleep(4)
        ans = input('''\nSpin the Wheel of Opportunity and Misfortune.
    enter'x' for a gentle turn,
    enter 'xx' for a brave turn,
    enter 'xxx' for a pornographic turn,
    enter 'xxxx' for warrior strength.''').lower()
        if ans == ('x'):
            DelayPrint('Someone called in sick.')
            time.sleep(2)
            percentage_played.append(1)
            DelayPrint('\nMother fucker.')
            ansOne()
        elif ans == ('xx'):
            DelayPrint('\nShit! The Health Department is here for an inspection!')
            time.sleep(2)
            percentage_played.append(1)
            DelayPrint('\nTHROW OUT THE HOLLANDAISE!')
            time.sleep(2)
            DelayPrint('\nYou have an open ENERGY DRINK on the line. You know that is a violation, so you throw it out.')
            del finalScore[-1]
            time.sleep(2)
            DelayPrint('\nTime to find out how true that caribou heart, in fact, is. \nAre you ready to take a chance?')
            ansTwo = input('\nyes, or no? :').lower()
            if ansTwo == ('yes'):
                DelayPrint('\nEverything temped out fine. \nYou are awarded two ENERGY DRINKS.')
                finalScore.append(1)
                finalScore.append(1)
                percentage_played.append(1)
                time.sleep(2)
                nineAMb()
            elif ansTwo == ('no'):
                DelayPrint(
                    '\nThe health inspector shut the restaurant down \ndue to abundant fecal mater on every surface. You are fired.')
                time.sleep(2)
                del finalScore[:]
                percentage_played.append(1)
                time.sleep(3)
                endGame()
            else:
                   print('Wrong answer' * 100)
                   time.sleep(2)
                   DelayPrint("\nLet's try this section over again...")
                   percentage_played.append(1)
                   beginService()
        elif ans == ('xxx'):
            DelayPrint('\nThe power just went out.')
            time.sleep(3)
            DelayPrint('\n...   ...   ...')
            time.sleep(2)
            percentage_played.append(1)
            DelayPrint('\nEveryone turns on their smartphone flashlights. \nYou try to sell what you can.')
            time.sleep(2)
            a=random.randint(0,2)
            if a==1:
                DelayPrint("\nIt's been fifteen minutes. \nThe powers that be decide to close the restaurant for the day.\nIn the confusion you forget your ENERGY DRINK(S)")
                time.sleep(3)
                percentage_played.append(1)
                del finalScore[:]
                endGame()
            else:
                DelayPrint('\nThe lights came back on.')
                percentage_played.append(1)
                nineAMc()

        else:
            time.sleep(2)
            DelayPrint('\nYou survived. Somehow.')
            percentage_played.append(1)
            nineAMc()

    def ansOne():  #This is what happens if someone calls in sick.
        ansOne = input('\nSpin the Wheel of Opportunity and Misfortune. \nx for a gentle turn, xx for a brave turn.').lower()
        if ansOne == ('x'):
            DelayPrint("\nIt's the person you don't like anyway.\nThe one who smells bad. \nStill, ou are down a comrade. \nThe busboy is on hashbrowns until the Chef comes in.")
            time.sleep(2)
            percentage_played.append(1)
            RandomThought()
            nineAMa()
        elif ansOne == ('xx'):
            DelayPrint("\nThe Chef got ahold of a night cook and got them to come in. \nYou will have to give them your ENERGY DRINK.")
            del finalScore[-1]
            percentage_played.append(1)
            time.sleep(2)
            nineAMa()
        else:
            DelayPrint('\nYou spun it a bit too hard...')
            time.sleep(2)
            percentage_played.append(1)
            ansOne()


    def nineAMa():  # This is what happens if someone calls in sick, later on.
        DelayPrint("\nIt's 9:00 AM. You've made all people food-heavy. \nThere have been many mandatory poops in the bathroom. \nGood God. It is a lot to deal with.")
        time.sleep(2)
        percentage_played.append(1)
        DelayPrint('\nYou got past your staffing woes.')
        time.sleep(2)
        CurrentTally()
        goodRush()


    def nineAMb():  # This is what happens if the Health Inspector visited.
        DelayPrint("\nEveryone goes outside to have a cigarette after the Health Inspector leaves. \nEverybody needed one.")
        time.sleep(1)
        percentage_played.append(1)
        DelayPrint('\n...and continued to smoke...')
        time.sleep(2)
        DelayPrint('''
    \nBack on the line the printer was going haywire. \nOrders were flooding in.''')
        time.sleep(2)
        DelayPrint('''
    \nYou return to the line to a major backlog of orders.
    \nBy the time you sort out the long fire items on the seven top ticket \nthree four tops roll in. \nIt's all pancakes.''')
        time.sleep(2)
        DelayPrint('''
    \nPancakes are quick on and off the grill, \nbut there may be a minor meltdown.''')
        time.sleep(3)
        ans = input('''
    Are you made of strong stuff?
        ''').lower()
        if ans =='yes':  # Good outcome
            DelayPrint("\nYou got that line of tickets out. the Chef gives everyone three ENERGY DRINKS")
            finalScore.append(1)
            finalScore.append(1)
            finalScore.append(1)
            percentage_played.append(1)
            time.sleep(2)
            CurrentTally()
            DelayPrint('You made it through many trials and tribulations.\nOn to the rush!')
            time.sleep(2)
            goodRush()
        else:  # Bad outcome
            percentage_played.append(1)
            DelayPrint('''
    \nyour servers are complaining right and left. \nThese eggs have broken yolks, \nthat toast is bread, not toast, \nseveral cooks can, \napparently go to hell.
    \nThe new guy asks if he can take a break. \nEveryone condescends to let him off the line. \nEveryone hopes in their heart of hearts that he comes back.''')
            time.sleep(3)
            CurrentTally()
            badRush()



    def nineAMc():  # This is what happens if you pass the initial challenges. You get a 50/50 chance of good/bad rush
        ans = input('\nWhat are you going to do about it? \n(yes or no)').lower()
        if ans == ('yes'):
            percentage_played.append(1)
            time.sleep(2)
            DelayPrint('Time flys by. On to the good midmorning rush.')
            finalScore.append(1)
            RandomThought()
            time.sleep(3)
            CurrentTally()
            goodRush()

        else:
            time.sleep(2)
            percentage_played.append(1)
            DelayPrint('You brought this on yourself!')
            time.sleep(2)
            RandomThought()
            CurrentTally()
            time.sleep(2)
            badRush()

    def goodRush():
        for i in range(15):
            print ('')
            time.sleep(.5)
        percentage_played.append(1)
        DelayPrint('\nTHIS IS THE BEST OF ALL POSSIBLE OUTCOMES!!!!!!!')

        DelayPrint('\nYou know those days?')

        DelayPrint('\nThose \n  times \n    when \n        everything \n          is \nlike aerospace tolerances, \nlike a ballet of problem-solving?')

        DelayPrint('\nThis is one of those times.')
        time.sleep(2)
        DelayPrint('''
              ___
                                    _-"_-"
                                  _-_-"
                               _-_-"
      _______________________-"-"_
      \                          /
       \                        /
    .--_\______________________/_--.
     ""--------------------------""
     ''')
        time.sleep(3)
        RandomThought()
        time.sleep(2)
        goodRushTwo()

    def year_two_a():# If you chose interdimentional robots
        DelayPrint('''
        The robots didn't look that impressive. There were no turrets, no ornamental shoulder pads.

        Hell, they didn't even have shoulders.

        Not a humanoid among them. Rectangles on wheels. Whoop-di-shit.''')
        percentage_played.append(1)
        ans = random.randint(0,2)
        if ans == 1:
            DelayPrint('\nYou fucked their shit up but good. You are awarded 5 ENERGY DRINKS!')
            finalScore.append(1)
            finalScore.append(1)
            finalScore.append(1)
            finalScore.append(1)
            finalScore.append(1)
            percentage_played.append(1)
            endGame()
        else:
            DelayPrint('\nTurns out rectangles on wheels know how to murder. \nYou get torn apart subatomic particle by subatomic particle. Everything is really hard for you right now.')
            percentage_played.append(1)
            endGame()


    def year_two_b(): ## If you birdify the world.
        DelayPrint('\nThis behavior gets the world powers (such as they are) pretty well organized against you pretty quick')
        DelayPrint('\nYou are assassinated.')
        percentage_played.append(1)
        endGame()

    def year_two_c(): ## If you become a surprise good guy.
        DelayPrint('\nWell look at you!')
        DelayPrint('\nYou are awarded one ENERGY DRINKS')
        finalScore.append(1)
        percentage_played.append(1)
        endGame()

    def yearsLater(): # If you chose to become a super villian.
            DelayPrint('\nMany, many years later....')
            time.sleep(2)
            DelayPrint("\nThey saw you first flying in the sky...")
            DelayPrint("\nSoon thereafter they learned to fear you...")
            time.sleep(3)
            percentage_played.append(1)
            DelayPrint('''
            In what came to be known as Year 1, you first took control of what was left of the worlds powers....

            ....''')
            ans = input('''What do you want to have happened in Year 2?
            a: Interdimensional robot superheros arrive to challenge you.
            b: You begin reshaping every mountain range into an effigy of you flipping the bird.
            c: You surprise everyone and become mega-super helpful to humanity.''')
            if ans == 'a':
                time.sleep(1)
                percentage_played.append(1)
                year_two_a()
            elif ans == 'b':
                time.sleep(1)
                percentage_played.append(1)
                year_two_b()
            elif ans == 'c':
                time.sleep(1)
                percentage_played.append(1)
                year_two_c()

    def goodRushTwo():
        DelayPrint('''
    \nIt's all robotic in a good way. The orders pour in.

    \nSomewhere out there you hear a baby scream.



    \nYou hear chairs scoot on the floor.

    \nYou hear knives and forks on plates.''')
        percentage_played.append(1)
        time.sleep(4)
        DelayPrint("\nThat's all out there.")
        time.sleep(2)
        DelayPrint('\nIn the dining room.')
        time.sleep(2)
        DelayPrint('\nYou hear it all.')
        time.sleep(2)
        RandomThought()
        time.sleep(2)
        DelayPrint('\n                                         Your knives-')
        time.sleep(1)
        DelayPrint('''
     emmmmmmmm-----------,
            ""|_________/
            `
              ''')
        time.sleep(1)
        DelayPrint('         They fly.')
        time.sleep(3)
        ans = input('''


    The pains in your head just woke up. Do you:
    a) start humming the Jurassic Park theme?
    b) take over the radio and put on the Bee Gees?
    c) remind whoever is working next to you that we are currently hurtling through space?
    d) reveal your telekinetic abilities?

    (Choose a letter.) :''').lower()
        if ans == 'a':
            time.sleep(2)
            DelayPrint('\nI love you.')
            percentage_played.append(1)
            DelayPrint('\nYour musical choices, as per usual, are spot fucking on.')
            DelayPrint('\nEveryone joins in on a sing-a-long.')
            DelayPrint('\nYou are awarded one ENERGY DRINK!')
            finalScore.append(1)
            endGame()

        elif ans == 'b':
            time.sleep(2)
            DelayPrint('\nI love you.')
            percentage_played.append(1)
            DelayPrint('\nYour musical choices, as per usual, are spot fucking on.')
            DelayPrint('\nEveryone joins in on a sing-a-long.')
            DelayPrint('\nYou are awarded one ENERGY DRINK!')
            finalScore.append(1)
            endGame()

        elif ans == 'c':
            time.sleep(2)
            percentage_played.append(1)
            DelayPrint('\nNobody is ready to take on these troubling realities.')
            time.sleep(2)
            DelayPrint("\nOK so you're still weird. Could be worse.")
            endGame()

        elif ans == 'd':
            time.sleep(2)
            percentage_played.append(1)
            DelayPrint('\nNobody is ready to take on these troubling realities.')
            time.sleep(2)
            DelayPrint("\nThis does not go unnoticed by the authorities.")
            time.sleep(2)
            del finalScore[-1]
            DelayPrint('\nEverything goes dark...')
            time.sleep(5)
            DelayPrint('\nHours later you come-to and you are in a hospital room.''')
            ansTwo = input('''
            Do you:
            a) reach out with your mind to try to move things
            b) call out for help
            c) look for your phone
            d) look around you''').lower()
            if ansTwo == "a":
                DelayPrint('\nYou are under restraints. \nYou can feel the clasp in the middle of your chest. \nYou focus your attention on it')
                DelayPrint("\nUnfortunately you haven't trained enough. \nTrying for the clasp you tear your aorta")
                DelayPrint('...')
                percentage_played.append(1)
                DelayPrint('You died ' + finalName[0] + ' .')
                del finalScore[:]
                endGame()
            elif ansTwo == "b":
                DelayPrint('\nZombies burst into the room and eat you.')
                DelayPrint('...')
                percentage_played.append(1)
                DelayPrint('You died ' + finalName[0] + ' .')
                del finalScore[:]
                endGame()
            else:
                DelayPrint("\nJust then you realize that you didn't clock out.")
                DelayPrint("\nThen you realize that you can fly.")
                print('')
                percentage_played.append(1)
                yearsLater()


    def badRush():
        DelayPrint('...')
        time.sleep(2)
        percentage_played.append(1)
        DelayPrint('\nThis is the worst rush of all possible rushes.')
        ans = input('''\nI need to see if you have what it takes to get through this rush.
    complete the following sentence: "All sandwiches are ____ ."
    a: basically the same.
    b: bullshit.
    c: ignorant.
    d: racist.''').lower()
        if ans == ('a'):
            DelayPrint('\nYou made the best of a shitty situation. \nYou are awarded one ENERGY DRINK!')
            finalScore.append(1)
            percentage_played.append(1)
            time.sleep(2)
            RandomThought()
            time.sleep(2)
            badRushTwo()
        else:
            percentage_played.append(1)
            badRushTwo()

    def badRushTwo():
        DelayPrint('...')
        percentage_played.append(1)
        time.sleep(2)
        DelayPrint("\nWhere to begin... \nWhen the grill caught on fire below, \nwhere all the various puddles of grease collect...")
        time.sleep(3)
        DelayPrint('\n(I mean, you try. \nYou try to fight back the grease, \nbut it is a force against which you cannot win.)')
        time.sleep(2)
        DelayPrint("\nIf you need a force to compare the grease force to, \nthink of Shai-Hulud, the Sandworm of Dune")
        DelayPrint('')
        time.sleep(4)
        DelayPrint('\nWell that happened, \nanyway. \nThe fire led to the screaming match between the Chef and the FOH.')
        DelayPrint('')
        time.sleep(2)
        DelayPrint('')
        DelayPrint('\nThe servers wanted everything refired. \nThat, of course, was ludicrous.')
        DelayPrint('')
        ans = input('''\nWhat do you want to have happened?
    a: Your chef coat caught on fire.
    b: Your worst enemy found terrible justice.
    c: The radio starts spitting out static.
    d: The eggs start sticking to the pans like crazy.''')
        if ans == ('a'):
            DelayPrint('\nWay to take one for the team! \nYou are awarded five ENERGY DRINKS!')
            finalScore.append(1)
            finalScore.append(1)
            percentage_played.append(1)
            finalScore.append(1)
            finalScore.append(1)
            finalScore.append(1)
            time.sleep(2)
            CurrentTally()
            goodRush()
        elif ans == ('b'):
            DelayPrint('Dark. These kinds of choices are bad, and you are bad.')
            time.sleep(2)
            percentage_played.append(1)
            DelayPrint('\nYou are FIRED!')
            endGame()
        elif ans == ('c'):
            DelayPrint('\nGO FUCKING APE!')
            time.sleep(2)
            percentage_played.append(1)
            endGame()
        elif ans == ('d'):
            DelayPrint('\nThis was your god damned redemption.')
            time.sleep(2)
            percentage_played.append(1)
            DelayPrint('\nThere were new egg pans in the office the whole time. \nThe Chef brought them out. \nThere was much rejoicing.')
            time.sleep(3)
            goodRush()


    def endGame():
        time.sleep(5)
        DelayPrint('\nYou made it to the end.')
        how_much = len(percentage_played)
        DelayPrint('\nYou made ' + str(how_much) + ' voluntary and involuntary choices.')
        Score = len(finalScore)
        DelayPrint('\nYou have ' + str(Score) + ' ENERGY DRINKS to get you through your commute home.')
        time.sleep(2)
        DelayPrint('\nTry playing again, and make different choices.')
        time.sleep(2)
        DelayPrint('\nI love you.')
        time.sleep(2)
        DelayPrint('\nHere come your energy drinks...')
        time.sleep(3)
        print(int(Score) * '''

                    /())
              .-'""////"`-.
             (.-##| ''   ) )
             |`-._______.-'|
             |::::::::::   |
             |:::::::::'   |
             |:::::::::    |
             |::::::::'    |
             |::::::::     |
             |THUNDER      |
             |     BRUNCH  |
             |::::::       |
             |:::::::      |
             |           ::|
             |     `-::::::|
             |     ::::::::|
             |     ::::::::|
             |    .::::::::|
             |    :::::::::|
             |    :::::::::|
             |   ::::::::::|
             |.  ::::::::::|
             |::.::::::::::|
              \___________/
                       ''')

        for i in range(3):
            print ('******************************************************************************************')

        DelayPrint('\nTHUNDER-BRUNCH by Tom Mohrman')
        DelayPrint('\n..............................................................................................')
        DelayPrint('\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')



    def grillCook():  # This is a choice. There may be more here soon.
        time.sleep(1)
        print('')
        time.sleep(1)
        lineSetup()


    def eggCook():  # This is a choice. There may be more here soon.
        time.sleep(1)
        print('')
        time.sleep(1)
        lineSetup()


    def pantryCook():  # This is a choice. There may be more here soon.
        time.sleep(1)
        print('')
        time.sleep(1)
        lineSetup()


    def eXpo():  # This is a choice. There may be more here soon.
        time.sleep(1)
        print('')
        time.sleep(1)
        lineSetup()


    def WhatKind():  # Introduces the text adventure and makes them pick a position on the line. The position they pick doesn't really have any bearing right now. It might.
        time.sleep(1)
        DelayPrint('''
    **************************************************
    ___              _   __  _   _   _           __
     |  |_| | | |\| | \ |_  |_) |_) |_) | | |\| /   |_|
     |  | | |_| | | |_/ |__ | \ |_) | \ |_| | | \__ | |
    +++++++++++++++++++++++++++++++++++++++++++++++++++
    \nYou are a line cook at a busy restaurant! \nIt is 6:00AM on Saturday. THUNDER-BRUNCH!
    Today you will have your skills and wits tested. \nYou can work any station.''')

        ans = input('''

    Are you:

    a: A grill cook?
    b: An egg cook?
    c: A pantry cook
    d: Expo

    (pick a letter)
    :''').lower()

        if ans == ('a'):
            time.sleep(1)
            DelayPrint('\nThy Name Shall be HashBrown.')
            time.sleep(1)
            grillCook()
        elif ans == ('b'):
            time.sleep(1)
            DelayPrint('\nGoodbye arm hair...')
            time.sleep(1)
            eggCook()
        elif ans == ('c'):
            time.sleep(1)
            DelayPrint('\nReady the waffle irons!')
            time.sleep(1)
            pantryCook()
        elif ans == ('d'):
            time.sleep(1)
            DelayPrint("\nFire toast! \n86 Jokes! Fire frowns! \nTen poachers all day! \nFood up, let's go!")
            time.sleep(1)
            eXpo()
        else:
            time.sleep(.25)
            DelayPrint('\nWRONG ANSWER! YOU BRING THE WRATH OF GREASE TROLLS UPON US ALL' * 20)
            WhatKind()


    WhatKind()
    ans = input('\nDo you want to play again? (yes, or no)')
    if ans == 'yes':
        del finalScore[:]
        finalScore.append(1)
        finalName = ([])
        continue
    else:
        break

