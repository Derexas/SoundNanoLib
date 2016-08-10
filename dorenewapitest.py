import soundapi

# 2* PI / 44100 * freq
DO = 0.037275246167682
RE = 0.041840030159809
MI = 0.046963889416093
FA = 0.049756558695141
SOL = 0.055849823684532
LA = 0.062689377214490
SI = 0.070366403833691

notes = [DO, RE, MI, FA, SOL, LA ,SI]

audio = soundapi.Audio()

for note in notes:
    audio.adsound(note, round(0.5*44100))
audio.writefromprearray()
audio.saveaudioas('dorenewapitest.wav')
