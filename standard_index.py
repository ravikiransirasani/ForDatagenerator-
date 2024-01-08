x = "aaabbbbcc"

def standard_index(s):
    index_list = []
    last_char = s[0]
    start_index = 0
    for idx, ch in enumerate(s[1:],1):
        if ch == last_char:
            continue
        else:
            index_list.append([start_index,idx-1])
            last_char = ch
            start_index = idx
    index_list.append([start_index,idx])
    return index_list
print(standard_index(x))

    
    
