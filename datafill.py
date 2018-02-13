import time
import pymongo
import dtppl

m = pymongo.MongoClient()


i = 0


while (i < 100000000):

    doc = dtppl.pack(dtppl.appname, dtppl.methname, dtppl.message)

    start = time.time()
    m.tests.insertTest.insert(doc, manipulate=False, w=1)
    end = time.time()

    executionTime = (end - start) * 1000 # Convert to ms

    print(executionTime)

    i = i + 1
