import Textos

class Ending:
    
    def __init__(self, text, picture, endingID):
        self.text = text
        self.picture = picture
        self.endingID = endingID

BoringEnding = Ending(Textos.BoringEndingText, "Picture_Boring", 0)
NormalEnding = Ending(Textos.NormalEndingText, "Picture_Normal", 1)
ChaoticEnding = Ending(Textos.ChaoticEndingText, "Picture_Chaotic", 2)