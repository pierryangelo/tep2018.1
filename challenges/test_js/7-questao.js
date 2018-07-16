var savingsAccount = {
    balance: 1000,
    interestRatePercent: 1,

    deposit:
    function addMoney(amount) {
        if (amount > 0) {
            savingsAccount.balance += amount;
        }
    },

    withdraw:
    function removeMoney(amount) {
        var verifyBalance = savingsAccount.balance - amount;
        if (amount > 0 && verifyBalance >= 0) {
            savingsAccount.balance -= amount;
        }
    },

    printAccountSummary:
    function () {
        return "Welcome! \nYour balance is currently $" + String(savingsAccount.balance) +
        " and your interest rate is " + String(savingsAccount.interestRatePercent) + "%.";
    },
};


// tests
console.log(savingsAccount["printAccountSummary"]())

savingsAccount["balance"] = 2000
savingsAccount["interestRatePercent"] = 2

console.log(savingsAccount["printAccountSummary"]())

savingsAccount["balance"] = 500
savingsAccount["interestRatePercent"] = 3
