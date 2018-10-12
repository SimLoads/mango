Dim message, sapi
message=InputBox("Bingus", "Bingus") 
Set sapi=CreateObject("sapi.spvoice")
sapi.Speak message