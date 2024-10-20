import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog
from tkinter import simpledialog
from tkinter import scrolledtext


def extract_pages_with_word(pdf_path, search_word):
    # Open the PDF file
    doc = fitz.open(pdf_path)
    found_pages = []

    # Iterate through pages
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text = page.get_text("text")

        # Search for the word in the page's text
        if search_word.lower() in text.lower():
            found_pages.append(page_num + 1)  # Page numbers start at 1

    doc.close()
    return found_pages


def select_pdf_and_search_word():
    # Open a file dialog to select the PDF file
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

    # If a file was selected, proceed to search for the word
    if pdf_path:
        search_word = simpledialog.askstring("Input", "Enter the word you are searching for:")
        if search_word:
            pages = extract_pages_with_word(pdf_path, search_word)
            if pages:
                result_text = f"The PDF file '{pdf_path}' contains the word '{search_word}'.\n"
                result_text += f"The word '{search_word}' was found on pages: {pages}"
            else:
                result_text = f"The PDF file '{pdf_path}' does not contain the word '{search_word}'."

            # Display the result in the scrolled text widget
            output_text.delete(1.0, tk.END)
            output_text.insert(tk.END, result_text)


# Create the main window
root = tk.Tk()
root.title("PDF Word Search")

# Create a button to open the file dialog and search for the word
search_button = tk.Button(root, text="Select PDF and Search for Word", command=select_pdf_and_search_word)
search_button.pack(pady=20)

# Create a scrolled text widget to display the output
output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20)
output_text.pack(pady=20)

# Run the application
root.mainloop()
