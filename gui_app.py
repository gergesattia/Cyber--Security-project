import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
from pathlib import Path
from cipher_wrapper import CIPHERS

# Set appearance mode and color theme
ctk.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class EncryptionGUI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Secure File Encryption & Decryption")
        self.geometry("1100x850")
        self.minsize(900, 700)
        
        # Grid layout
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Variables
        self.cipher_var = ctk.StringVar(value="Caesar Cipher")
        self.selected_file = ctk.StringVar(value="No file selected")
        
        self.create_sidebar()
        self.create_main_content()
        self.update_key_info()

    def create_sidebar(self):
        # Sidebar Frame
        self.sidebar_frame = ctk.CTkFrame(self, width=250, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(6, weight=1)

        # Logo / Title
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="Cyper\nStudio", font=ctk.CTkFont(size=28, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(30, 30))

        # Cipher Selection
        self.cipher_label = ctk.CTkLabel(self.sidebar_frame, text="Select Cipher:", anchor="w", font=ctk.CTkFont(size=14, weight="bold"))
        self.cipher_label.grid(row=1, column=0, padx=20, pady=(10, 0))
        
        self.cipher_menu = ctk.CTkOptionMenu(self.sidebar_frame, values=list(CIPHERS.keys()), variable=self.cipher_var, command=self.update_key_info)
        self.cipher_menu.grid(row=2, column=0, padx=20, pady=(10, 20))

        # Key Input
        self.key_label = ctk.CTkLabel(self.sidebar_frame, text="Secret Key:", anchor="w", font=ctk.CTkFont(size=14, weight="bold"))
        self.key_label.grid(row=3, column=0, padx=20, pady=(10, 0))
        
        self.key_input = ctk.CTkEntry(self.sidebar_frame, placeholder_text="Enter key...", show="*")
        self.key_input.grid(row=4, column=0, padx=20, pady=(10, 5))
        
        self.show_key_switch = ctk.CTkSwitch(self.sidebar_frame, text="Show Key", command=self.toggle_key_visibility)
        self.show_key_switch.grid(row=5, column=0, padx=20, pady=(5, 20))

        self.key_info_label = ctk.CTkLabel(self.sidebar_frame, text="", text_color="gray", font=ctk.CTkFont(size=12))
        self.key_info_label.grid(row=6, column=0, padx=20, pady=(0, 20), sticky="n")

        # Appearance mode
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_menu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Dark", "Light", "System"],
                                                      command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=8, column=0, padx=20, pady=(10, 20))

    def create_main_content(self):
        # Top Frame for File Operations
        self.file_frame = ctk.CTkFrame(self)
        self.file_frame.grid(row=0, column=1, padx=20, pady=(20, 10), sticky="new")
        self.file_frame.grid_columnconfigure(1, weight=1)

        self.file_title = ctk.CTkLabel(self.file_frame, text="File Operations", font=ctk.CTkFont(size=16, weight="bold"))
        self.file_title.grid(row=0, column=0, padx=20, pady=(10, 5), sticky="w")

        self.select_file_btn = ctk.CTkButton(self.file_frame, text="📁 Select File", command=self.select_file, width=120)
        self.select_file_btn.grid(row=1, column=0, padx=20, pady=(5, 15))

        self.file_path_label = ctk.CTkLabel(self.file_frame, textvariable=self.selected_file, text_color="gray")
        self.file_path_label.grid(row=1, column=1, padx=10, pady=(5, 15), sticky="w")

        self.encrypt_file_btn = ctk.CTkButton(self.file_frame, text="🔐 Encrypt File", command=self.encrypt_file, fg_color="#2b7a4b", hover_color="#1d5433", width=120)
        self.encrypt_file_btn.grid(row=1, column=2, padx=10, pady=(5, 15))

        self.decrypt_file_btn = ctk.CTkButton(self.file_frame, text="🔓 Decrypt File", command=self.decrypt_file, fg_color="#8a3030", hover_color="#5e2121", width=120)
        self.decrypt_file_btn.grid(row=1, column=3, padx=20, pady=(5, 15))

        # Main Text Area Frame
        self.text_frame = ctk.CTkFrame(self)
        self.text_frame.grid(row=1, column=1, padx=20, pady=10, sticky="nsew")
        self.text_frame.grid_columnconfigure(0, weight=1)
        self.text_frame.grid_columnconfigure(2, weight=1)
        self.text_frame.grid_rowconfigure(1, weight=1)

        # Input Text
        self.input_label = ctk.CTkLabel(self.text_frame, text="Input Text", font=ctk.CTkFont(size=14, weight="bold"))
        self.input_label.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="w")
        
        self.input_text = ctk.CTkTextbox(self.text_frame)
        self.input_text.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="nsew")

        # Action Buttons in Middle
        self.actions_frame = ctk.CTkFrame(self.text_frame, fg_color="transparent")
        self.actions_frame.grid(row=1, column=1, padx=10, pady=0)

        self.encrypt_text_btn = ctk.CTkButton(self.actions_frame, text="Encrypt ➔", command=self.encrypt_text, width=100)
        self.encrypt_text_btn.pack(pady=10)

        self.decrypt_text_btn = ctk.CTkButton(self.actions_frame, text="Decrypt ➔", command=self.decrypt_text, width=100)
        self.decrypt_text_btn.pack(pady=10)

        self.swap_btn = ctk.CTkButton(self.actions_frame, text="Swap ↔", command=self.swap_text, width=100, fg_color="#555555")
        self.swap_btn.pack(pady=10)

        self.clear_btn = ctk.CTkButton(self.actions_frame, text="Clear 🗑", command=self.clear_all, width=100, fg_color="#8a3030", hover_color="#5e2121")
        self.clear_btn.pack(pady=10)

        # Output Text
        self.output_label = ctk.CTkLabel(self.text_frame, text="Output Text", font=ctk.CTkFont(size=14, weight="bold"))
        self.output_label.grid(row=0, column=2, padx=10, pady=(10, 5), sticky="w")
        
        self.output_text = ctk.CTkTextbox(self.text_frame)
        self.output_text.grid(row=1, column=2, padx=10, pady=(0, 10), sticky="nsew")

        # Bottom Frame for Save/Copy Actions
        self.bottom_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.bottom_frame.grid(row=2, column=1, padx=20, pady=(10, 20), sticky="ew")
        
        self.copy_btn = ctk.CTkButton(self.bottom_frame, text="📋 Copy Output", command=self.copy_output, width=120)
        self.copy_btn.pack(side="left", padx=(0, 10))

        self.save_btn = ctk.CTkButton(self.bottom_frame, text="💾 Save Output", command=self.save_output, width=120)
        self.save_btn.pack(side="left")

        self.help_btn = ctk.CTkButton(self.bottom_frame, text="ℹ️ Help", command=self.show_help, width=120, fg_color="#555555")
        self.help_btn.pack(side="right")

    def change_appearance_mode_event(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)

    def update_key_info(self, *args):
        cipher_name = self.cipher_var.get()
        cipher_info = CIPHERS[cipher_name]
        key_type = cipher_info["key_type"]
        example_key = cipher_info["example_key"]
        info_text = f"Key Required:\n{key_type}\n(e.g., {example_key})"
        self.key_info_label.configure(text=info_text)

        cipher_name_no_space = cipher_name.replace(" ", "").lower()
        needs_key = "rot13" not in cipher_name_no_space

        if needs_key:
            self.key_input.configure(state="normal")
            self.show_key_switch.configure(state="normal")
        else:
            self.key_input.delete(0, "end")
            self.key_input.configure(state="disabled")
            self.show_key_switch.configure(state="disabled")

    def toggle_key_visibility(self):
        if self.show_key_switch.get():
            self.key_input.configure(show="")
        else:
            self.key_input.configure(show="*")

    def select_file(self):
        file_path = filedialog.askopenfilename(
            title="Select file",
            filetypes=[("All Files", "*.*"), ("Text Files", "*.txt")]
        )
        if file_path:
            self.selected_file.set(f"Selected: {os.path.basename(file_path)}")
            self.current_file = file_path

    def _get_params(self):
        cipher_name = self.cipher_var.get()
        key = self.key_input.get()
        cipher_funcs = CIPHERS[cipher_name]
        cipher_name_no_space = cipher_name.replace(" ", "").lower()
        needs_key = "rot13" not in cipher_name_no_space
        return cipher_name, key, cipher_funcs, needs_key

    def encrypt_text(self):
        text = self.input_text.get("1.0", "end-1c").strip()
        if not text:
            messagebox.showwarning("Warning", "Please enter text to encrypt")
            return
            
        cipher_name, key, cipher_funcs, needs_key = self._get_params()
        if needs_key and not key:
            messagebox.showwarning("Warning", "Please enter a key")
            return
            
        try:
            result = cipher_funcs["encrypt"](text, key) if needs_key else cipher_funcs["encrypt"](text)
            self.output_text.delete("1.0", "end")
            self.output_text.insert("end", result)
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {str(e)}")

    def decrypt_text(self):
        text = self.input_text.get("1.0", "end-1c").strip()
        if not text:
            messagebox.showwarning("Warning", "Please enter text to decrypt")
            return
            
        cipher_name, key, cipher_funcs, needs_key = self._get_params()
        if needs_key and not key:
            messagebox.showwarning("Warning", "Please enter a key")
            return
            
        try:
            result = cipher_funcs["decrypt"](text, key) if needs_key else cipher_funcs["decrypt"](text)
            self.output_text.delete("1.0", "end")
            self.output_text.insert("end", result)
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")

    def encrypt_file(self):
        if not hasattr(self, 'current_file'):
            messagebox.showwarning("Warning", "Please select a file first")
            return
            
        cipher_name, key, cipher_funcs, needs_key = self._get_params()
        if needs_key and not key:
            messagebox.showwarning("Warning", "Please enter a key")
            return

        try:
            with open(self.current_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
            result = cipher_funcs["encrypt"](content, key) if needs_key else cipher_funcs["encrypt"](content)
            
            ext = Path(self.current_file).suffix
            out_file = self.current_file.replace(ext, f"_encrypted.txt")
            
            with open(out_file, 'w', encoding='utf-8') as f:
                f.write(result)
                
            self.output_text.delete("1.0", "end")
            self.output_text.insert("end", f"File saved to:\n{out_file}\n\nPreview:\n{result[:500]}...")
            messagebox.showinfo("Success", "File encrypted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"File encryption failed: {str(e)}")

    def decrypt_file(self):
        if not hasattr(self, 'current_file'):
            messagebox.showwarning("Warning", "Please select a file first")
            return
            
        cipher_name, key, cipher_funcs, needs_key = self._get_params()
        if needs_key and not key:
            messagebox.showwarning("Warning", "Please enter a key")
            return

        try:
            with open(self.current_file, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
            result = cipher_funcs["decrypt"](content, key) if needs_key else cipher_funcs["decrypt"](content)
            
            ext = Path(self.current_file).suffix
            out_file = self.current_file.replace(ext, f"_decrypted.txt")
            
            with open(out_file, 'w', encoding='utf-8') as f:
                f.write(result)
                
            self.output_text.delete("1.0", "end")
            self.output_text.insert("end", f"File saved to:\n{out_file}\n\nPreview:\n{result[:500]}...")
            messagebox.showinfo("Success", "File decrypted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"File decryption failed: {str(e)}")

    def swap_text(self):
        input_content = self.input_text.get("1.0", "end-1c")
        output_content = self.output_text.get("1.0", "end-1c")
        
        self.input_text.delete("1.0", "end")
        self.input_text.insert("end", output_content)
        
        self.output_text.delete("1.0", "end")
        self.output_text.insert("end", input_content)

    def clear_all(self):
        self.input_text.delete("1.0", "end")
        self.output_text.delete("1.0", "end")
        self.key_input.delete(0, "end")

    def copy_output(self):
        output_content = self.output_text.get("1.0", "end-1c")
        if output_content:
            self.clipboard_clear()
            self.clipboard_append(output_content)
            self.update()
            messagebox.showinfo("Success", "Output copied to clipboard!")
        else:
            messagebox.showwarning("Warning", "Output text is empty")

    def save_output(self):
        output_content = self.output_text.get("1.0", "end-1c")
        if not output_content:
            messagebox.showwarning("Warning", "Output text is empty")
            return
            
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(output_content)
                messagebox.showinfo("Success", f"Output saved to:\n{file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save: {str(e)}")

    def show_help(self):
        help_text = "ENCRYPTION ALGORITHMS:\n\n"
        for name, info in CIPHERS.items():
            help_text += f"• {name}\n  Key: {info['key_type']}\n\n"
            
        messagebox.showinfo("Help", help_text)

class LoginGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login - Cyper Studio")
        self.geometry("400x500")
        self.resizable(False, False)
        self.login_successful = False
        
        # Grid layout
        self.grid_columnconfigure(0, weight=1)
        
        self.create_widgets()
        
    def create_widgets(self):
        # Logo / Title
        self.logo_label = ctk.CTkLabel(self, text="Cyper\nStudio", font=ctk.CTkFont(size=32, weight="bold"))
        self.logo_label.grid(row=0, column=0, pady=(60, 40))
        
        # Username
        self.username_entry = ctk.CTkEntry(self, placeholder_text="Username", width=250, height=40)
        self.username_entry.grid(row=1, column=0, pady=(10, 10))
        
        # Password
        self.password_entry = ctk.CTkEntry(self, placeholder_text="Password", show="*", width=250, height=40)
        self.password_entry.grid(row=2, column=0, pady=(10, 30))
        
        # Login Button
        self.login_btn = ctk.CTkButton(self, text="Login", command=self.login, width=250, height=40, font=ctk.CTkFont(size=14, weight="bold"))
        self.login_btn.grid(row=3, column=0, pady=(10, 10))
        
        # Error Label
        self.error_label = ctk.CTkLabel(self, text="", text_color="red")
        self.error_label.grid(row=4, column=0, pady=(5, 10))

        # Bind Enter key to login
        self.bind('<Return>', lambda event: self.login())

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Default credentials for demonstration
        if username == "admin" and password == "admin":
            self.login_successful = True
            self.destroy()
        else:
            self.error_label.configure(text="Invalid username or password!")


def main():
    login_app = LoginGUI()
    login_app.mainloop()
    
    if login_app.login_successful:
        app = EncryptionGUI()
        app.mainloop()

if __name__ == "__main__":
    main()
