#from left_money import *
#from all_money import *
import json

with open('all_money.json') as data_file:
    money = json.load(data_file)
data_file.close()
with open('left_money.json') as data_file_1:
    left_money = json.load(data_file_1)
data_file_1.close()
Moname =[1,5,10,50,100,500,1000]

user = int(input('請輸入你的座號： '))
print('你要付{}元'.format(money[user-1]['money_2_pay']))
your_money = int(input('請輸入你帶來的錢： '))
if your_money==money[user-1]['money_2_pay']:
    money[user-1]['paid']=True
    print('感謝你的零錢，你真棒')
else :
    need_to_return=your_money-money[user-1]['money_2_pay']
    print('需要找{}元'.format(need_to_return))
    return_money(need_to_return)

total=0


#print(return_money(need_to_return))

# compute how to give change
def return_money(nr):
    return_change = [0 for x in range(6)]
    if nr > 500:
        while left_money['500'] !=0 and nr>0:
            return_change[5] +=1
            nr-=500
    if nr>100:
        while left_money['100'] !=0 and nr>0:
            return_change[4] +=1
            nr-=100
    if nr>50:
        while left_money['50'] !=0 and nr>0:
            return_change[3] +=1
            nr-=50
    if nr>10:
        while left_money['10'] !=0 and nr>0:
            return_change[2] +=1
            nr-=10
    if nr>5:
        while left_money['5'] !=0 and nr>0:
            return_change[1] +=1
            nr-=5
    if nr>1:
        while left_money['1'] !=0 and nr>0:
            return_change[0] +=1
            nr-=1
    if nr:
        print('無法找錢，請稍候再來')
    else :
        money[user-1]['paid']=True
        f = open('all_money.json','w')
        f.write(json.dumps(money))
        f.close()
        for x in range(6):
            print('{}個{}元'.format(return_change[x],Moname[x]))
            left_money['{}'.format(Moname[x])]-=return_change[x]


if money[user-1]['paid']:
    total += money[user-1]['money_2_pay']



'''
import json

with open('all_money.json') as data_file:
    money = json.load(data_file)



# manually change change
def change_change(aadd):
    pass
    #left_money[change_n] +=aadd
這個部分先暫停


# print status
# 其實另外開一個檔案監控就可以了（？
# 或許可以像斂晶場記分板那樣（？


def print_remain():
    print('目前收到{}元'.format(total_ammount))
    #print('還有{}人沒交錢，分別是{}'.format())
    print(left_money)
'''