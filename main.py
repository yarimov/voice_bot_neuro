from libraries import NeuroNetLibrary, NeuroVoiceLibrary

import hello_logic
import main_logic
import hungup_logic
import forward_logic


nn = NeuroNetLibrary()
nv = NeuroVoiceLibrary()

def main_2():
    result_hello_logic = hello_logic.run(nn=nn, nv=nv)
    param_main_logic = result_hello_logic.get('entity/value', {})
    hello_logic_user_answer = result_hello_logic.get('user_answer', '')

    if hello_logic_user_answer == 'answer_yes' or hello_logic_user_answer == 'DEFAULT':
        result_main_logic = main_logic.run(nn=nn, nv=nv, **param_main_logic)
        param_hungup_logic = result_main_logic.get('entity/value', {})
        if result_main_logic.get('user_answer', '') in ('answer_zero', 'answer_one', 'answer_two', 'answer_three',
                                                        'answer_four', 'answer_five', 'answer_six', 'answer_seven',
                                                        'answer_eight', 'answer_nine', 'answer_ten',
                                                        'answer_wrong_time'):
            result_hungup_logic = hungup_logic.run(nn=nn, nv=nv, **param_hungup_logic)
            return result_hungup_logic
        if result_main_logic.get('user_answer', '') == 'answer_question':
            forward_logic.run(nv=nv, question=True)

    if hello_logic_user_answer == 'answer_not' or hello_logic_user_answer == 'wrong_time':
        param_hungup_logic = result_hello_logic.get('entity/value', {})
        result_hungup_logic = hungup_logic.run(nn=nn, nv=nv, **param_hungup_logic)
        return result_hungup_logic

if __name__ == "__main__":
    print(main_2())
