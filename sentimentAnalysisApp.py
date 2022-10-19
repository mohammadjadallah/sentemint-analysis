# GUI Application
"""
Packages
  - tkinter
  - textblob

user inputs some text and the app will read the text
then return the the rate of sentiment as a label


"""
# global variables
start_btn = None
text = None

class App:
    """

       Sentiment anaysis application
     _________________________________
     1. how to use:
        1. hit start when window of the application opened
        2. write your text in the text box
        3. hit analyze
     2. You will see a small if screen that show your result
        1. if the polarity > 0, so your text is positive
        2. if the polarity < 0, so your text is negative
        3. if the polarity = 0, so your text is natural

    it is easy, so what are you wait, get started!

    """
    def __init__(self, img_background1, img_background2):
        self.root = Tk()
        self.root.title("Sentiment Analysis App")
        self.geometry = self.root.geometry("700x600")
        self.photo = PhotoImage(file=img_background1)
        self.bgmain = PhotoImage(file=img_background2)
        self.screen_background = Label(self.root, image=self.photo)
        self.main_screen_background = Label(self.root, image=self.bgmain)
        self.screen_background.pack()
        self.root.resizable(False, False)
        self.splash_screen()

    def splash_screen(self):
        # create a button to start the game
        global start_btn
        start_btn = Button(self.root, text='Getting Started', font="arial 25 bold",
                           relief=SOLID, bd=0, fg='#4D0FD3', highlightcolor="#a1b0e4",
                           activeforeground='#183AC6', cursor="hand2",
                           default='active', highlightthickness=4, command=self.destroied)

        start_btn.place(x=200, y=150, width=300, height=100)

    def destroied(self):
        start_btn.destroy()
        self.screen_background.destroy()
        self.main_screen()

    def main_screen(self):
        self.main_screen_background.place(x=0, y=0)

        Label(self.root, text="Write your text below",
              font=("arial", 20, 'bold'), background='#510CCF',
              fg='#FFEB2D').place(x=220, y=10)

        frame_textbox = Frame(self.root)
        frame_textbox.place(x=100, y=60, width=500, height=300)

        yscrollbar = Scrollbar(frame_textbox)
        yscrollbar.pack(side=RIGHT, fill=Y)

        text_box = Text(frame_textbox, font="arial 15 bold", wrap="word",
                        yscrollcommand=yscrollbar.set, undo=True, selectbackground='#b4a7e0',
                        selectforeground='black', background='#E6E6E6', highlightbackground='#7152AB',
                        bd=0, highlightcolor='#6743A8', highlightthickness=4, spacing1=5, insertbackground="#7593FE")
        # highlightcolor: عند الضغط كيف سيصبح لون البوردر
        # highlightbackground: قبل الضغط كيف سيكون لون البوردر
        # highlightthickness: الخمالة للبوردر
        text_box.place(x=0, y=0, width=485, height=300)

        yscrollbar.configure(command=text_box.yview)

        # button play "Analayze"
        def analyzing():
            global text
            text = text_box.get(0.0, 'end-1c').strip()
            text = ''.join(text.replace("\n", ""))
            # initialize textblob object --> Textblob(sentence)
            # we must put the sentance inside the class parantheses
            blob = TextBlob(text)
            # find the polarity
            result = blob.sentiment.polarity
            if len(text) > 0:
                if result > 0:
                    showinfo("Sentiment Analysis", "That is good: \"Positive\" ")
                elif result < 0:
                    showinfo("Sentiment Analysis", "That is bad: \"Negative\" ")
                else:
                    showinfo("Sentiment Analysis", "That is moderate: \"Natural\" ")
                print(blob.sentiment.polarity)
            else:
                showwarning("Sentiment Analysis", "Write your text")


        analyze_btn = Button(self.root, text="Analyze", font="arial 25 bold",
                             relief=SOLID, bd=0, fg='#4D0FD3', highlightcolor="#7152AB",
                             activeforeground='#183AC6', cursor="hand2",
                             default='active', highlightthickness=4, command=analyzing)
        analyze_btn.place(x=280, y=380, width=150, height=50)


    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    from tkinter import *
    from tkinter.messagebox import showinfo, showwarning
    from textblob import TextBlob

    app = App("SentimentAnalysis.png", "background.png")
    app.run()
