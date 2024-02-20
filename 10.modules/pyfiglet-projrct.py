# import pyfiglet
# help(pyfiglet.figlet_format)
#
# text = pyfiglet.figlet_format("hello")
# print(text)
from colorama import init

# use colorama to make termcolor work on Windows too

from pyfiglet import figlet_format
from termcolor import colored

init()
colour_text = None
message = input("What message do you want to print? ")
colour_input = input("What colour")

allowed_colours = ["black", "red", "green", "yellow", "blue", "magenta", "cyan", "white", "light_grey", "dark_grey", "light_red", "light_green", "light_yellow", "light_blue", "light_magenta", "light_cyan"]

ascii_text = figlet_format(message)
if colour_input in allowed_colours:
    colour_text = colored(ascii_text, color=colour_input)
else:
    colour_text = colored(ascii_text, color="green")

print(colour_text)
