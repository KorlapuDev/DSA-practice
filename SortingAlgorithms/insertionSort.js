let arr1 = [11, 12, 13, 5, 6];

// Start from the second element (index 1)
for (let i = 1; i < arr1.length; i++) {
    let key = arr1[i]; // The element to be inserted
    let j = i - 1;

    // Shift elements of arr1[0..i-1] that are greater than key
    // to one position ahead of their current position
    while (j >= 0 && arr1[j] > key) {
        arr1[j + 1] = arr1[j];
        j--;
    }
    
    // Place the key in its correct sorted position
    arr1[j + 1] = key;
}

console.log(arr1); // Output: [5, 6, 11, 12, 13]




// Bidirectional and sort// Shuttle sort it is combination og bubble and insertion sort. 
// let arr1 = [11,12,13,5,6]

// for(let i = 0; i< arr1.length; i++){
//     for(let j = i+1; j>0; j--){
//         if(arr1[j] < arr1[j-1]){
//             let temp = arr1[j]
//             arr1[j] = arr1[j-1]
//             arr1[j-1] = temp
//         }
//     }
// }

// console.log(arr1)