from libraries import NeuroVoiceLibrary


def forward(nv: NeuroVoiceLibrary) -> str:
    pass


def end_logic(tag) -> dict:
    pass


def run(nv: NeuroVoiceLibrary, question: bool = False) -> dict:
    """Запуск логики forward_logic"""
    if question:
        return end_logic(forward(nv))
    return {}


if __name__ == "__main__":
    neuro_voice = NeuroVoiceLibrary()
    res = run(nv=neuro_voice, question=True)
    print(res)

