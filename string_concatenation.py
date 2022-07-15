
# string concatenation (aka how to put strings together)
# suppose we want to create a string thats says "subscribe to ___________"

# a few ways to do this 
#print("subscribe to " + youtuber)
#print("subscribe to {}".format(youtuber))
#print(f"subscribe to {youtuber}")



adj = input("Adjective: ")
verb1 = input("Verb1: ")
verb2 = input("Verb2: ")
famous_person = input("famous_person: ")

madlib = f"Computer programming is so {adj}! \
It makes me so excited all the time because I love to \
{verb1}. Stay hydrated and {verb2} like you are {famous_person}!"

print (madlib)
