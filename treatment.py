import pymongo
import qsort

client = pymongo.MongoClient()
def trans (string):
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
    return ((((day*24 + hour)*60 + minute)*60 + second)*1000 + ms)

user_sum_1 = trans(input("sat"))
user_sum_2 = trans(input("tas"))
viborka = []
i = 0
for men in client.tests.insertTest.find():
    post_sum = trans(men['Date/Time'])
    if user_sum_1 <= post_sum <= user_sum_2:
        viborka.append([post_sum,{'Method name' : men['Method name']}, {'App name' : men['App name']}])

print(qsort.sort(viborka))