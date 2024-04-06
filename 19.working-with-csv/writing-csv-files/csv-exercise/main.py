'''
add_user("Dwayne", "Johnson") # None
# CSV now has two data rows:

# First Name,Last Name
# Colt,Steele
# Dwayne,Johnson
'''
import csv



def add_user(first_name, last_name):
    with open("users.csv", "a", newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([first_name, last_name])

first_name = input("Enter user's first name:")
last_name = input("Enter user's last name:")

add_user(first_name, last_name)