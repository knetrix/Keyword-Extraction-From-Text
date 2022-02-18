import numpy as np


def textrank(
    wanted_words_in_text,
    unique_wanted_words_in_text,
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

    sorted_word = np.flip(np.argsort(word_value), 0)

    if 0 < unique_wanted_words_in_text_size <= 30:
        keyword_limit = 2

    elif unique_wanted_words_in_text_size <= 60:
        keyword_limit = 3

    elif unique_wanted_words_in_text_size <= 90:
        keyword_limit = 4

    else:
        keyword_limit = 5

    print()
    print("Sorted Candidate keywords:\n")

    sorted_key_words = []

    if keyword_limit <= unique_wanted_words_in_text_size:
        for i, j in zip(range(keyword_limit), range(keyword_limit)):
            print(str(f"{j + 1} -> " + unique_wanted_words_in_text[sorted_word[i]]))
            sorted_key_words.append(unique_wanted_words_in_text[sorted_word[i]])

    return sorted_key_words


print()
