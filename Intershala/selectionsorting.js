function selectionSort(arr){
    for (let i=0; i<arr.length; i++){
        let min = i;
        for (let j=i+1; j<arr.length; j++){
            if(arr[j]<arr[min]){
                min = j;
            }
        }
        if(min!==i){
            let temp = arr[i];
            arr[i] = arr[min];
            arr[min] = temp;
        }
    }
    return arr;
}

const unsortedArray = [9, 12, 5, 16, 14, 3, 7, 10, 1, 8];
const sortedArray = selectionSort(unsortedArray.slice());
console.log(sortedArray);
