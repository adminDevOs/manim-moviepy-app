import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from pdf_handler import load_pdf_thread, select_pdf
from animation_handler import preview_manim_animation, create_manim_animation
from video_handler import create_moviepy_video

# Définir la variable d'environnement pour ImageMagick
os.environ["IMAGEMAGICK_BINARY"] = r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"

def create_main_window():
    app = tk.Tk()
    app.title("Animation & Vidéo avec Manim et MoviePy")
    app.geometry("1000x900")

    app.pdf_path = tk.StringVar()
    app.text_content = tk.StringVar()

    tk.Label(app, text="Aucun fichier PDF sélectionné").pack()
    tk.Button(app, text="Sélectionner un PDF", command=lambda: select_pdf(app)).pack()

    tk.Label(app, text="Numéro de la page que vous souhaitez extraire :").pack()
    page_var = tk.StringVar()
    tk.Entry(app, textvariable=page_var).pack()

    # Créer la boîte de texte pour afficher le contenu PDF extrait
    pdf_text_box = tk.Text(app, wrap=tk.WORD, height=20, width=100)
    pdf_text_box.pack()

    tk.Button(app, text="Charger la page sélectionnée", command=lambda: load_pdf_thread(app, page_var, pdf_text_box)).pack()

    tk.Button(app, text="Prévisualiser l'Animation avec Manim", command=lambda: preview_manim_animation(app)).pack()
    tk.Button(app, text="Créer une Animation avec Manim", command=lambda: create_manim_animation(app)).pack()

    progress_var = tk.DoubleVar()
    progress_bar = ttk.Progressbar(app, variable=progress_var, maximum=100)
    progress_bar.pack(fill=tk.X, padx=10, pady=10)

    tk.Button(app, text="Créer une Vidéo avec MoviePy", command=lambda: create_moviepy_video(app, progress_var, progress_bar)).pack()

    # Ajouter un bouton pour capturer le texte sélectionné
    def capture_selected_text():
        try:
            selected_text = pdf_text_box.get("sel.first", "sel.last")
            if not selected_text:
                raise ValueError("Aucun texte sélectionné.")
            app.text_content.set(selected_text)
            messagebox.showinfo("Texte Sélectionné", f"Texte sélectionné : {selected_text}")
        except tk.TclError:
            messagebox.showerror("Erreur", "Veuillez sélectionner du texte avant de capturer.")
        except ValueError as e:
            messagebox.showerror("Erreur", str(e))

    tk.Button(app, text="Capturer le Texte Sélectionné", command=capture_selected_text).pack()

    app.mainloop()

if __name__ == "__main__":
    create_main_window()
