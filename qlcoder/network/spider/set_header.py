import requests

url = 'http://www.qlcoder.com/task/17/solve'
headers = {
    'Host': 'www.qlcoder.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'http://cpc.people.com.cn',
    'Connection': 'keep-alive',
    'Cookie':'gr_user_id=3949c66a-56d6-49be-99e6-dc48710481cd; uuid=57fc74b0a788e; è¿é¢çç­æ¡æ¯oreo=eyJpdiI6ImZ3RStIa2tZYkYrWmJ5aWs4RDljZXc9PSIsInZhbHVlIjoiak00NktUQVpBcUtpbExGVU04UThSQT09IiwibWFjIjoiN2MyNDEzNDUyZDA5OTQ0N2UzYjQ4M2VhNjA2NDJlYzg4NDY3NjgzNzZmMGNjYWZhNmIzNDFlNzY1ZmVhZjFmZCJ9; XSRF-TOKEN=eyJpdiI6IlhEajVqN1VlR3ZJeGxZWWxtYTdYUFE9PSIsInZhbHVlIjoiRXNTbzhEK3Q2c0JkSG1zOERUV1RGa2czVHRzZzFvUmp0U2JyRkdzSHFnem90QmNkYTRxd2hXcWVMS0E2WXBVZlJpYTlWSW9tOG42WEQwaXk4d0pIN2c9PSIsIm1hYyI6IjhkOGM0OWE2YWY3MmMwOWU1YTMzZThhYjMyMTk1OGI3MDllYzA5MmQ1YzQxMTYyNjMzMzlmNDQ4MThmYTg2NWMifQ%3D%3D; laravel_session=eyJpdiI6IlRJWFZFbnpIdDZOVDJBYlwvQU85eDdRPT0iLCJ2YWx1ZSI6Ik12TGNZVXREV0MrU0tPekhMOHlBT2Q5RkJiQmRBMzR4SnN1VmlNTkk5WDFRS1c4aXJlaW1zUWJ0V211aEFlV29hUEM3XC9qa0JSakdqMXdEUnZkWkdDdz09IiwibWFjIjoiNzRiYzhkZGJjMGU3ZGY3NGFkZDAyNzExODIwMTU3YTgzOWJlY2QxMWQ0NzFjMzc2ZDFkN2NkZGY4N2FkMDc3YSJ9; gr_session_id_80dfd8ec4495dedb=350ec5ff-da1d-4294-8e84-d61c56357041; Hm_lvt_420590b976ac0a82d0b82a80985a3b8a=1476151535,1476158967,1476162163,1476162738; Hm_lpvt_420590b976ac0a82d0b82a80985a3b8a=1476163037'
}
data = {
     'answer':'referer',
     '_token':'XaWes4eXOqUlBXv4c5LtQuqqiwIQ4ZZLpg6HHHvE',
}
r = requests.post(url, headers=headers,data = data)

print(r)
