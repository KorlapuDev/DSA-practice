let arr1 = [2,8,5,3,9,4,1]

for(let i = 0; i<arr1.length; i++){
    let minIndxEle = i
    for(let j = i+1; j<arr1.length; j++){
        if(arr1[minIndxEle] > arr1[j]){
            minIndxEle = j   
        }
    }
    let temp = arr1[i]
    arr1[i] = arr1[minIndxEle]
    arr1[minIndxEle] = temp
}

console.log(arr1)