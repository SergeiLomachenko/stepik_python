import random

answer = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да","Можешь быть уверен в этом", "Мне кажется - да",
          "Вероятнее всего", "Хорошие перспективы", "Знаки говорят - да", "Да", "Пока неясно, попробуй снова", "Спроси позже",
          "Лучше не рассказывать", "Сейчас нельзя предсказать", "Сконцентрируйся и спроси опять", "Даже не думай",
          "Мой ответ - нет", "По моим данным - нет", "Перспективы не очень хорошие", "Весьма сомнительно"]

def shar():
    input("Задай вопрос: ")
    num = random.randint(0, 19)
    print(answer[num])

    if input("Хочешь задать еще вопрос? ").lower() in ("да", 'yes'):
        shar()
    else:
        print("Тогда до встречи")

shar()

