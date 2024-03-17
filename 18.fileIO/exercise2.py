# Write a function called statistics, which takes in a file name and returns a dictionary with the number of lines, words, and characters in the file.
#
# (Note: we've provided you with the first chapter of Alice's Adventures in Wonderland to give you some sample text to work with. This is also the text used in the tests.)

def statistics(file_name):
    with open(file_name) as file:
        lines = file.readlines()

    return {"lines": len(lines),
            "words": sum(len(line.split(" ")) for line in lines),
            "characters": sum(len(line) for line in lines)}
