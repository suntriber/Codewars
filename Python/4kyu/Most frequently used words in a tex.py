"""
Write a function that, given a string of text (possibly with punctuation and line-breaks), 
returns an array of the top-3 most occurring words, in descending order of the number of occurrences.
"""

def main():
    #print(top_3_words("a a a  b  c c  d d d d  e e e e e"), ["e", "d", "a"])
    
    print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"), ["e", "ddd", "aa"])
    print(top_3_words("  //wont won't won't "), ["won't", "wont"])
    print(top_3_words("  , e   .. "), ["e"])
    print(top_3_words("  ...  "), [])
    print(top_3_words("  '  "), [])
    print(top_3_words("  '''  "), [])
    
    print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
    #mind, there lived not long since one of those gentlemen that keep a lance
    #in the lance-rack, an old buckler, a lean hack, and a greyhound for
    #coursing. An olla of rather more beef than mutton, a salad on most
    #nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
    #on Sundays, made away with three-quarters of his income."""), ["a", "of", "on"])
    
    """
def top_3_words(text):
    from collections import Counter
    s = ''
    for i in text:
        s += i.lower()
        
        
    num_of_occurences = Counter(s.split(' '))

    n = {}
    
    for k, v in num_of_occurences.items():
        if k != '' and k.isalpha() or k == "'":
            n[v] = k
    print(n)
    l = []
    for i in sorted(list(n.keys()))[::-1]:
        l.append(n[i].lower())
    
    return l[:3:]
    """


"""
def top_3_words(text):
    from collections import Counter
    s = ''
    for i in text:
        s += i.lower()
    ss = s.split(' ')
    sss = []
    for i in ss:
        s = ''
        for j in i:
            if j.isalpha() or j=="'":
                s += j
        sss.append(s)
    
    num_of_occurences = Counter(sss)

    n = {}
    

    for k, v in num_of_occurences.items():
        if k != '':
            n[v] = k
    
    l = []
    for i in sorted(list(n.keys()))[::-1]:
        l.append(n[i].lower())
    
    if "'" in l:
        l.remove("'")
    if "'''" in l:
        l.remove("'''")
        print(l)

    return l[:3:]
"""

"""
def top_3_words(text):
    from collections import Counter
    import re
    # count the input, pass through a regex and lowercase it
    c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
    # return the `most common` 3 items
    
    return [w for w,_ in c.most_common(3)]
"""
"""
def top_3_words(text):
    from collections import Counter
    import re

    pattern = r"[a-z']+", re.sub(r" '+ ", " ", text.lower())
    sub = r" '+ ", " "

    c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower()))).most_common(3)
    return [x for x,_ in c]
"""

def top_3_words(text):
    from collections import Counter
    import re

    c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ "," ", text.lower())))

    return [x for x,_ in c.most_common(3)]
    

if __name__ == "__main__":
    main()


"""

import re
from collections import Counter

top_3_words=lambda t:[w for w,c in Counter(re.findall("'*[a-z][a-z']*",t.lower())).most_common(3)]



import re
from collections import Counter

def top_3_words(text):
    words = re.findall(r"[a-z']*[a-z]+[a-z']*", text.lower())
    top_3 = Counter(words).most_common(3)
    return [tup[0] for tup in top_3]



import re
from collections import Counter

def top_3_words(text):
    c = Counter(re.findall(r"'*[a-z][a-z|']*",  text.lower()))
    return [w for w,_ in c.most_common(3)]




from collections import Counter
import re

def top_3_words(text):
    words = re.findall(r"[a-z][a-z']*|[a-z']*[a-z]", text, re.IGNORECASE)
    topchart = Counter([word.lower() for word in words]).most_common(3)
    return [top[0] for top in topchart]




import re
from collections import Counter


def top_3_words(text):
    words_list = re.findall(r"[']*[a-z][a-z']*", text.lower())
    return [item[0] for item in Counter(words_list).most_common(3)]





import re

def top_3_words(text):
    re_non_valid = re.compile('[^a-z\' ]')
    re_chars = re.compile('[a-z]')
    text = text.lower()
    text = ' '.join([x for x in re_non_valid.sub(' ',text).split() if re_chars.search(x)])
    words = {}
    top = {}                    # Dictionary with no more than 3 words
    for word in text.split():
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
        top[word] = words[word] # Add the new word to the top
        if len(top) > 3:        # If the top is too big remove the worst word
            top.pop(min(top, key=top.get))
    return sorted(top, key=top.get, reverse=True)





from collections import Counter
from string import ascii_letters, printable

keep = ascii_letters + "'"
remove = printable.translate(str.maketrans('', '', keep))
table = str.maketrans(keep + remove, keep.lower() + ' ' * len(remove))

def top_3_words(text):
    words = (word for word in text.translate(table).split() if set(word) != {"'"})
    return [word for word, freq in Counter(words).most_common(3)]






from string import punctuation

def top_3_words(text):
    for p in punctuation: 
        if p != "'": text = text.replace(p, " ")
    count = {}
    for w in text.lower().split():
        if w.strip(punctuation) == '':
            pass
        elif w in count.keys():
            count[w] += 1
        else:
            count[w] = 1
    lcount = [(w,c) for w,c in count.items()]
    lcount.sort(key=lambda x: x[1], reverse=True)
    return [x[0] for x in lcount[:3]]







def top_3_words(text):
    for c in text:
        if not (c.isalpha() or c=="'"):
            text = text.replace(c,' ')
    words,counts,out = [],[],[]
    for word in list(filter(None,text.lower().split())):
        if all([not c.isalpha() for c in word]):
            continue
        if word in words:
            counts[words.index(word)] += 1
        else:
            words.append(word); counts.append(0)
    while len(words)>0 and len(out)<3:
        out.append(words.pop(counts.index(max(counts))).lower())
        counts.remove(max(counts))
    return out


"""
