import random

def pack(name, country, number, digits):
    rname = name[random.randrange(len(name))]
    randcn = random.randrange(len(country))
    rcountry = country[randcn]
    n = 0
    rnumber = number[randcn]
    while n < 12 - len(number[randcn]):
        rnumber += digits[random.randrange(10)]
        n += 1
    return {'name' : rname, 'country' : rcountry, 'number' : rnumber}

name = ['John', 'James', 'Hugh', 'Sam', 'Michael', 'Quentin', 'Harry', 'Gary', 'Ryan', 'Patrick', 'Daniel', 'Rick',
        'Aaron', 'Robert', 'Richard',
        'Tobey', 'Tom', 'Carl', 'Peter', 'Tyron', 'Chris', 'Benjamin', 'Bryan', 'Barry', 'Ivan', 'George']
country = ['USA', 'Great Britain', 'France', 'Russian Federation', 'China', 'Canada']
number = ['+1', '+44', '+33', '+7', '+86', '+1']
digits = '1234567890'
