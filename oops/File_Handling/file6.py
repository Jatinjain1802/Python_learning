import json
with open("File_Handling/sample.json",'w+') as f:
    d={1:"jatin",2:"manish"}
    # json_str=json.dumps(d)
    # f.write(json_str)
    json.dump(d,f)
    f.seek(0)
    # data=f.read()
    # print(json_str)
    # dd=json.loads(data)
    dd=json.load(f)

    print(dd)