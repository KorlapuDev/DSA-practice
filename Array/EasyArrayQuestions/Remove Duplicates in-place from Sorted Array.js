let arr1 = [1,1,2,2,2,3,3]
let removedArr=[]
removedArr.push(arr1[0])
for(let i = 1; i<arr1.length; i++){
    if(arr1[i] !== arr1[i-1]){
        removedArr.push(arr1[i])
    }
}

console.log(removedArr)

