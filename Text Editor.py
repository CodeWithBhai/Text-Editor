import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def Open_file():
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not filepath:
        return

    txt_edit.delete(1.0, tk.END)
    with open(filepath, "r") as input_file:
        text = input_file.read()
        txt_edit.insert(tk.END, text)
    window.title(f"Text Editor-{filepath}")

    # for save files


def Save_file():
    filepath = asksaveasfilename(
        defaultextension="txt", filetype=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if not filepath:
        return

    with open(filepath, "w") as output_file:
        text = txt_edit.get(1.0, tk.END)
        output_file.write(text)
    window.title(f"Text Editor-{filepath}")


window = tk.Tk()
window.title("Text Editor")
#window.geometry("600x600")

window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

txt_edit = tk.Text(window)
fr_button = tk.Frame(window, relief=tk.RAISED, bd=2)
btn_open = tk.Button(fr_button, text="Open", command=Open_file)

btn_save = tk.Button(fr_button, text="Save As..", command=Save_file)
btn_open.grid(row=0, column=0, sticky="ew", padx=2, pady=2)
btn_save.grid(row=1, column=0, sticky="ew", padx=2)

fr_button.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()
