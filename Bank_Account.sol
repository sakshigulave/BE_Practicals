//Bank_Account.sol

// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BankAccount {
    address public owner;
    uint256 private balance;

    // Constructor to initialize the owner and set initial balance
    constructor(uint256 initialBalance) {
        owner = msg.sender;
        balance = initialBalance;
    }

    // Modifier to allow only the owner to perform certain actions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Function to deposit money into the account
    function deposit(uint256 amount) public onlyOwner {
        require(amount > 0, "Deposit amount must be greater than zero");
        balance += amount;
    }

    // Function to withdraw money from the account
    function withdraw(uint256 amount) public onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(amount <= balance, "Insufficient balance");
        balance -= amount;
    }

    // Function to check the current balance
    function showBalance() public view returns (uint256) {
        return balance;
    }
}
