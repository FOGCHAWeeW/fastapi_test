from tkinter import *
import random

class PizzaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Мини-пиццерия")
        self.root.geometry("800x600")
        
        self.ingredients = []
        self.sizes = ["Маленькая", "Средняя", "Большая"]
        
        # Текущий заказ
        self.order_label = Label(root, text="", font=("Arial", 18))
        self.order_label.pack(pady=10)
        
        # Холст для пиццы
        self.canvas = Canvas(root, width=800, height=300, bg="white")
        self.canvas.pack()
        
        # Кнопки
        self.btn_frame = Frame(root)
        self.btn_frame.pack(pady=20)
        
        Button(self.btn_frame, text="Добавить соус", command=self.add_sauce).grid(row=0, column=0)
        Button(self.btn_frame, text="Добавить сыр", command=lambda: self.add_ing("Сыр")).grid(row=0, column=1)
        Button(self.btn_frame, text="Добавить пепперони", command=lambda: self.add_ing("Пепперони")).grid(row=0, column=2)
        
        self.bake_btn = Button(root, text="В печь!", command=self.send_to_oven, bg="orange")
        
        self.new_order()

    def new_order(self):
        size = random.choice(self.sizes)
        self.order_label.config(text=f"Заказ: {size} пицца")
        self.canvas.delete("all")
        # Рисуем тесто
        r = 50 if size == "Маленькая" else 80 if size == "Средняя" else 110
        self.pizza_id = self.canvas.create_oval(400-r, 150-r, 400+r, 150+r, fill="#F3E5AB", outline="#8B4513", width=3)
        self.bake_btn.pack_forget()
        self.ingredients = []

    def add_sauce(self):
        self.canvas.itemconfig(self.pizza_id, fill="#FF6347") # Цвет соуса
        self.bake_btn.pack(pady=10)

    def add_ing(self, name):
        self.ingredients.append(name)
        # Визуализация ингредиента (простые кружочки)
        x, y = random.randint(350, 450), random.randint(100, 200)
        self.canvas.create_oval(x, y, x+10, y+10, fill="yellow" if name=="Сыр" else "red")

    def send_to_oven(self):
        for _ in range(50):
            self.canvas.move("all", 10, 0)
            self.root.update()
            self.root.after(20)
        self.new_order()

root = Tk()
app = PizzaApp(root)
root.mainloop()
