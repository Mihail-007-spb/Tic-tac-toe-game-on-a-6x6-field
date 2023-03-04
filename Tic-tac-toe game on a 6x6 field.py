"""Tic-tac-toe game on a 6x6 field.
The image and sound files are located in the repository by
name 'Image-and-sound-for-the-published-repositories'"""


"""Игра крестики-нолики на поле 6х6.
Файлы изображения и звука находятся в repository по имени
 'Image-and-sound-for-the-published-repositories'"""


from tkinter import *
import random
import winsound
import threading
from multiprocessing import Process


def musika_clik_igrok_m():
    w = Process(target=musika_clik_igrok)
    w.daemon = True
    w.start()


def musika_clik_comp_m():
    w = Process(target=musika_clik_comp)
    w.daemon = True
    w.start()


def musika_clik_comp_p():
    thr_p5 = threading.Thread(target=musika_clik_comp).start()


def musika_win_comp_p():
    thr_p1 = threading.Thread(target=musika_win_comp).start()


def musika_win_igrok_p():
    thr_p2 = threading.Thread(target=musika_win_igrok).start()


def musika_clik_igrok_p():
    thr_p3 = threading.Thread(target=musika_clik_igrok).start()


def musika_win_comp():
    winsound.PlaySound(r"C:\\FOTO  Python\\poragen igr.wav",
                       winsound.SND_FILENAME)


def musika_win_igrok():
    winsound.PlaySound(r"C:\\FOTO  Python\\pobeda igr.wav",
                       winsound.SND_FILENAME)


def musika_clik_comp():
    winsound.PlaySound(r"C:\\FOTO  Python\\clik computer.wav",
                       winsound.SND_FILENAME)


def musika_clik_igrok():
    winsound.PlaySound(r"C:\\FOTO  Python\\clik igroka.wav",
                       winsound.SND_FILENAME)


def new_game(event):
    for row in range(6):
        for col in range(6):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = '#add6b8'

    global game_run
    game_run = True
    global cross_count
    cross_count = 0
    c.itemconfig('new', state='hidden')

    row = random.randint(2, 3)
    col = random.randint(2, 3)
    field[row][col]['text'] = 'O'
    print('Случайно')
    check_win('O')


def click(row, col):

    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global cross_count
        cross_count += 1
        musika_clik_igrok_m()
        check_win('X')
        
        if game_run and cross_count < 18:
            computer_move()
            check_win('O')


def check_win(smb): # ПРОВЕРЕНО 100%
    for n in range(6):

        check_line(field[n][0], field[n][1], field[n][2],
                   field[n][3], smb)

        check_line(field[n][1], field[n][2], field[n][3],
                   field[n][4], smb)

        check_line(field[n][2], field[n][3], field[n][4],
                   field[n][5], smb)
        #####
        check_line(field[0][n], field[1][n], field[2][n],
                   field[3][n], smb)

        check_line(field[1][n], field[2][n], field[3][n],
                   field[4][n], smb)

        check_line(field[2][n], field[3][n], field[4][n],
                   field[5][n], smb)

    #### БОЛЬШАЯ ДИАГОНАЛЬ 1
    check_line(field[0][0], field[1][1], field[2][2],
               field[3][3], smb)

    check_line(field[1][1], field[2][2], field[3][3],
               field[4][4], smb)

    check_line(field[2][2], field[3][3], field[4][4],
               field[5][5], smb)

    ##### БОЛЬШАЯ ДИАГОНАЛЬ 2
    check_line(field[0][5], field[1][4], field[2][3],
               field[3][2], smb)

    check_line(field[1][4], field[2][3], field[3][2],
               field[4][1], smb)

    check_line(field[2][3], field[3][2], field[4][1],
               field[5][0], smb)

    #### малая диагональ
    check_line(field[0][3], field[1][2], field[2][1],
               field[3][0], smb)

    #### средняя диагональ
    check_line(field[0][4], field[1][3], field[2][2],
               field[3][1], smb)

    check_line(field[1][3], field[2][2], field[3][1],
               field[4][0], smb)
    ####
    check_line(field[2][5], field[3][4], field[4][3],
               field[5][2], smb)
    ####
    check_line(field[1][5], field[2][4], field[3][3],
               field[4][2], smb)

    check_line(field[2][4], field[3][3], field[4][2],
               field[5][1], smb)
    ###
    check_line(field[5][3], field[4][2], field[3][1],
               field[2][0], smb)
    ###
    check_line(field[1][0], field[2][1], field[3][2],
               field[4][3], smb)

    check_line(field[2][1], field[3][2], field[4][3],
               field[5][4], smb)
    ####
    check_line(field[0][2], field[1][3], field[2][4],
               field[3][5], smb)
    ####
    check_line(field[0][1], field[1][2], field[2][3],
               field[3][4], smb)

    check_line(field[1][2], field[2][3], field[3][4],
               field[4][5], smb)


