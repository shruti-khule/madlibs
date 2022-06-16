def madlib():
    location1 = input("Enter a location:")
    location2 = input("Enter a location:")
    plural_noun1 = input("Enter a plural noun:")
    plural_noun2 = input("Enter a plural noun:")
    plural_noun3 = input("Enter a plural noun:")
    adj1 = input("Enter an adjective:")
    adj2 = input("Enter an adjective:")
    noun1 = input("Enter a noun:")
    noun2 = plural_noun1[0:(len(plural_noun1) - 1)]
    noun3 = input("Enter a noun:")
    noun4 = input("Enter a noun:")
    verb1 = input("Enter a verb:")
    verb2 = input("Enter a verb:")
    verb3 = input("Enter a verb:")
    verb_pasttense1 = input("Enter past tense of a verb:")
    verb_pasttense2 = input("Enter past tense of a verb:")
    verb_pasttense3 = input("Enter past tense of a verb:")
    name = input("Enter a name :")
    celebrity1 = input("Enter a celebrity:")
    celebrity2 = input("Enter a celebrity:")
    celebrity3 = input("Enter a celebrity:")

    madlib = f"The Lord of the Rings Part 1: The Tale of the One Ring \n" \
             f"The story of the One Ring began in a {noun1} long past, in the realm of " \
             f"Middle-{location1}.\nThe lords of each race was given a set of" \
             f" {plural_noun1} to {verb1} their subjects, but in secret, a master" \
             f" {noun2} was {verb_pasttense1} by the Dark Lord {name}.\n" \
             f"To counter this, an alliance of {plural_noun2} and {plural_noun3}" \
             f" fought against {name} and his armies of Orcs.\nOrcs are {adj1} " \
             f"creatures {verb_pasttense2} from pits in the ground in the land of" \
             f" {location2}.\nThe battle was long, but the power of the One {name} " \
             f"could not be stopped.\n{name} struck down the King of Gondor, but his " \
             f"son, {celebrity1}, took up the {adj2} sword of the king and used it to" \
             f" {verb2} the ring from {name}'s hand.\nHe had one chance to {verb3} " \
             f"all evil in Middle-{location1} by destroying the {plural_noun1}," \
             f" but instead he kept it.\nIt eventually led him to his {noun2}, and " \
             f"escaped from {celebrity1}, lying at the bottom of a {noun3} " \
             f"until it was found by the creature {celebrity2}, whose mind was " \
             f"{verb_pasttense3} for 100 years by the {noun2}'s evil.\n" \
             f"But when it abandoned {celebrity2}, it was picked up by an even more " \
             f"unlikely person, {celebrity3}, who was a Hobbit of the {noun4}" \
             f".\nAnd this is how the One {noun2} was found. "

    print(madlib)


