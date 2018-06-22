import json
import os
from tkinter import ttk
from tkinter import StringVar


def read_json():
    CWD = os.path.abspath('.')
    input_file = os.path.join(CWD, 'Progression\\fws.json')
    with open(input_file, 'r') as fid:  # TODO: Hardcoded Name
        data = json.load(fid)

    activties = data[::]

    with open('data.json', 'w') as outputfile:
        json.dump(data, outputfile)




class App:

    value_of_combo = 'X'

    def __init__(self, parent):
        self.parent = parent
        self.combo()

    def combo(self):
        self.box_value = StringVar()
        self.box = ttk.Combobox(self.parent, textvariable=self.box_value)
        self.box['values'] = ('X', 'Y', 'Z')
        self.box.current(0)
        self.box.grid(column=0, row=0)


if __name__ == '__main__':
    '''
        Launch GUI for progresson application
    '''

    read_json()

    # root = Tk()
    # app = App(root)
    # root.mainloop()
