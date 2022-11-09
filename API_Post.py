import requests #request library

url = "https://todn22mvx9.execute-api.ap-south-1.amazonaws.com/dev/access" #url
head= {"x-api-key" : 'JU9eKYSwUW6lVlvGKrUkF71P1aybSR9y73jZ00y0'} #headers
myEmail = {'email': "sheiikhnadif@gmail.com"} #json object
x = requests.post(url, headers= head, json= myEmail) 
print(x.text)