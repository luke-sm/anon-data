import pandas as pd
from Tkinter import *


root = Tk()
var = StringVar()


def clean_df(df,cols):
    for col_name in cols:
        try:
            keys = {cats: i for i, cats in enumerate(df[col_name].unique())}
            df[col_name] = df[col_name].apply(lambda x: keys[x])
            anon_success(col_name)

        except KeyError:
            anon_fail(col_name)
    return df



def anonymise(files, cols):
    try:
        df = pd.read_csv(files)
    except IOError, e:
        file_fail(files)
        #print sys.exc_type
    df = clean_df(df,cols)
    df.to_csv('anon_data.csv')




def user_details():
    csvfile=entry1.get()
    collumntitles=entry2.get()

    files=csvfile.strip()
    #uinput=csvfile.split(",")
    #files = [f.strip() for f in uinput]

    splitting=collumntitles.split(",")
    cols = [s.strip() for s in splitting]

    anonymise(files, cols)


def anon_success(col_name):
    print('Collumn', col_name, 'succesfully anonymised')
    success_print = "Collumn %s succesfully anonymised\n" %col_name
    T.insert(END, success_print, 'success')

def anon_fail(col_name):
    print('Collumn', col_name ,'could not be found')
    fail_print = "Collumn %s could not be found\n" %col_name
    T.insert(END, fail_print, 'fail')

def file_fail(files):
    print ('File', files ,'could not be found')
    file_print = "File %s could not be found\n" %files
    T.insert(END, file_print, 'fail')




label1 = Label(root, text="Select your file:")
entry1 = Entry(root)
entry1.get()
label2 = Label(root, text="Which rows should be anonymised:")
entry2 = Entry(root)
entry2.get()
button1 = Button(root, text="Anonymise!", command=user_details)
T = Text(root, height=10, width=40)
T.tag_config('success', background="#a6f5bb")
T.tag_config('fail', background="#f5ada6")


label1.grid(row=0, sticky=E)
label2.grid(row=1, sticky=E)

entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)

button1.grid(row=2, column=1)
T.grid(row=3, column=0, columnspan = 2)


root.mainloop()