def check_line(a1, a2, a3, a4, smb):
    global game_run, z_igr, z_com
    if a1['text'] == 'X' and a2['text'] == 'X' and a3['text'] == 'X' and \
            a4['text'] == 'X':
        a1['background'] = a2['background'] = a3['background'] = \
            a4['background'] = '#178e17'
        z_igr = z_igr + 1
        print("z_igr=", z_igr)
        c.delete("ch")
        chet = c.create_text(30, 20,
                             text=(s * 65 + 'КОМПЬЮТЕР   %s : %s   ИГРОК'
                                   % (z_com, z_igr)),
                             font='Times 20', fill='black',
                             state='normal', tag="ch")
        musika_win_igrok_p()
        c.itemconfig('new', state='normal')
        game_run = False

    if a1['text'] == 'O' and a2['text'] == 'O' and a3['text'] == 'O' and \
            a4['text'] == 'O':
        a1['background'] = a2['background'] = a3['background'] = \
            a4['background'] = '#d90640'
        z_com = z_com + 1
        print("z_com=", z_com)
        c.delete("ch")
        chet = c.create_text(30, 20,
                             text=(s * 65 + 'КОМПЬЮТЕР   %s : %s   ИГРОК'
                                   % (z_com, z_igr)),
                             font='Times 20', fill='black',
                             state='normal', tag="ch")
        musika_win_comp_p()
        c.itemconfig('new', state='normal')
        game_run = False


"""ОБУЧЕНИЕ КОМПЬЮТЕРА"""
def can_win(a1, a2, a3, a4, smb):
    res = False

    # ЗА 1 ХОД ДО ПОБЕДЫ
    if a1['text'] == 'O' and a2['text'] == 'O' and a3['text'] == 'O' \
            and a4['text'] == ' ':
        a4['text'] = 'O'
        print('за 1 ход до победы')
        res = True

    if a1['text'] == 'O' and a2['text'] == 'O' and a3['text'] == ' ' \
            and a4['text'] == 'O':
        a3['text'] = 'O'
        print('за 1 ход до победы')
        res = True

    if a1['text'] == 'O' and a2['text'] == ' ' and a3['text'] == 'O' \
            and a4['text'] == 'O':
        a2['text'] = 'O'
        print('за 1 ход до победы')
        res = True

    if a1['text'] == ' ' and a2['text'] == 'O' and a3['text'] == 'O' \
            and a4['text'] == 'O':
        a1['text'] = 'O'
        print('за 1 ход до победы')
        res = True


    #ЗА 2 ХОДА ДО ПОБЕДЫ
    if a1['text'] == 'O' and a2['text'] == 'O' and a3['text'] == ' ' \
            and a4['text'] == ' ':
        a3['text'] = 'O'
        print('за 2 хода до победы')
        res = True

    if a1['text'] == ' ' and a2['text'] == ' ' and a3['text'] == 'O' \
            and a4['text'] == 'O':
        a2['text'] = 'O'
        print('за 2 хода до победы')
        res = True

    if a1['text'] == 'O' and a2['text'] == ' ' and a3['text'] == 'O' \
            and a4['text'] == ' ':
        a2['text'] = 'O'
        print('за 2 хода до победы')
        res = True

    if a1['text'] == ' ' and a2['text'] == 'O' and a3['text'] == ' ' \
            and a4['text'] == 'O':
        a3['text'] = 'O'
        print('за 2 хода до победы')
        res = True

    if a1['text'] == ' ' and a2['text'] == 'O' and a3['text'] == 'O' \
            and a4['text'] == ' ':
        a1['text'] = 'O'
        print('за 2 хода до победы')
        res = True

    if a1['text'] == 'O' and a2['text'] == ' ' and a3['text'] == ' ' \
            and a4['text'] == 'O':
        a2['text'] = 'O'
        print('за 2 хода до победы')
        res = True

    return res


