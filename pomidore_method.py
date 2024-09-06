import PySimpleGUI as sg
import time
import datetime
import json 
import sys


setting=sys.argv[1]
config=json.load(open(setting))
job_sec=10

score=config["score"]
layout = [
    [sg.Image('./pictures/Untitled0.png', key = 'image')],
    [sg.Text(f'счет: {round(score,1)}',key = 'score')],
    [sg.Button("-5",key = "-"),sg.Text(str(datetime.timedelta(seconds=job_sec*60)),key = "job"),sg.Button("+5",key = "+")],
    [sg.Button('Ok')]
]
num = 0
layout1=[
    [sg.Text(num, key="timer")],
                [sg.Text("Рабочее время",key = 'time')],
                [sg.Button('STOP',key='STOP')]
]
megalayout=[[sg.Column(layout, key='-UAHAHA-'), sg.Column(layout1, visible=False, key='-AUF-')]]

is_timer = False

window = sg.Window('tomato',megalayout)

def job_time( window):
    window['-UAHAHA-'].update(visible=False)
    window['-AUF-'].update(visible=True)

def main_window(window):
    window['-UAHAHA-'].update(visible=True)
    window['-AUF-'].update(visible=False)

def timer(window, job_sec, timer_status, job_or_break):
    job_time(window)
    if timer_status == 'rest':
        window['time'].update("Время отдыха")
        window['STOP'].update(visible=False)
    else:
        window['time'].update("Рабочее время")
        window['STOP'].update(visible=True)
    heh = window['time']
    if heh == 'время отдыха' and job_sec <= 0:
        job_or_break = False
    window['timer'].update(datetime.timedelta(seconds=job_sec))
    job_sec-=1
    time.sleep(1)
    if job_sec <= 0:
        return job_sec, 'job_end'
    
    return job_sec, 'job_runnig'
    
job_or_break=False
while True:
    event, values = window.read(10)

    if score >= 0 and score < 10:
        window['image'].update(config["0"])  

    if score >= 10 and score < 20:
        window['image'].update(config["1"])     
    
    if score >= 20 and score < 30:
        window['image'].update(config["2"]) 

    if score >= 30 and score < 40:
        window['image'].update(config["3"])
    if score >= 40 :
        window['image'].update(config["4"])
    
    if event == sg.WIN_CLOSED:
        break
    
    elif event == "+":
        if job_sec >= 120:
            job_sec = 120
            window["job"].update(str(datetime.timedelta(seconds=job_sec*60)))
        else:
            job_sec += 5
            window["job"].update(str(datetime.timedelta(seconds=job_sec*60)))
    elif event == "-":
        if job_sec <= 10:
            job_sec = 10
            window["job"].update(str(datetime.timedelta(seconds=job_sec*60)))
        else:
            job_sec -= 5
            window["job"].update(str(datetime.timedelta(seconds=job_sec*60)))

    elif event == 'Ok':
        is_timer = True
        
    
    if event == 'STOP':
        btn_func = window['STOP'].get_text()
        if btn_func == 'STOP':
            window['STOP'].update('PLAY')
            is_timer = False
        else:
            window['STOP'].update('STOP')
            is_timer = True
        

    if is_timer and job_or_break == False:
        job_sec, status = timer(window, job_sec, 'job_runnig',job_or_break)
        with open(setting, 'r') as file:
            data = json.load(file)
        data["score"] += 0.01
        with open(setting, 'w') as file:
            
            json.dump(data, file, indent=4)
            

        if status == 'job_end':
            job_or_break = True
         
        
    if is_timer and job_or_break:
        break_sec, status = timer(window, break_sec, 'rest', job_or_break)
        if status == 'job_end':
            job_or_break = False
            is_timer = False
            
            score=json.dumps(data["score"], indent=4)
            window['score'].update(f'счёт: {round(score,1)}')
            main_window(window)
    
            
print(score)
window.close
