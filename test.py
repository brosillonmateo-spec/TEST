import tkinter as tk

# Création de la fenêtre
fenetre = tk.Tk()
fenetre.title("Bonjour")
fenetre.geometry("300x150")

# Texte affiché
label = tk.Label(fenetre, text="Bonjour", font=("Arial", 20))
label.pack(expand=True)

# Boucle principale
fenetre.mainloop()