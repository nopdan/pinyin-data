import re
from collections import OrderedDict


# 转换单个拼音 zhōng => zhong
def conv(pinyin):
    pinyin = re.sub(r"[āáǎà]", "a", pinyin)
    pinyin = re.sub(r"[ōóǒò]", "o", pinyin)
    pinyin = re.sub(r"[ēéěè]", "e", pinyin)
    pinyin = re.sub(r"[īíǐì]", "i", pinyin)
    pinyin = re.sub(r"[ūúǔù]", "u", pinyin)
    pinyin = re.sub(r"[ǖǘǚǜü]", "v", pinyin)
    pinyin = re.sub(r"m̄|ḿ|m̀", "m", pinyin)
    pinyin = re.sub(r"ń|ň|ǹ", "n", pinyin)
    pinyin = re.sub(r"ê̄|ế|ê̌|ề", "ê", pinyin)
    return pinyin


# 单字读音
pinyin = {}
# 多音字，value 为最常用的读音
duoyinzi = {}
# 带有多音字的词
words = []
words_set = set()


def convert(path, save_path, isWord=False):
    f = open(path, "r", encoding="utf-8")
    lines = f.readlines()
    f.close()

    fout = open(save_path, "wt", encoding="utf-8")
    for line in lines:
        if isWord:
            convWord(line, fout)
        else:
            convChar(line, fout)
    fout.close()


# 转换单字拼音数据
def convChar(line, fout):
    res = re.match(r"U\+(\S+): *(\S+)", line)
    if res is None:
        return
    # 转换 unicode 码
    char = res.group(1)
    char = chr(int(char, 16))
    fout.write(char)
    fout.write("\t")

    # 转换拼音
    pys = res.group(2).split(",")
    pys = [conv(py) for py in pys]
    pys = list(OrderedDict.fromkeys(pys))  # 去重
    fout.write(" ".join(pys))
    fout.write("\n")

    pinyin[char] = pys
    # 多音字
    if len(pys) != 1:
        duoyinzi[char] = pys[0]


# 转换词组拼音数据
def convWord(line, fout):
    if line.startswith("#"):
        return
    li = line.split(": ")
    if len(li) != 2:
        return
    word = li[0]
    pys = [conv(py) for py in li[1].split()]
    pys = list(OrderedDict.fromkeys(pys))  # 去重
    if len(word) != len(pys):
        return
    for i, char in enumerate(word):
        if pys[i] not in pinyin.get(char, []):
            return

    fout.write(word)
    fout.write("\t")
    fout.write(" ".join(pys))
    fout.write("\n")

    # 含有多音字且不是最常用的读音
    flag = False
    for char in word:
        if char in duoyinzi:
            flag = True
            break
    if flag:
        entry = word + "\t" + " ".join(pys)
        if entry not in words_set:
            words_set.add(entry)
            words.append(entry)


if __name__ == "__main__":
    convert("./pinyin-data/pinyin.txt", "pinyin.txt")

    convert("./phrase-pinyin-data/pinyin.txt", "phrase.txt", isWord=True)
    convert("./phrase-pinyin-data/large_pinyin.txt", "large.txt", isWord=True)

    fout = open("duoyin.txt", "wt", encoding="utf-8")
    # words = list(OrderedDict.fromkeys(words))
    for entry in words:
        fout.write(entry)
        fout.write("\n")
    fout.close()
