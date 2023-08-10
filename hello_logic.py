from libraries import NeuroNetLibrary, NeuroVoiceLibrary


def hello(nn: NeuroNetLibrary, nv: NeuroVoiceLibrary):
    """ Логика начального приветствия. """
    nv.say('hello')
    # Воспроизведение сообщения 'hello'
    user_answer = has_reaction_by_answer()
    # Запрос ответа пользователя
    return map_resolver(nn, nv, user_answer=user_answer)
    # Определение дальнейшего шага (функции)


def hello_null(nn: NeuroNetLibrary, nv: NeuroVoiceLibrary):
    """ Логика обработки ответа пользователя, который ничего не сказал (NULL)."""
    if nn.counter("hello_null") == 0:
        nv.say('hello_null')
        # Воспроизведение сообщения 'hello_null'
        user_answer = has_reaction_by_answer()
        # Запрос ответа пользователя
        nn.counter("hello_null", "+")
        # Прибавление счетчика "hello_null" +1
        return map_resolver(nn, nv, user_answer=user_answer)
        # Определение дальнейшего шага (функции)
    else:
        return end_logic("NULL")


def hello_repeat():
    pass


def has_reaction_by_answer():
    """ Логика получения ответа от пользователя. """
    user_answer = 'answer_yes'
    # Имитация ответа пользователя
    return user_answer
    # Описать, что должно быть в этом модуле...


def map_resolver(nn: NeuroNetLibrary, nv: NeuroVoiceLibrary, user_answer: str):
    """ Логика определения последующих шагов логики (действий). """
    result = state_map[user_answer]
    # Определение ссылки на функцию следующего шага логики
    return result(nn, nv) if result is not end_logic else result(user_answer)


def end_logic(user_answer: str):
    pass


def run(nn: NeuroNetLibrary, nv: NeuroVoiceLibrary) -> dict:
    """Запуск логики hello_logic"""
    return hello(nn, nv)


state_map = {
    'NULL': hello_null,
    'DEFAULT': end_logic,
    'answer_yes': end_logic,
    'answer_not': end_logic,
    'answer_wrong_time': end_logic,
    'answer_repeat': hello_repeat
}


if __name__ == "__main__":
    neuro_net = NeuroNetLibrary()
    neuro_voice = NeuroVoiceLibrary()
    res = run(neuro_net, neuro_voice)
    print(res)
