import tkinter as tk
from tkinter.messagebox import askquestion, showinfo


class SampleApp(tk.Tk):
    login = 'a'
    password = 'a'

    def __init__(self, *arg, **kwargs):
        tk.Tk.__init__(self, *arg, **kwargs)
        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (StartPage, MenuPage, Registration, Tuvak, Gul, Buket, Yordam):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            frame.grid(row=0, column=0, sticky='nsew')

            self.show_frame('StartPage')

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="Pink")
        self.controller = controller
        self.controller.title('REKMIX')
        self.controller.state('zoomed')

        big_lable = tk.Label(self, text='Цветочный магазин', font=('Times New Roman', 50, 'bold'), fg='black', bg='Pink')
        big_lable.pack(side=tk.LEFT, padx=30, pady=30)

        login_lable = tk.Label(self, text='Введите свой логин', font=('Times New Roman', 15, 'bold'), fg='black',
                               bg='yellow')
        login_lable.pack(pady=30)

        my_login = tk.StringVar()
        login_entry = tk.Entry(self, textvariable=my_login, bd='5', font=('Times New Roman', 15, 'bold'), fg='black',
                               bg='white')
        login_entry.pack(pady=30)

        password_lable = tk.Label(self, text='Введите ваш пароль', font=('Times New Roman', 15, 'bold'), fg='black',
                                  bg='yellow')
        password_lable.pack(pady=30)

        my_password = tk.StringVar()
        password_entry = tk.Entry(self, textvariable=my_password, bd='5', font=('Times New Roman', 15, 'bold'),
                                  fg='black',
                                  bg='white',
                                  show='*')
        password_entry.pack(pady=30)

        def check_password():
            if my_password.get() == SampleApp.password and my_login.get() == SampleApp.login:
                controller.show_frame('MenuPage')

            else:
                right_lable['text'] = "Неверный логин или пароль"
                right_lable.config(fg='red')
                right_lable.place(x=750, y=417)

        password_button = tk.Button(self, text='Вход ', bd='5', command=check_password,
                                    font=('Times New Roman', 15, 'bold'),
                                    fg='white', bg='grey')
        password_button.pack()
        right_lable = tk.Label(self, font=('Times New Roman', 15, 'bold'), fg='black', bg='white')
        right_lable.pack(pady=30)

        def registr():
            controller.show_frame('Registration')

        registr_button = tk.Button(self, text='Регистрация', bd='5', command=registr,
                                   font=('Times New Roman', 15, 'bold'), fg='white', bg='grey')
        registr_button.pack(pady=30)
        registr_button.place(x=1230, y=430)


class Registration(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='Pink')
        self.controller = controller

        heading_lable = tk.Label(self, text="Создать новый \n аккаунт", font=('Times New Roman', 50, 'bold'), fg='black',
                                 bg='pink')
        heading_lable.pack(side=tk.LEFT, padx=25, pady=25)

        name_1_lable = tk.Label(self, text="Фамилия", font=('Times New Roman', 15, 'bold'), fg='black', bg='yellow')
        name_1_lable.pack(pady=25)

        name_1_entry = tk.Entry(self, font=('Times New Roman', 15, 'bold'), bd='5', fg="black")
        name_1_entry.pack(pady=0)

        name_2_lable = tk.Label(self, text="Имя", font=('Times New Roman', 15, 'bold'), fg='black', bg='yellow')
        name_2_lable.pack(pady=25)

        name_2_entry = tk.Entry(self, font=('Times New Roman', 15, 'bold'), bd='5', fg="black")
        name_2_entry.pack(pady=0)

        manzil_label = tk.Label(self, text="Телефон номер", font=('Times New Roman', 15, 'bold'), fg='black', bg='yellow')
        manzil_label.pack(pady=25)

        manzil_entry = tk.Entry(self, font=('Times New Roman', 15, 'bold'), bd='5', fg="black")
        manzil_entry.pack(pady=0)

        manzil_label = tk.Label(self, text="Адрес", font=('Times New Roman', 15, 'bold'), fg='black', bg='yellow')
        manzil_label.pack(pady=25)

        manzil_entry = tk.Entry(self, font=('Times New Roman', 15, 'bold'), bd='5', fg="black")
        manzil_entry.pack(pady=0)

        name_3_lable = tk.Label(self, text="Логин", font=('Times New Roman', 15, 'bold'), fg='black', bg='yellow')
        name_3_lable.pack(pady=25)

        name_3_entry = tk.Entry(self, font=('Times New Roman', 15, 'bold'), bd='5', fg="black")
        name_3_entry.pack(pady=0)

        name_4_lable = tk.Label(self, text="Пароль", font=('Times New Roman', 15, 'bold'), fg='black', bg='yellow')
        name_4_lable.pack(pady=25)

        name_4_entry = tk.Entry(self, font=('Times New Roman', 15, 'bold'), bd='5', fg="black", show='*')
        name_4_entry.pack(pady=0)



        save_button = tk.Button(self, text="Добавить новую учетную запись", bd="5",
                                command=lambda: save(name_3_entry, name_4_entry),
                                bg="grey", width=25, font=('Times New Roman', 15, 'bold'), fg="white")
        save_button.pack()
        save_button.place(x=1070, y=730)

        def save(logins=tk.Entry, passwords=tk.Entry):
            SampleApp.login = logins.get()
            SampleApp.password = passwords.get()
            back()

        def back():
            controller.show_frame('StartPage')

        back_button = tk.Button(self, text='Назад', bd='5', command=back, font=('Times New Roman', 10, 'bold'),
                                fg='white',
                                bg='grey')
        back_button.pack(pady=30)
        back_button.place(x=10, y=10)


class MenuPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='orange')
        self.controller = controller
        big_lable = tk.Label(self, text="Добро пожаловать в \n Мир цветов !", font=('Times New Roman', 50, 'bold'),
                             fg='black',
                             bg='orange')
        big_lable.pack(pady=30)
        big_lable.place(x=500, y=300)

        def get_template():
            controller.show_frame('Tuvak')

        contact_button = tk.Button(self, text="Горшки ", bd='5', command=get_template,
                                   font=('Times New Roman', 10, 'bold'),
                                   fg='white', bg='grey')
        contact_button.pack(pady=30)
        contact_button.place(x=10, y=10)

        def get_clothes():
            controller.show_frame('Gul')

        contact_button = tk.Button(self, text="Цветы", bd='5', command=get_clothes,
                                   font=('Times New Roman', 10, 'bold'),
                                   fg='white',
                                   bg='grey')
        contact_button.pack(pady=30)
        contact_button.place(x=83, y=10)

        def get_subs():
            controller.show_frame('Buket')

        contact_button = tk.Button(self, text="Букеты", bd='5', command=get_subs,
                                   font=('Times New Roman', 10, 'bold'),
                                   fg='white',
                                   bg='grey')
        contact_button.pack(pady=30)
        contact_button.place(x=139, y=10)

        def get_help():
            controller.show_frame('Yordam')

        contact_button = tk.Button(self, text="Помощь", bd='5', command=get_help, font=('Times New Roman', 10, 'bold'),
                                   fg='white',
                                   bg='grey')
        contact_button.pack(pady=30)
        contact_button.place(x=1200, y=10)


class Tuvak(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="yellow")
        self.controller = controller
        self.controller.title("Цветочный магазин")
        self.controller.state('zoomed')

        big_lable = tk.Label(self, text='горшки для \n цветов', font=('Times New Roman', 50, 'bold'), fg='black',
                             bg='white')
        big_lable.pack(pady=30)
        text = tk.Label(self, text='', font=('Times New Roman', 12, 'bold'), fg='black', bg='white')
        text.pack(pady=30)

        def return_MenuPage():
            controller.show_frame('MenuPage')

        return_button = tk.Button(self, text='Назад', bd='5', command=return_MenuPage,
                                  font=('Times New Roman', 10, 'bold'),
                                  fg='white',
                                  bg='grey')
        return_button.pack(pady=300)
        return_button.place(x=10, y=10)

        def buy():
            askquestion('Купить', 'Вы хотите купить \nэтот горшок?')
            if True:
                showinfo('Купить', 'Спасибо за покупку.\nГоршок будет доставлен по вашему адресу.')

        tuvak1_button = tk.Button(self, text='Маленький горшок 30000 so\'m', bd='5', command=buy,
                                  font=('Times New Roman', 15, 'bold'),
                                  fg='black', bg='white')
        tuvak1_button.pack(pady=30)
        tuvak1_button.place(x=540, y=200)

        tuvak2_button = tk.Button(self, text='Средний горшок 50000 so\'m', bd='5', command=buy,
                                  font=('Times New Roman', 15, 'bold'), fg='black', bg='white')
        tuvak2_button.pack(pady=30)
        tuvak2_button.place(x=540, y=250)

        tuvak3_button = tk.Button(self, text='Большой горшок 100000 so\'m', bd='5', command=buy,
                                  font=('Times New Roman', 15, 'bold'),
                                  fg='black', bg='white')
        tuvak3_button.pack(pady=30)
        tuvak3_button.place(x=540, y=300)


