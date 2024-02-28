import speech_recognition as sr
import datetime
# Set the file name of the transcription file as the date
now = datetime.datetime.now()
txtname= now.strftime('%Y%m%d_%H%M%S') + ".txt"
r = sr.Recognizer()
mic = sr.Microphone()
r.dynamic_energy_threshold= False # This will speed up the response
# https://stackoverflow.com/questions/32753415/python-speechrecognition-ignores-timeout-when-listening-and-hangs
while True:
print("Say something ...")
with mic as source:
r.adjust_for_ambient_noise(source) # Noise countermeasures
audio = r.listen(source)
now = datetime.datetime.now()
wavname= now.strftime('%Y%m%d_%H%M%S') + ".wav"
with open(wavname, "wb") as file:
file.write(audio.get_wav_data())
print ("Now to recognize it...")
try:
rcg= r.recognize_google(audio, language='ja-JP')
print(rcg)
with open(txtname, 'a') as f: # Append to the end of the file
f.write(rcg+ "¥n")
# Stop voice recognition when you say "stop"
if rcg== "ストップ" :
print("end")
break
# Below is the exception handling when the voice cannot be recognized
except sr.UnknownValueError:
print("could not understand audio")
except sr.RequestErroras e:
print("Could not request results from Google Speech Recognition service; {0}".format(e))