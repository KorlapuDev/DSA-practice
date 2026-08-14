let arr1 = [1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]
let arrNums = []
let arrZeros = []
for(let i =0; i<arr1.length; i++) {
    if(arr1[i] === 0){
        arrZeros.push(0)
    }
    else{
        arrNums.push(arr1[i])
    }

}
console.log(arrNums, arrZeros)

console.log(arrNums.concat(arrZeros))