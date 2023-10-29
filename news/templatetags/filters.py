from django import template


register = template.Library()  # если мы не зарегестрируем наши фильтры, то django никогда не узнает где именно их искать 

censor_words = {
    'плохо': 'хорошо',
    'нецензурное': 'цензурное',
}


@register.filter(name='censor')
def censor(value):
    censored_text = value
    for word, replacement in censor_words.items():
        censored_text = censored_text.replace(word, replacement)
    return censored_text
