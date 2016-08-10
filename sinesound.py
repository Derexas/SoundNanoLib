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

t = 2 * math.pi / 44100 * 3000
ft = lambda i: t * math.sin(i/10000) + 1
audio.adsound(ft, 8 * 44100)

print(time.time() - time0)
time0 = time.time()
    
audio.writefromprearray()
audio.saveaudioas('growingfreq.wav')

print(time.time() - time0)
