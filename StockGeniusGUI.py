from tkinter import *
import tkinter as tk
import csv
import yfinance as yf
import urllib
import json
from BankClient import BankClient
from Portfolio import Portfolio
from UserClient import UserClient
from tkinter import messagebox
from PriceDATABASEclient import PriceClient
from MonthlyPayment import MonthlyPayment

class StockGeniusGUI:

    def __init__(self):


        root = Tk()
        self.opening_slide(root)
        root.geometry("1000x600")

        root.mainloop()

    def create_csvarray(self):

        with open('/Users/roypinhas/Desktop/pythonProject/symbols2.csv') as f:
            reader = csv.reader(f)
            data = [tuple(row)[0] for row in reader]
        return data

    def opening_slide(self,window):
        def signup_btn_clicked():
            self.signup_slide(window)


        def login_btn_clicked():
            print("login Clicked")
        window.geometry("1000x600")
        window.configure(bg="#000000")
        canvas = Canvas(
            window,
            bg="#000000",
            height=600,
            width=1000,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        canvas.place(x=0, y=0)

        img0 = PhotoImage(file=f"openingimg0.png")

        signup_b = Button(
            image=img0,
            bg="#000000",
            borderwidth=0,
            highlightthickness=0,
            command=signup_btn_clicked,
            relief="flat")
        signup_b.image = img0

        signup_b.place(
            x=226, y=449,
            width=248,
            height=70)

        img1 = PhotoImage(file=f"openingimg1.png")
        login_b = Button(
            image=img1,
            borderwidth=0,
            highlightthickness=0,
            command=login_btn_clicked,
            relief="flat")
        login_b.image=img1

        login_b.place(
            x=501, y=449,
            width=248,
            height=70)

        background_img = PhotoImage(file=f"openingbackground.png")
        background = canvas.create_image(
            486.0, 195.0,
            image=background_img)
        canvas.image = background_img

        window.resizable(False, False)

    def signup_slide(self,window):

        def signup_btn_clicked():
            username_input = entry0.get().replace(" ", "")
            password_input = entry2.get().replace(" ", "")
            email_input = entry1.get().replace(" ", "")

            client = UserClient('SIGNUP',username=username_input, password=password_input, email=email_input)
            client_answer = client.run()

            if client_answer == 'True':
                self.payment_slide(window,username_input, True)

            elif client_answer == 'exists':
                messagebox.showerror("showerror", "Username Already Exists.")
            else:
                messagebox.showerror("showerror", "Invalid Credentials.")
        def login_btn_clicked():
            print("login btn clicked")
        window.geometry("1000x600")
        window.configure(bg="#000000")
        canvas = Canvas(
            window,
            bg="#000000",
            height=600,
            width=1000,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        canvas.place(x=0, y=0)

        background_img = PhotoImage(file=f"signupbackground.png")
        background = canvas.create_image(
            535.0, 297.5,
            image=background_img)
        canvas.image = background_img
        img0 = PhotoImage(file=f"signupimg0.png")
        signup_b = Button(
            image=img0,
            borderwidth=0,
            highlightthickness=0,
            command=signup_btn_clicked,
            relief="flat")
        signup_b.image = img0
        signup_b.place(
            x=77, y=411,
            width=263,
            height=39)

        img1 = PhotoImage(file=f"signupimg1.png")
        login_b = Button(
            image=img1,
            borderwidth=0,
            highlightthickness=0,
            command=login_btn_clicked,
            relief="flat")
        login_b.image = img1
        login_b.place(
            x=159, y=468,
            width=88,
            height=20)

        entry0_img = PhotoImage(file=f"signupimg_textBox0.png")
        entry0_bg = canvas.create_image(
            203.5, 243.5,
            image=entry0_img)

        entry0 = Entry(
            bd=0,
            bg="#ffffff",
            highlightthickness=0)
        entry0.image = entry0_img
        entry0.place(
            x=91.5, y=224,
            width=224.0,
            height=37)

        entry1_img = PhotoImage(file=f"signupimg_textBox1.png")
        entry1_bg = canvas.create_image(
            208.5, 373.5,
            image=entry1_img)

        entry1 = Entry(
            bd=0,
            bg="#ffffff",
            highlightthickness=0)
        entry1.image = entry1_img
        entry1.place(
            x=96.5, y=354,
            width=224.0,
            height=37)

        entry2_img = PhotoImage(file=f"signupimg_textBox2.png")
        entry2_bg = canvas.create_image(
            203.5, 308.5,
            image=entry2_img)

        entry2 = Entry(
            show='*',
            bd=0,
            bg="#ffffff",
            highlightthickness=0)
        entry2.image = entry2_img
        entry2.place(
            x=91.5, y=289,
            width=224.0,
            height=37)

        window.resizable(False, False)

    def payment_slide(self,window, username, pay):

        def btn_clicked():
            print("Button Clicked")
            creditcard_num = entry0.get().replace(" ","")
            expiration_date = entry1.get().replace(" ","")
            security_code = entry2.get().replace(" ","")
            print(creditcard_num)
            print(expiration_date)
            p = UserClient('PAYMENT',username =username, creditcard_num = creditcard_num, expiration_date=expiration_date, security_code=security_code).run()
            print('p:' + str(p))
            price_per_month = MonthlyPayment().MONTHLY_PRICE

            if pay == True:
                if p == 'True':
                    b = BankClient('CHANGE',creditcard_number=creditcard_num, expiration_date=expiration_date, security_code=security_code,sum=price_per_month).run()
                    if b == 'True':
                        print('in')
                        self.into_slide(window,username)
                    else:
                        BankClient('CREATE',creditcard_number=creditcard_num, expiration_date=expiration_date, security_code=security_code).run()
                        BankClient('CHANGE',creditcard_number=creditcard_num, expiration_date=expiration_date,
                                        security_code=security_code,sum=price_per_month).run()
                        self.into_slide(window, username)

                else:
                    messagebox.showerror("showerror", "The entered credentials \n are not valid")
            else:
                if p == 'True':
                    b = BankClient('CHANGE', creditcard_number=creditcard_num, expiration_date=expiration_date,
                               security_code=security_code, sum=0).run()
                    if b == 'True':
                        self.main_page(window,username)
                    else:
                        BankClient('CREATE', creditcard_number=creditcard_num, expiration_date=expiration_date,
                               security_code=security_code).run()

                        self.main_page(window, username)

                else:
                    messagebox.showerror("showerror", "The entered credentials \n are not valid")

        window.geometry("1000x600")
        window.configure(bg="#000000")
        canvas = Canvas(
            window,
            bg="#000000",
            height=600,
            width=1000,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        canvas.place(x=0, y=0)

        entry0_img = PhotoImage(file=f"paymentimg_textBox0.png")
        entry0_bg = canvas.create_image(
            218.0, 268.5,
            image=entry0_img)

        entry0 = Entry(
            bd=0,
            bg="#313131",
            highlightthickness=0)
        entry0.image = entry0_img
        entry0.place(
            x=74.5, y=251,
            width=287.0,
            height=33)




        entry1_img = PhotoImage(file=f"paymentimg_textBox1.png")
        entry1_bg = canvas.create_image(
            126.5, 345.5,
            image=entry1_img)

        entry1 = Entry(
            bd=0,
            bg="#313131",
            highlightthickness=0)
        entry1.image = entry1_img
        entry1.place(
            x=74.5, y=328,
            width=104.0,
            height=33)

        entry2_img = PhotoImage(file=f"paymentimg_textBox2.png")
        entry2_bg = canvas.create_image(
            297.5, 345.5,
            image=entry2_img)

        entry2 = Entry(
            bd=0,
            bg="#313131",
            highlightthickness=0)
        entry1.image = entry1_img
        entry2.place(
            x=245.5, y=328,
            width=104.0,
            height=33)

        background_img = PhotoImage(file=f"paymentbackground.png")
        background = canvas.create_image(
            220.0, 234.5,
            image=background_img)
        canvas.image = background_img
        img0 = PhotoImage(file=f"paymentimg0.png")
        b0 = Button(
            image=img0,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked,
            relief="flat")
        b0.image = img0
        b0.place(
            x=144, y=399,
            width=139,
            height=35)

        window.resizable(False, False)

    def into_slide(self, window,username):
        def btn_clicked():
            self.main_page(window,username)
        window.geometry("1000x600")
        window.configure(bg="#000000")
        canvas = Canvas(
            window,
            bg="#000000",
            height=600,
            width=1000,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        canvas.place(x=0, y=0)

        background_img = PhotoImage(file=f"introbackground.png")
        background = canvas.create_image(
            494.0, 255.5,
            image=background_img)
        canvas.image = background_img
        img0 = PhotoImage(file=f"introimg0.png")
        b0 = Button(
            image=img0,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked,
            relief="flat")
        b0.image = img0
        b0.place(
            x=374, y=494,
            width=267,
            height=58)

        window.resizable(False, False)

    def Update(self,listbox,data):

            listbox.delete(0, 'end')

            # put new data
            for item in data:
                listbox.insert('end', item)

    def stock_page(self, username, window2, symbol,lb):
        def get_symbol(symbol):

            response = urllib.request.urlopen(f'https://query2.finance.yahoo.com/v1/finance/search?q={symbol}')
            content = response.read()
            data = json.loads(content.decode('utf8'))['quotes'][0]['shortname']
            return data

        def btn_clicked1():
            print("plus Clicked")
            p = Portfolio(username)
            p.add_symbol(symbol)
            print("symbol added to this user's Portfolio!")

            list = UserClient('GETPORTFOLIO',username=username).run()

            self.Update(lb,list)


        def btn_clicked2():
            print("arrow Clicked")

        def on_closing():
            print("destoryed")
            window2.destroy()

        # window2 = Tk()
        # window2 = tk.Toplevel()
        window2.grab_set()
        window2.bind()
        window2.protocol("WM_DELETE_WINDOW", on_closing)
        window2.geometry("400x463")
        window2.configure(bg="#070707")
        canvas2 = Canvas(
            window2,
            bg="#000000",
            height=463,
            width=400,
            bd=0,
            highlightthickness=0,
            relief="ridge")
        canvas2.place(x=0, y=0)


        img12 = PhotoImage(file=f"img1S.png")
        b12 = Button(
            window2,
            image=img12,
            # bg=img12,
            borderwidth=0,
            highlightthickness=0,
            command=btn_clicked1,
            relief="flat")
        # b12.pack(side=tk.TOP, anchor=NE)
        b12.image = img12

        b12.place(

            x=344, y=16,
            width=37,
            height=33)

        l2 = tk.Label(window2, text=symbol)
        l2.config(font=("Arial bold", 32), bg="black", fg="light grey")
        l2.place(x=45,
                 y=55,
                 )
        short_symbol_name = yf.Ticker(symbol).info['shortName']
        l23 = tk.Label(window2, text=str(short_symbol_name))
        l23.config(font=("Arial", 14), bg="black", fg="light grey")
        l23.place(x=45,
                  y=104,
                  )
        # todo - threads
        data = yf.download(symbol)
        price = data['Adj Close'][len(data)-1]
        l245 = tk.Label(window2, text=str(price))
        l245.config(font=("Arial", 38), bg="black", fg="light grey")
        l245.place(x=215,
                   y=55,
                   )
        l24 = tk.Label(window2, text="Price In:")
        l24.config(font=("Arial", 25), bg="black", fg="light grey")
        l24.place(x=30,
                  y=400,
                  )

        ##############
        OPTIONS = [
            "Pick A Day",
            "-1 Day",
            "-2 Days",
            "-3 Days",
            "-4 Days",
            "-5 Days",
            "-6 Days",
            "-7 Days",
            "1 Day",
            "2 Days",
            "3 Days",
            "4 Days",
            "5 Days",
            "6 Days",
            "7 Days"
        ]  # etc

        variable = StringVar(window2)
        variable.set(OPTIONS[0])  # default value

        w = OptionMenu(window2, variable, *OPTIONS).place(x=140, y=370)


        def btn_clicked3():
            print('clicked' + str(variable.get()))
            if variable.get() != OPTIONS[0]:
                lp = tk.Label(window2, text=PriceClient('GETPRICE',symbol=symbol,days=variable.get().split(' ')[0]).run())
                lp.config(font=("Arial", 25), bg="black", fg="light grey")
                lp.place(x=50,
                        y=420,
                        )


        b1 = Button(window2,
                    bg='#000000',
                    borderwidth=0,
                    highlightthickness=0,
                    command=btn_clicked3,
                    relief="flat",
                    text="Calculate",

                    )
        b1.place(
            x=220, y=400,
            width=70, height=20
        )
        print(variable.get())
        window2.resizable(False, False)
    def main_page(self,window,username):


        def double_left_click_suggestions(event):

            print('lefts')
            print(listbox3.get(ANCHOR))
            top = tk.Toplevel(window)
            s = self.stock_page(username, top,listbox3.get(ANCHOR),listbox2 )
            #s.run()
            listbox3.place_forget()

        def double_left_click_portfolio(event):

            print('left')
            print(listbox2.get(ANCHOR))
            top = tk.Toplevel(window)
            s = self.stock_page(username, top,listbox2.get(ANCHOR), listbox2)
            #s.run()
            listbox2.place_forget()

        def double_left_click(event):

            print('left')
            print(listbox.get(ANCHOR))
            top = tk.Toplevel(window)
            s = self.stock_page(username, top,listbox.get(ANCHOR), listbox2)
            #s.run()
            listbox.place_forget()

        def right_click(event):
            print('right')

        def btn_clicked():
            print("listbox8")
            listbox8.place(x=800,y=100)


        #window = Tk()

        window.geometry("1000x600")
        window.configure(bg = "#000000")
        canvas = Canvas(
            window,
            bg = "#000000",
            height = 600,
            width = 1000,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        def left_click(event):

            if not isinstance(event.widget, type(entry)) and not isinstance(event.widget, type(listbox)) and not isinstance(event.widget, type(b8)):
                listbox.pack_forget()
                listbox8.place_forget()
        window.bind("<Button-3>", right_click)
        window.bind("<Button-1>",left_click)

        background_img = PhotoImage(file = f"backgrounddd.png")
        background = canvas.create_image(
            524.0, 330.5,
            image=background_img)
        canvas.image = background_img


        l = tk.Label(window, text="Portfolio")
        l.config(font=("Arial bold", 32), bg="black", fg="white")
        l.place(x=70,
                y=55,
                )

        l4 = tk.Label(window, text="Suggestions")
        l4.config(font=("Arial bold", 32), bg="black", fg="white")
        l4.place(x=480,
                y=55,
                )

        l5 = tk.Label(window, text="Symbol")
        l5.config(font=("Arial bold", 20), bg="#313131", fg="light grey")
        l5.place(x=480,
                 y=130,
                 )

        l6 = tk.Label(window, text="Accuracy")
        l6.config(font=("Arial bold", 20), bg="#313131", fg="light grey")
        l6.place(x=600,
                 y=130,
                 )



        def open_list(event):
            print('forget')
            listbox.place()
            listbox.pack()

        def Scankey(event):

            val = event.widget.get()
            print(val)

            if val == '':
                data = list
            else:
                data = []
                for item in list:
                    if val.lower() in item.lower():
                        data.append(item)

            Update(listbox,data)

        def Update(listbox,data):

            listbox.delete(0, 'end')

            # put new data
            for item in data:
                listbox.insert('end', item)

        list = self.create_csvarray()
        print(list)
        ''''('C', 'C++', 'Java',
                'Python', 'Perl',
                'PHP', 'ASP', 'JS','s','v','b','c')

'''

        def double_left_click_settings(event):
            selection = listbox8.get(ANCHOR)
            if selection == 'Change form\n of Payment':
                self.payment_slide(window,username,False)
            if selection == 'Cancel Subscription':
                UserClient('CANCEL',username=username).run()

        b8 = Button(window,
                    bg='#000000',
                    borderwidth=0,
                    highlightthickness=0,
                    command=btn_clicked,
                    relief="flat",
                    text="o",
                    fg = 'white'

                    )
        b8.place(
            x=970, y=10,
            width=20, height=20
        )

        listbox8 = Listbox(window, bg='#313131', fg='white')

        listbox8.place_forget()
        listbox8.bind("<Double-1>", double_left_click_settings)

        # listbox.pack()
        listbox8.bind()
        options = ['Change form\n of Payment', 'Cancel Subscription']
        Update(listbox8, options)




        entry = Entry(window, bg='#313131',fg='white')
        entry.pack()
        entry.bind('<KeyRelease>', Scankey)
        entry.bind('<Button-1>', open_list)

        listbox = Listbox(window, bg='#313131',fg='white')

        listbox.place_forget()
        listbox.bind("<Double-1>", double_left_click)

        #listbox.pack()
        listbox.bind()
        Update(listbox,list)


        #portfolio - todo make client server nopt use portfolio directly
        portfolio_list =  UserClient('GETPORTFOLIO',username = username).run()
        print('p')
        print(portfolio_list)
        listbox2 = Listbox(window, height=10,
                          width=10,
                          bg="#313131",
                          activestyle='dotbox',
                          font=("Helvetica",20),
                          fg="#FFFFFF")


        listbox2.bind("<Double-1>", double_left_click)

        listbox2.place(x=100, y=130)
        listbox2.bind()

        Update(listbox2, portfolio_list)


        r = PriceClient('GETSUGGESTIONS',symbols='/ Users / roypinhas / Desktop / pythonProject/symbols2.csv')#todo
        a = r.run()
        print('--------a--------: '  +str(a))
        listbox3 = Listbox(window, height=10,
                           width=10,
                           bg="#313131",
                           activestyle='dotbox',
                           font=("Helvetica", 20),
                           fg="white",

                           )

        listbox3.bind("<Double-1>", double_left_click_suggestions)

        listbox3.place(x=500, y=200)
        listbox3.bind()

        print(a)
        Update(listbox3, a)



        # create a root window.
        def open_list8(event):
            print('forget')
            listbox8.place()
            listbox8.pack()

        window.resizable(False, False)

