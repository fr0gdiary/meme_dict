import time
meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            "РОФЛ": "Шутка",
            "КРИПОВЫЙ": "Страшный, пугающий"
            }

print('Привет! Добро пожаловать в ВСС(Владение Современым Сленгом)!')
time.sleep(2)
word = input("Введите непонятное слово (большими буквами!), а мы расскажем значение: ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print('Мы такого слова к сожалению не знаем.')
