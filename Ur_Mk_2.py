import tkinter as tk
import random as rnd
import math as mth
import aggdraw as agg


def klyk(eff, a, b, c):
    mcvb(a, b, c)


def meiksq(a, b, c, d, e):

    g = tk.Canvas(board, width=100, height=100, bg=c, highlightthickness=1, highlightbackground='#000')
    if c == '#fea':
        leaf(g, 'red', 67)
        leaf(g, 'red', 157)
        leaf(g, 'red', 247)
        leaf(g, 'red', 337)

        leaf(g, 'blue', 22)
        leaf(g, 'blue', 112)
        leaf(g, 'blue', 202)
        leaf(g, 'blue', 292)

        g.create_oval(43, 43, 57, 57, fill='red', outline='blue')

    if d['c'] == 'D' or d['c'] == 'B':
        if d['c'] == 'D':
            x = '#fff'
        else:
            x = '#000'
        g.create_oval(20, 20, 80, 80, fill=x, outline=x)
        if c == '#00a' or c == '#a0f':
            dotmap(g, e)
        if x == rnumb.trn:
            g.bind('<Button-1>', lambda eff: klyk(eff, d['n'], rnumb.a, iface))
    g.grid(column=a, row=b)


def leaf(zgz, c, d):

    d -= 40
    d2 = d + 180

    rad = (d / 180) * mth.pi
    rad2 = ((d + 80) / 180) * mth.pi

    chordstartx = mth.cos(rad) * 35
    chordstarty = mth.sin(rad) * 35

    chordendx = mth.cos(rad2) * 35
    chordendy = mth.sin(rad2) * 35

    zgz.create_arc(15 - chordstartx, 15 + chordstarty, 85 - chordstartx, 85 + chordstarty, start=d, extent=80, fill=c, style=tk.CHORD, outline=c)
    zgz.create_arc(15 + chordendx, 15 - chordendy, 85 + chordendx, 85 - chordendy, start=d2, extent=80, fill=c, style=tk.CHORD, outline=c)


def dotmap(zgz, n):
    if n == 1:
        dot(zgz, 50, 50)
    if n == 2:
        dot(zgz, 50, 36)
        dot(zgz, 50, 64)
    if n == 3:
        dot(zgz, 50, 36)
        dot(zgz, 38, 57)
        dot(zgz, 62, 57)
    if n == 4:
        dot(zgz, 50, 36)
        dot(zgz, 36, 50)
        dot(zgz, 50, 64)
        dot(zgz, 64, 50)
    if n == 5:
        dot(zgz, 40, 40)
        dot(zgz, 60, 40)
        dot(zgz, 40, 60)
        dot(zgz, 60, 60)
        dot(zgz, 50, 50)
    if n == 6:
        dot(zgz, 50, 36)
        dot(zgz, 62, 43)
        dot(zgz, 62, 57)
        dot(zgz, 50, 64)
        dot(zgz, 38, 57)
        dot(zgz, 38, 43)
    if n == 7:
        dot(zgz, 36, 50)
        dot(zgz, 43, 62)
        dot(zgz, 57, 62)
        dot(zgz, 64, 50)
        dot(zgz, 57, 38)
        dot(zgz, 43, 38)
        dot(zgz, 50, 50)


def dot(zgz, a, b):
    zgz.create_oval(a - 5, b - 5, a + 5, b + 5, fill='#888', outline='#888')


