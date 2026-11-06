import requests
import time


URL = 'http://127.0.0.1:8000'
GET_URL = f"{URL}/get_cache"
POST_URL = f"{URL}/create_cache"

sess = requests.Session()

print(f"[+] Sending POST request... URL: {POST_URL}")
post_response = sess.post(POST_URL)
time.sleep(1)
print(f"[+] Sending GET request... URL: {GET_URL}")
get_response = sess.get(GET_URL)
print(f"[+] get_response: {get_response}")
print(f"[+] get_response: {get_response.text}")
