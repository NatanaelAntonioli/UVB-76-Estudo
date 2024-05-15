def extract_words():

    import re
    import codecs
    import os
    

    directory = 'other_radios'

    for filename in os.listdir(directory):

        file = os.path.join(directory, filename)

        f = codecs.open(file, 'r', encoding="utf8")
        full_text = (f.read())

        for word in full_text.split():
            if (re.search('[а-яА-Я]', word)) and 'Col' in word:
                with open('other-radios-wordlist.txt', 'a', encoding="utf-16") as output:
                    print(word)
                    output.write(word.replace('class="messageCol">', '') + '\n')
                    output.close()


def check_dict():

    import time
    import enchant

    d = enchant.Dict("en_US")
    translated_list = open('translated_list2.txt', 'r', encoding='utf-8')

    translated_lines = translated_list.readlines()

    for line1 in translated_lines:

        line1 = line1.strip().lower()

        if len(line1.split()) > 1:
            with open('english_words.txt', 'a', encoding="utf-16") as output:
                output.write(line1 + '\n')
                output.close()

        if d.check(line1):
            print(line1)
            with open('english_words.txt', 'a', encoding="utf-16") as output:
                output.write(line1 + '\n')
                output.close()


    
def divide_words():

    unique_words_file = open('unique words.txt', 'r', encoding='utf-8')
    unique_words = unique_words_file.readlines()

    count = 1
    main_count = 1

    for word in unique_words:
        with open('out/' + str(main_count) + ".txt", 'a', encoding="utf-16") as output:
            output.write(word)
        count = count + 1
        if count % 50 == 0:
            count = 1
            main_count += 1

def character_frequency():

    list = '8-digit-list.txt'
    enconding = 'utf-16' # Use this for russian main wordlist
    enconding = 'utf-8'
    
    fh = open(list,'r', encoding='utf-16').read()
    from collections import Counter
    res = Counter(fh)

    print(res)
    
    del res['\n']
    del res['s']
    del res['p']
    del res['a']
    del res['n']
    del res['<']
    del res['>']
    del res['?']
    del res['E']
    del res['T']
    del res['O']
    del res['I']
    del res['K']
    del res['N']
    del res['P']
    del res['І']
    del res['V']
    del res['h']
    del res['U']
    del res['B']
    del res['M']
    del res['D']
    del res['H']
    del res['Z']
    del res['Y']
    del res['e']
    del res['b']
    del res['G']
    del res['J']
    del res['C']
    del res['S']
    del res['E']
    del res['…']
    del res['&']
    del res[';']

    total = sum(res.values(), 0.0)
    res = {k: v / total for k, v in res.items()}


    import pandas as pd
    import matplotlib.pyplot as plt

    ts = pd.Series(res).sort_values(ascending=False).plot.bar()
    ts.plot()
    plt.show()


def extract_5_digit():
    import re
    import codecs
    import os
    

    directory = 'text_files'

    for filename in os.listdir(directory):

        file = os.path.join(directory, filename)

        f = codecs.open(file, 'r', encoding="utf8")
        full_text = (f.read())

        for word in full_text.split():
            if word.startswith('<p>') and word.endswith('</p>'):
                word = word.replace('<p>', '')
                word = word.replace('</p>', '')

                if 'Repeated' not in word and '-' not in word:
                    with open('5-digit-list.txt', 'a', encoding="utf-16") as output:
                        output.write(word + '\n')
                        output.close()


def extract_8_digit():
    import re
    import codecs
    import os
    

    directory = 'text_files'

    for filename in os.listdir(directory):

        file = os.path.join(directory, filename)

        f = codecs.open(file, 'r', encoding="utf8")
        for line in f:
            if line.startswith('<p class="messageCol">'):
                
                try:
                    number = re.findall("\d+", line)[0]
                    

                    if len(number) == 8:
                        print(number)
                        with open('8-digit-list.txt', 'a', encoding="utf-16") as output:
                            output.write(number + '\n')
                            output.close()
                except:
                    pass

def cross_number_frequency():

    import numpy as np

    list = '8-digit-list.txt'
    size = 5

    file = open(list, 'r', encoding='utf-16')
    lines = file.readlines()

    cross = np.zeros((10, 10))
    begin = np.zeros(10)
    end = np.zeros(10)

    for line in lines:
        for index in range(len(line)):
            if index == 0:
                try:
                    begin[int(line[index])] += 1
                except:
                    pass
            if index == size - 1:
                try:
                    end[int(line[index])] += 1
                except:
                    pass
            else:
                try:
                    cross[int(line[index])][int(line[index-1])] += 1
                    cross[int(line[index])][int(line[index+1])] += 1
                except:
                    pass
    
    print(begin)
    print(end)
    print(cross)


    import matplotlib.pyplot as plt
    import pandas as pd

    ts = pd.Series(end).sort_values(ascending=False).plot.bar()
    ts.plot()
    plt.show()


def look_for_matches():
    list1 = open('other-radios-wordlist.txt', 'r', encoding="utf-16")
    list2 = open('wordlist.txt', 'r', encoding="utf-16")

    for word in list1:
        for word2 in list2:
            if word == word2:
                print(word)

look_for_matches()

