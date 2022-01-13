# Internship Task

Thank you for your interest in our internship position. 

We ask you to finish two tasks: (i) the _Python competency task_, and (ii) the _Machine learning competency task_.

The tasks should not take you more than 30 minutes overall.

In the tasks: 
1. follow the python coding standards/best practices specified in http://www.python.org/dev/peps/pep-0008/ and the "lower_case_with_underscores" variable naming style,
2. in algorithmic parts, select appropriate data structures and algorithms to minimize computational complexity,
3. in theoretical parts, answer precisely and concisely.

To submit the task, create a gitlab/github repo, publish your solution to that repo, and share the repo with us.

Good luck.


## Python competency task

You are presented with data (in the `data` directory of this repository) of records stored in one-hour dumps named `HH_returned`, where `HH` means "hour", in the following json 
format:

```
{
  "271736829405315319062165375185738528887": {      # user_id
    "494398": [                                     # item_id
      [
        [
          "2021-12-02T00:00:00.546000+00:00",       # datetime of request
          "NotReadyYet"                             # variant returned
        ],
        [
          "2021-12-02T00:01:00.546000+00:00",       # datetime of next visit
          "similarInJsonList"                       # variant returned
        ]
      ],
      []
    ],
    "variant": [                                    # not important
      "NotCount",
      ""
    ]
  },
  "327369077869547705509707240484932336059": {      # user_id
    "3147684": [                                    # item_id
      [
        [
          "2021-12-02T00:00:00.437000+00:00",       # datetime of request
          "similarInJsonList"                       # variant returned
        ]
      ],
      []
    ],
    "variant": [                                    # not important
      "similarInJsonList",
      ""
    ]
  }
}
```

The data represents requests of _users_ (identified by unique `user_id`) 
for various _items_ (identified by unique `item_id`). Each _user_ might 
request data for several _item_ids_. For each request, the _datetime of 
request_  is recorded along with the _variant_ of returned data, which might 
be one of the `similarInJsonList`,`NotReadyYet`, 
or `NotEnoughSimilarsInStock`.

Your task is to parse the data and compute:
1. number of unique users in one day
2. number of unique requests (unique = multiple requests of the same item count as one)
3. average time between _item_id_ requests (in the sample data above, the average time between the requests would be 1 minute - computed from the _item_id_ `494398`, since the _item_id_ `3147684` was requested only once, so the average would only be computed from )
4. median time between _item_id_ requests (-||-),
5. maximum number of requests per a single _item_id_ for which the variant `similarInJsonList` was returned.

You are free to make reasonable assumptions and decisions in your solution if the 
assignment is not fully clear to you - be sure to comment on them.

Use only the Python Standard Library (no numpy etc.) and Python 3.

Create your solution so it runs by `python main.py`.

__Note__: Do not include the contents of the `data` directory in your solution, please.  

## Machine learning competency task

1. You are given a dataset of RGB images of shoes. Describe a procedure that would sort the shoes into groups by colors, possibly using some machine learning algorithm. Discuss the advantages/disadvantages of your solutions. Use less than 100 words, please.   
2. You are given a previously unseen image of a shoe. Design an algorithm that would retrieve 10 most similars shoes from your dataset. Use less than 100 words, please.

