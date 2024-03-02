import webbrowser as wb
import os, pyautogui, pyperclip, ctypes, wikipedia, pywhatkit, requests, bs4
from random import choice
from more_funcs import del_first_word
from sys import exit
#from sound.sound import Sound
from googletrans import Translator
from random import choice

wallpaper_path = 'C:/Users/black/Pictures/'
OPENWEATHER_APP_ID = '76391fcfc715c563fbd756cbc2cd0438'
NEWS_API_KEY = 'f249729b62714404b9cd3ccf6c15b4c1'

# браузерные

# открыть яндекс
def open_browser():
    wb.open_new_tab('https://dzen.ru/')

# переводчик
def translate(text, del_word=True):
    if del_word:
        text = del_first_word(text)
    translator = Translator()
    if (translator.translate(text).src == 'ru'):
        result = translator.translate(text, src='ru', dest='en')
    else:
        result = translator.translate(text, src='en', dest='ru')
    return result.text

# погода
def get_weather(text):
    city = text.replace('погода', '').replace('прогноз', '')
    city = translate(city, False)
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
    weather = translate(res["weather"][0]["main"], False)
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"температура {temperature}℃", f"ощущается как {feels_like}℃"

# новости
def get_news():
    news_headlines = []
    res = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append( article["title"])
    rnd_news = translate(choice(news_headlines), False)
    return rnd_news

# википедия
def wiki(text):
    text = del_first_word(text)
    res = wikipedia.summary(text, sentences=1, auto_suggest=False)
    return translate(res, False)

# гугл
def search_google(text):
    text = del_first_word(text)
    pywhatkit.search(text)

# найти видео
def find_yt_video(text):
    text = del_first_word(text)
    pywhatkit.playonyt(text)

# калькулятор
def open_calculator():
    wb.open_new_tab('https://okcalc.com/ru/')

# переводчик
def open_translator():
    wb.open_new_tab('https://www.deepl.com/translator')

# системные

# диспетчер задач
def open_task_manager():
    os.system('taskmgr')

# установить звук
def set_volume(value):
    value = int (''.join(filter(str.isdigit, value)))
    Sound.volume_set(value)
# консоль
def cmd():
    os.system('cmd')

# выключить пк
def off_PC():
    os.system('shutdown -s')

# переключить язык
def switch_language():
    pyautogui.hotkey('alt', 'shift')

# настройки
def open_options():
    pyautogui.hotkey('winleft', 'i')

# калькулятор
def calculate(text):
    text = str(text).replace('х', '*').replace('на', '*').replace('x', '*')
    try:
        result = eval(text)
    except:
        result = 'Вы определённо ошиблись.'
    return result

# ввод текста
def input_text(text):
    text = del_first_word(text)
    buffer = pyperclip.paste()
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl', 'v')
    pyperclip.copy(buffer)

# проводник
def open_explorer():
    os.system("start D:/")

# завершить процесс
def kill_process():
    pyautogui.hotkey('alt', 'f4')

# панель управления
def control_panel():
    os.system('control.exe')

# диспетчер устройств
def device_manager():
    os.system('devmgmt.msc')

# сменить обои
def wallpaper():
    path_to_image = wallpaper_path+choice(os.listdir(wallpaper_path))
    ctypes.windll.user32.SystemParametersInfoW(20,0,path_to_image,0)

# скриншот
def screenshot():
    pyautogui.hotkey('win', 'printscreen')

# остановить скрипт
def disable_script():
    exit()

# найти в тексте
def search_text():
    pyautogui.hotkey('ctrl', 'f')

# свернуть окна
def hide_windows():
    pyautogui.hotkey('winleft', 'd')

# notepad
def open_notepad():
    os.system("notepad.exe file.txt")

# шутка
def get_joke():
    response = requests.get('http://anekdotme.ru/random')
    soup = bs4.BeautifulSoup(response.text, 'html.parser')
    jokes_list = soup.find_all('div', class_='anekdot_text')
    random_joke = choice(jokes_list).text.strip()
    return random_joke
