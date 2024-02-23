import random
from tkinter import *
from tkinter import messagebox
from playsound import playsound
import math
from pygame import mixer

# from PIL import Image, ImageTk



## Variables
balance = 1000
bet = 0
bet_choice = ""
bet_choices = ['Odd', 'Even', 'Black', 'Red', '1st 12', '2nd 12', '3rd 12', '1 to 18', '19 to 35']

# blackjack random
dealer_first = 0
dealer_second = 0
player_first = 0
player_second = 0
player_third = 0

# sfx
lose_sound = 'src\lose_sfx.mp3'
win_sound = 'src\win_sfx.wav'
wheel_sound = "src\wheel_sfx.mp3"
reveal_sound = 'src\suspense.mp3'
music_sound = 'src\music.mp3'

# pictures
pic_photoimage = "src/newvegas.png"
pic_chip = "src\icons8-chip-50.ico"

window = Tk()
window.title("Alitex")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)
window.geometry("950x750")
window.iconbitmap(pic_chip)


# background music

def start():
    lbl_photo.place(x=-10, y=0)
    lbl_roulette_welcome.place(x=340, y=157)
    btn_roulette_Roulette.place(x=70, y=520)
    btn_roulette_Blackjack.place(x=510, y=520)
    lbl_balance.place(x=870, y=2)
    window['bg'] = '#000051'
    lbl_balance['bg'] = '#000051'


mixer.init()


def background_music():
    mixer.music.load(music_sound)
    mixer.music.play(loops=1, start=random.randrange(0, 360))


# background_music()


# def rotate_line(canvas):
#     angle_degrees = random.randrange(10, 360)
#     # Center point of rotation
#     center_x, center_y = 250, 250
#
#     # Length of the line
#     line_length = 100
#
#     # Convert angle from degrees to radians
#     angle_radians = math.radians(angle_degrees)
#
#     # Calculate the end point coordinates after rotation
#     end_x = center_x + line_length * math.cos(angle_radians)
#     end_y = center_y + line_length * math.sin(angle_radians)
#
#     # Create the rotated line
#     canvas.create_line(325, 325, end_x, end_y,
#                        fill='white', width=5, arrow=LAST,
#                        dash=(10, 2), arrowshape=(10, 20, 10), tags="rotated_line")
#     canvas.after(200)
#     #canvas.delete("rotated_line")


def btn_help_pressed(where):
    if where:
        messagebox.showinfo("Help", 'How to play this roulette? \n '
                                    '- Firstly, you have to set your bet by entering your bet in the \n   bottom left '
                                    'corner and pressing the \"Place your bet\" button \n'
                                    '- Then Choose your bet by pressing buttons in the grid in the \n   Left, '
                                    'or if you\'re feeling lucky you can enter the certain number (0<=n<=35) to set a '
                                    'certain number \n'
                                    '- Then you press the "Spin!" button and enjoy this game! \n\n'
                                    'You can see your balance in the top right corner \n\n'
                                    'If you want to choose the other game \nyou can press on a "<---" button')
    else:
        messagebox.showinfo("Help", 'How to play this blackjack? \n '
                                    '- Firstly, you have to set your bet by entering your bet in the \n   bottom left '
                                    'corner and pressing the \"Place your bet\" button \n'
                                    '- Then press the New game button and start a game\n'
                                    '- Then you will see the dealer\'s hand and yours\n'
                                    ' then you press the Reveal or the take button\n'
                                    '- The Reveal button reveals the hands and if dealer\'s hand is '
                                    '\n bigger than yours, you will lose and vice versa\n'
                                    '- The Take button will add a third card to your hand and reveal the cards \n\n'
                                    'You can see your balance in the top right corner \n\n'
                                    'If you want to choose the other game \nyou can press on a "<---" button')


