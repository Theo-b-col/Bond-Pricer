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

print(pricing.valuation_table(.05))
print(f"Macaulay Duration: {pricing.duration(.05):.2f}")
print(f"Modified Duration: {pricing.modified_duration(.05):.2f}")
print(f"Convexity: {pricing.convexity(.05):.2f}")

yields = [.02,.03,.04,.05,.06,.07,.08]
print("Yield Sensitivity:")
print(pricing.yield_sensitivity(yields))

shocks = [-0.02, -0.01, -0.005, 0.005, 0.01, 0.02]
print("\n Yield Shock Analysis:")
for shock in shocks: 
    result = pricing.yield_shock_analysis(.05, .05 + shock)
    print(
        f"Shock: {shock:+.2%} | "
        f"Actual: {result['Actual Change']:+.2%} | "
        f"Duration: {result['Duration Approximation']:+.2%} | "
        f"Duration + Convexity: "
        f"{result['Duration + Convexity Approximation']:+.2%}"
    )
