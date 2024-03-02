# Jarvis v1 ---------------------------------------------

import speech_recognition, pyttsx3, datetime
from funcs import *

# приветствие
def hello():
    now = datetime.datetime.now()
    if now.hour >= 6 and now.hour < 12:
        talk('Доброе утро, Денис')
    elif now.hour >= 12 and now.hour < 18:
        talk('Добрый день, Денис')
    elif now.hour >= 18 and now.hour < 23:
        talk('Добрый вечер, Денис')
    else:
        talk('Доброй ночи, Денис')

dictionary = {
    open_browser: ('браузер', 'открой', 'яндекс'),
    calculate: ('+', '-', '/', 'х', 'x'),
    switch_language: ('переключи', 'язык'),
    open_task_manager: ('диспетчер', 'задач', 'открой', 'открыть'),
    open_explorer: ('проводник', 'компьютер', 'мой', 'открой', 'открыть'),
    input_text: ('ввод', 'введи', 'напиши', 'набор', 'вот'),
    open_options: ('настройки', 'опции', 'открой', 'открыть'),
    off_PC: ('выключи', 'выключить', 'компьютер'),
    kill_process: ('заверши', 'процесс', 'завершить', 'программу'),
    control_panel: ('панель', 'управления', 'открой', 'открыть'),
    device_manager: ('диспетчер', 'устройств', 'устройства', 'открой', 'открыть'),
    wallpaper: ('фон', 'смена', 'рабочего', 'стола', 'обои', 'смени'),
    screenshot: ('скриншот', 'экрана', 'снимок', 'экран'),
    disable_script: ('выключись', 'остановись', 'вырубись', 'закругляйся', 'выход'),
    cmd: ('консоль', 'открой', 'открыть'),
    search_text: ('найти', 'фрагмент', 'текст', 'поиск', 'тексте', 'найди'),
    hide_windows: ('свернуть', 'окно', 'окна', 'рабочий', 'стол', 'спрячь', 'сверни', 'спрятать'),
    open_calculator: ('калькулятор', 'открой', 'открыть'),
    open_translator: ('переводчик', 'открой', 'открыть'),
    search_google: ('гугл', 'google'),
    find_yt_video: ('видео', 'video', 'youtube'),
    wiki: ('вики', 'википедия'),
    get_joke: ('шутка', 'пошути', 'шутку', 'анекдот'),
    translate: ('переведи', 'переводчик'),
    get_news: ('новость', 'новости'),
    get_weather: ('погода', 'прогноз')
}

# старт
def start():
    sr = speech_recognition.Recognizer()
    sr.pause_threshold = 0.5
    global ttsEngine
    ttsEngine = pyttsx3.init()
    ttsEngine.setProperty('voice', 'ru')   #

    hello()

    # постоянное прослушивание speech_recognition
    while True:
        with speech_recognition.Microphone() as mic:
            sr.adjust_for_ambient_noise(source=mic, duration=0.1) #стояло 0.1 (2)
            audio = sr.listen(source=mic)
            try:
                query = sr.recognize_google(audio_data=audio, language='ru-RU').lower()
                if 'лили' in query:
                    query = query.replace('лили', '')
                    query = query.strip()
                    res = response(query)
                    if type(res) is str:
                        talk(res)
                    else:
                        if res.__name__ in ['calculate', 'wiki', 'translate', 'get_weather']:
                            talk(res(query))
                        elif res.__name__ in ['get_joke', 'find_ip', 'coin', 'get_news', 'get_advice', 'rnd_feedback']:
                            talk(res())
                        elif res.__name__ in ['search_google', 'find_yt_video', 'set_volume', 'input_text']:
                            res(query)
                        else:
                            res()
            except SystemExit:
                raise
            except:
                pass

# обработка ответа
def response(query):
    res = None
    max = 0
    words_query = query.split(' ')
    for key, arr in dictionary.items():
        k = 0
        for value in arr:
            for word in words_query:
                if str(word) == str(value):
                    k += 2
                if word in value:
                    k += 1
        if k > max:
            max = k
            res = key
    return res

# озвучка
def talk(text):
    ttsEngine.say(text)
    ttsEngine.runAndWait()

# старт программы
if __name__ == '__main__':
    start()

