'''
Created on Feb 27, 2023

@author: ncharlton23
'''
import csv
import string

try:
    file_one = open("ComedyOfErrors.txt",'r')
except:
    print('File cannot be opened:')
    exit()
Comedy = dict()
 
for line in file_one:
    words = line.split()
    for word in words:
        if word not in Comedy:
            Comedy[word] = 1
        else:
            Comedy[word] += 1
    Comedy = dict(sorted(Comedy.items(), key = lambda item: item[1], reverse = True))
 
del Comedy['of']
del Comedy['i']
del Comedy['and']
del Comedy['the']
del Comedy['to']
del Comedy['you']
del Comedy['me']
del Comedy['my']
del Comedy['a']
del Comedy['in']
del Comedy['that']
del Comedy['for']
del Comedy['not']
del Comedy['it']
del Comedy['he']
del Comedy['with']
del Comedy['is']
del Comedy['thou']
del Comedy['this']
del Comedy['your']
del Comedy['but']
del Comedy['him']
del Comedy['his']
del Comedy['have']
del Comedy['will']
del Comedy['be']
del Comedy['by']
del Comedy['what']
del Comedy['at']
del Comedy['her']
del Comedy['so']
del Comedy['from']
del Comedy['thee']
del Comedy['if']
del Comedy['thy']
del Comedy['as']
del Comedy['no']
del Comedy['am']
del Comedy['did']
del Comedy['here']
del Comedy['or']
del Comedy['come']
del Comedy['we']
del Comedy['go']
del Comedy['now']
del Comedy['on']
del Comedy['would']
del Comedy['do']
del Comedy['all']
del Comedy['are']
del Comedy['was']
del Comedy['then']
del Comedy['had']
del Comedy['how']
del Comedy['when']
del Comedy['there']
del Comedy['see']
del Comedy['why']
del Comedy['were']
del Comedy['hath']
del Comedy['an']
del Comedy['let']
del Comedy['she']
del Comedy['sir']
del Comedy['enter']
del Comedy['know']
del Comedy['us']
del Comedy['them']
del Comedy['more']
del Comedy['well']
del Comedy['some']
del Comedy['say']
del Comedy['our']
del Comedy['one']
del Comedy['they']
del Comedy['these']
del Comedy['upon']
del Comedy['where']
del Comedy['tell']
del Comedy['o']
del Comedy['their']
del Comedy['shall']
del Comedy['out']
del Comedy['may']
del Comedy['till']
del Comedy['make']
del Comedy['mine']
del Comedy['scene']
del Comedy['too']
del Comedy['think']
del Comedy['like']
del Comedy['which']
del Comedy['same']
del Comedy['bear']
del Comedy['two']
    
for key, value in Comedy.items():
    if value > 20:
        print(key + "," + str(value))

with open('ComedyOfErrors.csv', 'w') as f:
    for key,value in Comedy.items():
        if value > 20:
            f.write("%s,%s\n" % (key,str(value)))
    
if __name__ == '__main__':
    pass