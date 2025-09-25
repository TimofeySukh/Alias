import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
from random import *
import threading
import time
working = True
remaining_seconds = 0 # Или другое начальное значение, это будет перезаписано
class alias_default:
    # Настройка API
    API_KEY = os.getenv("GOOGLE_API_KEY")
    genai.configure(api_key=API_KEY)
    # Инициализация модели
    model = genai.GenerativeModel('gemini-1.5-flash')
    def countdown_timer(seconds):
        global working
        global remaining_seconds
        remaining_seconds = seconds

        while remaining_seconds > 0:
            time.sleep(1)
            remaining_seconds -= 1

        print("finished")
        working = False
    def generating_alias():
        word = input("Введите тему/фандом для генерации слов (например, 'Берсерк' или 'Гарри Поттер'): ")
        prompt = f"""Сгенерируй список из 50 русских слов для игры Элиас, связанных с темой или фандомом '{word}'.
        Приоритет отдай словам из следующих категорий, если они применимы к фандому:
        1. Персонажи (герои, злодеи, второстепенные)
        2. Предметы и Артефакты (оружие, магические предметы, важные вещи)
        3. Названия (локации, заклинания, организация, книги, события)
        4. Города, Локации и Места действия
        5. Монстры, Существа и Расы
        Если после перечисления слов из этих категорий не наберется 50 слов, дополни список другими словами, тесно связанными с темой/фандомом.
        Слова должны быть:
        - Существительными в единственном числе
        - Не слишком сложными для объяснения
        - Разделенными запятыми
        - Без нумерации
        Верни только список слов, без дополнительного текста."""
        
        response = alias_default.model.generate_content(prompt)
        word_list = [word.strip() for word in response.text.split(',')]
        return word_list
        
global_word_list = []
global_word_list = alias_default.generating_alias()

class alias_game:
    points = 20
    seconds = 60
    settings = input("Do you want default settings: 20 points, 60 sec? ")
    if settings == "yes":
        pass
    elif settings == "no":
        points = int(input("ok then how many points you need to win? "))
        seconds = int(input("ok how many seconds is one round? "))
    
    while True:
        counter = 0
        ready = input("Are you ready? ")
        if ready:
            timer_thread = threading.Thread(target=alias_default.countdown_timer, args=(seconds,))
            timer_thread.start()
            print("timer started - write a if correct and s if wrong")
            working = True
            while remaining_seconds > 0 and counter < points:
                print(choice(global_word_list))
                checking = input()
                if checking == "a":
                    counter += 1
                else:
                    counter -= 1
 
            print("jo you got ", counter)
            counter = 0
        #restart = input("you wanna play again? ")
        #if restart 
        
























if __name__ == "__main__":
    result = generating_alias() # Здесь мы получаем список из функции!

