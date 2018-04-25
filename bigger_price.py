from operator import itemgetter

def bigger_price(limit, data):
    result = []
    for i in range(limit):
        result.append(sorted(data, key=itemgetter("price"), reverse=True)[i])
    return result

if __name__ == "__main__":
    limit = 2
    data = [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
            ]
    print bigger_price(limit, data)