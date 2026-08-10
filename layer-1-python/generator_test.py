import time

def count():
    print("STRAT")
    yield 1
    print("woke up after 1")
    yield 2
    print("woke up after 2")
    yield 3
    print("done")


# for value in count():
#     time.sleep(2)
#     print("   got:", value)



# example = [1,2,3,4,5,6,7,8,9,10]

# page_size = 3


def paginate(data, page_size):

    for i in range(0, len(data), page_size):
        print("pagination i range is:", i )
        yield data[i: i+page_size]



for i in paginate([1,2,3,4,5,6,7,8,9,10], 4):
    print(i)