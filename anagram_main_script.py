
def anagram_check(li):
    dict = {}
    index = 0
    for i in range(0, len(li)):
        originalfirst = li[index]
        sortedfirst = ''.join(sorted(str(li[index]).replace(" ", "").upper()))
        for j in range(index + 1, len(li)):
            next = ''.join(sorted(str(li[j]).replace(" ", "").upper()))
            if sortedfirst == next:
                dict.update({originalfirst: li[j]})
        index += 1
    print ("The following are the Anagrams : ")
    print (dict)


def read_file():
    whole_list = []
    try:
        file_path = 'English.txt'  # mention file full path here
        with open(file_path, 'r') as f_read:
            whole_data = f_read.read()
            whole_data = whole_data.strip()
            whole_list = whole_data.split('\n')
    except Exception as e:
        print (e)
    return whole_list


data_list = read_file()
print (len(data_list))

Anagrams_result = anagram_check(data_list[0:10000])  # default length of lines considering 10000  only
print (Anagrams_result)
