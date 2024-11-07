
import tkinter as tk
from tkinter import*
from PIL import Image, ImageTk

class Product:
    def __init__(self, name, price, quantity):
        self.name=name
        self.price=price
        self.quantity=quantity

    def get_total_price(self):
        return self.price*self.quantity

class ShoppingCart:
    def __init__(self):
        self.products=[]

    def add_product(self, product):
        self.products.append(product)

    def get_total_price(self):
        return sum(product.get_total_price() for product in self.products)

    def clear_cart(self):
        self.products.clear()
        return f"Grozs ir iztukšots"

class App:
    def __init__(self, master):
        self.master=master
        self.master.geometry("345x550")
        self.master.title("Veikals")
        self.master.configure(background="#6c6058")
        self.cart=ShoppingCart()

        input_frame = tk.Frame(master)
        input_frame.grid(pady=10, padx=20)

        self.name_label=tk.Label(input_frame, text="Nosaukums")
        self.name_label.grid(row=1, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(input_frame)
        self.name_entry.grid(row=1, column=1, padx=20)

        self.quantity_label=tk.Label(input_frame, text ="Daudzums")
        self.quantity_label.grid(row=2, column=0, padx=5, pady=5)
        self.quantity_entry = tk.Entry(input_frame)
        self.quantity_entry.grid(row=2, column=1, padx=20)

        self.price_label=tk.Label(input_frame, text="Cena")
        self.price_label.grid(row=3, column=0, padx=5, pady=5)
        self.price_entry =tk.Entry(input_frame)
        self.price_entry.grid(row=3, column=1, padx=20)

        self.add_button=tk.Button(master, text="Pievienot grozam", command=self.add_to_cart)
        self.add_button.grid(pady=10, padx=20)

        self.cart_listbox=tk.Listbox(master, width=50)
        self.cart_listbox.grid(pady=10, padx=20)

        self.total_label = tk.Button(master, text="Kopējā cena: 0.00 Eur", font=("Arial", 12))
        self.total_label.grid(pady=10, padx=20)

        self.clear_button = tk.Button(master, text="Dzēst grozu", command=self.clear_cart)
        self.clear_button.grid(pady=5, padx=20)

    
        self.card = Image.open("card.png")
        self.card = self.card.resize((100, 100)) 
        self.card_tk = ImageTk.PhotoImage(self.card)
        self.card_label = tk.Label(self.master, image=self.card_tk)
        self.card_label.grid(pady=10, padx=30)

            
    def add_to_cart(self):
        name=self.name_entry.get()
        price= float(self.price_entry.get())
        quantity = float(self.quantity_entry.get())

        product = Product(name, price, quantity)
        self.cart.add_product(product)
        self.cart_listbox.insert(tk.END, f"| Produkts: {name} | Cena: ${price} | Daudzums: {quantity} gab. |")

        self.name_entry.delete(0, tk.END)
        self.price_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)

        self.update_total_price()

    def update_total_price(self):
        total=self.cart.get_total_price()
        self.total_label.config(text=f"Kopējā cena: {total:.2f} $")

    def clear_cart(self):
        self.cart.clear_cart()
        self.cart_listbox.delete(0, tk.END)
        self.update_total_price()



if __name__=="__main__":
    root=tk.Tk()
    app=App(root)
    root.mainloop()