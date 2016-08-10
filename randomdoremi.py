import soundapi, math, time
from random import random

time0 = time.time()

DO = 0.037275246167682
RE = 0.041840030159809
MI = 0.046963889416093
FA = 0.049756558695141
SOL = 0.055849823684532
LA = 0.062689377214490
SI = 0.070366403833691

notes = [DO, RE, MI, FA, SOL, LA ,SI]
nnotes = 20 # round(random()*10)

audio = soundapi.Audio()

for i in range(nnotes):
    t = notes[math.floor(random()*len(notes))]
    ft = lambda i: t
    audio.adsound(ft, round(random()*44100) + 2000)

print(time.time() - time0)
time0 = time.time()


for i in range(nnotes//2):
	note = notes[math.floor(random()*len(notes))]
	ft = lambda i: t
	beginning = int(audio.getlength()*random())
	end = beginning + round(random()*44100 * 2) + 2000
	audio.adddsound(ft, beginning, end)


print(time.time() - time0)
time0 = time.time()
    
audio.writefromprearray()

print(time.time() - time0)
time0 = time.time()
    
audio.saveaudioas('rddoremifasollasi.wav')

print(time.time() - time0)
