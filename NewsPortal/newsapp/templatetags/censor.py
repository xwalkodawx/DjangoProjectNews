from django import template


register = template.Library()

censored_word = ['Блять',
				 'Блядина',
				 'Пизда',
				 'Хуй',
				 'Хуевый',
				 'Хуевато',
				 'Хуйня',
				 'Пиздлявый',
				 'Ебанутый',
				 'Ебать',
				 'Ебаться',
				 'Ебан',
				 'Хуйло',
				 'Хуисос',
				 'Хуисосина',
				 ]


@register.filter()
def censor(text):
	#text.replace(word, '*' * len(censored_word)))
	return f'{text}'
