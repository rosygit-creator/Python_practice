import requests
import pytest

credentials={}

def get_credential():
    with open("f1.txt",'r') as f:
        for line in f:
            print("line is",line)
            key,value=line.split(",")
            credentials[key]=value
        for key, value in credentials.items():
            print("key is", key)
            print("value is", value)
    return credentials


credential1=get_credential()

# for key, value in credential1.items():
#     print(f"key1 is", key)
#     print(f"value2 is", value)
# print(credential1)

def test_post_request():

    data={"name": "a1", "age":21}
    url="abc"
    for key, value in credential1.items():
        response=requests.post(url,data, auth={ key,value })
        assert response.status_code==200


# use csv to directly read data using @pytest.mark.parameterize decorator
#https://masteringbackend.com/posts/parameterized-testing-with-pytest-and-selenium

# Import csv
# # Define a function to read data from the CSV file
# def read_test_data_from_csv(file_path):
#    test_data = []
#    with open(file_path, newline='') as csvfile:
#        reader = csv.DictReader(csvfile)
#        for row in reader:
#            test_data.append(row)
#    return test_data
#
#
# # Path to your CSV file (change this to your CSV file's path)
# csv_file_path = 'test_details.csv'
#
# # Use pytest's parametrize decorator to run the test with different data from the CSV
# @pytest.mark.parametrize("test_data", read_test_data_from_csv(csv_file_path))