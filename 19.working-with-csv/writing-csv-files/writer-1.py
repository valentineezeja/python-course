from csv import writer
with open("cats.csv", "w") as file:
    csv_writer = writer(file)
    csv_writer.writerow(["Name", "Age"])
    csv_writer.writerow(["cat1", "2"])
    csv_writer.writerow(["cat2", "5"])