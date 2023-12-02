# File Explorer GUI with Tree View and Checkboxes - File: file_explorer_gui.py
# GUI for selecting, displaying, and interacting with directory trees with checkboxes.
# Version: 3.2
# Updated: 2023-12-01
# Author: Tim Leitch

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
from file_processor import merge_files


class FileExplorerApp:
    def __init__(self, root):
        self.root = root
        root.title("File Explorer with Tree View and Checkboxes")
        self.directory_base = None

        # Path selection button
        self.btn_select_path = tk.Button(
            root, text="Select Path", command=self.select_path)
        self.btn_select_path.pack()

        # Treeview for displaying files and directories with checkboxes
        self.tree = ttk.Treeview(root, columns=("checked",))
        self.tree.heading("#0", text="File/Folder", anchor=tk.W)
        self.tree.heading("checked", text="Select", anchor=tk.W)
        self.tree.column("checked", width=50, anchor="center")
        self.tree.pack(fill="both", expand=True)

        # Bind item click to toggle checkboxes
        self.tree.bind("<Button-1>", self.on_item_click)

        # Merge button
        self.btn_merge = tk.Button(
            root, text="Merge Files", command=self.merge_files)
        self.btn_merge.pack()

    def select_path(self):
        path = filedialog.askdirectory()
        if path:
            self.directory_base = path
            self.populate_tree(path, "")

    def populate_tree(self, path, parent):
        self.tree.delete(*self.tree.get_children())
        self.process_directory(path, "")

    def process_directory(self, path, parent):
        for entry in os.scandir(path):
            is_dir = entry.is_dir()
            id = self.tree.insert(
                parent, "end", text=entry.name, open=False, values=("☐",))
            if is_dir:
                self.process_directory(entry.path, id)

    def merge_files(self):
        file_paths = self.get_checked_files(self.tree.get_children(), [])
        if file_paths:
            merge_files(file_paths)
            messagebox.showinfo("Success", "Files merged successfully.")
        else:
            messagebox.showwarning("Warning", "No files selected.")

    def get_checked_files(self, items, file_paths):
        for item in items:
            if self.tree.item(item)["values"][0] == "☑":
                full_path = os.path.join(
                    self.directory_base, self.get_item_path(item))
                if os.path.isfile(full_path):
                    file_paths.append(full_path)
            if self.tree.get_children(item):
                self.get_checked_files(
                    self.tree.get_children(item), file_paths)
        return file_paths

    def get_item_path(self, item):
        path = []
        while item:
            path.insert(0, self.tree.item(item, "text"))
            item = self.tree.parent(item)
        return "/".join(path)

    def on_item_click(self, event):
        region = self.tree.identify("region", event.x, event.y)
        if region == "cell":
            item = self.tree.identify_row(event.y)
            self.toggle_check(item)

    def toggle_check(self, item):
        if self.tree.item(item)["values"][0] == "☐":
            self.tree.item(item, values=("☑",))
        else:
            self.tree.item(item, values=("☐",))


if __name__ == "__main__":
    root = tk.Tk()
    app = FileExplorerApp(root)
    root.mainloop()