def btn_roulette_pressed():
    global canvas
    global btn_help
    lbl_photo.place_forget()
    btn_roulette_Blackjack.place_forget()
    btn_roulette_Roulette.place_forget()
    lbl_roulette_welcome.place_forget()

    window['bg'] = '#008000'
    lbl_roulette_place_your_bet['bg'] = '#008000'
    lbl_balance['bg'] = '#008000'
    lbl_roulette_place_your_bet.place(x=6, y=128)
    btn_back.place(x=0, y=0)

    btn_help = Button(font=('Roboto', 15), text='?', bg='#E8392C', command=lambda: btn_help_pressed(1))

    frm_roulette_bets.place(x=8, y=160)
    btn_roulette_Number.grid(row=0, column=0)
    ent_roulette_Number_entry.grid(row=0, column=1)
    btn_roulette_Odd.grid(row=1, column=0)
    btn_roulette_Even.grid(row=1, column=1)
    btn_roulette_Black.grid(row=2, column=0)
    btn_roulette_Red.grid(row=2, column=1)
    btn_roulette_1st12.grid(row=3, column=0)
    btn_roulette_2nd12.grid(row=3, column=1)
    btn_roulette_3nd12.grid(row=4, column=0)
    btn_roulette_1to18.grid(row=4, column=1)
    btn_roulette_19to36.grid(row=5, column=0)
    btn_bet.place(x=0, y=710)
    ent_bet.place(x=151, y=710)
    lbl_bet.place(x=0, y=680)
    lbl_roulette_your_bet.place(x=8, y=401)
    lbl_roulette_cell.place(x=600, y=15)
    btn_roulette_spin.place(x=600, y=700)
    btn_help.place(x=900, y=700)

    canvas = Canvas(window, width=600, height=600, bg='#008000', highlightbackground='#008000')
    canvas.place(x=325, y=45)

    t = True
    for i in range(0, 360, 10):
        if i == 90:
            canvas.create_arc(50, 50, 600, 600, start=i, extent=10, fill="green")
            t = True
            continue
        if t:
            canvas.create_arc(50, 50, 600, 600, start=i, extent=10, fill="black")

            t = False
        else:
            canvas.create_arc(50, 50, 600, 600, start=i, extent=10, fill="#B00000")
            t = True
        line = canvas.create_line(325, 325, 325, 50, fill='white',
                                  width=5, arrow=LAST, dash=(10, 2),
                                  activefill='lightgreen',
                                  arrowshape=(10, 20, 10))


def btn_bet_bet_choose_pressed(choice):
    global bet_choice
    if choice == 0:
        a = ent_roulette_Number_entry.get()
        if not a.isdigit():
            messagebox.showerror("Error", "Invalid input \nThe choice must be a natural number and exist between 1 "
                                          "and 35")
            return 0
        else:
            if 35 >= int(a) >= 0 == float(a) % 1:
                bet_choice = ent_roulette_Number_entry.get()
                lbl_roulette_your_bet['text'] = ent_roulette_Number_entry.get()
            elif not 0 <= int(a) <= 35 or not float(a) % 1 == 0:
                messagebox.showerror("Error", "Invalid input \nThe choice must be a natural number and exist between "
                                              "1 and 35")
                ent_roulette_Number_entry.delete(0, END)
                return 0
            else:
                messagebox.showerror("Error ", "Invalid input \nThe choice must be a natural number and exist "
                                               "between 1 and 35")
                ent_roulette_Number_entry.delete(0, END)
                return 0
    elif choice == 1:
        bet_choice = "Odd"
        lbl_roulette_your_bet['text'] = "Odd"
    elif choice == 2:
        bet_choice = "Even"
        lbl_roulette_your_bet['text'] = "Even"
    elif choice == 3:
        bet_choice = "Black"
        lbl_roulette_your_bet['text'] = "Black"
    elif choice == 4:
        bet_choice = "Red"
        lbl_roulette_your_bet['text'] = "Red"
    elif choice == 5:
        bet_choice = "1st 12"
        lbl_roulette_your_bet['text'] = "1 st 12"
    elif choice == 6:
        bet_choice = "2nd 12"
        lbl_roulette_your_bet['text'] = "2nd 12"
    elif choice == 7:
        bet_choice = "3rd 12"
        lbl_roulette_your_bet['text'] = "3rd 12"
    elif choice == 8:
        bet_choice = "1 to 18"
        lbl_roulette_your_bet['text'] = "1 to 18"
    elif choice == 9:
        bet_choice = "19 to 35"
        lbl_roulette_your_bet['text'] = "19 to 35"


