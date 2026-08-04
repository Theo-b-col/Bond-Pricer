import pandas as pd 

class bond: 
    """
    Represents an option free fixed-rate bond calculation
    """
    def __init__(self, 
                 face_value, 
                 coupon_rate,
                 maturity,
                 compoundingfreq=2): 
        self.face_value = face_value
        self.coupon_rate = coupon_rate
        self.maturity = maturity
        self.compoundingfreq = compoundingfreq

    def coupon_payment(self): 
        # returns the coupon payment for each period 
        return (self.face_value * self.coupon_rate/self.compoundingfreq)
    
    def discounting_periods(self):
        # returns the number of coupons over the life of the bond
        return self.compoundingfreq * self.maturity
    
    def cash_flows(self): 
        """
        Creates a per period analysis of coupons recieved 
        """
        cash_flows = [] 

        periods = self.discounting_periods()
        for p in range(1, periods + 1): 
            if p < periods: 
                cash_flow = self.coupon_payment()
            else: 
                cash_flow = self.coupon_payment() + self.face_value
            cash_flows.append(cash_flow)
        return pd.DataFrame({
            "Period": range(1,periods + 1), 
            "Cash Flow": cash_flows
        })
    