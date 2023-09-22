import { Algorithm } from './Algorithm';

class Insertion extends Algorithm {
    public static sort(array: number[]): number[] {
        for (let i = 0; i < array.length - 1; i++) {
            let minIndex = i;
            for (let j = i + 1; j < array.length; j++) {
                if (array[j] < array[minIndex]) {
                    minIndex = j;
                }
            }
            this.swap(array, i, minIndex);
        }
        return array;
    }
}
