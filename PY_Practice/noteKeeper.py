from tkinter import *
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
import os
import datetime
import requests

def frameSetUp():
    global canvas, buttonFrame, noteFrame, reminderFrame
    canvas = Canvas(root, width=300)
    canvas.grid(row=1, column=1, sticky=NS)
    vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
    vsb.grid(row=1, column=1, sticky=E + NS)
    canvas.configure(yscrollcommand=vsb.set)

    buttonFrame = LabelFrame(root, text ="Tools")
    buttonFrame.grid(row = 1, column = 0, sticky=NS)
    noteFrame = LabelFrame(canvas, text ="To-Be-Done")
    canvas.create_window((0, 0), window=noteFrame, anchor="nw")
    canvas.bind("<Configure>", canvas.configure(scrollregion=canvas.bbox("all")))
    # noteFrame.grid(row = 1, column = 1, padx = 10, pady = 10, sticky=NS)
    reminderFrame = LabelFrame(root, text ="Check Weather")
    reminderFrame.grid(row = 1, column = 2, padx = 10, pady = 10)


def addNote():
    newWindow = Toplevel()
    newWindow.title("Add New Note")
    newWindow.geometry("500x500")

    msgLocation = Label(newWindow, text="Location: ").grid(row=0, column=0)
    e1 = Entry(newWindow)
    e1.grid(row=0, column=1, sticky=EW)

    msgDate = Label(newWindow, text="Date: ").grid(row=1, column=0)
    e2 = Entry(newWindow)
    e2.grid(row=1, column=1, sticky=EW)

    msgTime = Label(newWindow, text="Time: ").grid(row=2, column=0)
    e3 = Entry(newWindow)
    e3.grid(row=2, column=1, sticky=EW)

    msgNote = Label(newWindow, text="Note: ").grid(row=3, column=0)
    e4 = ScrolledText(newWindow, wrap = WORD, width = 40, height = 10)
    e4.grid(row=3, column=1)

    btnAdd = Button(newWindow, text="Add", command= lambda: [saveInput(e1, e2, e3, e4), newWindow.destroy(), readFile()]).grid(row=4, column=0, columnspan=2, sticky = EW)
    # btnExit = Button(newWindow, text = "Close", command=newWindow.destroy).grid(row=4, column=1, sticky= EW)

def saveInput(e1, e2, e3, e4):
    enLocation = e1.get()
    enDate = e2.get()
    enTime = e3.get()
    enNote = e4.get("1.0", END)
    fileInfo = open("note.txt", "a")
    fileInfo.write("Location: " + str(enLocation) + "\n" 
                   + "Date    : " + str(enDate) + "\n" 
                   + "Time    : " + str(enTime) + "\n" 
                   + "Note    : " + str(enNote) + "\n"
                   + "--------------------------------" + "\n")
    fileInfo.close()

def readFile():
    f = open("note.txt", "a")
    f.close()
    f = open("note.txt", "r")
    i = 0
    noteText = ""
    for line in f:
        if not line.startswith("---"):
            noteText += line
        else:
            text_widget = Text(noteFrame, wrap="word", height=5)
            text_widget.insert("1.0", noteText)
            text_widget.config(state="disabled")
            text_widget.grid(row=i, column=0)
            noteText = ""
            i += 1
            continue
    # Update the canvas's scroll region to fit the new content
    canvas.update_idletasks()  # Ensures all widgets have been updated
    canvas.configure(scrollregion=canvas.bbox("all"))

def checkWeather(e5):
    weather_forecast_api = "4750acfc42377fc5ec19b4b67bea1f80"
    location = e5.get()
    complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+ location + "&appid=" + weather_forecast_api
    forecast_api_link = "https://api.openweathermap.org/data/2.5/forecast?q=" + location + "&appid=" + weather_forecast_api
    api_link = requests.get(forecast_api_link)
    api_data = api_link.json()
    msgForecast = ''

    #5day/3hour weather forecast code
    if api_data['cod'] == '404':
        msgForecast = "Invalid city entered:{}, please check your city name".format(location)
    else:
        for i in range(5):
            temp_city = api_data["list"][i]["main"]["temp"] - 273.15
            weather_desc = api_data["list"][i]['weather'][0]['description']
            hmdt = api_data["list"][i]['main']['humidity']
            wind_speed = api_data["list"][i]['wind']['speed']
            time = api_data["list"][i]["dt_txt"]

            msgForecast += """--------------------------------------------------------------------------------\n
            Weather stats for {} || {}\n
            --------------------------------------------------------------------------------\n
            City temperature       : {:.2f} deg C\n
            Weather description    : {}\n
            Humidity               : {}%\n
            Wind speed             : {}kmph\n\n""".format(location, time, temp_city, weather_desc, hmdt, wind_speed)

    msgForecast_widget = Text(reminderFrame, wrap="word")
    msgForecast_widget.insert("1.0", msgForecast)
    msgForecast_widget.grid(row=3, column=0)
    weatherScrollbar = Scrollbar(reminderFrame, command=msgForecast_widget.yview)
    weatherScrollbar.grid(row=3, column=1)
    msgForecast_widget.config(yscrollcommand=weatherScrollbar.set)



#--------------------------------------------------------------------------------------------------------------------------------
root = Tk()
root.title("Note Keeper")
root.geometry("750x300")

frameSetUp()
btnAddNote = Button(buttonFrame, text="Add Note", command= addNote, width=10, height=10).grid(row = 0, column = 0, sticky = EW, pady = 10, padx = 10)
readFile()
msgWeather = Label(reminderFrame, text="Enter the city name for weather checking:")
msgWeather.grid(row=0, column=0)
e5 = Entry(reminderFrame)
e5.grid(row=1, column=0)
btnCheckWeather = Button(reminderFrame, text="Check Weather", command=lambda: checkWeather(e5)).grid(row=2, column=0)


root.mainloop()