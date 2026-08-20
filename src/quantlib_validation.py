import QuantLib as ql 

#Following code utilizes QuantLib for validation of pricing engine
face_value = 100
coupon_rate = .05 

settlement_date = ql.Date.todaysDate()
calendar = ql.NullCalendar()

maturity_date = calendar.advance(
    settlement_date, ql.Period(10, ql.Years)
)

schedule = ql.Schedule(
    settlement_date,
    maturity_date,
    ql.Period(ql.Semiannual),
    calendar, 
    ql.Unadjusted,
    ql.Unadjusted,
    ql.DateGeneration.Forward, 
    False
)

bond = ql.FixedRateBond(
    0,
    face_value, 
    schedule,
    [coupon_rate],
    ql.Actual365Fixed()
)

yields = [.03,.05,.07]
for ytm in yields: 
    price = bond.cleanPrice(
    ytm, 
    ql.Actual365Fixed(),
        ql.Compounded, 
        ql.Semiannual
)
    print(f"YTM = {ytm:.0%} | QuantLib Price {price:.2f}")

Mac_duration = ql.BondFunctions.duration(
    bond,
    ytm, 
    ql.Actual365Fixed(),
    ql.Compounded,
    ql.Semiannual,
    ql.Duration.Macaulay 
)

modified_duration = ql.BondFunctions.duration(
    bond, 
    ytm, 
    ql.Actual365Fixed(),
    ql.Compounded,
    ql.Semiannual,
    ql.Duration.Modified
)

convexity = ql.BondFunctions.convexity(
    bond,
    ytm,
    ql.Actual365Fixed(),
    ql.Compounded,
    ql.Semiannual
)

print(f"\nQuantlib Macaulay Duration: {Mac_duration:.2f}")
print(f"\nQuantLib Modified Duration: {modified_duration:.2f}")
print(f"\nQuantLib Convexity: {convexity:.2f}")