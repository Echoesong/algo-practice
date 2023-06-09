// const isAnagram = function(s, t) {
//     // For each letter in string S, check if that letter is in t; if it is not, return falsel; if it is, pop it out and continue iterating
//     let sArray = [...s]
//     let tArray = [...t]
//     let testArray = tArray.filter(char => sArray.includes(char))
//     if(testArray === tArray){
//         return true
//     } else{
//         return false
//     }
// };

// isAnagram('anagram', 'nagaram')

// // Things I had to look up:
    
// // 1. 'Includes' method
// // 2. 'Filter' method

// // 2nd go around w/o references:

// let validAnagram2 = (string1, string2) => {
//     let str1Arr = [...string1]
//     let str2Arr = [...string2]
//     let testString = string2.filter(char => str1Arr.includes(char))
//     if(testString.length === str2Arr.length){
//         return true
//     } else{
//         return false
//     }
// }

var isAnagram = function(s, t) {
    let sArray = [...s]
    let tArray = [...t]
    let testArray = tArray.filter(char => sArray.includes(char))
    let newStr = testArray.join('')
    console.log('test', newStr)
    if(newStr === t && sArray.length === tArray.length){
        console.log(sArray, tArray, testArray)
        return true
    } else{
        console.log(sArray, tArray, testArray)
        return false
    }
};

console.log(isAnagram('anagram', 'nagaram'))