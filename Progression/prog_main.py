import json
import os
import tkinter as tk
from tkinter import ttk
from tkinter import StringVar


def read_json(file_name):
    CWD = os.path.abspath('.')
    input_file = os.path.join(CWD, file_name)
    with open(input_file, 'r') as fid:
        data = json.load(fid)
    return data


def write_json(data):
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


def get_activities():
    file_name = 'Progression\\fws.json'
    activities = {}

    fws = read_json(file_name)
    activities = [element['activities'] for element in fws]
    activities_dict = {}
    for elem in activities:
        for i in elem:
            activities_dict[i['name']] = i

    file_name = 'Progression\\ua.json'
    ua = read_json(file_name)
    for elem in ua:
        activities_dict[elem['name']] = elem
    return activities_dict


def on_keyrelease(event):

    # get text from entry
    value = event.widget.get()
    value = value.strip().lower()

    # get data from activit_names
    if value == '':
        data = activity_names
    else:
        data = []
        for item in activity_names:
            if value in item.lower():
                data.append(item)

    # update data in listbox
    listbox_update(data)


def listbox_update(data):
    # delete previous data
    listbox.delete(0, 'end')

    # sorting data
    data = sorted(data, key=str.lower)

    # put new data
    for item in data:
        listbox.insert('end', item)


def on_select(event):
    # display element selected on list
    print('(event) previous:', event.widget.get('active'))
    print('(event)  current:', event.widget.get(event.widget.curselection()))
    print('---')


if __name__ == '__main__':
    '''
        Launch GUI for progresson application
    '''
    activities = get_activities()

    activity_names = activities.keys()

    root = tk.Tk()

    entry = tk.Entry(root)
    entry.pack()
    entry.bind('<KeyRelease>', on_keyrelease)

    listbox = tk.Listbox(root)
    listbox.pack()
    #listbox.bind('<Double-Button-1>', on_select)
    listbox.bind('<<ListboxSelect>>', on_select)
    listbox_update(activity_names)

    root.mainloop()

    # https://stackoverflow.com/questions/47839813/python-tkinter-autocomplete-combobox-with-like-search

    print("Hello")

    # root = Tk()
    # app = App(root)
    # root.mainloop()
