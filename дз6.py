text = input('Вітаю!\nВведіть текск для конвертації текстових смайлів: ')

if '>:(' in text:
    print(text.replace('>:(', '😠'))
elif '>:)' in text:
    print(text.replace('>:)', '😈'))
elif ':)' in text:
    print(text.replace(':)', '🙂'))
elif 'XD' in text:
    print(text.replace('XD', '😂'))
elif ':(' in text:
    print(text.replace(':(', '🙁'))
else:
    print('Помилка')
