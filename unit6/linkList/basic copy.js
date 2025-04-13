class Node{
    constructor(data){
        this.data = data;
        this.next = null
    }
}

class Linklist{
    constructor(){
        this.head = null
    }
    inseratAtHead(data){
        let newNode = new Node(data)
        newNode.next = this.head
        this.head = newNode
    }
    addAtTail(data){
        let newNode = new Node(data)
        if(this.head ==null){
            this.head = newNode
            return
        }
        let curr = this.head
        while(curr.next){
            curr = curr.next
        }
        curr.next = newNode
    }
    sizeOfLinklist(){
        let curr = this.head
        let leng=0
        while(curr){
            leng+=1
            curr = curr.next
        }
        console.log( leng)
    }
    
    insertAtsecificPos(data,p){
        let newNode = new Node(data)
        let curr = this.head  //null
        if(p==0){
            newNode.next = curr  // new data next-
            this.head = newNode
            return 
        }
        for (let i=0;i<p-1;i++){
            curr = curr.next
        }
       newNode.next =  curr.next
        curr.next = newNode
    }
    deleteNode(p){
        let curr = this.head
        if(p==0){
            this.head = this.head.next.next
            return
        }
        for (let i=0;i<p-1;i++){
            curr = curr.next
        }
        curr.next = curr.next.next
    }
    
    deleteMiddle(l){
        let pos= Math.floor(l/2) + 1   //5
        let curr = this.head
        let temp = this.head
        for (let i=0;i<pos-1;i++){
            curr = curr.next
            temp = temp.next
        }
        curr.next = temp.next.next
    }
    
    findMiddle(){
        let slow = this.head
        let fast = this.head
        while (fast && fast.next){
            slow= slow.next
            fast = fast.next.next
            return slow.data
        }
        
    }
    
}


const arr = [1,2,3,4]
let ll = new Linklist()
for (let i=0;i<arr.length; i++){
    ll.inseratAtHead(arr[i])
}
ll.addAtTail(3)
ll.addAtTail(4)
ll.addAtTail(10)
ll.deleteMiddle(7)
ll.sizeOfLinklist()
console.log(ll)


// console.log(Math.floor(5/2), Math.ceil(5/2))
