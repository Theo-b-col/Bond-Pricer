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
    