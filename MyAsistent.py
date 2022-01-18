import subprocess
import speech_recognition
import pyautogui
import webbrowser
import random
from array import array
import keyboard


def music():
    webbrowser.open_new_tab('https://vk.com/audios561355664?section=all')
    koor = pyautogui.size()
    pyautogui.click(x=610, y=200, clicks=3, interval = 1.2, button='left')
    pyautogui.click(x=1800, y=0, clicks=1, button='left')
   

def porn():
    i = random.randint(1, 29700)
    webbrowser.open_new_tab(f'http://porno365.biz/movie/{i}')
    size = pyautogui.size()
    pyautogui.click(x = 800, y = 500, clicks = 2, interval = 1.5, button = 'left')

def gayporn():
    webbrowser.open_new_tab(f'http://porno365.biz/movie/{i}')
    size = pyautogui.size()
    pyautogui.click(x = 800, y = 500, clicks = 2, interval = 1.5, button = 'left')

def close():
    keyboard.send("alt+f4")

def minus():
    keyboard.send("windows + m")

def main():
#Словари#
    _music_ = ['музыка', 'включи музыку', 'слушать музыку', 'включить музыку']
#########
    print("Чем могу помочь?")
    
    sr = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as mic:
        sr.adjust_for_ambient_noise(source = mic, duration = 0.7)
        audio = sr.listen(source = mic)

        query = sr.recognize_google(audio_data = audio, language = "ru-RU").lower()
    print(query)

    if query == 'выключить':
        subprocess.call(["shutdown", "/s"])
        return main()
    elif query == 'перезагрузить':
        subprocess.call(["shutdown", "/r"])
        return main()
    elif query == 'отмена':
        subprocess.call(["shutdown", "/a"])
        return main()
    elif query == 'закрой ebalo':
        print('Сам закрой!')
        return main()
    elif query == 'открыть telegram':
        subprocess.call('C:/Users/Lenovo/Telegram Desktop/Telegram.exe')
        return main()
    elif query == 'запустить':
        subprocess.call('C:/D/steamapps/common/Counter-Strike Global Offensive/csgo.exe')
        return main()    
    for i in range(-1, len(_music_)):
        if query == _music_[i]:
            music()
            return main()
    if query == 'включить порно':
        porn()
        return main()
    elif query == 'выход':
        return 0
    elif query == 'гей':
        gay_porn()
    elif query == 'закрыть':
        close()
        return main()
    elif query == 'свернуть':
        minus()
        return main()
    else:
        print("Пока что я такого не умею ;(\n")
        return main()


main()
#on = speech_recognition.Recognizer()

#with speech_recognition.Microphone() as mic:
   #on.adjust_for_ambient_noise(source = mic, duration = 0.7)
   #audio = on.listen(source = mic)
   #point = on.recognize_google(audio_data = audio, language = "ru-RU").lower()
#print(point)

#while point != 'включить':
 #   if point == 'включить':
      #  print('Вы успешно вошли в систему\n\n')
       # main()
   # else: 
        #continue       
