import Textos

class Room:     
  
    def __init__(self, Label1_Boring, Label1_Normal, Label1_Chaotic, Label2, Button1, Button2, Button3, Map, RoomID):
        self.Label1_Boring = Label1_Boring
        self.Label1_Normal = Label1_Normal
        self.Label1_Chaotic = Label1_Chaotic
        self.Label2 = Label2
        self.Button1 = Button1
        self.Button2 = Button2
        self.Button3 = Button3
        self.Map = Map
        self.RoomID = RoomID

Hallway = Room(
    Textos.HallwayLabel1_All, Textos.HallwayLabel1_All, Textos.HallwayLabel1_All, 
    Textos.HallwayLabel2, Textos.HallwayButton1, Textos.HallwayButton2 , 
    Textos.HallwayButton3, Textos.HallwayMap, Textos.HallwayRoomID
    )

LivingR = Room(
    Textos.LivingRLabel1_Boring, Textos.LivingRLabel1_Normal, Textos.LivingRLabel1_Chaotic, 
    Textos.LivingRLabel2, Textos.LivingRButton1, Textos.LivingRButton2 , 
    Textos.LivingRButton3, Textos.LivingRMap, Textos.LivingRRoomID
    )

Kitchen = Room(
    Textos.KitchenLabel1_Boring, Textos.KitchenLabel1_Normal, Textos.KitchenLabel1_Chaotic,
    Textos.KitchenLabel2, Textos.KitchenButton1, Textos.KitchenButton2,
    Textos.KitchenButton3, Textos.KitchenMap, Textos.KitchenRoomID
    )

Bedroom = Room(
    Textos.BedroomLabel1_Boring,Textos.BedroomLabel1_Normal, Textos.BedroomLabel1_Chaotic,
    Textos.BedroomLabel2, Textos.BedroomButton1, Textos.BedroomButton2,
    Textos.BedroomButton3, Textos.BedroomMap, Textos.BedroomRoomID
    )

Bathroom = Room(
    Textos.BathroomLabel1_Boring, Textos.BathroomLabel1_Normal, Textos.BathroomLabel1_Chaotic,
    Textos.BathroomLabel2, Textos.BathroomButton1, Textos.BathroomButton2,
    Textos.BathroomButton3, Textos.BathroomMap, Textos.BathroomRoomID
    )