from pygame import mixer
from gtts import gTTS



def main():
  tts = gTTS('Subscribe to Akhy ROI channel')
  tts.save('python.mp3')
  mixer.init()
  mixer.music.load('python.mp3')
  mixer.music.play()





if __name__ == "__main__":
  main()