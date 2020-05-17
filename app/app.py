from scholarly import search_author
from tkinter import *


class Application(Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.pack()

        self.header_frame = Frame(self, bg="red", height=100, width=950)
        self.body_frame = Frame(self, bg="blue", height=600-self.header_frame.winfo_height(), width=950)

        self.first_person_frame = Frame(self.header_frame)

        self.first_person_label = Label(self.first_person_frame, text="Введите первого автора!")
        self.first_person_label.pack(expand=True, fill=BOTH)

        self.first_person_entry = Entry(self.first_person_frame)
        self.first_person_entry.pack(expand=True, fill=BOTH)

        self.first_person_frame.pack(side=LEFT, expand=True, fill=BOTH)

        self.buttons_frame = Frame(self.header_frame)

        self.find_button = Button(
            self.buttons_frame,
            text="Find",
            command=self.find
        )
        self.find_button.pack(expand=True, fill=BOTH)

        self.start_button = Button(self.buttons_frame, text="Start", command=self.start)
        self.start_button.pack(expand=True, fill=BOTH)

        self.buttons_frame.pack(side=LEFT, expand=True, fill=BOTH)

        self.second_person_frame = Frame(self.header_frame)

        self.second_person_label = Label(self.second_person_frame, text="Введите второго автора!")
        self.second_person_label.pack(expand=True, fill=BOTH)

        self.second_person_entry = Entry(self.second_person_frame)
        self.second_person_entry.pack(expand=True, fill=BOTH)

        self.second_person_frame.pack(side=LEFT, expand=True, fill=BOTH)

        self.header_frame.pack(expand=True, fill=BOTH)
        self.body_frame.pack(expand=True, fill=BOTH)

    def find(self):
        first_person_name = self.first_person_entry.get()
        first_authors = [e for e in search_author(first_person_name)]
        first_authors_names_and_universities = [f"{e.name} | {e.affiliation}" for e in first_authors]

        second_person_name = self.second_person_entry.get()
        second_authors = [e for e in search_author(second_person_name)]
        second_authors_names_and_universities = [f"{e.name} | {e.affiliation}" for e in second_authors]

        if len(first_authors) > 1 and len(second_authors) > 1:
            text_v_1 = StringVar(value="Выберите автора!")
            text_v_2 = StringVar(value="Выберите автора!")
            self.first_person_select = OptionMenu(
                self.first_person_frame,
                text_v_1,
                *first_authors_names_and_universities,
                command=self.first_select_event
            )
            self.first_person_select.pack(expand=True, fill=BOTH)

            self.second_person_select = OptionMenu(
                self.second_person_frame,
                text_v_2,
                *second_authors_names_and_universities,
                command=self.second_select_event
            )
            self.second_person_select.pack(expand=True, fill=BOTH)

        else:
            self.first_person_entry.delete(0, END)
            self.first_person_entry.insert(END, first_authors[0])

            self.second_person_entry.delete(0, END)
            self.second_person_entry.insert(END, second_authors[0])

    def first_select_event(self, value):
        print(value)
        self.first_person_entry.delete(0, END)
        self.first_person_entry.insert(END, value)
        self.first_person_select.destroy()

    def second_select_event(self, value):
        print(value)
        self.second_person_entry.delete(0, END)
        self.second_person_entry.insert(END, value)
        self.second_person_select.destroy()

    def start(self):
        print("Start!")


root = Tk()
root.geometry("950x600")
root.resizable(height=False, width=False)
app = Application(root)
app.mainloop()
