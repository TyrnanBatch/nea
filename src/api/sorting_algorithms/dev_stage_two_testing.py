import requests


def test_for_rest_api():
    base_url = 'http://127.0.0.1:5000'

    def sort_data(data, algorithm):
        url = f"{base_url}/sort"
        payload = {
            "input_data": data,
            "algorithms": algorithm
        }
        response = requests.post(url, json=payload)

        if response.status_code == 200:
            return response.json().get("result")
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None

    if __name__ == '__main__':
        input_data = [235, 2, 524, 614, 623, 52, 43, 42, 5, 46, 3146, 14, 32, 5124, 6]
        alg = "bubble"

        result = sort_data(input_data, alg)

        if result:
            print(f"Sorted result using {alg} sort and got response: {result}")


test_for_rest_api()
