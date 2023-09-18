''' Goal '''
# Create a Budget class that can instantiate objects based on different budget categories like food,
# clothing, and entertainment. These objects should allow for depositing and withdrawing funds from
# each category, as well computing category balances and transferring balance amounts
# between categories.

class Budget:

    ''' Class representing a budget pot '''

    def __init__(self,passed_funds, passed_pot):
        self.funds = passed_funds
        self.pot = passed_pot

    def display_funds(self):
        """ Display funds to the user """
        print("You currently have a total of {} pounds in the {} pot.".format(self.funds, self.pot))

    def deposit_funds(self):
        """ Deposit funds into a chosen pot """
        user_confirmation = input("Would you like to deposit into the {} pot? (please answer Y or N)".format(self.pot))
        if user_confirmation == "Y":
            deposit_amount = int(input("How much would you like to deposit into the {} pot?".format(self.pot)))
            print("You have deposited {} pounds into the {} pot.".format(deposit_amount, self.pot))
            self.funds = self.funds + deposit_amount
            self.display_funds()

    def withdraw_funds(self):
        """ Withdraw funds from a chosen pot """
        user_confirmation = input("Would you like to withdraw from the {} pot? (please answer Y or N)".format(self.pot))
        if user_confirmation == "Y":
            withdraw_amount = int(input("How much would you like to withdraw into the {} pot?".format(self.pot)))
            print("You have withdrawn {} pounds from the {} pot.".format(withdraw_amount, self.pot))
            self.funds = self.funds - withdraw_amount
            self.display_funds()

    def transfer_funds(self, other_pot):
        """ Transfer funds from one pot to another """
        user_confirmation = input("Would you like to transfer any funds from the {} pot to the {} pot? (please answer Y or N)".format(self.pot, other_pot.pot))
        if user_confirmation == "Y":
            transfer_amount = int(input("How much do you wish to transfer from the {} pot into the {} pot?".format(self.pot, other_pot.pot)))
            print("You have transferred a total of {} pounds from the {} pot into the {} pot".format(transfer_amount, self.pot, other_pot.pot))
            other_pot.funds = other_pot.funds + transfer_amount
            self.funds = self.funds - transfer_amount
            self.display_funds()
            other_pot.display_funds()

####################################################
# Create a new budget pot
food_budget = Budget(250, "Food")
food_budget.deposit_funds()
food_budget.withdraw_funds()
# Create a new budget pot
clothing_budget = Budget(50, "Clothing")
clothing_budget.deposit_funds()
clothing_budget.withdraw_funds()
# Transfer funds from one pot to another
food_budget.transfer_funds(clothing_budget)
clothing_budget.transfer_funds(food_budget)
####################################################