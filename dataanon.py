import unicodecsv as csv
from faker import Factory
from collections import defaultdict
from csv import reader
from Tkinter import *


root = Tk()


def anonymize_rows(rows):

    # Load the faker and its providers
    faker  = Factory.create()

    # Create mappings of data to faked data.
    data  = defaultdict(faker.name)

    # Iterate over the rows and yield anonymized rows.
    for row in rows:
        # Replace the user definied fields with faked fields.
        for i in splitrows:
                    row[i]  = data[row[i]]
        # Yield the row back to the caller
        yield row


def anonymize(source, target):

    with open(source, 'rU') as f:
        with open(target, 'w') as o:
            # Use the DictReader to easily extract fields
            reader = csv.DictReader(f)
            writer = csv.DictWriter(o, reader.fieldnames)

            # Read and anonymize data, writing to target file.
            for row in anonymize_rows(reader):
                writer.writerow(row)


def commandline():

    csvfile=entry1.get()
    collumntitles=entry2.get()

    #uinput=raw_input("Name the file you would like to anonymise")
    uinput=csvfile
    # Request file name


#    with open(uinput, 'r') as readobj:
#        csv_reader = reader(readobj)
#        for row in csv_reader:
#            print("Which of the following rows would you like to anonymise? Seperate them with a single space", row)
#            break
            # Read the header for each collumn and prompt the user to select one or multiple

    global newrow
    #newrow=raw_input()
    newrow=collumntitles
    # Collect eh users input

    global splitrows
    splitrows=newrow.split()
    # Split the users input into its components

    anonymize(uinput, "data/anon set.csv")



label1 = Label(root, text="Select your file:")
entry1 = Entry(root)
entry1.get()
label2 = Label(root, text="Which rows should be anonymised:")
entry2 = Entry(root)
entry2.get()
button1 = Button(root, text="Anonymise!", command=commandline)

label1.grid(row=0, sticky=E)
label2.grid(row=1, sticky=E)

entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)

button1.grid(row=2, column=1)



root.mainloop()
