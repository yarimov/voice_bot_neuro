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
    pass


def recommend_repeat_2(nn: NeuroNetLibrary, nv: NeuroVoiceLibrary):
    pass

def recommend_score_negative(nn: NeuroNetLibrary, nv: NeuroVoiceLibrary):
    pass

def recommend_score_neutral(nn: NeuroNetLibrary, nv: NeuroVoiceLibrary):
    pass

def recommend_score_positive(nn: NeuroNetLibrary, nv: NeuroVoiceLibrary):
    pass

def recommend_null(nn: NeuroNetLibrary, nv: NeuroVoiceLibrary):
    pass

def recommend_default(nn: NeuroNetLibrary, nv: NeuroVoiceLibrary):
    pass

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
    pass


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
