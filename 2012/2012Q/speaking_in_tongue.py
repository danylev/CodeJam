import sys 
from string import ascii_lowercase

from shared.stdread import read_input

def learning():
    base = ascii_lowercase
    google = 'ejp mysljylc kd kxveddknmc re jsicpdrysirbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcdde kr kd eoya kw aej tysr re ujdr lkgc jv'.replace(' ','')
    normal = 'our language is impossible to understandthere are twenty six factorial possibilitiesso it is okay if you want to just give up'.replace(' ','')
    translate_list = list(zip(google,normal)) + [('q','z'),('y','a'), ('z','q')]
    googlers_dict = {k:v for k,v in translate_list}
    return(googlers_dict)

if __name__ == '__main__':
    meta = read_input(sys.stdin)
    for i,line in enumerate(meta[1]):
        print(f'Case #{i+1}: ' + line.translate(str.maketrans(learning())), end='')
