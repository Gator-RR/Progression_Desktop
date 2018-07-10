import json
import os
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont
from tkinter import StringVar


class ProgressionDesktop(tk.Tk):

    def __init__(self, *args, **kwargs):
        # Get activities ready
        # TODO: Consider putting these all in a single shared_data dict
        self.activities = self.get_activities()
        self.activity_names = self.activities.keys()
        self.new_activities = []

        # GUI stuff
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(
            family='Helvetica', size=18, weight='bold')

        # the container is where we'll stat a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (ExercisePage, DetailsPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame('ExercisePage')

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]

        # TODO: I hate this
        if page_name == 'DetailsPage':
            frame.update_entry()

        frame.tkraise()

    def get_activities(self):
        file_name = 'Progression\\ma.json'

        ma = self.read_json(file_name)
        activities_dict = {}
        for elem in ma:
            activities_dict[elem['name']] = elem

        file_name = 'Progression\\ua.json'
        ua = self.read_json(file_name)
        for elem in ua:
            activities_dict[elem['name']] = elem
        return activities_dict

    def read_json(self, file_name):
        # TODO: Verify this is even the one I think I am calling
        CWD = os.path.abspath('.')
        input_file = os.path.join(CWD, file_name)
        with open(input_file, 'r') as fid:
            data = json.load(fid)
        return data

    def write_json(self, data):
        # TODO: Figure out how to append rather than re-write, will be much faster
        # TODO: to use Unicode https://stackoverflow.com/questions/31306887/make-json-dumps-output-unicode-characters-properly-in-python
        with open('Progression\\up.json', 'w') as outputfile:
            json.dump(data, outputfile)

    def add_day(self):
        up = self.read_json('Progression\\up.json')
        quad_guy = [prog for prog in up if prog['name'] == 'Quad Guy']
        day = quad_guy[0]['days'][-1].copy()
        day['index'] += 1
        day['name'] = self.frames['DetailsPage'].entry_name.get()
        day['activities'] = self.set_activity_parameters()
        quad_guy[0]['days'].append(day)
        self.write_json(up)

        self.destroy()

    def set_activity_parameters(self):
        frame = self.frames['DetailsPage']
        parameter = {
            'allOut': False,
            'index': 0,
            'mark': 0,
            'maxReps': 0,
            'minReps': 0
        }

        for target in range(0, len(frame.entry_list)):
            parameters = []
            set_rep_note = frame.entry_list[target].get().split('#')
            set_rep = set_rep_note[0].split()
            for i in range(0, len(set_rep)):
                parameters.append(parameter.copy())
                parameters[-1]['maxReps'] = int(set_rep[i])
                parameters[-1]['minReps'] = int(set_rep[i])
                parameters[-1]['index'] = i

            self.new_activities[target]['performanceTarget']['parameters'] = parameters
            if len(set_rep_note) > 1:
                note = set_rep_note[1]
                self.new_activities[target]['performanceTarget']['note'] = note

        return self.new_activities


class ExercisePage(tk.Frame):

    def __init__(self, parent, controller):

        # Layout GUI
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text='Add Excercises',
                         font=controller.title_font)
        label.pack(side='top', fill='x', pady=10)

        entry = tk.Entry(self)
        entry.pack()
        entry.bind('<KeyRelease>', self.on_keyrelease)

        self.entry_listbox = tk.Listbox(self)
        # TODO: Add enter to trigger same function
        self.entry_listbox.pack()
        # TODO: Global functions, should be moved to.. some class
        self.entry_listbox.bind('<Double-Button-1>', self.on_select)
        self.listbox_update(self.controller.activity_names)

        self.selected_listbox = tk.Listbox(self)
        self.selected_listbox.pack(side='right')
        self.selected_listbox.bind('<Double-Button-1>', self.on_deselect)

        button1 = tk.Button(self, text='Finish',
                            command=lambda: controller.show_frame('DetailsPage'))
        button1.pack()

    def on_keyrelease(self, event):

        # get text from entry
        value = event.widget.get()
        value = value.strip().lower()

        # get data from activity_names
        if value == '':
            data = self.controller.activity_names
        else:
            data = []
            for item in self.controller.activity_names:
                if value in item.lower():
                    data.append(item)

        # update data in listbox
        # TODO: This is grabbing the wrong widget... needs to update listbox
        self.listbox_update(data)

    def on_select(self, event):
        # display element selected on list
        print('(event) previous:', event.widget.get('active'))
        print('(event)  current:', event.widget.get(
            event.widget.curselection()))
        name = event.widget.get(event.widget.curselection())
        print('---')
        self.controller.new_activities.append(self.controller.activities[name])
        self.selected_listbox_update()

    def listbox_update(self, data):
        # delete previous data
        self.entry_listbox.delete(0, 'end')

        # sorting data
        data = sorted(data, key=str.lower)

        # put new data
        for item in data:
            self.entry_listbox.insert('end', item)

    def on_deselect(self, event):
        # display element selected on list
        print('(event) previous:', event.widget.get('active'))
        print('(event)  current:', event.widget.get(
            event.widget.curselection()))
        name = event.widget.get(event.widget.curselection())
        print('---')
        # TODO: Review this
        self.controller.new_activities[:] = [
            activity for activity in self.controller.new_activities if not activity['name'] == name]
        self.selected_listbox_update()

    def selected_listbox_update(self):
        # delete previous data
        self.selected_listbox.delete(0, 'end')

        # put new data
        for item in self.controller.new_activities:
            self.selected_listbox.insert('end', item['name'])


class DetailsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.entry_list = []
        label = tk.Label(self, text='Enter Details',
                         font=controller.title_font)
        label.pack(side='top', fill='x', pady=10)

        self.entry_name = tk.Entry(
            self, text='Name', font=controller.title_font)
        self.entry_name.insert(tk.END, 'name')
        self.entry_name.pack(side='top', fill='x', pady=10)

        self.update_entry()

        button_back = tk.Button(self, text='Back',
                                command=lambda: controller.show_frame('ExercisePage'))
        button_back.pack()

        # TODO: this should close the window
        button_finish = tk.Button(
            self, text='Write', command=lambda: controller.add_day())
        button_finish.pack()

    def update_entry(self):
        for activity in self.controller.new_activities:
            self.entry_list.append(tk.Entry(self))
            self.entry_list[-1].insert(tk.END, activity['name'])
            self.entry_list[-1].pack(side='top', fill='x', pady=10)


if __name__ == '__main__':
    '''
        Launch GUI for progresson application
    '''

    app = ProgressionDesktop()
    app.mainloop()
