class BondPricing: 

    def __init__(self, bond):
        self.bond = bond 

    def bond_pricer(self, ytm):
        """
        Prices a Fixed-rate bond using discounted cash flows 

        parameters: 
            YTM: Annual yield to maturity
        
        Returns:
            Present value of the bond
        """
        periodic_ytm = ytm / self.bond.compoundingfreq
        price = 0 
        periods = self.bond.discounting_periods()
        for p in range(1, periods +1): 
            if p < periods: 
                cashflow = self.bond.coupon_payment()
            else: 
                cashflow = self.bond.coupon_payment() + self.bond.face_value
            present_value = cashflow / (1+periodic_ytm) ** p
            price += present_value
        return price
        