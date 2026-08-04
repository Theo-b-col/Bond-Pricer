class BondPricing: 

    def __init__(self, bond):
        self.bond = bond 

    def discount_factor(self, ytm, period): 
        """ 
        Calculates discount factor for a given period
        """
        periodic_ytm = ytm / self.bond.compoundingfreq
        return 1 / (1+periodic_ytm) ** period

    def bond_pricer(self, ytm):
        """
        Prices a Fixed-rate bond using discounted cash flows 

        parameters: 
            YTM: Annual yield to maturity
        
        Returns:
            Present value of the bond
        """
        price = 0 
        cashflows = self.bond.cash_flows()
        for _, row in cashflows.iterrows(): 
            period = row["Period"]
            cashflow = row["Cash Flow"]
            
            discount_factor = self.discount_factor(ytm, period)
            
            present_value = cashflow * discount_factor
            price += present_value
        return price
        
    