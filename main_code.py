import os
from pocketsphinx import LiveSpeech, get_model_path
import sys
from Class import Qie_Bot, match
from programm_design import create_window
from connection import is_working, cfile

model_path = get_model_path()

speech = LiveSpeech(
    verbose=False,
    sampling_rate=16000,
    buffer_size=2048,
    no_search=False,
    full_utt=False,
    hmm=os.path.join(model_path, 'zero_ru.cd_cont_4000'),
    lm=os.path.join(model_path, 'ru.lm'),
    dic=os.path.join(model_path, 'Qie_dictionary_curr')
)
print('--->Ready to get cmds')
for phrase in speech:
    print(phrase)