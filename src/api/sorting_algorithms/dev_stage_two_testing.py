def test_for_REST_API():
    import requests

    BASE_URL = 'http://127.0.0.1:5000'

    def sort_data(input_data, algorithm):
        url = f'{BASE_URL}/sort'
        payload = {
            "input_data": input_data,
            "algorithms": algorithm
        }
        response = requests.post(url, json=payload)

        if response.status_code == 200:
            return response.json().get("result")
        else:
            print(f"Error: {response.status_code} - {response.text}")
            return None

    if __name__ == '__main__':
        input_data = [5, 3, 8, 4, 6]
        algorithm = "bubble"

        result = sort_data(input_data, algorithm)

        if result:
            print(f"Sorted result using {algorithm} sort: {result}")