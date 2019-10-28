from collections import defaultdict

class RuleRegistry:
    ''' Класс для обработки сообщений исходя из почтового домена '''
    
    # тут и будут лежать все списки правил для почтового провайдера
    mapping = defaultdict(list)

    @classmethod
    def add_rule(cls, provider):
        def wrapper(rule):
            cls.mapping[provider].append(rule)
            return rule
        return wrapper

    @classmethod
    def apply_rules(cls, provider, message):
        for rule in cls.mapping[provider]:
            message['content'] = rule(message['content'])    
        return message