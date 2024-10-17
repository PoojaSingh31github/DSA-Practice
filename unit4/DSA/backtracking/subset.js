function odd_subset(n,arr,k,i,res) {
  if (i == n) {
    return 
  }
  res.push(arr[i])
  console.log(res)
  odd_subset(n,arr,k,i+1,res)
  res.pop()
  odd_subset(n,arr,k,i+1,res)

}
let n=3
let arr=[1,2,3]
let k=2
let res =[]
let ans = odd_subset(n,arr,k,0,res)