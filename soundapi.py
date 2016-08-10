import wave, struct, math

class Audio:

    """ SAMPLE_LEN, posinaudio, audioarray """
    
    def __init__(self):
        self.posinsin = 0
        self.audioarray = []
        self.prearray = []

    def addsound(self, t, length):
        for i in range(length): # nombre de frame concernées
            value = round(math.sin(self.posinsin) * 32267/10) # * the max data size (int 32bit) / to reduce sound
            packed_value = struct.pack('h', value) # pack each little hertz in the struct
            self.audioarray.append(packed_value) # double append because the sound is bi-canal
            self.audioarray.append(packed_value)
            self.posinsin += t # update val with the last t to continue following the sin curve with the good decal
            
    def adsound(self, ft, length):
        framelength = len(self.prearray)
        self.adddsound(ft, framelength, framelength + length)
            
    def adddsound(self, ft, b, e): # beginning and end of the sound in frames
        if e > b:
            if len(self.prearray) > b:
                #stupid because it's the sum total which must be calibrated
                #posin must be at 0 at existing jonctions so it doesn't create problems
                #begin at 0 so it don't break in two existing sounds
                posinsin = 0
            elif len(self.prearray) == b and b != 0:
                posinsin = self.posinsin
                posinsin += ft(1)
                self.prearray.append(0)
            else:
                posinsin = 0
            for frame in range(b,e): # nombre de frame concernées
                i0 = self.geti0(frame, b, e)
                value = round(math.sin(posinsin) * 32267/10 * i0) # * the max data size (int 32bit) / to reduce sound
                while frame >= len(self.prearray):
                    self.prearray.append(0)
                self.prearray[frame] += value
                #self.posinsin = posinsin
                posinsin += ft(frame - b)
            self.posinsin -= ft(e - b)
            if e < len(self.prearray):
                frame = e
                while round(math.sin(posinsin) * 32267/10) != 0:
                    if frame >= len(self.prearray):
                        self.prearray.append(0)
                    self.prearray[frame] += value
                    #self.posinsin = posinsin
                    posinsin += ft(frame - b)
                    frame += 1
        else:
            print("You can't use a e smaller than the b")
        
    def writefromprearray(self):
        b = list(self.audioarray)
        for i in range(len(b)):
            self.audioarray[i] = b[i][0]
        for v in self.prearray:
            packed_value = struct.pack('h', v) # pack each little hertz in the struct
            self.audioarray.append(packed_value) # double append because the sound is bi-canal
            self.audioarray.append(packed_value)
            
    def saveaudioas(self, filename):
        audio_output = wave.open(filename, 'w')
        audio_output.setparams((2, 2, 44100, len(self.audioarray), 'NONE', 'not compressed'))
        audio_str = b''.join(self.audioarray) # encode the content of values to a bit string
        audio_output.writeframes(audio_str) # write the data into the file
        audio_output.close()
        print('done')
        
    def getlength(self):
        return len(self.prearray)
    
    def geti0(self, frame, b, e):
        vv = 100 #too short and short sounds may not even have the to born and die quietly!
        i0 = 1
        if (frame - b)/44100 < 1/vv:
           i0 = (frame - b)/44100 * vv
           #i0 = 0
        elif (e - frame)/44100 < 1/vv:
            i0 = (e - frame)/44100 * vv
            #i0 = 0
        else:
            i0 = 1
        return i0


