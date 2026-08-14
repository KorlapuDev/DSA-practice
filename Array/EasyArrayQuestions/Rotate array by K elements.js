function rotateArrByKelement(reqArr,eleNum,side){
    let tempArr = []
    let eleRotate = []
    if(side==="right"){
        for(let i = 0; i<reqArr.length;i++){
            if(i>reqArr.length-eleNum-1){
                eleRotate.push(reqArr[i])
            }else{
                tempArr.push(reqArr[i])
            }
        }
        return eleRotate.concat(tempArr)
    }
    if(side==="left"){
        for(let i = 0; i<reqArr.length;i++){
            if(i<eleNum){
                eleRotate.push(reqArr[i])
            }
            else{
                tempArr.push(reqArr[i])
            }
        }
        return tempArr.concat(eleRotate)
    }
}

let arr1 = [1, 2, 3, 4, 5, 6, 7]

console.log(rotateArrByKelement(arr1, 2, "left"))