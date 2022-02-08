from requests import get, utils


def currency_rates(code: str) -> float:
    """возвращает курс валюты `code` по отношению к рублю"""
    # ваша реализация здесь
    response = utils.get_unicode_from_response(get(('http://www.cbr.ru/scripts/XML_daily.asp')))
    new_text = str(response).split('<Valute ID=')
    save_value = []
    notepad ={}
    for i in range(len(new_text)):
        start = new_text[i].find('<Value>')
        end = new_text[i].find('</Value>')
        start_code = new_text[i].find('<CharCode>')
        end_code = new_text[i].find('</CharCode>')
        save_value = new_text[i][start + 7: end].replace(",", ".")
        code_save = new_text[i][start_code + 10: end_code]
        notepad[code_save] = save_value
        # print(notepad)
    result_value = notepad.get(code.upper())
    return result_value

print(currency_rates("JPY"))
print(currency_rates("ER"))




"""
 for i in range(len(new_text)):
        if code in new_text[i]:
            start = new_text[i].find('<Value>')
            end = new_text[i].find('</Value>')
            save_str = new_text[i][start + 7: end].replace(",", ".")
            #print(save_str)
            notepad = notepad.fromkeys([code], save_str)
    result_value = notepad.get(code)
    print(notepad)
    return result_value
"""


