import tkinter as tk
from functools import partial
import Textos
import Rooms
import Endings

#Variables
currentPoints = [0]
currentRoom = [0]
roomsList = [Rooms.Hallway, Rooms.LivingR, Rooms.Kitchen, Rooms.Bedroom, Rooms.Bathroom]

boringPoints = 0
normalPoints = 5
chaoticPoints = 10

#Root y frame

root = tk.Tk()

frame = tk.Frame(root)

frame.config(width = 1400, height = 900)
frame.grid_propagate(False) 
frame.grid()

root.title("La venganza de Loki")

#Label1: descripción del juego o respuesta a la decisión de la habitación anterior.. Column 0, row 0

Label1 = tk.Label(frame, text = Textos.HallwayLabel1_All)
Label1.config(fg ="white", bg = "black", font = ("Tahoma", 16))
Label1.grid(columnspan = 3, row = 1, column = 1)

#Resto de columna 0:
Label2 = tk.Label(frame, text = Textos.HallwayLabel2)
Label2.config(fg ="white", bg = "black", font = ("Tahoma", 16))
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
            MapLabel['text'] = room.Map

            if pointsIncrement == boringPoints:
                Label1['text'] = room.Label1_Boring
            elif pointsIncrement == normalPoints:
                Label1['text'] = room.Label1_Normal
            elif pointsIncrement == chaoticPoints:
                Label1['text'] = room.Label1_Chaotic

def Ending():
    chosenEnding = [" "]

    if (currentPoints[0] == boringPoints * 5):
        chosenEnding = Endings.BoringEnding.text
    elif (currentPoints[0] > boringPoints * 5) and (currentPoints[0] <= normalPoints * 5):
        chosenEnding = Endings.NormalEnding.text
    elif (currentPoints[0] > normalPoints * 5):
        chosenEnding = Endings.ChaoticEnding.text
    
    Label1['text'] = chosenEnding
    
    for label in frame.winfo_children():
        if(label != Label1):
            label.destroy()

Button1 = tk.Button(frame, text = Textos.HallwayButton1, command = partial(ChangeRoomText, currentRoom, currentPoints, boringPoints), font = ("Tahoma", 16))
Button1.grid(row = 5, column = 1)

Button2 = tk.Button(frame, text = Textos.HallwayButton2, command = partial(ChangeRoomText, currentRoom, currentPoints, normalPoints), font = ("Tahoma", 16))
Button2.grid(row = 7, column = 1)

Button3 = tk.Button(frame, text = Textos.HallwayButton3, command = partial(ChangeRoomText, currentRoom, currentPoints, chaoticPoints), font = ("Tahoma", 16))
Button3.grid(row = 9, column = 1)

#Mapa y columna 4:
MapLabel = tk.Label(frame, text = Textos.HallwayMap)
MapLabel.config(fg ="white", bg = "black", font = ("Tahoma", 28))
MapLabel.grid(column = 5, columnspan = 1, row = 1)

#Configuración provisional de espacios entre columnas con contenido
frame.grid_columnconfigure(0, minsize = 100)
frame.grid_columnconfigure(4, minsize = 100)
frame.grid_rowconfigure(0, minsize = 50)
frame.grid_rowconfigure(2, minsize = 50)
frame.grid_rowconfigure(4, minsize = 50)
frame.grid_rowconfigure(6, minsize = 50)
frame.grid_rowconfigure(8, minsize = 50)

root.mainloop()