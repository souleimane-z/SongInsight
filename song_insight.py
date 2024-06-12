import tkinter as tk
from tkinter import filedialog, messagebox
from mutagen import File
import os

def extraire_toutes_metadonnees(fichier):
    audio = File(fichier)
    if audio is None:
        raise ValueError("Format de fichier non pris en charge")

    metadonnees = {}


    for cle, valeur in audio.tags.items():
        if isinstance(valeur, list):
            metadonnees[cle] = ', '.join(map(str, valeur))
        else:
            metadonnees[cle] = str(valeur)


    if audio.info:
        duree_sec = int(audio.info.length)
        heures, reste = divmod(duree_sec, 3600)
        minutes, secondes = divmod(reste, 60)
        metadonnees['Durée'] = f"{heures}:{minutes:02d}:{secondes:02d}"
    else:
        metadonnees['Durée'] = 'Inconnue'

    return metadonnees

def afficher_metadonnees(fichier):
    try:
        metadonnees = extraire_toutes_metadonnees(fichier)
        
        for widget in scrollable_frame.winfo_children():
            widget.destroy()

        # Trier les métadonnées par ordre alphabétique des clés
        metadonnees_tries = dict(sorted(metadonnees.items()))

        for i, (cle, valeur) in enumerate(metadonnees_tries.items()):
            label_cle = tk.Label(scrollable_frame, text=cle, font=('Helvetica', 10, 'bold'), bg='#D3D3D3')
            label_cle.grid(row=i, column=0, sticky='w', padx=5, pady=2)
            label_valeur = tk.Label(scrollable_frame, text=valeur, font=('Helvetica', 10), bg='#D3D3D3')
            label_valeur.grid(row=i, column=1, sticky='w', padx=5, pady=2)
        
        global current_metadata, current_filename
        current_metadata = metadonnees_tries
        current_filename = os.path.splitext(os.path.basename(fichier))[0]
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de la lecture du fichier : {e}")

def ouvrir_fichier():
    fichier = filedialog.askopenfilename(filetypes=[
        ("Fichiers audio", "*.mp3;*.flac;*.m4a;*.mp4;*.ogg;*.wav;*.wv"),
        ("Tous les fichiers", "*.*")
    ])
    if fichier:
        afficher_metadonnees(fichier)

def exporter_metadonnees():
    if current_metadata and current_filename:
        with open(f"{current_filename}_metadata.txt", 'w', encoding='utf-8') as f:
            for cle, valeur in current_metadata.items():
                f.write(f"{cle}: {valeur}\n")
        messagebox.showinfo("Exportation réussie", f"Les métadonnées ont été exportées vers {current_filename}_metadata.txt")
    else:
        messagebox.showwarning("Avertissement", "Aucune métadonnée à exporter")


current_metadata = {}
current_filename = ""


root = tk.Tk()
root.title("SongInsight")
root.configure(bg='#D3D3D3')

frame = tk.Frame(root, bg='#D3D3D3', padx=20, pady=20)
frame.pack(fill='both', expand=True, padx=10, pady=10)

label = tk.Label(frame, text="Sélectionnez un fichier audio pour voir les métadonnées.", bg='#D3D3D3', pady=10)
label.pack()

bouton_ouvrir = tk.Button(frame, text="Ouvrir Fichier", command=ouvrir_fichier, padx=10, pady=5)
bouton_ouvrir.pack()


table_frame = tk.Frame(frame, bg='#D3D3D3')
table_frame.pack(fill='both', expand=True, pady=10)

canvas = tk.Canvas(table_frame, bg='#D3D3D3')
scrollbar = tk.Scrollbar(table_frame, orient="vertical", command=canvas.yview)
scrollable_frame = tk.Frame(canvas, bg='#D3D3D3')

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

bouton_exporter = tk.Button(frame, text="Exporter les Métadonnées", command=exporter_metadonnees, padx=10, pady=5)
bouton_exporter.pack()


root.bind("<Configure>", lambda event: canvas.config(scrollregion=canvas.bbox("all")))

root.mainloop()
