from flask import Flask, request, jsonify

from sorting_algorithms.bubble_sort import BubbleSort
from sorting_algorithms.insertion_sort import InsertionSort
from sorting_algorithms.merge_sort import MergeSort

app = Flask(__name__)


@app.route('/sort', methods=['POST'])
def sort():
    request_data = request.json
    input_data = request_data.get("input_data")
    algorithms = request_data.get("algorithms")

    if algorithms == "insertion":
        return jsonify({"result": InsertionSort.sort(input_data)})
    elif algorithms == "bubble":
        return jsonify({"result": BubbleSort.sort(input_data)})
    elif algorithms == "merge":
        return jsonify({"result": MergeSort.sort(input_data)})

    return jsonify({"error": "Error at /sort http request"}), 400


if __name__ == '__main__':
    app.run(debug=True)
