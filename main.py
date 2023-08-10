""" Logic_unit: main.
Объединяет модули логики, устанавливает правила перехода между ними и производит обзвон абонентов

"""

from libraries import NeuroNetLibrary, NeuroVoiceLibrary

import hello_logic
import main_logic
import hungup_logic
import forward_logic


nn = NeuroNetLibrary()
nv = NeuroVoiceLibrary()
# Считаем, что ранее было прописано, то что должно быть для запуска обзвона, проинициализированы переменные окружения,
# указаны маршруты SIP, информация о провайдерах, транках, COS, указана информация о языковых настройках, загружен
# список обзвона абонентов с временем начала.

# nn.dialog.entry_point = 'main_2'
# Задаем точку входа в логику.


# Примечание: Если бы логика в ТЗ была больше, то структура переходов была бы реализована аналогично переходам в
# модулях hello_logic <-> main_logic
def main_2():
    """ Точка входа в логику, обработка переходов между logic_unit
    (hello_logic <-> main_logic <-> hangup_logic <-> forward_logic).
    Обработка переадресации и отбой вызова по завершении логических модулей.

    """
    result_hello_logic = hello_logic.run(nn=nn, nv=nv)
    # Запуск hello_logic
    param_main_logic = result_hello_logic.get('entity/value', {})
    # Формирование аргументов для запуска следующего логического модуля.
    hello_logic_user_answer = result_hello_logic.get('user_answer', '')
    # Получение ответа пользователя из результата отработанной логики

    if hello_logic_user_answer == 'answer_yes' or hello_logic_user_answer == 'DEFAULT':
        # Определение дальнейших шагов в зависимости от ответов пользователя
        result_main_logic = main_logic.run(nn=nn, nv=nv, **param_main_logic)
        param_hungup_logic = result_main_logic.get('entity/value', {})
        if result_main_logic.get('user_answer', '') in ('answer_zero', 'answer_one', 'answer_two', 'answer_three',
                                                        'answer_four', 'answer_five', 'answer_six', 'answer_seven',
                                                        'answer_eight', 'answer_nine', 'answer_ten',
                                                        'answer_wrong_time'):
            result_hungup_logic = hungup_logic.run(nn=nn, nv=nv, **param_hungup_logic)
            # После логики hungup_logic.run запустить метод для завершения вызова (не нашел в описании библиотек)
            return result_hungup_logic
        if result_main_logic.get('user_answer', '') == 'answer_question':
            forward_logic.run(nv=nv, question=True)
            # После логики forward_logic.run запустить экшен bridge_action '

    if hello_logic_user_answer == 'answer_not' or hello_logic_user_answer == 'wrong_time':
        param_hungup_logic = result_hello_logic.get('entity/value', {})
        result_hungup_logic = hungup_logic.run(nn=nn, nv=nv, **param_hungup_logic)
        # После логики hungup_logic.run запустить метод для завершения вызова (не нашел в описании библиотек)
        return result_hungup_logic


if __name__ == "__main__":
    print(main_2())
