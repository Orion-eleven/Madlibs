""" Simple Mad Libs Generator """

#story taken from http://www.redkid.net/cgi-bin/madlibs/scenefromsitcom.pl
#Loop back to this point once code finishes

loop = 1

while (loop < 10):

# prompt user for words

    adjective1 = input("Enter an adjective: ")
    adjective2 = input("Enter an adjective: ")
    adjective3 = input("Enter an adjective: ")
    adverb1 = input("Enter an adverb: ")
    adverb2 = input("Enter an adverb: ")
    article = input("Enter an article of clothing: ")
    fem_name = input("Enter a female name: ")
    male_name = input("Enter a male name: ")
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter a noun: ")
    noun3 = input("Enter a noun: ")
    noun4 = input("Enter a noun: ")
    p_animal = input("Enter an animal (plural): ")
    p_noun = input("Enter a plural noun: ")
    place = input("Enter a type of room: ")
    verb1 = input("Enter a verb: ")
    verb2 = input("Enter a verb: ")

#Fill story with user words
    print ("SCENE FROM A SITCOM")

    print ("------------------------------------------")

    print ("(Amy enters through the front", noun1, "flops onto the overstuffed", noun2, "and heaves a",adjective1,"sigh of exhaustion.)")

    print ("(Jenny comes out of the", place, ".)")

    print ("JENNY: Hi! Did you have a", adjective2, "day?")

    print ("AMY: a(n)", adjective1,"exhausting day. You're home early.")

    print ("JENNY: Had to change my",article, "before we go out.")

    print ("AMY: Go out? Wild", p_animal, "couldn't drag me out. I'm really ADJ3.")

    print ("JENNY: We're meeting",fem_name,"for a quick ",verb1,". She's bringing",male_name,"to",verb2,"you.")

    print ("AMY: No more blind",p_noun," for me. Never again!")

    print ("JENNY: But he's",adverb1, " your type... a self-made",noun3,"and",adverb2,"handsome")

    print ("AMY: Oh well, one more",noun4, "can't hurt me.")

    print ("(fin.)")

    print ("------------------------------------------")

# Loop back to "loop = 1"

loop = loop + 1