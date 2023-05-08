# pinyin-data

将汉字拼音数据 [mozillazg/pinyin-data](https://github.com/mozillazg/pinyin-data)  
和词语拼音数据 [mozillazg/phrase-pinyin-data](https://github.com/mozillazg/phrase-pinyin-data)  
转换为更适合拼音输入法的格式

|             | 来源                                | 备注                     |
| ----------- | ----------------------------------- | ------------------------ |
| pinyin.txt  | pinyin-data/pinyin.txt              | 汉字拼音数据             |
| phrase.txt  | phrase-pinyin-data/pinyin.txt       | 词语拼音数据             |
| large.txt   | phrase-pinyin-data/large_pinyin.txt | 词语拼音数据             |
| correct.txt | 部分来自深蓝词库转换                | 补充或对以上数据进行修正 |
| duoyin.txt  |                                     | 筛选出含多音字的词       |

## 特殊音节字

原始：
```
㕶	ň ňg
呒	wu ḿ
呣	ḿ m̀ mou
咹	e an ń
哏	gen hen ǹ
哽	geng ying ńg ń
唔	wu ńg ḿ ń
嗯	ń ńg ňg ǹg ň ǹ
嘸	fu wu m̄ ḿ
欸	ai ê̄ ế ê̌ ề xie ei
誒	ei xi yi ê̄ ế ê̌ ề
𠮾	ǹ ǹg
哼	heng hng
噷	hm xin hen
```

转换规则：
```
m̄ ḿ m̀ -> m
ń ň ǹ -> n
ńg ňg ǹg -> ng
ê̄ ế ê̌ ề -> ê
hm -> hm
hng -> hng
```

结果：
```
㕶	n ng
呒	wu m
呣	m mou
咹	e an n
哏	gen hen n
哽	geng ying ng n
唔	wu ng m n
嗯	n ng
嘸	fu wu m
欸	ai ê xie ei
誒	ei xi yi ê
𠮾	n ng
哼	heng hng
噷	hm xin hen
```