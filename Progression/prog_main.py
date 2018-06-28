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
        frame.tkraise()

    def get_activities(self):
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
        # TODO: right now on_keyrelease is global, not sure where I should put it.  Probably in self
        entry.bind('<KeyRelease>', on_keyrelease)

        # TODO: Add enter to trigger same function
        entry_listbox = tk.Listbox(self)
        entry_listbox.pack()
        # TODO: Global functions, should be moved to.. some class
        entry_listbox.bind('<Double-Button-1>', on_select)
        listbox_update(self.controller.activity_names)

        selected_listbox = tk.Listbox(self)
        selected_listbox.pack(side='right')
        selected_listbox.bind('<Double-Button-1>', on_deselect)

        button1 = tk.Button(self, text='Finish',
                            command=lambda: controller.show_frame('DetailsPage'))
        button1.pack()


class DetailsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text='Enter Details',
                         font=controller.title_font)
        label.pack(side='top', fill='x', pady=10)
        # TODO: this should close the window
        button = tk.Button(self, text='Finished',
                           command=lambda: controller.show_frame('ExercisePage'))
        button.pack()


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
    new_activities[:] = [
        activity for activity in new_activities if not activity['name'] == name]
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

    app = ProgressionDesktop()
    app.mainloop()

