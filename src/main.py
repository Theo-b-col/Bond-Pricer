from src.bond import bond
from src.pricing import BondPricing

bond = bond(
    face_value = 100, 
    coupon_rate =.05,
    maturity=10, 
    compoundingfreq=2 
)

print("Bond Created")
print("----------------")
print("Face Value:", bond.face_value)
print("Coupon Rate:", f"{bond.coupon_rate:.2%}")
print("Maturity:", bond.maturity, "years")
print("Coupon Payment:", bond.coupon_payment())
print("Number of Discounting Periods:", bond.discounting_periods())
print("Cash Flows:")
print(bond.cash_flows())

pricing = BondPricing(bond)
print(f"YTM = 5% --> price = {pricing.bond_pricer(0.05):.2f}")
print(f"YTM = 7%  --> Price = {pricing.bond_pricer(0.07):.2f}")
print(f"YTM = 3%  --> Price = {pricing.bond_pricer(0.03):.2f}")