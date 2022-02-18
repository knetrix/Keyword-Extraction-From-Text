import string

from trankit import Pipeline


def text_processing_eng(text: str):
    p = Pipeline("english")

    token_list = []

    token_list_temp = (
        text.replace("'", "")
        .replace("?", " ?")
        .replace("!", " !")
        .replace("’", "")
        .replace("´", "")
        .replace("(", "")
        .replace(")", "")
        .replace("{", "")
        .replace("}", "")
        .replace("[", "")
        .replace("]", "")
        .split()
    )

    print(token_list_temp)
    for token in token_list_temp:
        if token[-1] == "." and token != ".":
            token = token[:-1]
            token_list.append(token)
            token_list.append(" . ")

        else:
            token_list.append(token)

    print("\nSplit text into tokens: \n", token_list, end="\n\n")

    # POS Text

    pos_dict = p.posdep(token_list, is_sent=True)

    pos_list = [
        token.get("upos", "An error occurred in the POS.")
        for token in pos_dict["tokens"]
    ]

    pos_token_list = list(zip(token_list, pos_list))

    print("Finding POS of Tokens: \n", pos_token_list, end="\n\n")

    # Lemmatization Text

    lemma_dict = p.lemmatize(token_list, is_sent=True)

    lemma_list = [
        token.get("lemma", "An error occurred in the Lemmatization.")
        for token in lemma_dict["tokens"]
    ]

    lemma_token_pos_list = list(zip(token_list, lemma_list, pos_list))

    print(
        "Lemmatization of tokens and POS information: \n",
        lemma_token_pos_list,
        end="\n\n",
    )

    # Stopword Process

    want_pos = ["NOUN", "ADJ", "PROPN"]
    word_count = []
    stopword_text = [
        lemma_word
        for lemma_word, word_pos in zip(lemma_list, pos_list)
        if word_pos not in want_pos
        if word_count.count(lemma_word) <= 1
    ]

    stopword_punctuations = list(string.punctuation)

    file = open("stopword_list_eng.txt", "r")

    stopwords_file = [line.strip() for line in file.readlines()]

    all_stopwords = set(stopword_text + stopword_punctuations + stopwords_file)

    wanted_words_in_text = [word for word in lemma_list if word not in all_stopwords]

    unique_wanted_words_in_text = []
    for word in wanted_words_in_text:
        if word not in unique_wanted_words_in_text:
            unique_wanted_words_in_text.append(word)

    print(
        "Word Type Filter Applied to Words in the Text and Removed Stopwords from the Text: \n",
        wanted_words_in_text,
        end="\n\n",
    )
    print(
        "Removed Duplicate Words from 'wanted_words_in_text' List: \n",
        unique_wanted_words_in_text,
        end="\n\n",
    )

    return (
        wanted_words_in_text,
        unique_wanted_words_in_text,
        all_stopwords,
        lemma_list,
        pos_list,
    )
