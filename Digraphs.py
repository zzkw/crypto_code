 
s="rsuodacyadvwfplbmdvwfpzsuodavlsy kduolb pgbfjhaduqnbfpbfpg fpouzsvl cabfvlvlvwcybf vllbjhjhbfvlvllelbmdmduqsy dpvwvl dauofp fpuouo pgzslelezsjhlbmdfp bfzsfpoubfadmp ntvwvl zsfpgo dpbfmdmdmp cyuouopg ynuofgsy wmdafpbfad fpouzsvl wfbfuqntuoadpg vwvl vluomdlbfpzsuodadf jhzsbfbfuomdbfbfcyvwnbdasy"
'''
将组成句子的基本单元提取出来（字符串不能有空格）
lists=s.split(" ")
list1=[]
i=0
str1=""
for i in lists:
    if list1.count(i)==0:
        list1.append(i)
print list1
'''
#将基本单元随即换成字符并作调整知道得到正确的句子
dict1={'rs':'C','uo':'o','da':'n','cy':'g','ad':'r','vw':'a','fp':'t','lb':'u','md':'l','zs':'i','vl':'s','kd':'Y','pg':'d','bf':'e','jh':'c','uq':'y','nb':'p','ou':'h','ca':'m','le':'f','wf':'k', 'df':':','sy':'.','dp':'H','mp':'?','nt':'w','go':'x','yn':'j','fg':'b','wm':'A'}
mingwen=""
str1=""
i=0
while i<len(s):
    if s[i]==" ":
        mingwen+=" "
        i=i+1
    else:
        str1=s[i:i+2]
        mingwen+=dict1[str1]
        i=i+2
 
print (mingwen) 
