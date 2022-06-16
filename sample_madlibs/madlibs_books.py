def madlib():
    adj1 = input("Enter an adjective:")
    adj2 = input("Enter an adjective:")
    adj3 = input("Enter an adjective:")
    adj4 = input("Enter an adjective:")
    adj5 = input("Enter an adjective:")

    noun1 = input("Enter a noun:")
    noun2 = input("Enter a noun:")
    noun3 = input("Enter a noun:")
    noun4 = input("Enter a noun:")

    plural_noun1 = input("Enter a plural noun:")
    plural_noun2 = input("Enter a plural noun:")

    verb1 = input("Enter a verb:")

    place = input("Enter name of a place:")
    madlib = f"There are many {adj1} to choose a/an {noun1} to read. First, you could ask " \
             f"your friends and {plural_noun1}. If your friends and family are no help, " \
             f"try checking out the {noun2} Review in The {noun3} Times. You could also " \
             f"choose a book the {adj2} fashioned way. Head to your local library or" \
             f" {place} " \
             f"and browse the shelves until something catches your {noun4}. Or, you could " \
             f"save yourself a whole lot of {adj3} trouble and log on to bookish.com, " \
             f"the {adj4} website to {verb1} for books ! With all the time you'll save " \
             f"not " \
             f"having to search for {plural_noun2}, you can read {adj5} books!  "
    print(madlib)


