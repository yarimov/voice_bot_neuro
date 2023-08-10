from libraries import NeuroNetLibrary, NeuroVoiceLibrary


def recommend_main(nn: NeuroNetLibrary, nv: NeuroVoiceLibrary):
    """ Логика начального вопроса. """
    nv.say('recommend_main')
    # Воспроизведение сообщения 'recommend_main'
    user_answer = has_reaction_by_answer()
    # Запрос ответа пользователя
    return map_resolver(nn, nv, user_answer=user_answer)
    # Определение дальнейшего шага (функции)


def recommend_repeat(nn: NeuroNetLibrary, nv: NeuroVoiceLibrary):
    """ Логика обработки ответа пользователя: - "еще раз". """
    nv.say('recommend_repeat')
    # Воспроизведение сообщения 'recommend_repeat'
    user_answer = has_reaction_by_answer()
    # Запрос ответа пользователя
    return map_resolver(nn, nv, user_answer=user_answer)
    # Определение дальнейшего шага (функции)


def recommend_repeat_2(nn: NeuroNetLibrary, nv: NeuroVoiceLibrary):
    """ Логика обработки ответа пользователя: - "Не знаю". """
    nv.say('recommend_repeat_2')
    # Воспроизведение сообщения 'recommend_repeat_2'
    user_answer = has_reaction_by_answer()
    # Запрос ответа пользователя
    return map_resolver(nn, nv, user_answer=user_answer)
    # Определение дальнейшего шага (функции)


def recommend_score_negative(nn: NeuroNetLibrary, nv: NeuroVoiceLibrary):
    """ Логика обработки ответа пользователя: - "Нет". """
    nv.say('recommend_score_negative')
    # Воспроизведение сообщения 'recommend_score_negative'
    user_answer = has_reaction_by_answer()
    # Запрос ответа пользователя
    return map_resolver(nn, nv, user_answer=user_answer)
    # Определение дальнейшего шага (функции)


def recommend_score_neutral(nn: NeuroNetLibrary, nv: NeuroVoiceLibrary):
    """ Логика обработки ответа пользователя: - "Возможно". """
    nv.say('recommend_score_neutral')
    # Воспроизведение сообщения 'recommend_score_neutral'
    user_answer = has_reaction_by_answer()
    # Запрос ответа пользователя
    return map_resolver(nn, nv, user_answer=user_answer)
    # Определение дальнейшего шага (функции)


def recommend_score_positive(nn: NeuroNetLibrary, nv: NeuroVoiceLibrary):
    """ Логика обработки ответа пользователя: - "Да". """
    nv.say('recommend_score_positive')
    # Воспроизведение сообщения 'recommend_score_positive'
    user_answer = has_reaction_by_answer()
    # Запрос ответа пользователя
    return map_resolver(nn, nv, user_answer=user_answer)
    # Определение дальнейшего шага (функции)


def recommend_null(nn: NeuroNetLibrary, nv: NeuroVoiceLibrary):
    """ Логика обработки ответа пользователя, который ничего не сказал (NULL)."""
    if nn.counter("recommend_null") == 0:
        nv.say('recommend_null')
        # Воспроизведение сообщения 'recommend_null'
        user_answer = has_reaction_by_answer()
        # Запрос ответа пользователя
        nn.counter("recommend_null", "+")
        # Прибавление счетчика "recommend_null" +1
        return map_resolver(nn, nv, user_answer=user_answer)
        # Определение дальнейшего шага (функции)
    else:
        return end_logic("NULL")


def recommend_default(nn: NeuroNetLibrary, nv: NeuroVoiceLibrary):
    """ Логика обработки ответа пользователя, если ничего не подошло. """
    if nn.counter("recommend_default") == 0:
        nv.say('recommend_null')
        # Воспроизведение сообщения 'recommend_null'
        user_answer = has_reaction_by_answer()
        # Запрос ответа пользователя
        nn.counter("recommend_default", "+")
        # Прибавление счетчика "recommend_default" +1
        return map_resolver(nn, nv, user_answer=user_answer)
        # Определение дальнейшего шага (функции)
    else:
        return end_logic("DEFAULT")


def has_reaction_by_answer():
    """ Логика получения ответа от пользователя. """
    user_answer = 'answer_six'
    # Имитация ответа пользователя
    return user_answer
    # Описать, что должно быть в этом модуле...


def map_resolver(nn: NeuroNetLibrary, nv: NeuroVoiceLibrary, user_answer: str):
    """ Логика определения последующих шагов логики (действий). """
    result = state_map[user_answer]
    # Определение ссылки на функцию следующего шага логики
    return result(nn, nv) if result is not end_logic else result(user_answer)


def end_logic(user_answer: str) -> dict:
    """ Логика окончания logic_unit (main_logic)"""
    entity_map = {
        'answer_zero': {'recommendation_score': 0},
        'answer_one': {'recommendation_score': 1},
        'answer_two': {'recommendation_score': 2},
        'answer_three': {'recommendation_score': 3},
        'answer_four': {'recommendation_score': 4},
        'answer_five': {'recommendation_score': 5},
        'answer_six': {'recommendation_score': 6},
        'answer_seven': {'recommendation_score': 7},
        'answer_eight': {'recommendation_score': 8},
        'answer_nine': {'recommendation_score': 9},
        'answer_ten': {'recommendation_score': 10},
        'answer_wrong_time': {'wrong_time': True},
        'answer_question': {'question': True}
    }
    # Словарь с параметрами для запуска следующих логических модулей
    return {'user_answer': user_answer, 'entity/value': entity_map[user_answer]}


def run(nn: NeuroNetLibrary, nv: NeuroVoiceLibrary, default: bool = False, confirm: bool = False) -> dict:
    pass


state_map = {
    'NULL': recommend_null,
    'DEFAULT': recommend_default,
    'answer_zero': end_logic,
    'answer_one': end_logic,
    'answer_two': end_logic,
    'answer_three': end_logic,
    'answer_four': end_logic,
    'answer_five': end_logic,
    'answer_six': end_logic,
    'answer_seven': end_logic,
    'answer_eight': end_logic,
    'answer_nine': end_logic,
    'answer_ten': end_logic,
    'answer_not': recommend_score_negative,
    'answer_neutral': recommend_score_neutral,
    'answer_yes': recommend_score_positive,
    'answer_repeat': recommend_repeat,
    'answer_dont_know': recommend_repeat_2,
    'answer_wrong_time': end_logic,
    'answer_question': end_logic,
}
# Словарь с адресами функций, участвует в определении следующего шага логики.


if __name__ == "__main__":
    neuro_net = NeuroNetLibrary()
    neuro_voice = NeuroVoiceLibrary()
    res = run(neuro_net, neuro_voice)
    print(res)
