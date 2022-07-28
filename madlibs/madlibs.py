# There are multiple ways to concatenate a string in python
# The example is inserting a value at the end of this sentence, "I really like ____"

# whatILike = "food!"

# The ways to do it:
# print("I really like " + whatILike)
# print("I really like {}".format(whatILike))
# print(f"I really like {whatILike}")

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
famous_person = input("Famous person: ")

# Using the \ says that the code continues on the next line
madlib = f"Computer programming is so {adj}! \
It makes me so excited all the time because \
I love to {verb1}. Stay hydrated and {verb2} \
like you are {famous_person}!"

print(madlib)