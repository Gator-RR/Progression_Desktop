''' This is more of a place holder, don't know if I will ever
    use it, but I need somewhere to save this data, and I 
    don't want comments cluttering the code.
'''

#   newActivities = [{'@type': 'MuscleActivity', 'custom': False, 'id': '26', 'instructions': 'Stand in a cable machine with one handle in each hand. The handles should be at knee height while hanging freely. Begin to pull them together and up as if you were hugging a tree with them. You should end up with the handles in front of you at chest level. Then finish the movement by letting them back out to your sides until your arms form two "L"s.', 'name': 'Cable Crossover (with Low Angle)', 'performanceTarget': {'groupIndex': -1, 'parameters': [{'allOut': False, 'index': 0, 'mark': 0, 'maxReps': 0, 'minReps': 0}, {'allOut': False, 'index': 1, 'mark': 0, 'maxReps': 0, 'minReps': 0}, {'allOut': False, 'index': 2, 'mark': 0, 'maxReps': 0, 'minReps': 0}, {'allOut': False, 'index': 3, 'mark': 0, 'maxReps': 0, 'minReps': 0}], 'restPerSet': 0}, 'equipment': 6, 'mainTargetMuscle': 5, 'type': 0}, {'@type': 'MuscleActivity', 'custom': False, 'id': '186', 'instructions': 'Place a box at your side and explode through your heels and jump up on it.', 'name': 'Lateral Box Jump', 'performanceTarget': {'groupIndex': -1, 'parameters': [{'allOut': False, 'index': 0, 'mark': 0, 'maxReps': 0, 'minReps': 0}, {'allOut': False, 'index': 1, 'mark': 0, 'maxReps': 0, 'minReps': 0}, {'allOut': False, 'index': 2, 'mark': 0, 'maxReps': 0, 'minReps': 0}, {'allOut': False, 'index': 3, 'mark': 0, 'maxReps': 0, 'minReps': 0}], 'restPerSet': 0}, 'equipment': 3, 'mainTargetMuscle': 6, 'secondaryTargetMuscles': [4], 'type': 0}, {
# '@type': 'MuscleActivity', 'custom': False, 'id': '118', 'instructions': 'Adjust the machine so that your legs fit comfortably under the rack. Grab the bar and sit down with your legs under the rack. With a slight arch in your lower back begin pulling down towards your upper chest. After touching your chest with the bar, slowly return it until your arms and lats are fully stretched.', 'name': 'Machine Lat Pulldown', 'performanceTarget': {'groupIndex': -1, 'parameters': [{'allOut': False, 'index': 0, 'mark': 0, 'maxReps': 0, 'minReps': 0}, {'allOut': False, 'index': 1, 'mark': 0, 'maxReps': 0, 'minReps': 0}, {'allOut': False, 'index': 2, 'mark': 0, 'maxReps': 0, 'minReps': 0}, {'allOut': False, 'index': 3, 'mark': 0, 'maxReps': 0, 'minReps': 0}], 'restPerSet': 0}, 'equipment': 4, 'mainTargetMuscle': 2, 'secondaryTargetMuscles': [3], 'type': 0}, {'@type': 'MuscleActivity', 'custom': False, 'id': '128', 'instructions': 'Sit in a pulldown machine but rather than pulling towards your upper chest, pull the bar towards your neck. Stopping just before it touches it.', 'name': 'Machine Lat Pulldown (Behind the Neck)', 'performanceTarget': {'groupIndex': -1, 'parameters': [{'allOut': False, 'index': 0, 'mark': 0, 'maxReps': 0, 'minReps': 0}, {'allOut': False, 'index': 1, 'mark': 0, 'maxReps': 0, 'minReps': 0}, {'allOut': False, 'index': 2, 'mark': 0, 'maxReps': 0, 'minReps': 0}, {'allOut': False, 'index': 3, 'mark': 0, 'maxReps': 0, 'minReps': 0}], 'restPerSet': 0}, 'equipment': 4, 'mainTargetMuscle': 2, 'secondaryTargetMuscles': [3], 'type': 0}]

# https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne"))
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo"))
        button1.pack()
        button2.pack()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 1", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is page 2", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tk.Button(self, text="Go to the start page",
                           command=lambda: controller.show_frame("StartPage"))
        button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()