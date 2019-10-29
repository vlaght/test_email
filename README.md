# Требования
- Python 3
- requests 2.22.0

# Проверка
```shell
git clone git@github.com:vlaght/test_email.git
cd test_email
pipenv install
pipenv shell
python example.py
```
# Использование 
```python
from messaging.email import Email

email = Email(
    'test2@yandex.ru',
    'Hello yandex! I have an pic <img src="https://spam.org/pic1.png" /> for you.',
)
email.send() # пошлет POST-запрос на указанный url (messaging.email.EmailController.api_url)
email.fake_send() # для тестов, вернет обработанное сообщение 
```

# Создание правил

В **messaging/email/rules.py**

Новые правила пишутся в формате
```python
@RuleRegistry.add_rule('почтовый провайдер')
def rule1(content):
    #... Видоизменяем содержимое ...
    # возвращаем строку, которая будет новым содержимым
    return content
```

# Добавление почтовых провайдеров

В **messaging/email/controller.py**. Помимо добавления новых провайдеров, создание алиасов на существующие так же производится здесь.
```python
class EmailController:
    
    ...

    # Соответствие почтового домена почтовому провайдеру
    domain2provider = {
        'yandex.ru': 'yandex',
        'mail.ru': 'mail',
        'gmail.com': 'gmail',
        ...
        'почтовый домен': 'почтовый провайдер',
        # алиасы для mail.ru выглядели бы как
        'list.ru': 'mail',
        'bk.ru': 'mail',
        'inbox.ru': 'mail',
        ...
    }
```