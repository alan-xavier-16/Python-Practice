from tkinter import Tk, BOTH, RAISED, LEFT
from tkinter.ttk import Frame, Label, Button
from PIL import Image, ImageTk
from random import randint


class Dice:
    dice = ["./assets/die1.PNG", "./assets/die2.PNG", "./assets/die3.PNG",
            "./assets/die4.PNG", "./assets/die5.PNG", "./assets/die6.PNG"]

    def __init__(self):
        """Initialize random die"""
        self.die = self.get_random()

    def get_random(self):
        """Get random die"""
        n = randint(0, len(self.dice)-1)
        return self.dice[n]


class DieRollingSim(Frame):
    """Overall class for simulator"""

    def __init__(self):
        """Initialize simulator"""
        super().__init__()
        self.die = Dice()
        self.initUI()

    def initUI(self):
        """Initiate UI"""
        self.master.title("Roll the Die")
        self._load_random_die_frame()
        self.pack(fill=BOTH, expand=1)
        self._load_btns_frame()

    def _load_random_die_frame(self):
        """Die interface"""
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)
        self._load_die_img()

    def _load_die_img(self):
        """Get random die img"""
        die_img = Image.open(self.die.get_random())
        die = ImageTk.PhotoImage(die_img)
        lbl = Label(self, image=die)
        lbl.image = die
        lbl.place(x=20, y=20)

    def _load_btns_frame(self):
        """Btns interface"""
        roll_Btn = Button(self, text="ROLL", command=self._load_die_img)
        roll_Btn.pack(side=LEFT, padx=5, pady=5)


def main():
    """Create Die Simulator using Tkinter"""
    root = Tk()
    root.geometry("350x350+300+300")
    app = DieRollingSim()
    root.mainloop()


if __name__ == "__main__":
    # Make a Simulator instance and run
    main()
