function sub_seq(n,string,i,ss){
    if (i==n){
        return 
    }
    ss.push(string[i])
    console.log(ss.join(" ") )
    sub_seq(n,string,i+1,ss);
    ss.pop()
    sub_seq(n,string,i+1,ss);
}

n=4
string="abcd"
ans = sub_seq(n,string,0,[])

