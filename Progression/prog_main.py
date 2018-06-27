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


# class App:

#     value_of_combo = 'X'

#     def __init__(self, parent):
#         self.parent = parent
#         self.combo()

#     def combo(self):
#         self.box_value = StringVar()
#         self.box = ttk.Combobox(self.parent, textvariable=self.box_value)
#         self.box['values'] = ('X', 'Y', 'Z')
#         self.box.current(0)
#         self.box.grid(column=0, row=0)


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
    name = event.widget.get(event.widget.curselection())
    print('---')
    newActivities.append(activities[name])


def add_day():
    up = read_json('Progression\\up.json')
    quad_guy = [prog for prog in up if prog['name'] == 'Quad Guy']
    day = quad_guy[0]['days'][-1]
    day['index'] += 1
    # TODO:
    day['name'] = "FIGURE OUT HOW TO GET THIS FROM UI"
    day['activities'] = newActivities
    quad_guy[0]['days'].append(day)

    print('Hello')


if __name__ == '__main__':
    '''
        Launch GUI for progresson application
    '''
    # # Get all activities
    # activities = get_activities()

    # activity_names = activities.keys()
    # newActivities = []

    # # Created GUI

    # # https://stackoverflow.com/questions/47839813/python-tkinter-autocomplete-combobox-with-like-search
    # root = tk.Tk()

    # entry = tk.Entry(root)
    # entry.pack()
    # entry.bind('<KeyRelease>', on_keyrelease)

    # listbox = tk.Listbox(root)
    # listbox.pack()
    # #listbox.bind('<Double-Button-1>', on_select)
    # listbox.bind('<<ListboxSelect>>', on_select)
    # listbox_update(activity_names)

    # root.mainloop()

    newActivities = [{'@type': 'MuscleActivity', 'custom': False, 'id': '26', 'instructions': 'Stand in a cable machine with one handle in each hand. The handles should be at knee height while hanging freely. Begin to pull them together and up as if you were hugging a tree with them. You should end up with the handles in front of you at chest level. Then finish the movement by letting them back out to your sides until your arms form two "L"s.', 'name': 'Cable Crossover (with Low Angle)', 'performanceTarget': {'groupIndex': -1, 'parameters': [{'allOut': False, 'index': 0, 'mark': 0, 'maxReps': 0, 'minReps': 0}, {'allOut': False, 'index': 1, 'mark': 0, 'maxReps': 0, 'minReps': 0}, {'allOut': False, 'index': 2, 'mark': 0, 'maxReps': 0, 'minReps': 0}, {'allOut': False, 'index': 3, 'mark': 0, 'maxReps': 0, 'minReps': 0}], 'restPerSet': 0}, 'equipment': 6, 'mainTargetMuscle': 5, 'type': 0}, {'@type': 'MuscleActivity', 'custom': False, 'id': '186', 'instructions': 'Place a box at your side and explode through your heels and jump up on it.', 'name': 'Lateral Box Jump', 'performanceTarget': {'groupIndex': -1, 'parameters': [{'allOut': False, 'index': 0, 'mark': 0, 'maxReps': 0, 'minReps': 0}, {'allOut': False, 'index': 1, 'mark': 0, 'maxReps': 0, 'minReps': 0}, {'allOut': False, 'index': 2, 'mark': 0, 'maxReps': 0, 'minReps': 0}, {'allOut': False, 'index': 3, 'mark': 0, 'maxReps': 0, 'minReps': 0}], 'restPerSet': 0}, 'equipment': 3, 'mainTargetMuscle': 6, 'secondaryTargetMuscles': [4], 'type': 0}, {
        '@type': 'MuscleActivity', 'custom': False, 'id': '118', 'instructions': 'Adjust the machine so that your legs fit comfortably under the rack. Grab the bar and sit down with your legs under the rack. With a slight arch in your lower back begin pulling down towards your upper chest. After touching your chest with the bar, slowly return it until your arms and lats are fully stretched.', 'name': 'Machine Lat Pulldown', 'performanceTarget': {'groupIndex': -1, 'parameters': [{'allOut': False, 'index': 0, 'mark': 0, 'maxReps': 0, 'minReps': 0}, {'allOut': False, 'index': 1, 'mark': 0, 'maxReps': 0, 'minReps': 0}, {'allOut': False, 'index': 2, 'mark': 0, 'maxReps': 0, 'minReps': 0}, {'allOut': False, 'index': 3, 'mark': 0, 'maxReps': 0, 'minReps': 0}], 'restPerSet': 0}, 'equipment': 4, 'mainTargetMuscle': 2, 'secondaryTargetMuscles': [3], 'type': 0}, {'@type': 'MuscleActivity', 'custom': False, 'id': '128', 'instructions': 'Sit in a pulldown machine but rather than pulling towards your upper chest, pull the bar towards your neck. Stopping just before it touches it.', 'name': 'Machine Lat Pulldown (Behind the Neck)', 'performanceTarget': {'groupIndex': -1, 'parameters': [{'allOut': False, 'index': 0, 'mark': 0, 'maxReps': 0, 'minReps': 0}, {'allOut': False, 'index': 1, 'mark': 0, 'maxReps': 0, 'minReps': 0}, {'allOut': False, 'index': 2, 'mark': 0, 'maxReps': 0, 'minReps': 0}, {'allOut': False, 'index': 3, 'mark': 0, 'maxReps': 0, 'minReps': 0}], 'restPerSet': 0}, 'equipment': 4, 'mainTargetMuscle': 2, 'secondaryTargetMuscles': [3], 'type': 0}]

    # Add selected items to day

    add_day()

    print("Hello")

    # root = Tk()
    # app = App(root)
    # root.mainloop()
