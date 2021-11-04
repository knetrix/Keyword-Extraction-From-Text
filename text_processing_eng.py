""""""
import string
from trankit import Pipeline


def text_processing_eng(text: str):
    p = Pipeline("english")

    def clear_tokenizer_text(text):
        text = text.lower()

        printable = string.printable

        text = "".join(list(filter(lambda x: x in printable, text)))

        print("\nClear Text: " + text, end="\n\n")

        token_dict = p.tokenize(text, is_sent=True)

        # print(token_dict)
        # print(token_dict.keys())

        token_list = [
            token.get("text", "An error occurred in the tokenizer.")
            for token in token_dict["tokens"]
        ]

        print("Split text into tokens:", token_list, end="\n\n")

        return token_list

    token_list = clear_tokenizer_text(text)

    def pos_text():
        pos_dict = p.posdep(token_list, is_sent=True)

        pos_list = [
            token.get("upos", "An error occurred in the POS.")
            for token in pos_dict["tokens"]
        ]

        pos_token_list = list(zip(token_list, pos_list))

        print("Finding POS of Tokens: ", pos_token_list, end="\n\n")

        return pos_list

    pos_list = pos_text()

    def lemma_text():

        lemma_dict = p.lemmatize(token_list, is_sent=True)

        lemma_list = [
            token.get("lemma", "An error occurred in the Lemmatization.")
            for token in lemma_dict["tokens"]
        ]

        lemma_token_pos_list = list(zip(token_list, lemma_list, pos_list))

        print(
            "Lemmatization of tokens and POS information : ",
            lemma_token_pos_list,
            end="\n\n",
        )

        return lemma_list

    lemma_list = lemma_text()

    def stopword():

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

        wanted_words_in_text = [
            word for word in lemma_list if word not in all_stopwords
        ]

        unique_wanted_words_in_text = []
        for word in wanted_words_in_text:
            if word not in unique_wanted_words_in_text:
                unique_wanted_words_in_text.append(word)

        print(
            "Word Type Filter Applied to Words in the Text and Removed Stopwords from the Text",
            wanted_words_in_text,
            end="\n\n",
        )
        print(
            "Removed Duplicate Words from 'wanted_words_in_text' List",
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

    return stopword()
