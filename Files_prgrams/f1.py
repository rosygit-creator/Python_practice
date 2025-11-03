import requests

credentials={}

def get_credential():
    with open("f1.txt",'r') as f:
        for line in f:
            print(f"line is",line)
            key,value=line.split(",")
            credentials[key]=value
        for key, value in credentials.items():
            print(f"key is", key)
            print(f"value is", value)
    return credentials


credential1=get_credential()
for key, value in credential1.items():
    print(f"key1 is", key)
    print(f"value2 is", value)
# print(credential1)

def test_post_request():
    data={"name": "a1", "age":21}
    url="abc"
    for key, value in credential1.items():
        response=requests.post(url,data, auth={key,value})
        assert response.status_code==200

