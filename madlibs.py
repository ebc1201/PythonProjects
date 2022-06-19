# string concatenation
# suppose we want to create a string that says "Vote for ____"
# person = "Pedro"  # some string variable

# a few ways to do this
# print("Vote for " + person)
# print("Vote for {}".format(person))
# print(f"Vote for {person}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)
