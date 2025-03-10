from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from sorting_algorithms.bubble_sort import BubbleSort
from sorting_algorithms.insertion_sort import InsertionSort
from sorting_algorithms.merge_sort import MergeSort
from sorting_algorithms.quick_sort import QuickSort

app = Flask(__name__)
CORS(app)


@app.route('/sort', methods=['POST'])
def sort():
    request_data = request.json
    input_data = request_data.get("input_data")
    algorithms = request_data.get("algorithms")

    if algorithms == "insertion":
        return jsonify({"stages": InsertionSort.sort(input_data)})
    elif algorithms == "bubble":
        return jsonify({"stages": BubbleSort.sort(input_data)})
    elif algorithms == "merge":
        return jsonify({"stages": MergeSort.sort(input_data)})
    elif algorithms == "quick":
        return jsonify({"stages": QuickSort.sort(input_data)})

    return jsonify({"error": "Error at /sort http request"}), 400


if __name__ == '__main__':
    app.run(debug=True)
