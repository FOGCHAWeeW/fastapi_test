from tkinter import *
import random

class PizzaApp:
    def __init__(self, root):
        self.root = root
        # ОШИБКА 1: Неверный заголовок или его отсутствие
        self.root.title("Сломанная пицца") 
        self.root.geometry("800x600")
        
        self.sizes = ["Маленькая"] # ОШИБКА 3: Только один размер
        
        # Текущий заказ (ОШИБКА 2: Метка не размещена через pack/grid)
        self.order_label = Label(root, text="Ожидание...", font=("Arial", 18))
        
        self.canvas = Canvas(root, width=800, height=300, bg="white")
        self.canvas.pack()
        
        self.btn_frame = Frame(root)
        self.btn_frame.pack()
        
        # ОШИБКА 4: У кнопок нет параметров command
        Button(self.btn_frame, text="Добавить соус").grid(row=0, column=0)
        Button(self.btn_frame, text="Добавить сыр").grid(row=0, column=1)
        
        # ОШИБКА 5: Кнопка "В печь" видна сразу (используется pack вместо pack_forget)
        self.bake_btn = Button(root, text="В печь!", bg="orange")
        self.bake_btn.pack() 

    def new_order(self):
        size = random.choice(self.sizes)
        self.order_label.config(text=f"Заказ: {size}")
        # ОШИБКА 7: Код создания теста закомментирован или удален
        pass 

    def send_to_oven(self):
        # ОШИБКА 6: Пицца двигается в неправильную сторону или по Y
        self.canvas.move("all", 0, 10) 
        self.root.update()

root = Tk()
app = PizzaApp(root)
# ОШИБКА 1: Пропущена строка запуска окна