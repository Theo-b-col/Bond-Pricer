import pandas as pd 

class BondPricing: 

    def __init__(self, bond):
        self.bond = bond 

    def discount_factor(self, ytm, period): 
        """ 
        Calculates discount factor for a given period
        """
        periodic_ytm = ytm / self.bond.compoundingfreq
        return 1 / (1+periodic_ytm) ** period

    def valuation_table(self, ytm):
        cashflows = self.bond.cash_flows()
        cashflows["Discount Factor"] = [
            self.discount_factor(ytm, period) for period in cashflows["Period"]
        ]
        cashflows["Present Value"] = (
                cashflows["Cash Flow"] * cashflows["Discount Factor"]
            )
        

        return cashflows
    
    def bond_pricer(self, ytm):
        """
        Prices a Fixed-rate bond using discounted cash flows 

        parameters: 
            YTM: Annual yield to maturity
        
        Returns:
            Present value of the bond
        """
        table = self.valuation_table(ytm)
        return table["Present Value"].sum()
        
    def yield_sensitivity(self,yields):
        """
        Calculates the price of the bond under different yield curve scenarios 

        Parameters: List of annual yields
        returns: DataFrame containing YTM and bond price
        """
        prices = [] 
        for ytm in yields:
            price = self.bond_pricer(ytm)   
            prices.append(price)
        return pd.DataFrame({
            "YTM": yields,
            "Price": prices
        })

    def duration(self,ytm):
        """
        Calculates the Macaulay duration of a bond. 
        """
        table = self.valuation_table(ytm)

        price = table["Present Value"].sum()
        table["Duration Weight"] = (
            table["Period"] * table["Present Value"]
        )
        duration = table["Duration Weight"].sum() / price

        return duration/self.bond.compoundingfreq
    
    def modified_duration(self, ytm):
        """
        Calculates modified duration
        """
        macaulay = self.duration(ytm)

        periodic_ytm = ytm / self.bond.compoundingfreq
        return macaulay / (1+periodic_ytm)
    
    def convexity(self, ytm): 
        """
        Calculates convexity of fixed-rate bond(second order effect)
        """
        table = self.valuation_table(ytm)
        price = table["Present Value"].sum()
        periodic_ytm = ytm / self.bond.compoundingfreq
        periods = table["Period"]

        table["Convexity Weight"] = (
            periods * (periods + 1) * table["Present Value"]
        )

        convexity = ( 
            table["Convexity Weight"].sum() / 
            (price * (1+periodic_ytm) ** 2)
        )

        return convexity / self.bond.compoundingfreq ** 2
    
    def yield_shock_analysis(self, base_ytm, shocked_ytm):
        """
        Compares the actual bond price with duration and convextiy adjustments 
        """

        base_price = self.bond_pricer(base_ytm)
        shocked_price = self.bond_pricer(shocked_ytm)

        actual_change = (shocked_price - base_price) / base_price

        delta = shocked_ytm - base_ytm
        modified_duration = self.modified_duration(base_ytm)
        convexity = self.convexity(base_ytm)

        duration_approximation = -modified_duration * delta
        convexity_approximation = ( 
            duration_approximation + .5 * convexity * delta **2
        )
        
        return { 
            "Base Price": base_price,
            "Shocked Price": shocked_price,
            "Actual Change": actual_change,
            "Duration Approximation": duration_approximation,
            "Duration + Convexity Approximation": convexity_approximation
        }
