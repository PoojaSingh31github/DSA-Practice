class Stack{
    constructor(){
        this.items = [];
    }
    push(element){
        this.items.push(element);
        console.log("Data Added to Stack "+element);

    }
    pop(){
        if(this.isempty){
            console.log("under-Flow");
        }else{
           console.log("Pop Data (remove)"+this.items.pop()) 

        }
    }
    peek(){
        console.log(this.items[this.items.length-1] + " peek element in the stack");
    }
    isempty(){
        return this.items.length==0
    }
    size(){
        return this.items.length;
    }
    print(){
        console.log(this.items);
    }

}
    const stack = new Stack();
    stack.push(10);
    stack.push(20);
    stack.push(30);
    stack.push(40);
    stack.push(50);
    stack.print();
    //see the top element
    stack.peek();
    // remove the top element
    stack.pop();
    stack.pop();
    stack.print();
        