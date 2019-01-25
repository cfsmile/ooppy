# polymorphism demo
class AudioFile:
    def __init__(self, filename):
        if not filename.endswith(filename[-3:]):
            raise Exception("Invalid file format")
        self.filename = filename
        self.ext = filename[-3:]

    def play(self):
        print("Now an audio file is going to play...{} as {}".format(self.filename, self.ext))


class MP3File(AudioFile):
    def __init__(self, filename):
        super().__init__(filename)
        self.ext = "mp3"
        
    def play(self):
        # super().play()
        print("playing {} as mp3".format(self.filename))


class WavFile(AudioFile):
    def __init__(self, filename):
        super().__init__(filename)
        self.ext = filename[-3:]
        
    def play(self):
        print("playing {} as {}".format(self.filename, self.ext))


class OggFile(AudioFile):
    def __init__(self, filename):
        super().__init__(filename)
        self.ext = filename[-3:]
        
    def play(self):
        print("playing {} as ogg".format(self.filename))

        
class FlacFile(AudioFile):
    def __init__(self,filename):
        super().__init__(filename)
        self.ext = filename[-3:]
        
    def play(self):
 
        print("playing {} as flac".format(self.filename))

print("===split line ===")
mp3 = MP3File("myfile.mp3")
mp3.play()
print("===split line ===")
wav = WavFile("myfile.wav")
wav.play()
print("===split line ===")
not_an_mp3 = MP3File("myfile.nothing")
not_an_mp3.play()
print('Clearly, it is going to cause decoding error!')
print("===split line ===")
flac = FlacFile("myfile.flac")
flac.play()
print(flac.ext)
print("===split line ===")

print('----------another split line------------')
afile = MP3File("myfile.mp3")
bfile = WavFile("myfile.wav")
cfile = FlacFile("myfile.flac")

music_file = [afile, bfile, cfile]
for x in music_file:
    x.play()


# polymorphism demo
class Person(object):      
    def __init__(self, name, gender):
        self.name = name   
        self.gender = gender

    def whoAmI(self):      
        return 'I am a Person, my name is %s' % self.name
 
class Student(Person):     
    def __init__(self, name, gender, score):
        self.name = name   
        self.gender = gender

    def whoAmI(self):      
        return 'I am a Student, my name is %s' % self.name
 

class Teacher(Person):                                                                                                                                             
    def __init__(self, name, gender, course):
        super(Teacher, self).__init__(name, gender)
        self.course = course
    def whoAmI(self):
        return 'I am a Teacher, my name is %s' % self.name
 
  
def who_am_i(x):
    print(x.whoAmI())

    
p = Person('Tim', 'Male')
s = Student('Bob', 'Male', 88)
t = Teacher('Alice','Female', 'English')
 
who_am_i(p)
who_am_i(s)
who_am_i(t)
