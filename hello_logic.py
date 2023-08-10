from libraries import NeuroNetLibrary, NeuroVoiceLibrary


def hello(nn: NeuroNetLibrary, nv: NeuroVoiceLibrary):
    pass


def hello_null():
    pass


def hello_repeat():
    pass


def has_reaction_by_answer():
    pass


def map_resolver(nn: NeuroNetLibrary, nv: NeuroVoiceLibrary, user_answer: str):
    """ Логика определения последующих шагов логики (действий). """
    result = state_map[user_answer]
    # Определение ссылки на функцию следующего шага логики
    return result(nn, nv) if result is not end_logic else result(user_answer)


def end_logic():
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
