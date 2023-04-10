from django import template


register = template.Library()



@register.filter()
def censor(text):
	#text.replace(word, '*' * len(censored_word)))
	return f'{text}'


# так и не разобрался 