def btn_bet_pressed():
    global bet
    if not ent_bet.get().isdigit():
        messagebox.showerror("Error btn_bet_pressed", "Invalid input \nBet must be a natural number")
        return 0
    bet = int(ent_bet.get())
    lbl_bet['text'] = f'Bet:{bet}$'


def btn_spin_pressed():
    global balance

    if bet == 0 or len(bet_choice) == 0:
        messagebox.showerror("Error", "btn_spin_pressed_error")
        return 0
    elif bet > balance:
        messagebox.showinfo("Error", "Not enough money")
        return 0
    cell = random.randrange(0, 35)
    lbl_roulette_cell['text'] = f'{cell} rolled'
    playsound(wheel_sound)
    # rotate_line(canvas)
    if bet_choice == "Odd" and cell % 2 == 1:
        playsound(win_sound)
        messagebox.showinfo("Маладес", f'Выпало {cell} и ты выиграл {bet} деняк! \n Odd ore black')
        balance = balance + bet
        lbl_balance['text'] = f'Balance:\n{balance}$'

    elif bet_choice == "Even" and cell % 2 == 0:
        playsound(win_sound)
        messagebox.showinfo("Маладес", f'Выпало {cell} и ты выиграл {bet} деняк! \n Even or red')
        balance = balance + bet
        lbl_balance['text'] = f'Balance:\n{balance}$'

    elif bet_choice == "Black" and cell % 2 == 0:
        playsound(win_sound)
        messagebox.showinfo("Маладес", f'Выпало {cell} и ты выиграл {bet} деняк! \n Even or red')
        balance = balance + bet
        lbl_balance['text'] = f'Balance:\n{balance}$'

    elif bet_choice == "Red" and cell % 2 == 0:
        playsound(win_sound)
        messagebox.showinfo("Маладес", f'Выпало {cell} и ты выиграл {bet} деняк! \n Even or red')
        balance = balance + bet
        lbl_balance['text'] = f'Balance:\n{balance}$'

    elif bet_choice == "1st 12" and 0 <= cell <= 12:
        playsound(win_sound)
        messagebox.showinfo("Маладес", f'Выпало {cell} и ты выиграл {bet} деняк! \n 1st 12')
        balance = balance + bet
        lbl_balance['text'] = f'Balance:\n{balance}$'

    elif bet_choice == "2nd 12" and 13 <= cell <= 24:
        playsound(win_sound)
        messagebox.showinfo("Маладес", f'Выпало {cell} и ты выиграл {bet} деняк! \n 2nd 12')
        balance = balance + bet
        lbl_balance['text'] = f'Balance:\n{balance}$'

    elif bet_choice == "3rd 12" and 25 <= cell <= 35:
        playsound(win_sound)
        messagebox.showinfo("Маладес", f'Выпало {cell} и ты выиграл {bet} деняк! \n Even')
        balance = balance + bet
        lbl_balance['text'] = f'Balance:\n{balance}$'

    elif bet_choice == "1 to 18" and 1 <= cell <= 18:
        playsound(win_sound)
        messagebox.showinfo("Маладес", f'Выпало {cell} и ты выиграл {bet} деняк! \n Even')
        balance = balance + bet
        lbl_balance['text'] = f'Balance:\n{balance}$'

    elif bet_choice == "19 to 35" and 19 <= cell <= 35:
        playsound(win_sound)
        messagebox.showinfo("Маладес", f'Выпало {cell} и ты выиграл {bet} деняк! \n Even')
        balance = balance + bet
        lbl_balance['text'] = f'Balance:\n{balance}$'

    elif bet_choice.isdigit() and cell == int(bet_choice):
        playsound(win_sound)
        messagebox.showinfo("Маладес", f'Выпало {cell} и ты выиграл {bet * 10} деняк! \n Even')
        balance = balance + bet * 10
        lbl_balance['text'] = f'Balance:\n{balance}$'

    else:
        playsound(lose_sound)
        messagebox.showinfo("Проиграл", f'Выпало {cell} и ты проиграл {bet} деняк! \n Lose')
        balance = balance - bet
        lbl_balance['text'] = f'Balance:\n{balance}$'


