from collections import defaultdict

INPUT_FILE = 'text.txt'
OUTPUT_FILE = 'words_and_its_frequency.txt'


def main():
    dic_with_results = dic_with_words_and_frequency(INPUT_FILE)
    create_file_with_results(OUTPUT_FILE, dic_with_results)


def dic_with_words_and_frequency(name_file):
    with open(name_file) as file:
        text_from_file = file.read()
        dic_words_and_frequency = defaultdict(int)
        word = ''

        for letter in text_from_file.lower():
            if letter not in ' .,;\n':
                word += letter
            else:
                if word != '':
                    dic_words_and_frequency[word] += 1
                    word = ''
    return dic_words_and_frequency


def create_file_with_results(file_name, dic):
    with open(file_name, 'a') as file:
        for key, value in dic.items():
            file.write(f'Слово "{key}" зустрічається {value} раз(а)\n')


main()
