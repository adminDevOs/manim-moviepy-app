import tkinter as tk
from tkinter import messagebox
from manim import *

def preview_manim_animation(app):
    try:
        text_content = app.text_content.get()
        if not text_content:
            raise ValueError("Aucun texte sélectionné pour l'animation.")

        print(f"Texte pour la prévisualisation : {text_content}")  # Débogage

        class PreviewScene(Scene):
            def construct(self):
                text = Text(text_content, font_size=48)
                self.add(text)

        config.preview = True
        scene = PreviewScene()
        scene.render()
        messagebox.showinfo("Prévisualisation", "La prévisualisation est terminée.")
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur est survenue avec Manim : {str(e)}")

def create_manim_animation(app):
    try:
        text_content = app.text_content.get()
        if not text_content:
            raise ValueError("Aucun texte sélectionné pour l'animation.")

        print(f"Texte pour l'animation : {text_content}")  # Débogage

        class ExampleScene(Scene):
            def construct(self):
                text = Text(text_content, font_size=48)
                self.play(Write(text))
                self.wait(2)
                self.play(FadeOut(text))

        scene = ExampleScene()
        scene.render()
        messagebox.showinfo("Succès", "Animation créée avec succès.")
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur est survenue avec Manim : {str(e)}")
