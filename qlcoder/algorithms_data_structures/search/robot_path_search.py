#!/usr/bin/python
# coding:utf-8

import urllib2
import re
import os


def execute_answer():
    headers = {
        'Cookie': 'gr_user_id=3949c66a-56d6-49be-99e6-dc48710481cd; uuid=5811c0d121dd4; è¿é¢çç­æ¡æ¯oreo=eyJpdiI6Ik13RVwvTVlPd0pHMGFkWTJFdElndnhRPT0iLCJ2YWx1ZSI6ImJKUlMxaFA4a1lYV2J3b0NnN0ZUS1E9PSIsIm1hYyI6ImRjZTBjYjU4NDg5ZjNjYjk5OGNmZmE0MTk2MWU1NmIyMTA4NmViMmM2OWUxYTA3NjdhYjNiODdlOTNkMmFlNTYifQ%3D%3D; XSRF-TOKEN=eyJpdiI6IndsTFlJekoreDNFcTltQjJvQWYwNVE9PSIsInZhbHVlIjoiYis4SnV6SjliMWRhRVc0VnJzOVNCZGd6THREVENtOVR2ejV5QUQwRVNLdElFa2taeCs3cWJteVBseVdhdXJ2ZEI3SWRPd3pmNnRXSHNaeERBcVdaRHc9PSIsIm1hYyI6IjBhODM4MjczODQ3MmU3MDgzNWQ2OThiMGVmYzdkMjEzNWNhOWRiNmMxMjgzNDlkYjI1ZjBlYjMxYWU0NjVhZjcifQ%3D%3D; laravel_session=eyJpdiI6IkpPWGlaWXBmSWkzYVwvdE5NYTdUbWR3PT0iLCJ2YWx1ZSI6IndxZXN4MUdFc0pQTkFLZENWM1ZxMmxuMkRzODh0R0dUQ2liVVlJYlZkTmpodUVnR3g0YzR2bnRMNVBiR1hkMkhMdHN1RXFyY3NJME12VGtTWUFYa0pnPT0iLCJtYWMiOiI1NjAxODE1MjM5YjNiYzYyMDE5NjBlZTRlNWNlOWYxNzllY2Y5NjQ1ZThlNjI3N2MwOWI1YmY1ZWFmNDgyZTdlIn0%3D; gr_session_id_80dfd8ec4495dedb=00c7f621-140a-44d1-b53c-d356c37de177; Hm_lvt_420590b976ac0a82d0b82a80985a3b8a=1477531541,1477533371,1477535066,1477558482; Hm_lpvt_420590b976ac0a82d0b82a80985a3b8a=1477566715'
    }

    request = urllib2.Request('http://www.qlcoder.com/train/autocr', headers=headers)

    response_stream = urllib2.urlopen(request, timeout=200)
    html_str = response_stream.read()
    my_list = html_str.split('\n')
    for ele in my_list:
        if re.match('level=.*[0-9]+', ele):
            print ele
            ele = ele[0:len(ele) - 4]
            print ele
            params = ele.split('&')
            level = int(params[0].split('=')[1])
            row_num = int(params[1].split('=')[1])
            col_num = int(params[2].split('=')[1])
            map_info = params[3].split('=')[1]
            params_dict = {'level': level, 'row_num': row_num, 'col_num': col_num, 'map_info': map_info}
    # time.sleep(5)
    print params_dict
    os.system(
        './cpp_robot/build/cpp_robot ' + str(params_dict['row_num']) + ' ' + str(params_dict['col_num']) + ' ' +
        params_dict[
            'map_info'] + '>output_res.txt')
    new_url = str()
    with open('output_res.txt') as fs:
        content = fs.readlines()
        new_url = content[len(content) - 1]
    print new_url
    request = urllib2.Request(new_url, headers=headers)
    response_stream = urllib2.urlopen(request, timeout=200)
    print response_stream.read()


for i in range(1, 1000):
    try:
        execute_answer()
    except IOError:
        execute_answer()
    else:
        execute_answer()
