export abstract class Algorithm {
    // Helper method to swap two elements in an array
    protected static swap(array: number[], index1: number, index2: number): void {
        const temp = array[index1];
        array[index1] = array[index2];
        array[index2] = temp;
    }

    // Helper method to check if an array is sorted low to high
    protected static check(array: number[]): boolean {
        for (let i = 0; i < array.length - 1; i++) {
            if (array[i] > array[i + 1]) {
                return false;
            }
        }
        return true;
    }
}