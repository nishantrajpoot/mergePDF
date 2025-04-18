import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2

def merge_pdfs(pdf_list, output_path):
    pdf_writer = PyPDF2.PdfWriter()

    for pdf in pdf_list:
        pdf_reader = PyPDF2.PdfReader(pdf)
        for page in range(len(pdf_reader.pages)):
            pdf_writer.add_page(pdf_reader.pages[page])

    with open(output_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

def select_files():
    files = filedialog.askopenfilenames(
        title="Select PDF files",
        filetypes=[("PDF files", "*.pdf")],
        defaultextension=".pdf"
    )
    if files:
        file_list.delete(0, tk.END)
        for file in files:
            file_list.insert(tk.END, file)

def clear_selection():
    file_list.delete(0, tk.END)

def merge_and_save():
    pdf_files = file_list.get(0, tk.END)
    if not pdf_files:
        messagebox.showwarning("No Files", "Please select PDF files to merge.")
        return

    output_file = filedialog.asksaveasfilename(
        title="Save Merged PDF",
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")]
    )
    if output_file:
        try:
            merge_pdfs(pdf_files, output_file)
            messagebox.showinfo("Success", f"Merged PDF saved as {output_file}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Set up the main application window
root = tk.Tk()
root.title("PDF Merger")

# Create and place widgets
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

select_button = tk.Button(frame, text="Select PDF Files", command=select_files)
select_button.pack(fill=tk.X)

clear_button = tk.Button(frame, text="Clear Selection", command=clear_selection)
clear_button.pack(fill=tk.X, pady=5)

file_list = tk.Listbox(frame, selectmode=tk.MULTIPLE, width=50, height=10)
file_list.pack(pady=5)

merge_button = tk.Button(frame, text="Merge and Save", command=merge_and_save)
merge_button.pack(fill=tk.X)

# Start the application
root.mainloop()
