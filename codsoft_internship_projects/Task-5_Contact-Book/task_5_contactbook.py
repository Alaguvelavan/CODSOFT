import tkinter as tk
from tkinter import messagebox, simpledialog
import os
import json

color_white = "white"
color_black = "#1c1c1c"
color_red = "#FF2424"
color_blue = "#6588E2"
color_green = "#57E833"
color_sun = '#F8FF1F'
color_newblue = '#4D00FF'
color_mix = '#47E9CE'

class contactbook:
    
    def __init__(self,root):
        self.root = root
        self.root.title("Contact Book")
        self.root.geometry("500x500")
        
        self.contacts = {}
        self.file_path = "contacts.json"
        self.load_contacts()


        search_label = tk.Label(self.root, text="Search Contacts:", font=("Arial", 10))
        search_label.pack(pady=(10, 0))
        
        self.search_entry = tk.Entry(self.root, font=("Arial", 12))
        self.search_entry.pack(fill="x", padx=10, pady=5)
        self.search_entry.bind("<KeyRelease>", self.filter_contacts)
        
        self.listbox = tk.Listbox(self.root, font=("Arial", 12) , background= color_mix , foreground= color_newblue)
        self.listbox.pack(expand = True, fill = "both", padx =10, pady =10)
        self.listbox.bind("<<ListboxSelect>>", self.show_contact_details)
        
       
        self.detail_label = tk.Label(self.root, text="Select a contact to view details", font=("Arial", 12), anchor="center" , background=  color_sun , foreground= color_red)

        self.detail_label.pack(fill="x", padx =10, pady=5)
        
        
        self.add_button = tk.Button(self.root, text="Add contact", command = self.add_contact , background= color_blue)
        self.add_button.pack(side="left", padx=10, pady=10, )
        
        self.edit_button = tk.Button(self.root, text="Edit contact", command=self.edit_contact, state = "disabled" , background= color_green)
        self.edit_button.pack(side="left", padx=10, pady=10)
        
        self.delete_button = tk.Button(self.root, text="Delete contact", command=self.delete_contact, state = "disabled" , background=color_red , foreground= color_white)
        self.delete_button.pack(side="right", padx=10, pady=10)
        
        self.refresh_list()
        
        
    def load_contacts(self): 
        if os.path.exists(self.file_path):
            try:
                with open(self.file_path, "r") as file:
                    self.contacts = json.load(file)
            except json.JSONDecodeError:
                self.contacts = {}
        else:
            self.contacts = {}
            
    def save_contacts(self):
        with open(self.file_path, 'w') as file:
            json.dump(self.contacts, file)
            

    def refresh_list(self, data=None):
        self.listbox.delete(0, tk.END)
        items_to_display = data if data is not None else sorted(self.contacts.keys())
        for name in items_to_display:
            self.listbox.insert(tk.END, name)


    def filter_contacts(self, event):
        typed = self.search_entry.get().lower()
        if typed == '':
            self.refresh_list()
        else:
            filtered_names = [name for name in sorted(self.contacts.keys()) if typed in name.lower()]
            self.refresh_list(data=filtered_names)


    def show_contact_details(self, event): 
        selected = self.listbox.curselection()
        if selected:
            name = self.listbox.get(selected)
            details = self.contacts[name]
            self.detail_label.config(text=f"Contact details:\n Name: {name}\nPhone: {details['phone']}\nEmail: {details['email']}")
            self.edit_button.config(state="normal")
            self.delete_button.config(state="normal")
        else:
            self.detail_label.config(text="select a contact to view details")
            self.edit_button.config(state="disabled")
            self.delete_button.config(state="disabled")
            
            
    def add_contact(self):
        name = simpledialog.askstring( "Add Contact",  "Enter contact name :")
        if not name:
          return
        if name in self.contacts:
         messagebox.showerror("Error", "Contact already exists.")
         return
        phone = simpledialog.askstring("Add Contact", "Enter phone number :")
        email = simpledialog.askstring("Add Contact", "Enter email address :")
        self.contacts[name] = {"phone":phone, "email": email}
        self.save_contacts()
        self.refresh_list()
    
    
    def edit_contact(self):
        selected = self.listbox.curselection()
        if selected:
         name = self.listbox.get(selected)
        new_phone = simpledialog.askstring( "Edit contact", "Enter new phone number:", initialvalue=self.contacts[name]["phone"])
        new_email = simpledialog.askstring( "Edit contact",  "Enter new email address:", initialvalue=self.contacts[name]["email"])
        self.contacts[name] = {"phone": new_phone, "email": new_email}
        self.save_contacts()
        self.refresh_list()
        
    def delete_contact(self):
        selected = self.listbox.curselection()
        if selected:
          name = self.listbox.get(selected)
        if messagebox.askyesno("Delete Contact", f"Are you sure you want to delete '{name}contact'?"):
           del self.contacts[name]
           self.save_contacts()
           self.refresh_list()
           self.detail_label.config(text = "select a contact to view details")
           self.edit_button.config(state = "disabled")
           self.delete_button.config(state = "disabled")
           
if __name__=="__main__":
           root = tk.Tk()
           app = contactbook(root)
           root.mainloop()
        
    
    
    
    
    
        
