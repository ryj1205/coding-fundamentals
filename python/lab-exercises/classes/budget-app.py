###########################################################################################################
# Goal:
# Create a Budget class that can instantiate objects based on different budget categories like food, 
# clothing, and entertainment. These objects should allow for depositing and withdrawing funds from 
# each category, as well computing category balances and transferring balance amounts between categories.
###########################################################################################################

class Budget:

    def __init__(self,passedFunds, passedPot):
        self.funds = passedFunds
        self.pot = passedPot

    def displayFunds(self):
        print("You currently have a total of {} pounds in the {} pot.".format(self.funds, self.pot))

    def depositFunds(self):

        # Ask user if they wish to deposit:
        user_confirmation = input("Would you like to deposit any funds into the {} pot? (please answer Y or N)".format(self.pot))

        if (user_confirmation == "Y"):
            # Ask user how much they wish to withdraw:
            deposit_amount = int(input("How much would you like to deposit into the {} pot?".format(self.pot)))
            print("You have deposited {} pounds into the {} pot.".format(deposit_amount, self.pot))
            # Perform balance calculations:
            self.funds = self.funds + deposit_amount
            # Display updated pot balance:
            self.displayFunds()
        else:
            exit

    def withdrawFunds(self):

        # Ask user if they wish to withdraw:
        user_confirmation = input("Would you like to withdraw any funds from the {} pot? (please answer Y or N)".format(self.pot))

        if (user_confirmation == "Y"):
            # Ask user how much they wish to withdraw:
            withdraw_amount = int(input("How much would you like to withdraw into the {} pot?".format(self.pot)))
            print("You have withdrawn {} pounds from the {} pot.".format(withdraw_amount, self.pot))
            # Perform balance calculations:
            self.funds = self.funds - withdraw_amount
            # Display updated pot balance:
            self.displayFunds()
        else:
            exit

    def transferFunds(self, otherPot):

        # Ask user if they wish to transfer:
        user_confirmation = input("Would you like to transfer any funds from the {} pot to the {} pot? (please answer Y or N)".format(self.pot, otherPot.pot))

        if (user_confirmation == "Y"):
            # Ask user how much they wish to transfer:
            transfer_amount = int(input("How much do you wish to transfer from the {} pot into the {} pot?".format(self.pot, otherPot.pot)))
            print("You have transferred a total of {} pounds from the {} pot into the {} pot".format(transfer_amount, self.pot, otherPot.pot))
            # Perform balance calculations:
            otherPot.funds = otherPot.funds + transfer_amount
            self.funds = self.funds - transfer_amount
            # Display updated pot balances:
            self.displayFunds()
            otherPot.displayFunds()
        else:
            exit

###########################################################################################################

# Create a new budget pot:
food_budget = Budget(250, "Food")

# Deposit funds into the pot:
food_budget.depositFunds()

# Withdraw funds from the pot:
food_budget.withdrawFunds()

###########################################################################################################

# Create a new budget pot:
clothing_budget = Budget(50, "Clothing")

# Deposit funds into the pot:
clothing_budget.depositFunds()

# Withdraw funds from the pot:
clothing_budget.withdrawFunds()

###########################################################################################################

# Transfer funds from one pot to another:
food_budget.transferFunds(clothing_budget)
clothing_budget.transferFunds(food_budget)