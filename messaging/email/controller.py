import logging

import requests

from .rules import RuleRegistry


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class EmailController:
    ''' Данный класс занимается обработкой сообщений и их отправкой '''

    # куда POST-им сообщение
    api_url = 'https://email-machine.internal/api/email-gate/{email_domain}/'

    # Соответствие почтового домена почтовому провайдеру
    domain2provider = {
        'yandex.ru': 'yandex',
        'mail.ru': 'mail',
        'gmail.com': 'gmail',
    }

    # провайдер по-умолчанию, используется для писем, почтовых доменов которых 
    # нет в маппинге domain2provider
    default_provider = 'gmail'

    def __init__(self, email, content):
        self.original_message = dict(email=email, content=content)
        self.provider = self.get_provider()

    def get_provider(self):
        domain = self.original_message["email"].split("@")[-1]
        return self.domain2provider.get(domain, self.default_provider)

    def send(self):
        processed_message = RuleRegistry.apply_rules(
            self.provider,
            self.original_message
        )

        # мы же не хотим покрашить основной поток исполнения
        try:
            requests.post(
                self.api_url.format(email_domain=self.provider),
                json=processed_message
            )
        except requests.RequestException as e:
            logger.exception(e)

    def fake_send(self):
        ''' Для тестов, возвращает обработанное сообщение '''
        processed_message = RuleRegistry.apply_rules(
            self.provider,
            self.original_message
        )
        return processed_message

