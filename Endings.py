import Textos

class Ending:
    
    def __init__(self, text, endingID):
        self.text = text
        self.endingID = endingID

BoringEnding = Ending(Textos.BoringEndingText, 0)
NormalEnding = Ending(Textos.NormalEndingText, 1)
ChaoticEnding = Ending(Textos.ChaoticEndingText, 2)