def btn_blackjack_pressed():
    lbl_photo.place_forget()
    global btn_help
    window['bg'] = '#800000'
    lbl_balance['bg'] = '#800000'
    lbl_bet['bg'] = '#008000'

    btn_help = Button(font=('Roboto', 15), text='?', bg='#E8392C', command=lambda: btn_help_pressed(0))

    btn_roulette_Blackjack.place_forget()
    btn_roulette_Roulette.place_forget()
    lbl_roulette_welcome.place_forget()
    btn_bet.place(x=0, y=710)
    ent_bet.place(x=151, y=710)
    lbl_bet.place(x=0, y=680)
    btn_back.place(x=0, y=0)
    btn_blackjack_reveal.place(x=183, y=500)
    btn_blackjack_take.place(x=583, y=500)
    btn_blackjack_new_game.place(x=383, y=10)
    lbl_blackjack_dealercards.place(x=350, y=175)
    lbl_blackjack_playercards.place(x=350, y=300)
    btn_help.place(x=900, y=700)


def btn_blackjack_reveal_pressed():
    global balance, bet
    btn_blackjack_reveal['state'] = "disabled"
    btn_blackjack_take['state'] = "disabled"

    dealer_sum = dealer_first + dealer_second
    player_sum = player_first + player_second
    playsound(reveal_sound)
    lbl_blackjack_dealercards['text'] = f'Dealer\'s cards: {dealer_first} + {dealer_second} \n= {dealer_sum}'
    lbl_blackjack_playercards['text'] = f'Your cards: {player_first} + {player_second} \n= {player_sum}'

    if dealer_sum > player_sum:
        playsound(lose_sound)
        messagebox.showinfo("You lost!", f"Dealer's hand was {dealer_sum} and yours {player_sum} "
                                         f"\nand you lost {bet} dollars!")
        balance = balance - bet
        lbl_balance['text'] = f'Balance:\n{balance}$'
    elif dealer_sum < player_sum:
        playsound(win_sound)
        messagebox.showinfo("You won!", f"Dealer's hand was {dealer_sum} and yours {player_sum} "
                                        f"\nand you won {bet} dollars!")
        balance = balance + bet
        lbl_balance['text'] = f'Balance:\n{balance}$'
    else:
        playsound(lose_sound)
        messagebox.showinfo("Tie!", f"Dealer's hand was {dealer_sum} and yours {player_sum}")
    btn_blackjack_new_game['state'] = "normal"


def btn_blackjack_take_pressed():
    global balance, bet
    lbl_blackjack_playercards['text'] = f'Your cards: {player_first} + {player_second} + {player_third}'
    btn_blackjack_take['state'] = "disabled"
    btn_blackjack_reveal['state'] = "disabled"

    player_sum = player_first + player_second + player_third
    dealer_sum = dealer_first + dealer_second

    lbl_blackjack_dealercards['text'] = f'Dealer\'s cards: {dealer_first} + {dealer_second} \n= {dealer_sum}'
    lbl_blackjack_playercards[
        'text'] = f'Your cards: {player_first} + {player_second} + {player_third} \n= {player_sum}'

    playsound(reveal_sound)
    if player_first + player_second + player_third > 21:
        playsound(lose_sound)
        messagebox.showinfo("You lost!", f"Your cards exceeded 21! \nYou lost {bet} dollars!")
        balance = balance + bet
        lbl_balance['text'] = f'Balance:\n{balance}$'
    elif dealer_sum > player_sum:
        playsound(lose_sound)
        messagebox.showinfo("You lost!", f"Dealer's hand was {dealer_sum} and yours {player_sum} "
                                         f"\nand you lost {bet} dollars!")
        balance = balance - bet
        lbl_balance['text'] = f'Balance:\n{balance}$'
    elif dealer_sum < player_sum:
        playsound(win_sound)
        messagebox.showinfo("You won!", f"Dealer's hand was {dealer_sum} and yours {player_sum} "
                                        f"\nand you won {bet} dollars!")
        balance = balance + bet
        lbl_balance['text'] = f'Balance:\n{balance}$'
    else:
        playsound(lose_sound)
        messagebox.showinfo("Tie!", f"Dealer's hand was {dealer_sum} and yours {player_sum}")
    btn_blackjack_new_game['state'] = "normal"


