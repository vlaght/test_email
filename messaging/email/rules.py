import re

from .registry import RuleRegistry

'''
Новые правила пишутся в формате
@RuleRegistry.add_rule(provider_name)
def rule1(content):
    ... do something with content ...
    return new_content
'''

@RuleRegistry.add_rule('gmail')
def delete_offer_sentences(content):
    offer_re = re.compile(r"([^\!\?\.]*?offer.*?[\!\?\.])", re.IGNORECASE)
    content = offer_re.sub('', content, count=0)
    return content

@RuleRegistry.add_rule('gmail')
def uppercase(content):
    return content.upper()

@RuleRegistry.add_rule('mail')
def replace_gif_extension(content):
    img_tag_re = re.compile(
        r"<img src=[\"'](.+?)(\.gif)[\"'].*\/>", re.IGNORECASE
    )
    content = img_tag_re.sub(r'<img src="\1.png" />', content, count=0)
    return content

@RuleRegistry.add_rule('yandex')
def replace_img_tag(content):
    img_tag_re = re.compile(r"<img src=[\"'](.+?)[\"'].*\/>", re.IGNORECASE)
    content = img_tag_re.sub(r'\1', content, count=0)
    return content
