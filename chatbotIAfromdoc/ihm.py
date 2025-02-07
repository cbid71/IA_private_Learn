import tkinter as tk
import requests

def send_request(event=None):
    user_input = entry.get()
    if not user_input:
        return

    # Effet de clic sur le bouton envoyer
    send_button.config(relief=tk.SUNKEN)
    root.after(100, lambda: send_button.config(relief=tk.RAISED))
    
    try:
        response = requests.post("http://localhost:9876/api/search", json={"query": user_input})
        response_data = response.json()
        bot_response = response_data.get("message", "Erreur: Réponse non reçue")
    except Exception as e:
        bot_response = f"Erreur: {e}"
    

    chat_history.config(state=tk.NORMAL)
    chat_history.insert(tk.END, f"Vous: {user_input}\n")
    chat_history.insert(tk.END, f"Bot: {bot_response}\n\n")
    chat_history.config(state=tk.DISABLED)
    chat_history.yview(tk.END)
    entry.delete(0, tk.END)

# Création de la fenêtre principale
root = tk.Tk()
root.title("Chatbot GUI")

# Zone d'affichage des échanges avec scrollbar
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

chat_history = tk.Text(frame, height=20, width=50, state=tk.DISABLED, wrap=tk.WORD, yscrollcommand=scrollbar.set)
chat_history.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=chat_history.yview)

# Champ de saisie
entry = tk.Entry(root, width=40)
entry.pack(padx=10, pady=5)
entry.bind("<Return>", send_request)  # Lier la touche Entrée à l'envoi

# Bouton d'envoi
send_button = tk.Button(root, text="Envoyer", command=send_request)
send_button.pack(pady=5)

root.mainloop()
