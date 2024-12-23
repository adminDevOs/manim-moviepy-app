from tkinter import filedialog, messagebox
from threading import Thread
from moviepy.editor import TextClip, CompositeVideoClip, ColorClip

def calculate_duration(text):
    chars_per_second = 5  # Réduction du nombre de caractères par seconde pour ralentir la lecture
    num_chars = len(text)
    estimated_seconds = num_chars / chars_per_second
    return max(5, min(estimated_seconds, 120))  # Durée entre 5 secondes et 120 secondes

def create_moviepy_video(app, progress_var, progress_bar):
    try:
        if not app.text_content.get():
            raise ValueError("Veuillez d'abord sélectionner du texte extrait.")
        
        # Demander un fichier de sortie avec différents formats possibles
        file_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[
            ("MP4 files", "*.mp4"),
            ("AVI files", "*.avi"),
            ("GIF files", "*.gif")
        ])
        if not file_path:
            raise ValueError("Aucun chemin de sortie spécifié.")

        def render_video():
            try:
                background = ColorClip(size=(640, 480), color=(255, 255, 255))
                duration = calculate_duration(app.text_content.get())
                text_clip = TextClip(
                    app.text_content.get(),
                    fontsize=30,
                    color='black',
                    method='caption',
                    size=(640, 480)
                ).set_duration(duration)
                final_clip = CompositeVideoClip([background, text_clip.set_position('center')])

                # Déterminer le format de sortie en fonction de l'extension de fichier
                file_extension = file_path.split('.')[-1]
                if file_extension.lower() == 'mp4':
                    final_clip.write_videofile(file_path, fps=24, logger=None, threads=1)
                elif file_extension.lower() == 'avi':
                    final_clip.write_videofile(file_path, codec='png', fps=24, logger=None, threads=1)
                elif file_extension.lower() == 'gif':
                    final_clip.write_gif(file_path, fps=24)

                messagebox.showinfo("Succès", f"La vidéo a été créée avec succès à : {file_path}")
            except Exception as e:
                messagebox.showerror("Erreur", f"Une erreur est survenue avec MoviePy : {str(e)}")

        thread = Thread(target=render_video)
        thread.start()

    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur est survenue avec MoviePy : {str(e)}")
