from sample_madlibs import halloween, lotr, madlibs_books
import random

if __name__ == "__main__":
    r = random.choice([halloween, lotr, madlibs_books])
    r.madlib()
