left_money = {
    '1':0,
    '5':0,
    '10':0,
    '50':0,
    '100':0,
    '500':0,
    '1000':0
}

f = open('left_money.json','w')

import json

f.write(json.dumps(left_money))