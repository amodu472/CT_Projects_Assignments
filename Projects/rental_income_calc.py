import time


def main():
    print("Welcome to the ROI Calculator. ROI will be calculated after all entries have been made...")

    purchase_price = int(input("How much did you buy the property: ").strip())
    roi_calc_instance = ROICalculator(purchase_price)
    print(roi_calc_instance)

    entering_required_details = True
    while entering_required_details:
        selection = input(
            "Type I for Income, E for Expense, V for Investment, S to Show Entries or Q to Quit: ").strip().upper()
        if selection == "I":
            income_name = input("Enter a valid income name: ").strip().title()
            income_amount = int(input("Enter a valid income amount: ").strip())
            roi_calc_instance.add_income(income_name, income_amount)
        elif selection == "E":
            expense_name = input(
                "Enter a valid expense name: ").strip().title()
            expense_amount = int(
                input("Enter a valid expense amount: ").strip())
            roi_calc_instance.add_expense(expense_name, expense_amount)
        elif selection == "V":
            investment_name = input("Enter a valid investment name: ").strip()
            investment_amount = int(
                input("Enter a valid investment amount: ").strip())
            roi_calc_instance.add_investment(
                investment_name, investment_amount)
        elif selection == "S":
            roi_calc_instance.show_all_entries()
        elif selection == "Q":
            entering_required_details = False

    print("ROI is... drumroll please...")

    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)

    print(roi_calc_instance.cc_roi())


class ROICalculator:
    def __init__(self, purchase_price):
        if not isinstance(purchase_price, (int, float)):
            raise ValueError("Purchase price must be an integer or float")
        self._purchase_price = purchase_price
        self._total_income = {}
        self._total_expenses = {}
        self._total_investments = {}

    def __str__(self):
        return f"This property was purchased for ${self.purchase_price:,}.00"

    @property
    def purchase_price(self):
        return self._purchase_price

    @property
    def total_investments(self):
        return self._total_investments

    @property
    def total_income(self):
        return self._total_income

    @property
    def total_expenses(self):
        return self._total_expenses

    def add_expense(self, expense_name, expense_value):
        if not isinstance(expense_value, (int, float)) or not isinstance(expense_name, str):
            raise ValueError("Please check your inputs and try again.")
        self.total_expenses[expense_name] = self.total_expenses.get(
            expense_name, 0) + expense_value

    def add_income(self, income_name, income_value):
        if not isinstance(income_value, (int, float)) or not isinstance(income_name, str):
            raise ValueError("Please check your inputs and try again.")
        self.total_income[income_name] = self.total_income.get(
            income_name, 0) + income_value

    def add_investment(self, investment_name, investment_value):
        if not isinstance(investment_name, str) or not isinstance(investment_value, (int, float)):
            raise ValueError("Please check your inputs and try again.")
        self.total_investments[investment_name] = self.total_investments.get(
            investment_name, 0) + investment_value

    def monthly_cash_flow(self):
        total_income = sum(vals for vals in self.total_income.values())
        total_expenses = sum(vals for vals in self.total_expenses.values())
        total_monthly_cash_flow = total_income - total_expenses
        return total_monthly_cash_flow

    def cc_roi(self):
        annual_cash_flow = self.monthly_cash_flow() * 12
        total_investments = sum(val for val in self.total_investments.values())
        cc_roi = annual_cash_flow / total_investments * 100
        return f"{round(cc_roi, 1)}%"

    def show_all_entries(self):
        if self.total_income:
            print("All Income: ")
            for key, val in self.total_income.items():
                print(f"{key.title()}: ${val:,}.00")
            print()
        else:
            print("No income entries yet.")

        if self.total_expenses:
            print("All Expenses: ")
            for key, val in self.total_expenses.items():
                print(f"{key.title()}: ${val:,}.00")
            print()
        else:
            print("No expense entries yet.")

        if self.total_investments:
            print("All Investments: ")
            for key, val in self.total_investments.items():
                print(f"{key.title()}: ${val:,}.00")
            print()
        else:
            print("No investment entries yet.")

        return "End of entries."


if __name__ == "__main__":
    main()