def computer_move():

    # ДЛЯ КОМПЬЮТЕРА проверено 100%
    for n in range(6):
        if can_win(field[n][0], field[n][1], field[n][2],
                   field[n][3], 'O'):
            return

        if can_win(field[n][1], field[n][2], field[n][3],
                   field[n][4], 'O'):
            return

        if can_win(field[n][2], field[n][3], field[n][4],
                   field[n][5], 'O'):
            return

        if can_win(field[0][n], field[1][n], field[2][n],
                   field[3][n], 'O'):
            return

        if can_win(field[1][n], field[2][n], field[3][n],
                   field[4][n], 'O'):
            return

        if can_win(field[2][n], field[3][n], field[4][n],
                   field[5][n], 'O'):
            return

    if can_win(field[0][0], field[1][1], field[2][2],
               field[3][3], 'O'):
        return

    if can_win(field[1][1], field[2][2], field[3][3],
               field[4][4], 'O'):
        return

    if can_win(field[2][2], field[3][3], field[4][4],
               field[5][5], 'O'):
        return
#########
    if can_win(field[0][5], field[1][4], field[2][3],
               field[3][2], 'O'):
        return

    if can_win(field[1][4], field[2][3], field[3][2],
               field[4][1], 'O'):
        return

    if can_win(field[2][3], field[3][2], field[4][1],
               field[5][0], 'O'):
        return
########
    if can_win(field[0][3], field[1][2], field[2][1],
               field[3][0], 'O'):
        return

#########
    if can_win(field[0][4], field[1][3], field[2][2],
               field[3][1], 'O'):
        return

    if can_win(field[1][3], field[2][2], field[3][1],
               field[4][0], 'O'):
        return
########
    if can_win(field[2][0], field[3][1], field[4][2],
               field[5][3], 'O'):
        return
#######
    if can_win(field[1][0], field[2][1], field[3][2],
               field[4][3], 'O'):
        return

    if can_win(field[2][1], field[3][2], field[4][3],
               field[5][4], 'O'):
        return
    ######

    if can_win(field[0][2], field[1][3], field[2][4],
               field[3][5], 'O'):
        return
    #######
    if can_win(field[0][1], field[1][2], field[2][3],
               field[3][4], 'O'):
        return

    if can_win(field[1][2], field[2][3], field[3][4],
               field[4][5], 'O'):
        return
    ######
    if can_win(field[2][5], field[3][4], field[4][3],
               field[5][2], 'O'):
        return
    ########

    if can_win(field[1][5], field[2][4], field[3][3],
               field[4][2], 'O'):
        return

    if can_win(field[2][4], field[3][3], field[4][2],
               field[5][1], 'O'):
        return
    ######

####### ДЛЯ ИГРОКА проверено 100%

    for n in range(6):
        if can_win(field[n][0], field[n][1], field[n][2],
                   field[n][3], 'X'):
            return

        if can_win(field[n][1], field[n][2], field[n][3],
                   field[n][4], 'X'):
            return

        if can_win(field[n][2], field[n][3], field[n][4],
                   field[n][5], 'X'):
            return

        if can_win(field[0][n], field[1][n], field[2][n],
                   field[3][n], 'X'):
            return

        if can_win(field[1][n], field[2][n], field[3][n],
                   field[4][n], 'X'):
            return

        if can_win(field[2][n], field[3][n], field[4][n],
                   field[5][n], 'X'):
            return