def btn_blackjack_newgame_pressed():
    global player_first, player_second, player_third, dealer_first, dealer_second
    if bet == 0:
        messagebox.showerror("Error", "Bet is equal to 0! please enter the bet!")
        return 0
    elif bet > balance:
        messagebox.showinfo("Error", "Not enough money")
        return 0
    global player_first, player_second, player_third, dealer_first, dealer_second
    btn_blackjack_reveal['state'] = "normal"
    btn_blackjack_take['state'] = "normal"

    dealer_first = random.randrange(1, 11)
    dealer_second = random.randrange(1, 10)
    player_first = random.randrange(1, 11)
    player_second = random.randrange(1, 10)
    player_third = random.randrange(1, 11)
    lbl_blackjack_playercards['text'] = f'Your cards: {player_first} + {player_second}'
    lbl_blackjack_dealercards['text'] = f'Dealer\'s cards: ? + ?'
    lbl_blackjack_cant_take.place_forget()
    if player_first + player_second > 15:
        lbl_blackjack_cant_take.place(x=350, y=350)

        btn_blackjack_take['state'] = "disabled"
    btn_blackjack_new_game['state'] = "disabled"


def btn_back_pressed():
    for widget in window.winfo_children():
        widget.grid_forget()
        widget.place_forget()

    start()


## Reusable labels and buttons

photo = PhotoImage(file=pic_photoimage)
lbl_photo = Label(image=photo)

lbl_balance = Label(font=('Roboto', 15), text=f'Balance:\n{balance}$', fg='white', bg='#000051')

lbl_bet = Label(font=('Roboto', 15), text=f'Bet:{bet}$', fg='white', bg='#000051', width=20)

btn_help = Button(font=('Roboto', 15), text='?', bg='#E8392C', command=lambda: btn_help_pressed(1))

btn_back = Button(font=('Roboto', 15), text='<----', bg='#A4A4A4', activebackground='#747474',
                  command=lambda: btn_back_pressed())

ent_bet = Entry(font=('Roboto', 25), width=5, bg='#A4A4A4')

btn_bet = Button(font=('Roboto', 15), text="Place your bet:", fg='white', bg='#508050', height=1,
                 command=btn_bet_pressed)

## Greetings frame

lbl_roulette_welcome = Label(font=('Roboto', 15), fg='white', bg='#000051',
                             text="Welcome to the casino game!\nMake sure to lose all your money!", )
btn_roulette_Roulette = Button(command=lambda: btn_roulette_pressed(), font=('Roboto', 25), text="Roulette", width=20,
                               height=3,
                               bg='#008000', activebackground='#005000')
btn_roulette_Blackjack = Button(command=btn_blackjack_pressed, font=('Roboto', 25), text="Blackjack", width=20,
                                height=3,
                                bg='#800000', activebackground='#600000')

##Roulette frame
lbl_roulette_place_your_bet = Label(font=('Roboto', 15), text='Place your bet:', fg='white', bg='#000051')
lbl_roulette_your_bet = Label(font=('Roboto', 15), text='Your bet:', fg='white', bg='#000051')
lbl_roulette_cell = Label(font=('Roboto', 15), text='What rolled will be here', fg='white', bg='#000051')
frm_roulette_bets = Frame(master=window, bg='#008000')

