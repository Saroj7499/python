'''
step1: Import package (gtts-Google text to speech convertor library)
step2: Create an Object of class
step3: save as Mp3
step4: Play Mp3
'''

from gtts import gTTS
import os
mytext = "hello everyone! Welcome to Python Workshop.."
MyVoice = gTTS(text=mytext,lang='en',slow='True')
MyVoice.save("MyVoice.Mp3")
os.system("MyVoice.Mp3")