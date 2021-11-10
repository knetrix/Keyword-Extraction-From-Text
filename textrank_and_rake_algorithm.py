import numpy as np
import math

# wanted_words_in_text - islenmis_metin
# unique_wanted_words_in_text - essiz_islenmis_metin
# all_stopwords - stopwords_nihai
# lemma_list - metin_lemma
# pos_list - metin_token_pos


def textrank_and_rake(
    wanted_words_in_text,
    unique_wanted_words_in_text,
    all_stopwords,
    lemma_list,
    pos_list=0,
):
    # stopwords_nihai Listesi: RAKE algoritmasında etkisiz kelimelere göre cümle olusturma isleminde kullanıldı. Cümle oluştururken metin_lemma listesinden yararlanıldı. metin_lemma listesi metindeki tüm kelimelerin lemmatization yapılmış halinin listesini tutar.
    # metin_token_pos Listesi: Tokenlar'a ayrılmış metnin eşli bir şekilde POS Tagging yapılmış hallerinin tutulduğu listedir.

    unique_wanted_words_in_text_size = len(unique_wanted_words_in_text)

    connection_matrix = np.zeros(
        (unique_wanted_words_in_text_size, unique_wanted_words_in_text_size),
        dtype=np.float32,
    )

    word_value = np.zeros(unique_wanted_words_in_text_size, dtype=np.float32)

    window_size = 2
    is_index_available = []

    for i in range(0, unique_wanted_words_in_text_size):
        word_value[i] = 1
        for j in range(0, unique_wanted_words_in_text_size):
            if j == i:
                connection_matrix[i][j] = 0
            else:
                for window_start in range(
                    0, (len(wanted_words_in_text) - window_size + 1)
                ):
                    window_end = window_start + window_size
                    window = wanted_words_in_text[window_start:window_end]

                    if (unique_wanted_words_in_text[i] in window) and (
                        unique_wanted_words_in_text[j] in window
                    ):

                        index_i = window_start + window.index(
                            unique_wanted_words_in_text[i]
                        )
                        index_j = window_start + window.index(
                            unique_wanted_words_in_text[j]
                        )

                        if [index_i, index_j] not in is_index_available:

                            connection_matrix[i][j] = connection_matrix[i][j] + 1 / abs(
                                index_i - index_j
                            )

                            is_index_available.append([index_i, index_j])

    print("is_matrix_available: \n" + str(is_index_available))
    print()
    print("Connection Matrix: \n" + str(connection_matrix))

    print()

    connection_count_matrix = np.zeros(
        unique_wanted_words_in_text_size, dtype=np.float32
    )

    for i in range(0, unique_wanted_words_in_text_size):
        for j in range(0, unique_wanted_words_in_text_size):
            connection_count_matrix[i] += connection_matrix[i][j]

    print()

    print("Connection Count Matrix: \n" + str(connection_count_matrix))

    maximum_iteration = 100
    d = 0.85
    threshold_value = 0.0001

    iteration_info = 1

    for iter in range(0, maximum_iteration):
        prev_word_value = np.copy(word_value)

        for i in range(0, unique_wanted_words_in_text_size):

            total = 0
            for j in range(0, unique_wanted_words_in_text_size):
                if connection_matrix[i][j] != 0:
                    total += (
                        connection_matrix[i][j] / connection_count_matrix[j]
                    ) * word_value[j]

            word_value[i] = (1 - d) + d * total

        if np.sum(np.fabs(prev_word_value - word_value)) <= threshold_value:
            print()
            print(str(iteration_info) + "iteration's done.")
            break

        iteration_info += 1

    print()
    for i in range(0, unique_wanted_words_in_text_size):
        print(
            "Word Value -> "
            + unique_wanted_words_in_text[i]
            + ": "
            + str(word_value[i])
        )

    # RAKE

    sentences = []

    sentence = " "

    for word in lemma_list:

        if word in all_stopwords:
            if sentence != " ":
                sentences.append(str(sentence).strip().split())
            sentence = " "

        else:
            sentence += str(word)
            sentence += " "
            if word == lemma_list[-1]:
                sentences.append(str(sentence).strip().split())

    print()
    print("List of Candidate Keyword Groups: \n")
    print(sentences)


    unique_sentences = []
    for sentence in sentences:
        if sentence not in unique_sentences:
            unique_sentences.append(sentence)
    
    print()
    print("Unique List of Candidate Keyword Groups: \n")
    print(unique_sentences)