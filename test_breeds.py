import requests

BASE_URL = 'https://dog.ceo/api'

# def test_get_all_breeds_success():
#  resp = requests.get(f"{BASE_URL}/breeds/list/all")
#  assert resp.status_code == 200
#  data = resp.json()
#  assert data['status'] == 'success'

# def test_breeds_list_not_empty():
#  resp = requests.get(f"{BASE_URL}/breeds/list/all")
#  breeds = resp.json()['message']
#  assert len(breeds) > 0

# def test_breeds_contain_bulldog():
#  resp = requests.get(f"{BASE_URL}/breeds/list/all")
#  breeds = resp.json()['message']
#  assert 'bulldog' in breeds
 
# def test_breeds_contain_doberman():
#  resp = requests.get(f"{BASE_URL}/breeds/list/all")
#  breeds = resp.json()['message']
#  assert 'doberman' in breeds

# def test_breeds_contain_more_then_two():
#  resp = requests.get(f"{BASE_URL}/breeds/list/all")
#  breeds = resp.json()['message']
#  assert len(breeds) > 2

