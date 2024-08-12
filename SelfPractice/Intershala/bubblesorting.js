function bubblesort(arr){
    const n= arr.length;
    for(let i=0;i<n;i++){
        for(j=0;j<n-1;j++){   
            if(arr[j]>arr[j+1]){
                let temp = arr[j];
                arr[j]= arr[j+1];
                arr[j+1]= temp;
            }
        }
    }
    return arr;
}

const unsorteArray = [9, 2, 5, 6, 4, 3, 7, 10, 1, 8];
const sortedArray = bubblesort(unsorteArray);
console.log(sortedArray);