# health_chatbot_gui.py

import tkinter as tk
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

# Load your combined chatbot dataset
df = pd.read_csv('combined_chatbot_data.csv')

# Load SBERT model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Generate embeddings for all questions in your dataset
question_embeddings = model.encode(df['short_question'].tolist(), show_progress_bar=True)

# Chatbot response function
def chatbot_reply(user_input):
    input_embedding = model.encode([user_input])
    similarities = cosine_similarity(input_embedding, question_embeddings)
    index = np.argmax(similarities)
    return df['short_answer'].iloc[index]

# GUI response handling
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import tkinter as tk

# Load your CSV dataset
df = pd.read_csv("combined_chatbot_data.csv")

# Load sentence transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Generate embeddings
question_embeddings = model.encode(df['short_question'].tolist(), show_progress_bar=True)

# Chatbot logic
def chatbot_reply(user_input):
    input_embedding = model.encode([user_input])
    similarities = cosine_similarity(input_embedding, question_embeddings)
    index = np.argmax(similarities)
    return df['short_answer'].iloc[index]

def ask_question():
    user_input = entry.get()
    if user_input.strip() == "":
        return
    response = chatbot_reply(user_input)
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, f"You: {user_input}\nBot: {response}\n\n")
    chat_log.config(state=tk.DISABLED)
    entry.delete(0, tk.END)

# GUI layout
window = tk.Tk()
window.title("Health Chatbot")
window.geometry("400x500")

chat_log = tk.Text(window, bd=1, bg="white", font=("Arial", 12), state=tk.DISABLED, wrap=tk.WORD)
chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry = tk.Entry(window, bd=1, font=("Arial", 12))
entry.pack(padx=10, pady=(0, 10), fill=tk.X)

ask_button = tk.Button(window, text="Ask", font=("Arial", 12), command=ask_question)
ask_button.pack(pady=(0, 10))

window.mainloop()
