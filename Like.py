'''
Created on Mar 10, 2023

@author: ncharlton23
'''
import csv
import string

try:
    file_one = open("AsYouLikeIt.txt",'r')
except:
    print('File cannot be opened:')
    exit()
Like = dict()
 
for line in file_one:
    words = line.split()
    for word in words:
        if word not in Like:
            Like[word] = 1
        else:
            Like[word] += 1
    Like = dict(sorted(Like.items(), key = lambda item: item[1], reverse = True))
 
del Like['of']
del Like['i']
del Like['and']
del Like['the']
del Like['to']
del Like['you']
del Like['me']
del Like['my']
del Like['a']
del Like['in']
del Like['that']
del Like['for']
del Like['not']
del Like['it']
del Like['he']
del Like['with']
del Like['is']
del Like['thou']
del Like['this']
del Like['your']
del Like['but']
del Like['him']
del Like['his']
del Like['have']
del Like['will']
del Like['be']
del Like['by']
del Like['what']
del Like['at']
del Like['her']
del Like['so']
del Like['from']
del Like['thee']
del Like['if']
del Like['thy']
del Like['as']
del Like['no']
del Like['am']
del Like['did']
del Like['here']
del Like['or']
del Like['come']
del Like['we']
del Like['go']
del Like['now']
del Like['on']
del Like['would']
del Like['do']
del Like['all']
del Like['are']
del Like['was']
del Like['then']
del Like['had']
del Like['how']
del Like['when']
del Like['there']
del Like['see']
del Like['why']
del Like['were']
del Like['hath']
del Like['an']
del Like['let']
del Like['she']
del Like['sir']
del Like['enter']
del Like['know']
del Like['us']
del Like['them']
del Like['more']
del Like['well']
del Like['some']
del Like['say']
del Like['our']
del Like['one']
del Like['they']
del Like['these']
del Like['upon']
del Like['where']
del Like['tell']
del Like['o']
del Like['their']
del Like['shall']
del Like['out']
del Like['may']
del Like['till']
del Like['make']
del Like['mine']
del Like['scene']
del Like['too']
del Like['think']
del Like['like']
del Like['which']
del Like['same']
del Like['bear']
del Like['two']
del Like['than']
del Like['yet']
del Like['time']
del Like['who']
del Like['can']
del Like['must']
del Like['such']
del Like['most']
del Like['should']
del Like['very']
del Like['give']
del Like['take']
del Like['old']
del Like['much']
del Like['better']
del Like['own']
del Like['young']
del Like['into']
del Like['any']
del Like['speak']
del Like['exeunt']
del Like['never']
del Like['look']
del Like['doth']
del Like['therefore']
del Like['ever']
del Like['comes']
del Like['could']
del Like['fool']
del Like['made']
del Like['fair']
del Like['life']
del Like['cannot']
del Like['nor']
del Like['little']
del Like['every']
del Like['true']
del Like['le']
del Like['been']
del Like['many']
del Like['good']
del Like['first']
del Like['sweet']
    
for key, value in Like.items():
    if value > 20:
        print(key + "," + str(value))

with open('AsYouLikeIt.csv', 'w') as f:
    for key,value in Like.items():
        if value > 20:
            f.write("%s,%s\n" % (key,str(value)))
    
if __name__ == '__main__':
    pass