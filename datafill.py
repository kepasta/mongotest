import time
import pymongo
import dtppl

doc = pymongo.MongoClient()


i = 0

while (i < 200):

    doc = dtppl.pack(dtppl.name, dtppl.country, dtppl.number, dtppl.digits)

    start = time.time()
    m.tests.insertTest.insert(doc, manipulate=False, w=1)
    end = time.time()

    executionTime = (end - start) * 1000 # Convert to ms

    print(executionTime)

    i = i + 1
