import PySimpleGUI as sg
import time
import configparser
import os


#goals 
# total time of 2,048,400
# high score of 
#
#

sg.theme('DarkAmber') 

screen_width, screen_height = sg.Window.get_screen_size()
border_width = 1  # Change this value as desired

script_dir = os.path.dirname(os.path.realpath(__file__))
sg.user_settings_filename(filename=os.path.join(script_dir, 'Settings.json'))

total_time_key = 'total_time'
high_score_key = 'high_score'

high_score = sg.user_settings_get_entry(high_score_key, 0)
total_time = sg.user_settings_get_entry(total_time_key, 0)

score = 0
timeplayed = 0
button_pressed = False
goal_time_sum = 2048400
goal_high_score = 102420

layout = [
    [sg.Text("Total Time Spent:", font=("Helvetica", 15))], [sg.Text("0", key='total_time', font=("Helvetica", 15))],
    [sg.Text("High Score:", font=("Helvetica", 15))], [sg.Text("0", key='high_score', font=("Helvetica", 15))],
    [sg.Text("Score:", font=("Helvetica", 15))], [sg.Text("0", key='current_score', font=("Helvetica", 15))],
    [sg.HorizontalSeparator(color='black')],
    [sg.RealtimeButton('Live', key="hold_button", font=("Helvetica", 15)), sg.Button('Give Up', disabled=True, font=("Helvetica", 15))],
    [sg.Button("Why",font=("Helvetica", 15) )]
    ]

window = sg.Window('Zoe Simulator', layout)

while True:
    event, values = window.read(timeout=100) 


    
    if event == sg.WINDOW_CLOSED:
        break
    if event == "hold_button":
        time.sleep(1)
        score += 1
        window["current_score"].update(score)
    elif event != "hold_button":
        button_pressed = False
        if high_score < score :
            high_score = score
            sg.user_settings_set_entry(high_score_key, high_score)
        window["high_score"].update(high_score)
        total_time += score
        sg.user_settings_set_entry(total_time_key, total_time)
        window["total_time"].update(total_time)

        score = 0
        window["current_score"].update(score)
    if total_time >= goal_time_sum:
        window['Give Up'].update(disabled=False)
    if event == "Why":
        sg.Popup('How to win- Achieve a total time of 2,048,400 and a high score of 102,420', 'After Achieving the required total time, the Give Up button Unlocks', "That is the bare minimum way to <<win>>." , "As for why, this game is supposed to be preformance art and you act as the subject." , "It is supposed to highlight how monotonous each second in passing can be if you are forced to watch it pass by." , "How dreadful life would be if you were bound to your computer." , "Being bound to the button with no satisfaction outside of the slow progress of time's crawl." , "The numbers I have chosen are not arbitrary. The total time goal is the total amount of time I have played in one single game while being trapped in my home." , "The high score is a mere %5 of the total time goal." , "Time is precious and I have wasted years being unable to do what most can do on a whim." , "The time required is a fraction of how long I have been waiting" , "I hope this hurts" , font=("Helvetica", 15))
    if event == 'Give Up':
        break




window.close()