class Blak:
    def __init__(self, x, y, tp, on, num, q):
        self.x = x
        self.y = y
        self.tp = tp
        self.on = on
        self.bid = {'c': on, 'n': num}
        self.q = q
        if self.tp == 'sp':
            c = '#fea'
        elif self.tp == 'bg':
            c = '#00a'
        elif self.tp == 'ed':
            c = '#a0f'
        else:
            c = '#feb'
        self.can = tk.Canvas(board, width=100, height=100, bg=c, highlightthickness=1, highlightbackground='#000')

    def rendr(self):
        self.can.delete('all')
        self.can.unbind('<Button-1>')
        self.can.grid_forget()
        if self.tp == 'sp':
            leaf(self.can, 'red', 67)
            leaf(self.can, 'red', 157)
            leaf(self.can, 'red', 247)
            leaf(self.can, 'red', 337)

            leaf(self.can, 'blue', 22)
            leaf(self.can, 'blue', 112)
            leaf(self.can, 'blue', 202)
            leaf(self.can, 'blue', 292)

            self.can.create_oval(43, 43, 57, 57, fill='red', outline='blue')

        if self.bid['c'] == 'D' or self.bid['c'] == 'B':
            if self.bid['c'] == 'D':
                x = '#fff'
            else:
                x = '#000'
            self.can.create_oval(20, 20, 80, 80, fill=x, outline=x)
            if self.tp == 'bg' or self.tp == 'ed':
                dotmap(self.can, self.q)
            if x == rnumb.trn:
                self.can.bind('<Button-1>', lambda eff: klyk(eff, self.bid['n'], rnumb.a, iface))
        self.can.grid(column=self.x, row=self.y)


class Bead:
    def __init__(self, c, pos, num):
        self.c = c
        self.pos = pos
        self.num = num

    def move(self, b):
        self.pos += b


class Sett:
    def __init__(self, a, trn, re, mode):
        self.a = a
        self.trn = trn
        self.re = re
        self.mode = mode


def setb():
    p[0].q = 0
    p[5].q = 0
    p[20].q = 0
    p[23].q = 0
    for n in bcoll:
        if n.pos == 0:
            p[0].q += 1
        if n.pos == 15:
            p[20].q += 1
    for n in rcoll:
        if n.pos == 0:
            p[5].q += 1
        if n.pos == 15:
            p[23].q += 1
    for n in range(16):
        p[pa[n]].bid['c'] = ' '
        p[pb[n]].bid['c'] = ' '
        for m in bcoll:
            if m.pos == n:
                p[pa[n]].bid['c'] = 'B'
                p[pa[n]].bid['n'] = m.num
        for m in rcoll:
            if m.pos == n:
                p[pb[n]].bid['c'] = 'D'
                p[pb[n]].bid['n'] = m.num


def mcvb(num, mcv, jface):

    mess.grid_forget()

    blocked = False
    coll = rcoll
    ocoll = bcoll
    rnumb.re = False

# Check for rolling zero
    if mcv != 0:
        # Set coll to current player's pieces and ocoll to opponent's
        if rnumb.trn == '#000':
            coll = bcoll
            ocoll = rcoll

        # bid is the space the piece would land on
        bid = coll[num].pos + mcv

        # Check for special space
        for n in spnumb:
            if bid == n:
                rnumb.re = True

        # Check for space is occupied by a friendly piece
        for n in coll:
            if n.pos == bid:
                if not bid == 15:
                    tvar.set('Blocked')
                    mess.grid(row=0, column=0)
                    blocked = True

        # Check for space is occupied by enemy piece
        for n in ocoll:
            if 4 < bid < 13 and bid == n.pos:
                if n.pos == 8:
                    tvar.set('Blocked')
                    mess.grid(row=0, column=0)
                    blocked = True
                else:
                    n.pos = 0

        # Check if the space is off the board
        if bid > 15:
            tvar.set('Overshoot')
            mess.grid(row=0, column=0)
            blocked = True

        # Check if piece is already in goal
        if coll[num].pos == 15:
            tvar.set('Already Scored')
            mess.grid(row=0, column=0)

    # If all checks out
    if not blocked:
        coll[num].move(mcv)

        # Checks if all pieces have scored
        win = True
        for n in coll:
            if not n.pos == 15:
                win = False
        if win:
            board.grid_forget()
            game.grid_forget()
            winscreen.grid()
            wincan.create_oval(20, 20, 80, 80, fill=rnumb.trn, outline=rnumb.trn)
            dotmap(wincan, 7)
            x = [22, 36, 50, 64, 78]
            x2 = [31, 43, 57, 69]
            y = [14, 4, 24]
            wincan.create_polygon(29, 30, x[0], y[0], x2[0], y[2], x[1], y[0], x2[1], y[2], x[2], y[1], x2[2], y[2], x[3], y[0], x2[3], y[2], x[4], y[0], 71, 30, fill='#ca0')
            for m in range(5):
                j = 0
                if m == 2:
                    j = 1
                wincan.create_oval(x[m] - 2, y[j] - 2, x[m] + 2, y[j] + 2, fill='#ca0', outline='#ca0')
            reset(jface)
        setb()
        doroll(jface)
        massrend()