#########
    if can_win(field[0][0], field[1][1], field[2][2],
               field[3][3], 'X'):
        return

    if can_win(field[1][1], field[2][2], field[3][3],
               field[4][4], 'X'):
        return

    if can_win(field[2][2], field[3][3], field[4][4],
               field[5][5], 'X'):
        return
#########
    if can_win(field[2][5], field[3][4], field[4][3],
               field[5][2], 'X'):
        return
########
    if can_win(field[1][5], field[2][4], field[3][3],
               field[4][2], 'X'):
        return

    if can_win(field[2][4], field[3][3], field[4][2],
               field[5][1], 'X'):
        return
#########
    if can_win(field[0][2], field[1][3], field[2][4],
               field[3][5], 'X'):
        return
#########
    if can_win(field[0][1], field[1][2], field[2][3],
               field[3][4], 'X'):
        return

    if can_win(field[1][2], field[2][3], field[3][4],
               field[4][5], 'X'):
        return
##########
    if can_win(field[0][5], field[1][4], field[2][3],
               field[3][2], 'X'):
        return

    if can_win(field[1][4], field[2][3], field[3][2],
               field[4][1], 'X'):
        return

    if can_win(field[2][3], field[3][2], field[4][1],
               field[5][0], 'X'):
        return
    #######
    if can_win(field[0][3], field[1][2], field[2][1],
               field[3][0], 'X'):
        return
    #########
    if can_win(field[0][4], field[1][3], field[2][2],
                field[3][1], 'X'):
        return

    if can_win(field[1][3], field[2][2], field[3][1],
                field[4][0], 'X'):
        return
    ##########
    if can_win(field[2][0], field[3][1], field[4][2],
               field[5][3], 'X'):
        return
    #########
    if can_win(field[1][0], field[2][1], field[3][2],
                field[4][3], 'X'):
        return

    if can_win(field[2][1], field[3][2], field[4][3],
                field[5][4], 'X'):
        return

    while True:
        row = random.randint(2, 3)
        col = random.randint(2, 3)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            print('Случайно')
            break


if __name__ == '__main__':

    tk = Tk()
    s = ' '
    tk.title(s * 50 + 'ИГРА "КРЕСТИКИ-НОЛИКИ"')
    tk.iconbitmap(default=r"C:\\FOTO  Python\\monitor2.ico")
    tk.resizable(0, 0)
    tk.wm_attributes('-topmost', 1)
    tk.geometry('516x600+500+50')

    game_run = True
    field = []
    cross_count = 0
    z_com = 0
    z_igr = 0

    for row in range(6):
        line = []
        for col in range(6):
            button = Button(tk, text=' ', width=4, height=2,
                            font=('Verdana', 20, 'bold'),
                            background='#add6b8',
                            command=lambda row=row, col=col: click(row, col))
            button.grid(row=row, column=col, sticky='nsew')
            line.append(button)
        field.append(line)

    new_button = Button(tk, text='НОВАЯ     ИГРА', font=('Times', 15, 'bold'),
                        foreground="green", command=new_game)
    new_button.grid(row=7, column=0, columnspan=6, sticky='nsew')

    row = random.randint(2, 3)
    col = random.randint(2, 3)
    field[row][col]['text'] = 'O'
    check_win('O')

    c = Canvas(tk, width=516, height=70, bg="#cacaca")
    c.grid(row=6, column=0, columnspan=6, sticky='nsew')
    c.focus_set()

    new = c.create_text(30, 50,
                          text=s * 65 + "НОВАЯ ИГРА",
                          font=('Times', 20, 'bold'), fill='green',
                        state='hidden', tag="new")

    chet = c.create_text(30, 20,
                        text=(s * 65 + 'КОМПЬЮТЕР   %s : %s   ИГРОК'
                              % (z_com, z_igr)),
                        font=('Times', 20), fill='black',
                         state='normal', tag="ch")

    c.tag_bind(new, "<Button-1>", new_game)

    tk.mainloop()