btn_roulette_Number = Button(frm_roulette_bets, command=lambda: btn_bet_bet_choose_pressed(0), font=('Roboto', 15),
                             text="Set:",
                             width=8, height=1, bg='#A4A4A4', activebackground='#747474')
btn_roulette_Even = Button(frm_roulette_bets, font=('Roboto', 15), text="Even", width=8, height=1,
                           bg='#A4A4A4', activebackground='#747474', command=lambda: btn_bet_bet_choose_pressed(2))
btn_roulette_Odd = Button(frm_roulette_bets, font=('Roboto', 15), text="Odd", width=8, height=1,
                          bg='#A4A4A4', activebackground='#747474', command=lambda: btn_bet_bet_choose_pressed(1))
btn_roulette_Red = Button(frm_roulette_bets, font=('Roboto', 15), text="Red", width=8, height=1,
                          bg='#A4A4A4', activebackground='#747474', command=lambda: btn_bet_bet_choose_pressed(4))
btn_roulette_Black = Button(frm_roulette_bets, font=('Roboto', 15), text="Black", width=8, height=1,
                            bg='#A4A4A4', activebackground='#747474', command=lambda: btn_bet_bet_choose_pressed(3))
btn_roulette_1st12 = Button(frm_roulette_bets, font=('Roboto', 15), text="1st 12:", width=8, height=1,
                            bg='#A4A4A4', activebackground='#747474', command=lambda: btn_bet_bet_choose_pressed(5))
btn_roulette_2nd12 = Button(frm_roulette_bets, font=('Roboto', 15), text="2nd 12:", width=8, height=1,
                            bg='#A4A4A4', activebackground='#747474', command=lambda: btn_bet_bet_choose_pressed(6))
btn_roulette_3nd12 = Button(frm_roulette_bets, font=('Roboto', 15), text="3rd 12:", width=8, height=1,
                            bg='#A4A4A4', activebackground='#747474', command=lambda: btn_bet_bet_choose_pressed(7))
btn_roulette_1to18 = Button(frm_roulette_bets, font=('Roboto', 15), text="1 to 18", width=8, height=1,
                            bg='#A4A4A4', activebackground='#747474', command=lambda: btn_bet_bet_choose_pressed(8))
btn_roulette_19to36 = Button(frm_roulette_bets, font=('Roboto', 15), text="19 to 35:", width=8, height=1,
                             bg='#A4A4A4', activebackground='#747474', command=lambda: btn_bet_bet_choose_pressed(9))
btn_roulette_spin = Button(font=('Roboto', 15), text="Spin!", width=8, height=1,
                           bg='#EFDF00', activebackground='#505000', command=btn_spin_pressed)
ent_roulette_Number_entry = Entry(frm_roulette_bets, font=('Roboto', 25), width=5,
                                  bg='#A4A4A4')

##Blackjack frame
lbl_blackjack_dealercards = Label(font=('Roboto', 30), text='Dealer\'s cards: ? + ?', fg='white', bg='#800000')
lbl_blackjack_playercards = Label(font=('Roboto', 30), text='Your cards: ? + ?', fg='white', bg='#800000')
lbl_blackjack_cant_take = Label(font=('Roboto', 20), text='Because your hand is >10, you can\'t take a card',
                                fg='white',
                                bg='#800000')
btn_blackjack_reveal = Button(font=('Roboto', 30), text="Reveal", width=9, height=1,
                              bg='#A4A4A4', activebackground='#747474', command=btn_blackjack_reveal_pressed,
                              state='disabled')
btn_blackjack_take = Button(font=('Roboto', 30), text="Take", width=9, height=1,
                            bg='#A4A4A4', activebackground='#747474', command=btn_blackjack_take_pressed,
                            state='disabled')
btn_blackjack_new_game = Button(font=('Roboto', 30), text="New game", width=9, height=1,
                                bg='#A4A4A4', activebackground='#747474', command=btn_blackjack_newgame_pressed)
if __name__ == "__main__":
    start()
    window.mainloop()
