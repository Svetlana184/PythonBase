#%% md
# Дан файл, содержащий текст, включающий русские и английские слова. Подсчитать, каких букв в тексте больше - русских или английских
#%%
import re

def count_letters(filename):
    try:
        with open(filename, encoding='utf-8') as file:
            text = file.read()
    except:
        return "Ошибка при чтении файла"

    russian = len(re.findall(r'[А-Я, а-я]', text))
    english = len(re.findall(r'[A-Z, a-z]', text))

    if russian > english:
        return "Русских букв больше."
    elif english > russian:
        return "Английских букв больше."
    else:
         return "Русских и английских букв одинаково."
