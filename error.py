import requests

BASE_URL = 'https://dog.ceo/api'


def test_invalid404():
   resp = requests.get(f"{BASE_URL}/invaliendpoint")  
   assert resp.status_code == 404 

def test_breed_invalid404():
   resp = requests.get(f"{BASE_URL}/breeds/list/all/invaliendpoint")  
   assert resp.status_code == 404 

def test_bulldog_invalid404():
   resp = requests.get(f"{BASE_URL}/breed/bulldog/invaliendpoint")  
   assert resp.status_code == 404 

def test_Akita_invalid404():
   resp = requests.get(f"{BASE_URL}/breed/Akita/invaliendpoint")  
   assert resp.status_code == 404 

def test_Boxer_invalid404():
   resp = requests.get(f"{BASE_URL}/Breed/Boxer/invaliendpoint")  
   assert resp.status_code == 404 