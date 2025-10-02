import requests

BASE_URL = 'https://dog.ceo/api'


# def test_get_bulldogs_images():
#  resp = requests.get(f"{BASE_URL}/breed/bulldog/images")
#  assert resp.status_code == 200
#  data = resp.json()
#  assert data["status"] == "success"
#  assert isinstance(data["message"],list)
#  assert len(data["message"])>0


# def test_breeds_list_not_empty():
#  resp = requests.get(f"{BASE_URL}/breeds/Akita/images")
#  breeds = resp.json()['message']
#  assert len(breeds) > 0

# def test_breeds_contain_bulldog():
#  resp = requests.get(f"{BASE_URL}/breeds/bulldog/images")
#  breeds = resp.json()['message']
#  assert 'bulldog' in breeds

# def test_breeds_contain_Beagle():
#  resp = requests.get(f"{BASE_URL}/breeds/Beagle/images")
#  breeds = resp.json()['message']
#  assert 'Beagle' in breeds


# def test_breeds_contain_Boxer():
#  resp = requests.get(f"{BASE_URL}/breeds/Boxer/images")
#  breeds = resp.json()['message']
#  assert 'Boxer' in breeds
 