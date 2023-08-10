from libraries import NeuroNetLibrary, NeuroVoiceLibrary


def recommend_main(nn: NeuroNetLibrary, nv: NeuroVoiceLibrary):
    pass


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


state_map = {}
# Словарь с адресами функций, участвует в определении следующего шага логики.


if __name__ == "__main__":
    neuro_net = NeuroNetLibrary()
    neuro_voice = NeuroVoiceLibrary()
    res = run(neuro_net, neuro_voice)
    print(res)
