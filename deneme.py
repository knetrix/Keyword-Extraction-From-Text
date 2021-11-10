from file_selection_process import TEXT, STATE
from text_processing_eng import text_processing_eng
from text_processing_tur import text_processing_tur
from textrank_and_rake_algorithm import textrank_and_rake


# DOC_TEXT = """Hello! This is Cars. You are insane. Cars is beautiful"""
(
    wanted_words_in_text,
    unique_wanted_words_in_text,
    all_stopwords,
    lemma_list,
    pos_list,
) = text_processing_eng(TEXT)

"""
print(
    wanted_words_in_text,
    unique_wanted_words_in_text,
    lemma_list,
    pos_list,
)
"""
# todo sss
#  param sss

textrank_and_rake(wanted_words_in_text, unique_wanted_words_in_text, all_stopwords, lemma_list)
