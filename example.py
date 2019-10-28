from messaging.email import Email

if __name__ == '__main__':
    # немного простых тестов на основе примеров работы из описания задания

    # ex1
    email = Email(
        'test2@yandex.ru',
        'Hello yandex! I have an pic <img src="https://spam.org/pic1.png" /> for you.',
    )
    ex1 = {
        'email': "test2@yandex.ru",
        'content': 'Hello yandex! I have an pic https://spam.org/pic1.png for you.',
    }
    assert email.fake_send() == ex1, 'ex1 failed!'
    print('ex1 passed!')

    # ex2
    email = Email(
        'test3@mail.ru', 
        'Hello mail! I have an pic <img src="https://spam.org/pic1.gif" /> for you.',
    )
    ex2 = {
        'email': 'test3@mail.ru',
        'content': 'Hello mail! I have an pic <img src="https://spam.org/pic1.png" /> for you.',
    }
    assert email.fake_send() == ex2, 'ex2 failed!'
    print('ex2 passed!')

    # ex3
    email = Email(
        'test4@sailplay.ru',
        'Hello another mail client! I have an offer for you.'
    )
    ex3 = {
        'email': 'test4@sailplay.ru',
        'content': 'Hello another mail client!',
    }
    assert email.fake_send() == ex3, 'ex3 failed!'
    print('ex3 passed!')

    # ex4
    email = Email(
        'test1@gmail.com',
        'Hello gmail! I have an offer for you.'
    )
    ex4 = {
        'email': 'test1@gmail.com',
        'content': 'Hello gmail!',
    }
    assert email.fake_send() == ex4, 'ex4 failed!'
    print('ex4 passed!')