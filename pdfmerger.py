import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import PyPDF2

# Create the GUI window
window = tk.Tk()
window.title("PDF Merger")
window.geometry("750x300")  # Set the window size

# Define the merge function
def merge():
  # Open the file selection dialog for the first PDF
  filepath1 = filedialog.askopenfilename()
  if not filepath1:
    return

  # Open the file selection dialog for the second PDF
  filepath2 = filedialog.askopenfilename()
  if not filepath2:
    return
  
  # Open the PDFs
  pdf1 = open(filepath1, 'rb')
  pdf2 = open(filepath2, 'rb')
  pdf_reader1 = PyPDF2.PdfFileReader(pdf1)
  pdf_reader2 = PyPDF2.PdfFileReader(pdf2)
  
  # Create a new PDF
  pdf_writer = PyPDF2.PdfFileWriter()
  
  # Add the pages of the first PDF
  for page in range(pdf_reader1.getNumPages()):
    pdf_writer.addPage(pdf_reader1.getPage(page))
  
  # Add the pages of the second PDF
  for page in range(pdf_reader2.getNumPages()):
    pdf_writer.addPage(pdf_reader2.getPage(page))
  
  # Save the merged PDF
  output_filepath = filedialog.asksaveasfilename(defaultextension='.pdf')
  if not output_filepath:
    return
  with open(output_filepath, 'wb') as output_file:
    pdf_writer.write(output_file)
  
  # Close the input PDFs
  pdf1.close()
  pdf2.close()
  
  # Show a success message
  messagebox.showinfo("PDF Merger", "PDFs merged successfully! You can find the updated version where you chose to save the file")

# Create the "Merge" button
button = tk.Button(text="Merge", command=merge, font=("Arial", 20), bg='#3cba54', fg='#ffffff', activeforeground='#ffffff', activebackground='#2d9348', relief=tk.FLAT, bd=0, highlightthickness=0, pady=25, padx=35)
button.pack(pady=10)

# Add instructions
instructions = tk.Label(text="1. Select the first file with the first pop up and the second one with the second pop up\n2. Select where you want to put the merged file and name it using the third pop up", font=("Arial", 12))
instructions.pack()

# Run the GUI loop
window.mainloop()



