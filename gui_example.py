from tkinter import *  # Standard Binding to tk (tk interface)
from tkinter import ttk  # Binding to newer "themed widgets"
from tkinter import messagebox


def design_window():
'''
sets up the design window
'''
    def ok_button():
        message_out = "You have entered {} with blood type {}{}. \n" \
                      "Is this information correct?" \
            .format(donor_name.get(), blood_letter.get(), rh_factor.get())
        response = messagebox.askyesno(message=message_out, icon="question")
        if response is False:
            return
        print("Donor Name: {}".format(donor_name.get()))
        print("Blood letter: {}".format(blood_letter.get()))
        print("Rh factor: {}".format(rh_factor.get()))
        donor_name.set("")
        blood_letter.set("")
        rh_factor.set("-")
        #         do_other_stuff()
        return

    def cancel_button():
        root.destroy()
        return

    def checkbox_change():
        if rh_factor.get() == '+':
            rh_check["text"] = "Rh factor - Selected"
        elif rh_factor.get() == "-":
            rh_check["text"] = "Rh factor - Not Selected"

    root = Tk()  # Sets up the main window
    root.title("Blood Donor Database")
    root.columnconfigure(0, pad=5)
    root.columnconfigure(1, pad=5)
    root.columnconfigure(2, pad=5)
    #     root.rowconfigure(4, pad =10)
    #     root.rowconfigure(3, pad = 10)

    # Add Blood Donor Database Label
    top_label = ttk.Label(root, text="Blood Donor Database")
    top_label.grid(column=0, row=0, columnspan=2, sticky=W)

    # Add name label and entry
    name_label = ttk.Label(root, text="Name: ")
    name_label.grid(column=0, row=1)
    donor_name = StringVar()
    #     donor_name.set("Enter name here")
    name_entry = ttk.Entry(root, textvariable=donor_name, width=40)
    name_entry.grid(column=1, row=1, padx=5)

    # Add Radiobuttons
    blood_letter = StringVar()
    ttk.Radiobutton(root, text='A', variable=blood_letter,
                    value='A').grid(column=0, row=2, sticky=W)
    ttk.Radiobutton(root, text='B', variable=blood_letter,
                    value='B').grid(column=0, row=3, sticky=W)
    ttk.Radiobutton(root, text='AB', variable=blood_letter,
                    value='AB').grid(column=0, row=4, sticky=W)
    ttk.Radiobutton(root, text='O', variable=blood_letter,
                    value='O').grid(column=0, row=5, sticky=W)

    # Add Rh Factor Checkbox
    rh_factor = StringVar()
    rh_factor.set('-')
    rh_check = ttk.Checkbutton(root, text="Rh Positive", variable=rh_factor,
                               onvalue='+', offvalue='-',
                               command=checkbox_change)
    rh_check.grid(column=1, row=3)

    # Add buttons
    ok_btn = ttk.Button(root, text="ok", command=ok_button)
    ok_btn.grid(column=1, row=5)
    cancel_btn = ttk.Button(root, text="cancel", command=cancel_button)
    cancel_btn.grid(column=2, row=5)

    # Add Donation Center Dropdown
    ttk.Label(root, text="Nearest Donor Center").grid(column=2, row=0)
    donor_center = StringVar()
    donor_center_combo = ttk.Combobox(root, textvariable=donor_center)
    donor_center_combo.grid(column=2, row=1, padx=5)
    donor_center_combo['values'] = ("Durham", "Raleigh", "Cary", "Apex")
    donor_center_combo.state(['readonly'])

    root.mainloop()
    return


# def do_other_stuff():
#     print("This function will do lots of things")


if __name__ == '__main__':
    design_window()