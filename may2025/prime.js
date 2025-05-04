n =91

function isPrime(n){
for (let i=2; i<n**.5; i++){
    if (n % i === 0){
        return false
    }
}
  return true  
}
console.log(isPrime(n))
