let arr1 = [2,8,5,3,9,4,1]

for(let i = 0; i<arr1.length; i++){
    let swaped = false
    for(let j = 0; j<arr1.length - 1; j++){
        if(arr1[j] > arr1[j+1]){
            [arr1[j], arr1[j+1]] = [arr1[j+1], arr1[j]];
            swaped = true
        }   
    }
    if(swaped === false){
        break
    }
}
console.log(arr1);