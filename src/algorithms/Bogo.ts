import { Algorithm } from './Algorithm';

class Bogo extends Algorithm {
    public static sort(array: number[]): number[] {
        while (!this.check(array)) { // Checks if the array is sorted
            this.shuffle(array); // If the array is not sorted, shuffle it
        }

        return array;
    }

    // Randomly shuffles the array
    private static shuffle(array: number[]): void {
        const n = array.length;

        for (let i = n - 1; i > 0; i--) {
            const j = Math.floor(Math.random()*i); // Generate a random index in [0, i]

            this.swap(array, i, j);
        }
    }
}
