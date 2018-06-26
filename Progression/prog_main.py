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
    name = event.widget.get(event.widget.curselection())
    print('---')
    newActivities[name] = activities[name]


def add_day():
    up = read_json('Progression\\up.json')
    quad_guy = [prog for prog in up if prog['name'] == 'Quad Guy']
    day = quad_guy[0]['days'][-1]
    day['index'] += 1
    # TODO:
    day['name'] = "FIGURE OUT HOW TO GET THIS FROM UI"
    # TODO: Need to perserve order somehow, if it becomes an issue
    day['activities'] = newActivities.values()

    print('Hello')

if __name__ == '__main__':
    '''
        Launch GUI for progresson application
    '''
    # # Get all activities
    # activities = get_activities()

    # activity_names = activities.keys()
    # newActivities = {}

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

    newActivities = {'Alternating Dumbbell Curl': {'@type': 'MuscleActivity', 'custom': False, 'id': '31', 'name': 'Alternating Dumbbell Curl', 'performance': {'completedSets': [{'completedAt': 1459789094279, 'duration': 0, 'mark': 0, 'reps': 10, 'weight': 9.071848}, {'completedAt': 1459789200426, 'duration': 0, 'mark': 0, 'reps': 10, 'weight': 9.071848}, {'completedAt': 1459789327807, 'duration': 0, 'mark': 0, 'reps': 10, 'weight': 9.071848}]}, 'performanceTarget': {'groupIndex': -1, 'note': '', 'parameters': [{'allOut': False, 'index': 0, 'mark': 0, 'maxReps': 12, 'minReps': 10}, {'allOut': False, 'index': 1, 'mark': 0, 'maxReps': 12, 'minReps': 10}, {'allOut': True, 'index': 2, 'mark': 0, 'maxReps': 12, 'minReps': 10}], 'restPerSet': 60000}, 'equipment': 2, 'mainTargetMuscle': 3, 'type': 0}, 'Barbell Bench Press': {'@type': 'MuscleActivity', 'custom': False, 'id': '7', 'instructions': "Lie down on a flat bench under a barbell. Preferably in a rack, for your own safety. Begin the movement by unracking the barbell and lowering it towards your chest, once it hits the chest, push it back up. Consider using a spotter if you're lifting heavy weights.", 'name': 'Barbell Bench Press', 'performance': {'completedSets': [{'completedAt': 1457371273644, 'duration': 0, 'mark': 0, 'reps': 12, 'weight': 61.234974}, {'completedAt': 1457371443285, 'duration': 0, 'mark': 0, 'reps': 12, 'weight': 61.234974}, {'completedAt': 1457371703262, 'duration': 0, 'mark': 0, 'reps': 12, 'weight': 61.234974}]}, 'performanceTarget': {'groupIndex': -1, 'parameters': [{'allOut': False, 'index': 0, 'mark': 0, 'maxReps': 15, 'minReps': 12}, {'allOut': False, 'index': 1, 'mark': 0, 'maxReps': 15, 'minReps': 12}, {'allOut': False, 'index': 2, 'mark': 0, 'maxReps': 15, 'minReps': 12}], 'restPerSet': 0}, 'equipment': 1, 'mainTargetMuscle': 5, 'secondaryTargetMuscles': [7, 8], 'type': 0}, 'Barbell Concentration Curl': {'@type': 'MuscleActivity', 'custom': False, 'id': '47', 'name': 'Barbell Concentration Curl', 'performance': {'completedSets': [{'completedAt': 1479245617790, 'duration': 0, 'mark': 0, 'reps': 11, 'weight': 24.947582}, {'completedAt': 1479245620213, 'duration': 0, 'mark': 0, 'reps': 11, 'weight': 24.947582}, {'completedAt': 1479245804938, 'duration': 0, 'mark': 0, 'reps': 11, 'weight': 24.947582}]}, 'performanceTarget': {'groupIndex': -1, 'note': 'Seated barbell curl', 'parameters': [{'allOut': False, 'index': 0, 'mark': 0, 'maxReps': 0, 'minReps': 0}, {'allOut': False, 'index': 1, 'mark': 0, 'maxReps': 0, 'minReps': 0}, {'allOut': False, 'index': 2, 'mark': 0, 'maxReps': 0, 'minReps': 0}], 'restPerSet': 0}, 'equipment': 1, 'mainTargetMuscle': 3, 'type': 0}}

    # Add selected items to day

    add_day()

    print("Hello")

    # root = Tk()
    # app = App(root)
    # root.mainloop()
