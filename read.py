'''
JSON文件读程序
'''
import json
import os,sys,time

json_path = '/home/lrs/Documents/VScode/test/params.json'

dict = {}

def get_json_data(json_path):
    global dict
    with open(json_path, 'r') as f:
        try:
            params = json.load(f)
            params['batch_size'] = 16
            print("params",params)
            dict = params
        except:
            print('错误')
    return dict


def write_json_data(dict):
    with open(json_path,'w') as r:
        try:
            json.dump(dict,r)
        except IndentationError:
            print('错误')


if __name__ == '__main__':
    # the_revised_dict = {'name':'lrs', 'age':20}
    # write_json_data(the_revised_dict)
    while True:
        #time.sleep(0.5)
        the_revised_dict = get_json_data(json_path)
