import pandas as pd
from Tkinter import *


root = Tk()



def clean_df(df,cols):
    for col_name in cols:
        keys = {cats: i for i, cats in enumerate(df[col_name].unique())}
        df[col_name] = df[col_name].apply(lambda x: keys[x])
    return df



def anonymise(uinput, collumntitles, cols):
    df = pd.read_csv(uinput)
    df = clean_df(df,cols)
    df.to_csv('anon_data.csv')



def commandline():

    csvfile=entry1.get()
    collumntitles=entry2.get()

    uinput=csvfile.strip()

    splitting=collumntitles.split(",")
    cols = [s.strip() for s in splitting]


    anonymise(uinput, collumntitles, cols)



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