def massrend():

    for w in p:
        w.rendr()


def doroll(kface):

    if not rnumb.re:
        if rnumb.trn == '#fff':
            rnumb.trn = '#000'
        else:
            rnumb.trn = '#fff'
    displ = ''
    nf = 0
    for n in range(4):
        if rnd.randint(0, 1) == 1:
            nf += 1
            displ += '\u26ab'
        else:
            displ += '\u26aa'
        if n < 3:
            displ += '\n'
    rnumb.a = nf

    game.configure(bg=rnumb.trn)
    kface[1].configure(bg=rnumb.trn, text=displ)
    for zxz in range(0, 3):
        kface[zxz].configure(bg=rnumb.trn)

    if not valid(nf):
        if not nf == 0:
            tvar.set('No Valid Moves\nPress \u2205 To Pass')
            mess.grid(row=0, column=0)

    if rnumb.trn == '#000' and rnumb.mode == 1:
        mcvb(rnd.randint(0, 6), rnumb.a, kface)


def valid(num):

    coll = rcoll
    ocoll = bcoll

    if rnumb.trn == '#000':
        coll = bcoll
        ocoll = rcoll

    for n in coll:
        if not n.pos == 15:
            valyd = True
            bid = n.pos + num

            for m in coll:
                if bid == m.pos and m.pos < 15:
                    valyd = False

            if bid > 15:
                valyd = False

            if bid == 8:
                for m in ocoll:
                    if m.pos == 8:
                        valyd = False

            if valyd:
                return True
    return False


def passon(mcv):

    if valid(mcv):
        tvar.set('One Or More Valid Moves')
        mess.grid(row=0, column=0)
    else:
        mess.grid_forget()
        rnumb.re = False
        doroll(iface)
        massrend()


def reset(jface):
    mess.grid_forget()
    for n in rcoll:
        n.pos = 0
    for n in bcoll:
        n.pos = 0

    setb()
    massrend()
    doroll(jface)


def showboard(x):
    if x == 1:
        rnumb.mode = 1
    startscreen.grid_forget()
    board.grid(row=0, column=0)
    game.grid(row=0, column=1, sticky='ewns')


def goback():
    winscreen.grid_forget()
    startscreen.grid()


root = tk.Tk()
root.wm_title('Ur')
game = tk.Frame(root, bg='black')

startscreen = tk.Frame(root, bg='black', bd=10)
titlecard = tk.Label(startscreen, bg='#000', fg='#fff', text='The Royal Game of Ur', width=23, height=6)
vs = tk.Label(startscreen, bg='#000', fg='#fff', text='vs')
hvh = tk.Button(startscreen, text='Human', command=lambda: showboard(2), activebackground='#fa0', borderwidth=0)
hvc = tk.Button(startscreen, text='Computer', command=lambda: showboard(1), state=tk.DISABLED, borderwidth=0)

titlecard.grid(row=0, columnspan=3)
vs.grid(row=1, column=0)
hvh.grid(row=1, column=1)
hvc.grid(row=1, column=2)
startscreen.grid()

winscreen = tk.Frame(root, bg='#60a', bd=10)
wincard = tk.Label(winscreen, bg='#60a', fg='#ca0', text='Congratulations', width=30, height=3)
wincan = tk.Canvas(winscreen, width=100, height=100, bg='#60a', highlightbackground='#60a')
backbtn = tk.Button(winscreen, text='Back to Menu', command=goback, borderwidth=0, bg='#fff')

