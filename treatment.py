import pymongo
import qsort

client = pymongo.MongoClient()
def trans (string, norm = True):
    j = 0
    k = 0
    l = 8
    day = 0
    hour = 0
    minute = 0
    second = 0
    ms = 0
    for i in string:
        if i == ' ':
            if k == 2:
                day = int(string[l:j])
                l = j + 1
            elif k == 3:
                hour = int(string[l:j])
                l = j + 1
            elif k == 4:
                minute = int(string[l:j])
                l = j + 1
            elif k == 5:
                second = int(string[l:j])
                l = j + 1
            elif k == 6:
                ms = int(string[l:])
            k += 1
        j += 1
    if norm:
        return ((((day*24 + hour)*60 + minute)*60 + second)*1000 + ms)
    else:
        if hour < 10:
            hour = '0' + str(hour)
        else:
            hour = str(hour)
        if day < 10:
            day = '0' + str(day)
        else:
            day = str(day)
        if minute < 10:
            minute = '0' + str(minute)
        else:
            minute = str(minute)
        if second < 10:
            second = '0' + str(second)
        else:
            second = str(second)
        return hour + ':' + minute + ':' + second + ', '+ day + '.02.2018'

user_sum_1 = trans(input("sat"))
user_sum_2 = trans(input("tas"))

viborka = []
i = 0
for men in client.tests.insertTest.find():
    pre_sum = trans(men['Date/Time'], False)
    post_sum = trans(men['Date/Time'])
    if user_sum_1 <= post_sum <= user_sum_2:
        viborka.append([pre_sum, post_sum,{'Method name' : men['Method name']}, {'App name' : men['App name']}])
    i += 1
    print(i)
    if i > 100000:
        break

f = open('text.txt', 'w')
viborka = qsort.sort(viborka)

j = 0
for i in viborka:
    f.write(str(j + 1) + ')' + '\n' + i[0] + '\n' 'Method name : ' + i[2]['Method name'] + '\n' + 'App name: ' + i[3]['App name'])
    f.write('\n')
    j += 1
f.close()
