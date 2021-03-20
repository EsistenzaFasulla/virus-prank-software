import os
import time

def spam():
    spamfile = open("aa.txt", "w")
    spamfile.write("hacked")
    spamfile.close()
    os.system("start aa.txt")

file = open("ciccio.vbs", "w")

file.write("""
set speechobject = createobject("sapi.spvoice")
speechobject.speak "COMPUTER HACKED! We're sending your data in our servers, ty for your collaboration!"
speechobject.speak "Loading... 5%"
speechobject.speak "COMPUTER HACKED! We're sending your data in our servers, ty for your collaboration!"
speechobject.speak "Loading... 22%"
speechobject.speak "COMPUTER HACKED! We're sending your data in our servers, ty for your collaboration!"
speechobject.speak "Loading... 55%"
speechobject.speak "COMPUTER HACKED! We're sending your data in our servers, ty for your collaboration!"
speechobject.speak "Loading... 78%"
speechobject.speak "COMPUTER HACKED! We're sending your data in our servers, ty for your collaboration!"
speechobject.speak "Loading... 92%"
speechobject.speak "Operation complete, u are successfully trolled by EsistenzaFasulla, with pizza and love."

""")

file.close()

os.system('start ciccio.vbs')

time.sleep(1)

os.remove("ciccio.vbs")

for x in range(53):
    spam()
    time.sleep(1)
    os.remove("aa.txt")