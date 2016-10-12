def bwt(string , slice_len):
    string_len = len(string)
    string_slice = []
    for index in range(len(string)):
        s , e = index , (index+slice_len)%string_len
        if s < e :
            string_slice.append((string[s:e] , string[s-1]))
        else :
            string_slice.append((string[s:] + string[:e] , string[s-1]))
    return string_slice

with open("war_and_peace.txt") as f:
    data = f.read()
    with open ("out_war_and_peace.txt", 'w') as out_f:
        arr=bwt(data,100);
        for tmp_str in arr:
            print tmp_str
