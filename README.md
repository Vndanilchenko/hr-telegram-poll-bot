# hr-telegram-poll-bot
бот опроса соискателей о причинах отказа от позиции

стек: Python, Heroku

бот выполняет опрос согласно логике:
* старт + приветствие
* выбор пунктов из меню (узнать функционал, пройти опрос)
![greetings](media/приветствие.png)
* поэтапное прохождение сценария опроса и выбор вариантов вопросов
![first_question](media/1%20вопрос.png)
*  завершение сценария при прощании
![farewell](media/3%20вопрос%20другое%20+%20пока.png)
* выгрузка пройденных опросов (отправка только админу)
![export](media/экспорт%20базы%20данных.png) 

полезные команды Heroku:

<xml>

    проверить статус Сервиса
    heroku ps -a hr-telegram-poll-bot

</xml>

<xml>

    информация о Сервисе
    heroku apps:info -a hr-telegram-poll-bot

</xml>

<xml>

    вывести последние логи
    heroku logs -a hr-telegram-poll-bot --tail

</xml>

<xml>

    запуск приложения
    heroku ps:scale worker=1 -a hr-telegram-poll-bot

</xml>

<xml>

    остановка приложения
    heroku ps:scale worker=0 -a hr-telegram-poll-bot

</xml>

@author: vndanilchenko@gmail.com