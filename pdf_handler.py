import os
import tkinter as tk
from tkinter import filedialog, messagebox
from threading import Thread
from PyPDF2 import PdfReader

def load_pdf_thread(app, page_var, pdf_text_box):
    def worker():
        try:
            file_path = app.pdf_path.get()
            if not file_path:
                messagebox.showerror("Erreur", "Aucun chemin de fichier sélectionné.")
                return

            if not os.path.isfile(file_path):
                messagebox.showerror("Erreur", "Le chemin spécifié n'existe pas.")
                return

            with open(file_path, 'rb') as file:
                reader = PdfReader(file)
                selected_page = int(page_var.get()) - 1
                if 0 <= selected_page < len(reader.pages):
                    text_content = reader.pages[selected_page].extract_text()
                    if text_content:
                        pdf_text_box.delete('1.0', tk.END)  # Effacer la boîte
                        pdf_text_box.insert(tk.END, text_content)  # Afficher le contenu dans la boîte
                        messagebox.showinfo("PDF chargé", f"Contenu de la page {selected_page + 1} chargé.")
                    else:
                        messagebox.showerror("Erreur", "Aucun contenu texte trouvé dans la page.")
                else:
                    messagebox.showerror("Erreur", f"Numéro de page {selected_page + 1} hors limites.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Une erreur est survenue : {str(e)}")

    thread = Thread(target=worker)
    thread.start()

def select_pdf(app):
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        app.pdf_path.set(file_path)
        messagebox.showinfo("Fichier sélectionné", f"Fichier sélectionné : {file_path}")
    else:
        messagebox.showerror("Erreur", "Aucun fichier sélectionné.")
