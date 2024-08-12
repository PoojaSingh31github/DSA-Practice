class Account {
    constructor(name, balance) {
        this.name = name;
        this.balance = balance;
    }
    deposit(amount) {
        this.balance += amount;
    }
    withdraw(amount) {
        this.balance -= amount;
    }
    getBalance() {
        return this.balance;
    }

    showAccData(){
        console.log("---------------");
        console.log("Name: " + this.name);
        console.log("Balance: " + this.balance);
        
    }
    
}
const account1 = new Account("Suraj", 1000);
const account2 = new Account("Shivam", 1400);
const account3 = new Account("pooja", 1200);

const accs = [account1, account2, account3];
for (let obj of accs){
   obj.showAccData;
}

account1.deposit(100);
account2.withdraw(50);
account3.deposit(200);
console.log("pooja's balance: " + account3.getBalance());