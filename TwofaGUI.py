from tkinter import *
from TwoFactorAuthentication import TwoFA
from StockGeniusGUI import StockGeniusGUI
class TwoFAGUI:
#2fa doesnt work todo
#manage automatiton - charge a fee once a month
#before letting login check if person paid this month
#save first payment and then a month from that every time
#button on error message terminates everything (maybe just close no destory?) and stockgui still doesnt work properly
    def __init__(self, rcv_email):
        self.rcv_email = rcv_email

    def run(self):
        def btn_clicked():
            print("Button Clicked")
            t1 = TwoFA()
            inp = entry0.get()
            print('key2: ' + str(key))
            access = t1.validate_totp(inp, key)
            print(access)
            if access == True:
                window.destroy()
                m = StockGeniusGUI()
                m.run()



        t = TwoFA()

        key = t.generate_shared_secret()
        print('key1: ' + str(key))
        totp = t.generate_totp(key)
        t.send_email(totp, self.rcv_email, "roypinhas78@gmail.com", '04042004')
        window = Tk()

        window.geometry("232x249")
        window.configure(bg = "#000000")
        canvas = Canvas(
            window,
            bg = "#000000",
            height = 249,
            width = 232,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)

        background_img = PhotoImage(file =f"background1.png")
        background = canvas.create_image(
            115.5, 66.5,
            image=background_img)

        entry0_img = PhotoImage(file = f"img_textBox01.png")
        entry0_bg = canvas.create_image(
            115.5, 142.5,
            image = entry0_img)

        entry0 = Entry(
            bd = 0,
            bg = "#d2d2d2",
            highlightthickness = 0)

        entry0.place(
            x = 47.5, y = 124,
            width = 136.0,
            height = 35)

        img0 = PhotoImage(file =f"img01.png")
        b0 = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = btn_clicked,
            relief = "flat")

        b0.place(
            x = 61, y = 192,
            width = 99,
            height = 37)

        window.resizable(False, False)
        window.mainloop()

f = TwoFAGUI("royp444@gmail.com")
f.run()