class Gul(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="grey")
        self.controller = controller
        self.controller.title('Цветочный магазин')
        self.controller.state('zoomed')

        big_lable = tk.Label(self, text='Хотите купить цветы?\nПожалуйста', font=('Times New Roman', 50, 'bold'),
                             fg='black',
                             bg='white')
        big_lable.pack(pady=30)
        text = tk.Label(self, text='', font=('Times New Roman', 12, 'bold'), fg='black', bg='white')
        text.pack(pady=30)

        def return_MenuPage():
            controller.show_frame('MenuPage')

        return_button = tk.Button(self, text='Назад', bd='5', command=return_MenuPage,
                                  font=('Times New Roman', 10, 'bold'),
                                  fg='white',
                                  bg='grey')
        return_button.pack(pady=300)
        return_button.place(x=10, y=10)

        def buy():
            askquestion('Купить', 'Хотите купить\nэтот цветок?')
            if True:
                showinfo('Купить', 'Спасибо за покупку.\nЦветы будут доставлены по вашему адресу.')

        gul1_button = tk.Button(self, text='Тюльпан 50000 so\'m', bd='5', command=buy,
                                font=('Times New Roman', 15, 'bold'),
                                fg='black',
                                bg='white')
        gul1_button.pack(pady=30)
        gul1_button.place(x=540, y=200)

        gul2_button = tk.Button(self, text='Роза  10000 so\'m', bd='5', command=buy,
                                font=('Times New Roman', 15, 'bold'),
                                fg='black', bg='white')
        gul2_button.pack(pady=30)
        gul2_button.place(x=540, y=250)

        gul3_button = tk.Button(self, text='Пионы 15000 so\'m', bd='5', command=buy,
                                font=('Times New Roman', 15, 'bold'),
                                fg='black', bg='white')
        gul3_button.pack(pady=30)
        gul3_button.place(x=540, y=300)


class Buket(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="red")
        self.controller = controller
        self.controller.title('Цветочный магазин')
        self.controller.state('zoomed')

        big_lable = tk.Label(self, text='Красивые букеты', font=('Times New Roman', 50, 'bold'), fg='black',
                             bg='white')
        big_lable.pack(pady=30)
        text = tk.Label(self, text='', font=('Times New Roman', 12, 'bold'), fg='black', bg='white')
        text.pack(pady=30)

        def return_MenuPage():
            controller.show_frame('MenuPage')

        return_button = tk.Button(self, text='Назад', bd='5', command=return_MenuPage,
                                  font=('Times New Roman', 10, 'bold'),
                                  fg='white',
                                  bg='grey')
        return_button.pack(pady=300)
        return_button.place(x=10, y=10)

        def buy():
            askquestion('Купить', 'Хотите купить\nэтот цветок?')
            if True:
                showinfo('Купить', 'Спасибо за покупку.\nБукеты будут доставлены по вашему адресу.')

        buket1_button = tk.Button(self, text='Маленький букет 100000 so\'m', bd='5', command=buy,
                                  font=('Times New Roman', 15, 'bold'),
                                  fg='black', bg='white')
        buket1_button.pack(pady=30)
        buket1_button.place(x=540, y=200)

        buket2_button = tk.Button(self, text='Средний букет  150000 so\'m', bd='5', command=buy,
                                  font=('Times New Roman', 15, 'bold'), fg='black', bg='white')
        buket2_button.pack(pady=30)
        buket2_button.place(x=540, y=250)

        buket3_button = tk.Button(self, text='Большой букет 200000 so\'m', bd='5', command=buy,
                                  font=('Times New Roman', 15, 'bold'),
                                  fg='black', bg='white')
        buket3_button.pack(pady=30)
        buket3_button.place(x=540, y=300)


class Yordam(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg="white")
        self.controller = controller
        self.controller.title('Цветочный магазин')
        self.controller.state('zoomed')

        big_lable = tk.Label(self, text='Центр помощи', font=('Times New Roman', 50, 'bold'), fg='black', bg='white')
        big_lable.pack(pady=30)
        text = tk.Label(self, text='', font=('Times New Roman', 12, 'bold'), fg='black', bg='white')
        text.pack(pady=30)

        instruct_label = tk.Label(self,
                                  text="Добро пожаловать в Справочный центр!"
                                       "\nЗдесь вы найдете ответы на волнующие вас вопросы"
                                       "\nЕсли вы прошли список правильно,"
                                       "\nчто вам нужно от наших желаемых отделов"
                                       "\nкупить продукт"
                                       "\n\tAЕсли у вас есть другие вопросы, пожалуйста, свяжитесь с нами по адресу Flowers@gmail.com "
                                       "связь.",
                                  font=('Times New Roman', 20, 'bold'), fg='black', bg='white')
        instruct_label.pack(pady=30)
        instruct_label.place(x=270, y=200)

        def return_MenuPage():
            controller.show_frame('MenuPage')

        return_button = tk.Button(self, text='Назад', bd='5', command=return_MenuPage,
                                  font=('Times New Roman', 10, 'bold'),
                                  fg='white',
                                  bg='grey')
        return_button.pack(pady=300)
        return_button.place(x=10, y=10)


if __name__ == '__main__':
    app = SampleApp()
    app.mainloop()
