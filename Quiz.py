# This Is A Rock Paper Scissors Program Code ByTech With Tim Offical Video  https://www.youtube.com/watch?v=DLn3jOsNRVE Go watch it if you want full credit to him
#you can add questions if u want

print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for? ").lower
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ").lower
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ").lower
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ").lower
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")
