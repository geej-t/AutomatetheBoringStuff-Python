def commaCode(list):
    if len(list) == 1:
        return list[0]
    return '{}, and {}'.format(', '.join(list[:-1]), list[-1])

spam = ['apples','bananas','tofu','cats']
commaCode(spam)
