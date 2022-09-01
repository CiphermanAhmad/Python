import requests as r
url = "https://dummy.restapiexample.com/api/v1/employees"
response = r.get(url)
print(response.status_code)
