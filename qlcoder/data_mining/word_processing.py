text_str = '648159969691164817828591164816793258587879116481793791584919716481923878149589116481978918491988164974919966878765611648618781796169791961735891187916486148381791789586616971648196863912391169316871239681648511999847881896416485114597966197139596616485118293616481975616497416931687179619919919479781648511286839816486164874816497491164861539416481435871786816978879118791849581995815861988164851891648167836197891188198814879391128683981648158955818491878167836187934416916497716486168716487481648189759187816481978918491991'
text_strs = text_str.split('1')
print text_strs

with open('word_list.txt') as fs:
    english_words = fs.readlines()

english_words = map(lambda word: word[0: len(word) - 2], english_words)
english_words = set(english_words)

kb_mp = dict()
kb_mp['2'] = ['q','b','x']
kb_mp['3'] = ['z','u','v']
kb_mp['4'] = ['g','h','j']
kb_mp['5'] = ['m','p','l']
kb_mp['6'] = ['f','c','y','t']
kb_mp['7'] = ['k','n','r']
kb_mp['8'] = ['a','e','w']
kb_mp['9'] = ['i','d','o','s']


def print_possibles(my_str):
    if len(my_str) == 0:
        return
    print '-------------------------'
    tmp = list()
    for ele in dfs(my_str):
        if english_words.__contains__(ele):
            tmp.append(ele)
    if len(tmp) > 0:
        print reduce(lambda x, y: x + ',' + y, tmp)
    else:
        print ' or . or !'


def dfs(my_str):
    if len(my_str) == 1:
        return kb_mp[my_str[0]]
    cur_ch = my_str[0]
    ret_res = list()
    for ch in kb_mp[cur_ch]:
        tmp_res = map(lambda e: ch + e, dfs(my_str[1:len(my_str)]))
        ret_res.extend(tmp_res)
    return ret_res


for text in text_strs:
    print_possibles(text)
#
# print_possibles('648')
