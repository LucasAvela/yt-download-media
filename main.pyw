import customtkinter as ctk
import os
from tkinter import filedialog
from downloadManager import DownloadManager
import threading
import sys

class StdoutRedirector:
    def __init__(self, app):
        self.app = app
        self.is_update_status_call = False

    def write(self, message):
        if not message or message == '\n' or self.is_update_status_call:
            return
        self.is_update_status_call = True
        self.app.update_status(message)
        self.is_update_status_call = False

    def flush(self):
        pass


class YoutubeDownloaderApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.user = os.path.basename(os.path.expanduser("~"))
        self.init_ui()
        self.stdout_redirector = StdoutRedirector(self)
        sys.stdout = self.stdout_redirector

    def init_ui(self):
        self.title("Corylus Youtube Downloader")
        self.geometry("800x300")
        self.iconbitmap('Icon0.ico')

        self.create_label("Video or Playlist URL", 18).pack(pady=10)
        self.url_field = self.create_entry(750, font_size=18)
        self.url_field.pack(pady=0)

        self.create_label("Output PATH", 18).pack(pady=10)
        out_frame = ctk.CTkFrame(self)
        out_frame.pack(pady=0, padx=10)
        self.out_field = self.create_entry(650, font_size=18, parent=out_frame)
        self.out_field.pack(side="left", padx=(0, 10), fill="x", expand=True)
        self.out_field.insert(0, f"C:/Users/{self.user}/Desktop/Video/")

        browse_button = ctk.CTkButton(out_frame, text="Browse", width=90, command=self.choose_directory)
        browse_button.pack(side="right")

        self.button_frame = ctk.CTkFrame(self, fg_color='#242424')
        self.button_frame.pack(pady=20)

        self.create_download_button("Download .MP4", "#5aa356", "#73c76f",
                                     lambda: self.threaded_download(format="VIDEO")).pack(side=ctk.LEFT, padx=10)
        self.create_download_button("Download .MP3", "#c9ab10", "#e8c517",
                                     lambda: self.threaded_download(format="AUDIO", ext="mp3")).pack(side=ctk.LEFT, padx=10)
        self.create_download_button("Download .WAV", "#425385", "#5669a3",
                                     lambda: self.threaded_download(format="AUDIO", ext="wav")).pack(side=ctk.LEFT, padx=10)

        self.status_label = self.create_label("Ready", font_size=14, anchor="center")
        self.status_label.pack(side="bottom", fill="x", pady=10)

    def create_label(self, text, font_size=12, parent=None, **kwargs):
        parent = parent if parent else self
        return ctk.CTkLabel(parent, text=text, font=("Consolas", font_size), **kwargs)

    def create_entry(self, width, font_size=12, parent=None):
        parent = parent if parent else self
        return ctk.CTkEntry(parent, width=width, font=("Consolas", font_size))

    def create_download_button(self, text, fg_color, hover_color, command):
        return ctk.CTkButton(
            self.button_frame,
            text=text,
            font=("Consolas", 26),
            width=200,
            height=50,
            corner_radius=15,
            fg_color=fg_color,
            hover_color=hover_color,
            command=command,
        )

    def choose_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.out_field.delete(0, ctk.END)
            self.out_field.insert(0, directory)

    def update_status(self, message):
        self.status_label.configure(text=message)
        print(message)

    def threaded_download(self, format, ext=None):
        self.toggle_buttons(False)
        url = self.url_field.get()
        output = self.out_field.get()

        def download_task():
            try:
                self.update_status("Downloading...")
                DownloadManager.download(
                    self=DownloadManager(), url=url, out=output, format=format, audio_ext=ext
                )
                self.update_status("Download completed!")
            except Exception as e:
                self.update_status(f"Error: {e}")
            finally:
                self.toggle_buttons(True)

        threading.Thread(target=download_task).start()

    def toggle_buttons(self, state):
        for widget in self.button_frame.winfo_children():
            widget.pack_forget() if not state else widget.pack(side=ctk.LEFT, padx=10)


if __name__ == "__main__":
    app = YoutubeDownloaderApp()
    app.mainloop()
