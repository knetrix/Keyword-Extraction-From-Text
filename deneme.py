from text_processing_eng import text_processing_eng


DOC_TEXT = """Hello! This is Cars. You are insane. Cars is beautiful"""
(
    wanted_words_in_text,
    unique_wanted_words_in_text,
    all_stopwords,
    lemma_list,
    pos_list,
) = text_processing_eng(DOC_TEXT)

print(
    wanted_words_in_text,
    unique_wanted_words_in_text,
    all_stopwords,
    lemma_list,
    pos_list,
    sep="\n",
)
