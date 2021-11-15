import numpy as np


def textrank_and_rake(
    wanted_words_in_text,
    unique_wanted_words_in_text,
    all_stopwords,
    lemma_list: list,
    pos_list: list,
):

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

    for iteer in range(0, maximum_iteration):
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
            print(str(iteration_info) + " iteration's done.\n")
            break

        iteration_info += 1

    for i in range(0, unique_wanted_words_in_text_size):
        print(
            "Word Value -> "
            + unique_wanted_words_in_text[i]
            + ": "
            + str(round(word_value[i], 3))
        )

    # RAKE

    sentences = []
    sentence_temp = []

    sentence = " "

    for word in lemma_list:

        if len(word.split()) > 1:
            sentence_temp.append(word)
            sentences.append(sentence_temp)
            sentence_temp = []
            continue

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

    unique_sentences_end = unique_sentences.copy()
    sentence_word_count = 0
    noun_count = 0
    propn_count = 0
    temp_var = 0

    def split_sentence_and_delete(out):
        nonlocal temp_var
        for i in range(len(unique_sentences[out])):
            unique_sentences_end.append(unique_sentences[out][i].split())

        unique_sentences_end.pop(out - temp_var)
        temp_var += 1

    for i in range(len(unique_sentences)):
        for j in range(len(unique_sentences[i])):
            sentence_word_count += 1
            index = lemma_list.index(unique_sentences[i][j])
            word_tag = pos_list[index]

            if word_tag == "NOUN":
                noun_count += 1

            elif word_tag == "PROPN":
                propn_count += 1

        if sentence_word_count > 1:
            if sentence_word_count > 5:
                split_sentence_and_delete(i)

            elif noun_count >= 3:
                split_sentence_and_delete(i)

            elif (noun_count >= 1 or propn_count >= 1) and pos_list[
                lemma_list.index(unique_sentences[i][-1])
            ] == "ADJ":
                split_sentence_and_delete(i)

        sentence_word_count = 0
        noun_count = 0
        propn_count = 0

    print()
    print("Rules Applied to List of Candidate Keyword Groups: \n")
    print(unique_sentences_end)

    unique_sentences = []
    for sentence in unique_sentences_end:
        if sentence not in unique_sentences:
            unique_sentences.append(sentence)

    print()
    print("Unique List of Candidate Keyword Groups: \n")
    print(unique_sentences)

    for word in unique_wanted_words_in_text:
        for sentence in unique_sentences:
            if (
                (word in sentence)
                and ([word] in unique_sentences)
                and (len(sentence) > 1)
            ):
                unique_sentences.remove([word])

    print()
    print("Unique List of Candidate Keyword Groups (Single Word): \n")
    print(unique_sentences)

    sentences_value = []
    keyword_sentences = []

    for sentence in unique_sentences:
        sentence_value = 0
        keyword_sentence = ""
        for word in sentence:
            keyword_sentence += str(word)
            keyword_sentence += " "
            sentence_value += word_value[unique_wanted_words_in_text.index(word)]
        sentences_value.append(sentence_value)
        keyword_sentences.append(keyword_sentence.strip())

    print()

    i = 0
    for sentence in keyword_sentences:
        print(
            "Keyword Group: '"
            + str(sentence)
            + "', Score : "
            + str(round(sentences_value[i], 3))
        )
        i += 1

    sorted_sentence = np.flip(np.argsort(sentences_value), 0)

    keyword_sentence_size = len(keyword_sentences)

    if 0 < keyword_sentence_size <= 40:
        keyword_sentences_limit = 7

    elif keyword_sentence_size <= 50:
        keyword_sentences_limit = 8

    elif keyword_sentence_size <= 70:
        keyword_sentences_limit = 9

    elif keyword_sentence_size <= 80:
        keyword_sentences_limit = 10

    elif keyword_sentence_size <= 90:
        keyword_sentences_limit = 11

    elif keyword_sentence_size <= 100:
        keyword_sentences_limit = 12

    else:
        keyword_sentences_limit = 15

    print()
    print("Sorted Candidate keywords:\n")

    sorted_key_phrases = []

    if keyword_sentences_limit <= keyword_sentence_size:
        for i, j in zip(range(keyword_sentences_limit), range(keyword_sentences_limit)):
            print(str(f"{j + 1} -> " + keyword_sentences[sorted_sentence[i]]))
            sorted_key_phrases.append(keyword_sentences[sorted_sentence[i]])

    else:
        for i, j in zip(range(keyword_sentence_size), range(keyword_sentence_size)):
            print(str(f"{j + 1} -> " + keyword_sentences[sorted_sentence[i]]))
            sorted_key_phrases.append(keyword_sentences[sorted_sentence[i]])

    return sorted_key_phrases


print()
