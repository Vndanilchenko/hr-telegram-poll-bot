бот опроса соискателей о причинах отказа от позиции

стек: Python, Heroku

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

    усправление мультипроцессингом
    heroku ps:scale worker=1 -a hr-telegram-poll-bot

</xml>


@author: vndanilchenko@gmail.com