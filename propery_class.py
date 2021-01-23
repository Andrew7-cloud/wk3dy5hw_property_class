

class Property:
    """The program is designed to calculate a return return (cash ROI)on any given propery."""

    def __init__(self, rental_income, laundry_income, storage_income, taxes_expense, insurance_expense, electric_expense, water_expense, sewer_expense, garbage_expense, gas_expense, hoa_expense, lawncare_expense, snowcare_expense, repairs_expense, cap_expense, properymgmt_expense, mortgage_expense, vacancy, setup_downpmt, setup_closingcost, setup_rehab, setup_miscellaneous):
        self.rental_income = rental_income
        self.laundry_income = laundry_income
        self.storage_income = storage_income
        self.taxes_expense = taxes_expense
        self.insurance_expense = insurance_expense
        self.electric_expense = electric_expense
        self.water_expense = water_expense
        self.sewer_expense = sewer_expense
        self.garbage_expense = garbage_expense
        self.gas_expense = gas_expense
        self.hoa_expense = hoa_expense
        self.lawncare_expense = lawncare_expense
        self.snowcare_expense = snowcare_expense
        self.repairs_expense = repairs_expense
        self.cap_expense = cap_expense
        self.properymgmt_expense = properymgmt_expense
        self.mortgage_expense = mortgage_expense
        self.vacancy = vacancy
        self.setup_downpmt = setup_downpmt
        self.setup_closingcost = setup_closingcost
        self.setup_rehab = setup_rehab
        self.setup_miscellaneous = setup_miscellaneous

        self.total_monthly_income = rental_income + laundry_income + storage_income
        self.total_monthly_expenses = taxes_expense + insurance_expense + electric_expense + water_expense + sewer_expense + garbage_expense + \
            gas_expense + hoa_expense + lawncare_expense + snowcare_expense + \
            repairs_expense+cap_expense+properymgmt_expense+mortgage_expense+vacancy
        self.total_monthly_cash_flow = self.total_monthly_income - self.total_monthly_expenses
        self.total_annual_cash_flow = self.total_monthly_cash_flow * 12
        self.setup_total_expense = setup_downpmt + \
            setup_closingcost + setup_rehab + setup_miscellaneous

        self.ROI = self.total_annual_cash_flow/self.setup_total_expense

    def rental_income_display(self):
        print(f"Total Monthly Income: {self.total_monthly_income}")
        print(f"Total Monthly Expenses: {self.total_monthly_expenses}")
        print(f"Total Monthly Cash Flow: {self.total_monthly_cash_flow}")
        print(f"Total Annual Cash Flow: {self.total_annual_cash_flow}")
        print(f"Total Set Up Expenses: {self.setup_total_expense}")
        print(f"Total Set Up Expenses: {self.ROI}")


"""
    def total_monthly_income(self):
        total_monthly_income= self.rental_income  + self.laundry_income + self.storage_income
        
        total_monthly_income= f" Total Monthly Income of {total_monthly_income} consists of the following expenses: \n rental income: {self.rental_income} + laundry income: {self.laundry_income} + storage income: {self.storage_income}"
        
        print(total_monthly_income)
"""

# creating duplex,
duplex = Property(2000, 0, 0, 150, 100, 0, 0, 0, 0, 0, 0, 0,
                  0, 100, 100, 200, 860, 100, 40000, 3000, 7000, 0)

# calls a method that prints rental income for duplex
duplex.rental_income_display()

# duplex.total_monthly_income()


# print(duplex.total_monthly_income())
