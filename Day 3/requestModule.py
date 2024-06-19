#sending request to browser
#ex. searching  google.com on browser 
#request method get, post, put, delete, patch

#Requests

import requests
#url = 'https://images.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'

#result = requests.get(url)
#print("Status:", result.status_code)

#with open("cat.jpg", "wb") as file:
#    file.write(result.content)

a_url = "https://bit.ly"

data = requests.get(a_url, allow_redirects=False)
print(data.status_code)
