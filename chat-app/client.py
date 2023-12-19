import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

class ChatClient:
    def __init__(self, host, port):
        self.window = tk.Tk()
        self.window.title('Chat Application')

        self.chat_area = scrolledtext.ScrolledText(self.window, state='disabled', wrap=tk.WORD)
        self.chat_area.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.new_message_entry = tk.Entry(self.window)
        self.new_message_entry.grid(row=1, column=0, padx=10, pady=10, sticky='ew')

        self.send_button = tk.Button(self.window, text='Send', command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=10, sticky='ew')

        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))

    def run(self):
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.daemon = True
        receive_thread.start()

        self.window.protocol('WM_DELETE_WINDOW', self.on_closing)
        tk.mainloop()

    def send_message(self):
        message = self.new_message_entry.get()

        if message:
            self.client_socket.send(message.encode('utf-8'))
            self.new_message_entry.delete(0, tk.END)
            self.display_message(f'You: {message}')

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                    self.display_message(message)
            except OSError:
                break

    def display_message(self, message):
        self.chat_area.config(state='normal')
        self.chat_area.insert(tk.END, message + '\n')
        self.chat_area.config(state='disabled')
        self.chat_area.yview(tk.END)

    def on_closing(self):
        pass

if __name__ == '__main__':
    client = ChatClient('0.0.0.0', 8000)
    client.run()