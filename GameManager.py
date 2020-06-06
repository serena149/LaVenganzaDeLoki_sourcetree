import tkinter as tk
from functools import partial
import Textos
import Rooms
import Endings
import PIL
from PIL import Image
from PIL import ImageTk

#Variables
currentPoints = [0]
currentRoom = [0]
roomsList = [Rooms.Hallway, Rooms.LivingR, Rooms.Kitchen, Rooms.Bedroom, Rooms.Bathroom]
roomsNumber = 5

boringPoints = 0
normalPoints = 5
chaoticPoints = 10

emptyColumnsList = [0, 4]
emptyRowsList = [0, 2, 4, 6, 8]

#Root y frame

root = tk.Tk()

frame = tk.Frame(root)

frame.config(width = 1600, height = 900)
frame.grid_propagate(False) 
frame.grid()

root.title("La venganza de Loki")

#Label1: descripción del juego o respuesta a la decisión de la habitación anterior.. Column 0, row 0

Label1 = tk.Label(frame, text = Textos.HallwayLabel1_All)
Label1.config(fg = "black", font = ("Tahoma", 16))
Label1.grid(columnspan = 3, row = 1, column = 1)

#Resto de columna 0:
Label2 = tk.Label(frame, text = Textos.HallwayLabel2)
Label2.config(fg = "black", font = ("Tahoma", 16))
Label2.grid(columnspan = 3, row = 3, column = 1)

#Metodo para el boton

def ChangeRoomText(currentRoom, currentPoints, pointsIncrement):   
    currentPoints[0] += pointsIncrement
    currentRoom[0] += 1
    
    if(currentRoom[0] < 5):
        UpdateRoom(currentRoom, roomsList, pointsIncrement)
    elif(currentRoom[0] == 5):
        Ending()

def UpdateRoom(currentRoom, roomsList, pointsIncrement):
    for room in roomsList:
        if room.RoomID == currentRoom[0]:
            Label2['text'] = room.Label2
            Button1['text'] = room.Button1
            Button2['text'] = room.Button2
            Button3['text'] = room.Button3

            pic = Image.open(room.Map).resize(size = (400,400))
            tkpic = ImageTk.PhotoImage(pic)
            MapLabel['image'] = tkpic
            MapLabel.image = tkpic
            MapLabel.grid(column = 5, columnspan = 1, row = 1, rowspan = 3)

            if pointsIncrement == boringPoints:
                Label1['text'] = room.Label1_Boring
            elif pointsIncrement == normalPoints:
                Label1['text'] = room.Label1_Normal
            elif pointsIncrement == chaoticPoints:
                Label1['text'] = room.Label1_Chaotic

def Ending():
    chosenEnding = [" "]

    if (currentPoints[0] == boringPoints * roomsNumber):
        chosenEnding = Endings.BoringEnding.text
    elif (currentPoints[0] > boringPoints * roomsNumber) and (currentPoints[0] <= normalPoints * roomsNumber):
        chosenEnding = Endings.NormalEnding.text
    elif (currentPoints[0] > normalPoints * roomsNumber):
        chosenEnding = Endings.ChaoticEnding.text
    
    Label1['text'] = chosenEnding
    Label1['font'] = ("Tahoma", 26)
    
    for label in frame.winfo_children():
        if(label != Label1):
            label.destroy()

Button1 = tk.Button(frame, text = Textos.HallwayButton1, command = partial(ChangeRoomText, currentRoom, currentPoints, boringPoints), font = ("Tahoma", 16))
Button1.grid(row = 5, column = 1, columnspan = 3)

Button2 = tk.Button(frame, text = Textos.HallwayButton2, command = partial(ChangeRoomText, currentRoom, currentPoints, normalPoints), font = ("Tahoma", 16))
Button2.grid(row = 7, column = 1, columnspan = 3)

Button3 = tk.Button(frame, text = Textos.HallwayButton3, command = partial(ChangeRoomText, currentRoom, currentPoints, chaoticPoints), font = ("Tahoma", 16))
Button3.grid(row = 9, column = 1, columnspan = 3)

#Mapa y columna 4:
pic = Image.open(roomsList[0].Map).resize(size = (400,400))
tkpic = ImageTk.PhotoImage(pic)
MapLabel = tk.Label(frame, image=tkpic)
MapLabel.image = tkpic
MapLabel.grid(column = 5, columnspan = 1, row = 1, rowspan = 3)

#Configuración de espacios entre columnas con contenido

for x in emptyColumnsList:
    frame.grid_columnconfigure(x, minsize = 100)
for x in emptyRowsList:
    frame.grid_rowconfigure(x, minsize = 50)

root.mainloop()