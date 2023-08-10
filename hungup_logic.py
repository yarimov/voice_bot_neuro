from libraries import NeuroNetLibrary, NeuroVoiceLibrary


def hangup_positive(nv: NeuroVoiceLibrary) -> str:
    nv.say('hangup_positive')
    # Воспроизведение сообщения 'hangup_positive'
    tag = "высокая оценка"
    return tag


def hangup_negative(nv: NeuroVoiceLibrary) -> str:
    nv.say('hangup_negative')
    # Воспроизведение сообщения 'hangup_negative'
    tag = "низкая оценка"
    return tag


def hangup_wrong_time(nv: NeuroVoiceLibrary) -> str:
    nv.say('hangup_wrong_time')
    # Воспроизведение сообщения 'hangup_wrong_time'
    tag = "нет времени для разговора"
    return tag


def hangup_null(nv: NeuroVoiceLibrary) -> str:
    nv.say('hangup_null')
    # Воспроизведение сообщения 'hangup_null'
    tag = "проблемы с распознаванием"
    return tag


def hangup_action(tag: str) -> None:
    """ В данном модуле делается что-то, например записывается в nn.log (должна быть ссылка на объект nn в аргументах.
    Или запись в БД. В ТЗ описание модуля отсутствовало"""
    print(f"что-то делаем с тегом: {tag}")

def end_logic(nn) -> str:
    """ Логика окончания logic_unit (hungup_logic). """
    return 'complete'


def run(nn: NeuroNetLibrary, nv: NeuroVoiceLibrary, null: bool = None, confirm: bool = True, wrong_time: bool = None,
        recommendation_score: int = None) -> str | bool:
    """Запуск логики hangup_logic"""
    if not confirm:
        hangup_action(hangup_wrong_time(nv))
        return end_logic(nn)
    if wrong_time:
        hangup_action(hangup_wrong_time(nv))
        return end_logic(nn)
    if recommendation_score in (0, 1, 2, 3, 4, 5, 6, 7, 8):
        hangup_action(hangup_negative(nv))
        return end_logic(nn)
    if recommendation_score in (9, 10):
        hangup_action(hangup_positive(nv))
        return end_logic(nn)
    if null:
        hangup_action(hangup_null(nv))
        return end_logic(nn)

    return False


if __name__ == "__main__":
    neuro_net = NeuroNetLibrary()
    neuro_voice = NeuroVoiceLibrary()
    res = run(neuro_net, neuro_voice, confirm=False)
    print(res)