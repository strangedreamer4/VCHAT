import os
import threading
import subprocess
import pyrebase
import tkinter as tk
from tkinter import messagebox

class FirebaseChat:
    def __init__(self, config):
        self.firebase = pyrebase.initialize_app(config)
        self.db = self.firebase.database()

class ChatApp:
    def __init__(self, master, firebase_chat):
        self.master = master
        self.firebase_chat = firebase_chat

        master.title("VCHAT")
        master.configure(bg="black")

        self.username_label = tk.Label(master, text="Enter your username:", fg="green", bg="black",
                                       font=("Helvetica", 14))
        self.username_label.pack()

        # Increase the width and height of the entry box
        self.username_entry = tk.Entry(master, bg="black", fg="green", font=("Helvetica", 12), width=40)
        self.username_entry.pack(pady=20)  # Adding padding to separate the entry box from the button

        self.start_button = tk.Button(master, text="Start Chat", command=self.start_chat, bg="green",
                                      fg="black", font=("Helvetica", 12, "bold"))
        self.start_button.pack()

    def start_chat(self):
        username = self.username_entry.get()
        if username:
            self.master.destroy()
            chat_window = ChatWindow(username, self.firebase_chat)
            chat_window.start_chat()
        else:
            messagebox.showinfo("Error", "Please enter a valid username.")

class ChatWindow:
    def __init__(self, username, firebase_chat):
        self.username = username
        self.firebase_chat = firebase_chat
        self.root = tk.Tk()

        self.root.title("VCHAT - User: {}".format(username))
        self.root.configure(bg="black")

        self.message_listbox = tk.Listbox(self.root, width=50, height=20, bg="black", fg="green",
                                          font=("Helvetica", 12))
        self.message_listbox.pack(padx=10, pady=10)

        self.message_entry = tk.Entry(self.root, width=40, bg="black", fg="green", font=("Helvetica", 12))
        self.message_entry.pack(padx=10, pady=10, side=tk.LEFT)

        self.send_button = tk.Button(self.root, text="Send", command=self.send_message, bg="green",
                                     fg="black", font=("Helvetica", 12, "bold"))
        self.send_button.pack(pady=10, side=tk.LEFT)

        self.root.bind('<Return>', lambda event=None: self.send_message())
        self.message_listbox.insert(tk.END, "Welcome, {}!".format(username))
        self.animate_message_reveal()

    def text_to_voice(self, text):
        try:
            subprocess.run(["espeak-ng -p 54", text])
        except FileNotFoundError:
            print("Error: espeak not found. Install espeak or adjust the path.")
        except Exception as e:
            print(f"Error during text_to_voice: {e}")

    def receive_messages(self):
        messages_stream = self.firebase_chat.db.child('messages').stream(self.stream_handler)

    def stream_handler(self, message):
        try:
            # Check if the message is not None
            if message:
                data = message.get('data')
                if data:
                    sender = data.get('sender', 'Unknown Sender')
                    message_text = data.get('message', '')

                    if sender and message_text:
                        if sender != self.username:
                            message_display = f"{sender}: {message_text}"
                            self.message_listbox.insert(tk.END, message_display)
                            self.text_to_voice(message_text)
        except Exception as e:
            print(f"Error in ChatWindow.stream_handler: {e}")

    def send_message(self):
        text = self.message_entry.get()
        if text:
            self.firebase_chat.db.child('messages').push({'sender': self.username, 'message': text})
            self.message_entry.delete(0, tk.END)
        else:
            messagebox.showinfo("Error", "Please enter a message.")

    def start_chat(self):
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.start()

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.protocol("WM_DELETE_WINDOW", lambda: None)
            self.root.destroy()
            os._exit(0)  # Forcefully exit the Python interpreter

    def animate_message_reveal(self):
        message = "Welcome, {}!".format(self.username)
        for i in range(len(message) + 1):
            self.message_listbox.delete(0, tk.END)
            self.message_listbox.insert(tk.END, message[:i])
            self.root.update()
            self.root.after(100)

if __name__ == "__main__":
    try:
        firebase_config = {
            "apiKey": "AIzaSyCqBZSjN4Ucpt_3H6n3x0YEJnAZJcC1zCk",
            "authDomain": "vchat-88fee.firebaseapp.com",
            "databaseURL": "https://vchat-88fee-default-rtdb.europe-west1.firebasedatabase.app",
            "projectId": "vchat-88fee",
            "storageBucket": "vchat-88fee.appspot.com",
            "messagingSenderId": "238019458127",
            "appId": "1:238019458127:web:3a2ed727197523a769e63a",
            "measurementId": "G-VKHZ41QR7L"
        }
        
        firebase_chat = FirebaseChat(firebase_config)

        root = tk.Tk()
        app = ChatApp(root, firebase_chat)
        root.mainloop()

    except KeyboardInterrupt:
        print("Program interrupted by user.")
    except Exception as e:
        print(f"Error in main: {e}")



