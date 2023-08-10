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
    pass

def end_logic(nn) -> str:
    pass


def run(nn: NeuroNetLibrary, nv: NeuroVoiceLibrary, null: bool = None, confirm: bool = True, wrong_time: bool = None,
        recommendation_score: int = None) -> str | bool:
    pass

if __name__ == "__main__":
    neuro_net = NeuroNetLibrary()
    neuro_voice = NeuroVoiceLibrary()
    res = run(neuro_net, neuro_voice)
    print(res)