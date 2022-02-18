from file_selection_process import TEXT, STATE


if STATE == "Ing" or STATE == "":

    from text_processing_eng import text_processing_eng

    (
        wanted_words_in_text,
        unique_wanted_words_in_text,
        all_stopwords,
        lemma_list,
        pos_list,
    ) = text_processing_eng(TEXT)
    from textrank_and_rake_algorithm import textrank_and_rake

    sorted_key_phrases = textrank_and_rake(
        wanted_words_in_text,
        unique_wanted_words_in_text,
        all_stopwords,
        lemma_list,
        pos_list,
    )

    from show_results import Show_results

    Show_results(TEXT, lemma_list, pos_list, sorted_key_phrases)


elif STATE == "Tur":
    from text_processing_tur import text_processing_tur

    (
        wanted_words_in_text,
        unique_wanted_words_in_text,
        _,
        lemma_list,
        pos_list,
    ) = text_processing_tur(TEXT)

    from textrank_algorithm import textrank

    sorted_key_words = textrank(wanted_words_in_text, unique_wanted_words_in_text)

    from show_results import Show_results

    Show_results(TEXT, lemma_list, pos_list, sorted_key_words)
