import json
import os
import tkinter as tk
from tkinter import ttk
from tkinter import StringVar


def read_json(file_name):
    # TODO: Verify this is even the one I think I am calling
    CWD = os.path.abspath('.')
    input_file = os.path.join(CWD, file_name)
    with open(input_file, 'r') as fid:
        data = json.load(fid)
    return data


def write_json(data):
    with open('data.json', 'w') as outputfile:
        json.dump(data, outputfile)


def get_activities():
    file_name = 'Progression\\ma.json'

    ma = read_json(file_name)
    activities_dict = {}
    for elem in ma:
        activities_dict[elem['name']] = elem

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
    entry_listbox.delete(0, 'end')

    # sorting data
    data = sorted(data, key=str.lower)

    # put new data
    for item in data:
        entry_listbox.insert('end', item)


def selected_listbox_update():
    # delete previous data
    selected_listbox.delete(0, 'end')

    # put new data
    for item in new_activities:
        selected_listbox.insert('end', item['name'])


def on_select(event):
    # display element selected on list
    print('(event) previous:', event.widget.get('active'))
    print('(event)  current:', event.widget.get(event.widget.curselection()))
    name = event.widget.get(event.widget.curselection())
    print('---')
    new_activities.append(activities[name])
    selected_listbox_update()


def on_deselect(event):
    # display element selected on list
    print('(event) previous:', event.widget.get('active'))
    print('(event)  current:', event.widget.get(event.widget.curselection()))
    name = event.widget.get(event.widget.curselection())
    print('---')
    new_activities[:] = [activity for activity in new_activities if not activity['name'] == name]
    selected_listbox_update()


def add_day():
    up = read_json('Progression\\up.json')
    quad_guy = [prog for prog in up if prog['name'] == 'Quad Guy']
    day = quad_guy[0]['days'][-1].copy()
    day['index'] += 1
    # TODO:
    day['name'] = "FIGURE OUT HOW TO GET THIS FROM UI"
    day['activities'] = new_activities
    quad_guy[0]['days'].append(day)
    write_json(up)

    print('Hello')


def request_set_reps():
    mainframe.destroy()

    return


if __name__ == '__main__':
    '''
        Launch GUI for progresson application
    '''
    # Get all activities
    activities = get_activities()

    activity_names = activities.keys()
    # TODO: Figure out the order and crap with this.
    new_activities = []

    # Created GUI

    # https://stackoverflow.com/questions/47839813/python-tkinter-autocomplete-combobox-with-like-search
    root = tk.Tk()
    root.title("Progression Desktop")

    mainframe = ttk.Frame(root, padding="3 3 12 12")
    mainframe.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
    mainframe.columnconfigure(0, weight=1)
    mainframe.rowconfigure(0, weight=1)

    rep_frame = ttk.Frame(root, padding="3 3 12 12")
    rep_frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
    rep_frame.columnconfigure(0, weight=1)
    rep_frame.rowconfigure(0, weight=1)

    entry = tk.Entry(mainframe)
    entry.grid(column=1, row=1)
    entry.bind('<KeyRelease>', on_keyrelease)

    # TODO: Add enter to trigger same functions
    entry_listbox = tk.Listbox(mainframe)
    entry_listbox.grid(column=1, row=2)
    entry_listbox.bind('<Double-Button-1>', on_select)
    # listbox.bind('<<ListboxSelect>>', on_select)
    listbox_update(activity_names)

    selected_listbox = tk.Listbox(mainframe)
    selected_listbox.grid(column=2, row=2)
    selected_listbox.bind('<Double-Button-1>', on_deselect)

    button = ttk.Button(mainframe, text="Finished", command=request_set_reps)
    button.grid(column=1, row=3)

    root.mainloop()

    # Add selected items to day

    add_day()

    print("Hello")
