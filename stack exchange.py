import json,sys
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import HashingVectorizer
if sys.version_info[0]>=3: raw_input=input
transformer=HashingVectorizer(stop_words='english')

_t=[]
tl=[]
f=open('training.json')
for i in range(int(f.readline())):
    h=json.loads(f.readline())
    _t.append(h['question']+"\r\n"+h['excerpt'])
    tl.append(h['topic'])
f.close()
train = transformer.fit_transform(_t)
svm=LinearSVC()
svm.fit(train,tl)

_te=[]
for i in range(int(raw_input())):
    h=json.loads(raw_input())
    _te.append(h['question']+"\r\n"+h['excerpt'])
test = transformer.transform(_te)
test_l=svm.predict(test)
for e in test_l: print(e)
     
