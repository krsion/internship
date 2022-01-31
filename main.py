'''
ASSUMPTIONS:
- point 2) - this equals to number of unique item ids
- point 3 and 4)
        for each item id I calculated mean and average time between 
        requests (from any users and any hour) and then from
        from those mean spans per item_id I calculated a mean
        and similarly for each item_id I calculated median and from
        those medians I printed median

DATA
- for used id, requests are in the the first list item
- first element of request is date in ISO format
    - second element is returned type 

'''

import json
import datetime
import statistics

users = set()
item_requests = dict()


def main():
    for i in range(24):
        file_name = f"data/{i:02}_returned"
        file = open(file_name, 'r')
        data = json.load(file)
        file.close()
        process_one_hour(data)

    print(f"1) Number of unique users: {len(users)}")
    print(f"2) Number of unique items: {len(item_requests)}")
    median, mean = calculate_median_and_mean_span()
    print(f"3) Average time between item_id requests: {mean}")
    print(f"4) Median time between item_id requests: {median}")
    m = max([item_requests[id]['similarInJsonList'] for id in item_requests])
    print(f"5) Max number of requests per item_id with similarInJsonList: {m}")


def process_one_hour(data):
    for user_id in data:
        users.add(user_id)
        for item_id in data[user_id]:
            if item_id != "variant":
                # ASSUMPTION requests are in data[user_id][item_id][0]
                requests = data[user_id][item_id][0]
                for request in requests:
                    process_request(request, item_id)


def process_request(request, item_id):
    date = datetime.datetime.fromisoformat(request[0])
    if not item_id in item_requests:
        item_requests[item_id] = {
            'spans': [], 'last_date': date, 'similarInJsonList': 0
        }
    else:
        old_date = item_requests[item_id]['last_date']
        item_requests[item_id]['spans'].append(
            date-old_date)
        item_requests[item_id]['last_date'] = date
        if request[1] == 'similarInJsonList':
            item_requests[item_id]['similarInJsonList'] += 1


def calculate_median_and_mean_span():
    median_spans = []
    mean_spans = []
    for item_id in item_requests:
        X = item_requests[item_id]['spans']
        if len(X) > 0:
            median_spans.append(statistics.median(X))
            mean_spans.append(sum(X, datetime.timedelta())/len(X))
    return statistics.median(median_spans), (sum(mean_spans, datetime.timedelta())/len(mean_spans))


if __name__ == '__main__':
    main()