wincard.grid(row=0)
wincan.grid(row=1)
backbtn.grid(row=2)

board = tk.Frame(root, highlightthickness=0, bg='#000')

tvar = tk.StringVar()
tvar.set('Default')
mess = tk.Label(root, textvariable=tvar, bg='#000', fg='#fff')


rnumb = Sett(0, '#fff', False, 2)

bead1 = Bead('D', 0, 0)
bead2 = Bead('D', 0, 1)
bead3 = Bead('D', 0, 2)
bead4 = Bead('D', 0, 3)
bead5 = Bead('D', 0, 4)
bead6 = Bead('D', 0, 5)
bead7 = Bead('D', 0, 6)

read1 = Bead('B', 0, 0)
read2 = Bead('B', 0, 1)
read3 = Bead('B', 0, 2)
read4 = Bead('B', 0, 3)
read5 = Bead('B', 0, 4)
read6 = Bead('B', 0, 5)
read7 = Bead('B', 0, 6)

bcoll = [bead1, bead2, bead3, bead4, bead5, bead6, bead7]
rcoll = [read1, read2, read3, read4, read5, read6, read7]


s0a = Blak(4, 0, 'bg', 'None', 0, 0)
s1a = Blak(3, 0, '', 'None', 0, 0)
s2a = Blak(2, 0, '', 'None', 0, 0)
s3a = Blak(1, 0, '', 'None', 0, 0)
s4a = Blak(0, 0, 'sp', 'None', 0, 0)

s0b = Blak(4, 2, 'bg', 'None', 0, 0)
s1b = Blak(3, 2, '', 'None', 0, 0)
s2b = Blak(2, 2, '', 'None', 0, 0)
s3b = Blak(1, 2, '', 'None', 0, 0)
s4b = Blak(0, 2, 'sp', 'None', 0, 0)

s5 = Blak(0, 1, '', 'None', 0, 0)
s6 = Blak(1, 1, '', 'None', 0, 0)
s7 = Blak(2, 1, '', 'None', 0, 0)
s8 = Blak(3, 1, 'sp', 'None', 0, 0)
s9 = Blak(4, 1, '', 'None', 0, 0)
s10 = Blak(5, 1, '', 'None', 0, 0)
s11 = Blak(6, 1, '', 'None', 0, 0)
s12 = Blak(7, 1, '', 'None', 0, 0)

s13a = Blak(7, 0, '', 'None', 0, 0)
s14a = Blak(6, 0, 'sp', 'None', 0, 0)
s15a = Blak(5, 0, 'ed', 'None', 0, 0)

s13b = Blak(7, 2, '', 'None', 0, 0)
s14b = Blak(6, 2, 'sp', 'None', 0, 0)
s15b = Blak(5, 2, 'ed', 'None', 0, 0)


p = [s0a, s1a, s2a, s3a, s4a, s0b, s1b, s2b, s3b, s4b, s5, s6, s7, s8, s9,
     s10, s11, s12, s13a, s14a, s15a, s13b, s14b, s15b]

pa = [0, 1, 2, 3, 4, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
pb = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 21, 22, 23]
spnumb = [4, 8, 14]

pazz = tk.Button(game, text='\u2205', font=('Arial', 25), relief=tk.FLAT, bg=rnumb.trn, fg='#888', command=lambda: passon(rnumb.a))
lab = tk.Label(game, text='', bg=rnumb.trn, fg='#888', font=('Helvetica', 25))
rset = tk.Button(game, text='\u2b6f', font=('Helvetica', 20), relief=tk.FLAT, bg=rnumb.trn, fg='#888', command=lambda: reset(iface))
iface = [pazz, lab, rset]

for z in range(3):
    iface[z].grid(row=z, column=0, padx=1)


setb()
doroll(iface)
massrend()

root.iconbitmap(r'royalmini.ico')
root.mainloop()
