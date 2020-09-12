from typing import Sized
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import RELIEF_FLAT


def switchSessBreak(x, y):
    if x:
        x = False
    else:
        x = True
    if y:
        y = False
    else:
        y = True
    return (x, y)

black_bg = '#440000'
red_bg = ('white','#aa0000')
btn_color = ('white', '#005511')

timer = 0
#p_session = 60 * 25
p_session = 25
#p_short_break = 60 * 5
p_short_break = 10
#p_long_break = 60 * 20
p_long_break = 20
time_string = '00:00'
pomodoro_count = 1

max_session = 4
current_session = 1
current_session_time = p_session
current_break = 1

pomodoro_detail_frame = [[sg.T('Pomodoro Session', size=(None, 1), background_color=black_bg,  font=('arial', '15','bold')), sg.T(current_session, size=(None, 1), key='current_session_label', background_color=black_bg,  font=('arial', '15','bold'))]]
current_event_frame = [[sg.T('About to start', size=(14,1), key='current_event', background_color=black_bg,  font=('arial', '15','bold'))]]

#seconds_frame = [[sg.T('0', size=(1,1), key='seconds_label')]]

counter_frame = [[sg.T(time_string, size=(None, 1), key='label', background_color='#000000', font=('arial', '70', 'bold'), pad=((30, 20), (0, 0)))]]


control_frame = [[sg.B('Start', key='startBtn', button_color=btn_color, font=('arial', '20','bold')), sg.B('Pause', size = (5, 1), key='pauseBtn',visible = False,button_color=('white','#001155'),  font=('arial', '20','bold'))]]

layout = [[sg.Frame('', layout=pomodoro_detail_frame, background_color=black_bg, relief=RELIEF_FLAT), sg.Frame('', layout=current_event_frame, background_color=black_bg, relief=RELIEF_FLAT)],
          [sg.Frame('', layout=[[sg.T('', background_color=black_bg)]], background_color=black_bg, relief=RELIEF_FLAT), sg.Frame('', layout=counter_frame, background_color='#000000', relief=RELIEF_FLAT)],
          [sg.Frame('', layout=control_frame, background_color=black_bg, relief= RELIEF_FLAT)]]

window = sg.Window('Timer', layout=layout, element_justification='center', background_color=black_bg)


leveller = 0
paused = False
break_time = False
session_time = True
in_session = False
starting = True

while True:
    events, values = window.read(timeout=100)
    if events == None:
        break
    if events == 'pauseBtn':
        if paused:
            paused = False
            window['pauseBtn'].update('Pause')
            window['current_event'].update('In Session')
        else:
            paused = True
            window['pauseBtn'].update('Play')
            window['current_event'].update('Session Paused')
    if events == 'startBtn':
        if in_session:
            in_session = False
            window['pauseBtn'].update(visible=False)
            window['startBtn'].update(button_color=btn_color)
            window['startBtn'].update('Start')
            window['label'].update('00:00')
            paused = True
            timer = 0
            window['current_event'].update('Start Session')
        else:
            in_session = True
            window['pauseBtn'].update(visible=True)
            window['startBtn'].update(button_color=red_bg)
            window['startBtn'].update('Stop')
            paused = False
            window['current_event'].update('In Session')

    if in_session:
        if not paused:
            leveller += 100
            if leveller % 1000 == 0:
                timer += 1
                time = current_session_time - timer
                if time > 0:
                    minutes = time // 60
                    if minutes == 0:
                        minutes = '00'
                    seconds = time % 60
                    if seconds < 10:
                        seconds = '0'+str(time % 60)
                    time_string = str(minutes)+ ':' + str(seconds)
                    window['label'].update(time_string)
                    print(timer)
                    if current_session_time == p_long_break and timer >= p_long_break - 1:
                        print('Time for long Break')
                        session_continue = sg.popup_yes_no(
                            'End of session \n Do you want to continue?')
                        print('>>>>>>  ',session_continue)
                        if session_continue == 'Yes':
                                current_break = 0
                        else:
                            in_session = False
                            window['pauseBtn'].update(visible=False)
                            window['startBtn'].update(button_color=btn_color)
                            window['startBtn'].update('Start')
                            window['label'].update('00:00')
                            window['current_event'].update('Start Session')
                            paused = True
                            timer = 0
                            current_session_time = p_session
                   # print(timer)
                else:
                    
                    session_time, break_time = switchSessBreak(session_time, break_time )
                    if session_time:
                        current_session += 1
                        current_session_time = p_session
                        current_break += 1
                        print('In session')
                        window['current_event'].update('In session')
                        window['current_session_label'].update(current_session)
                    if break_time:

                        if pomodoro_count == 1 and current_break == 2:
                            current_session_time = p_long_break
                            print('Long break')
                        elif pomodoro_count == 2 and current_break == 4:
                            current_session_time = p_long_break
                            print('long break')
                        else:
                            current_session_time = p_short_break
                            print(' short Break time')
                        window['current_event'].update('On break')
                    
                    timer = 0
    
