import matplotlib.pyplot as plt
import pandas as pd 

def plot_yield_sensitivity(yield_table):
    """
    Plots bond price against Yield to Maturity
    """
    
    plt.figure(figsize=(8,5))   
    plt.plot(
    yield_table["YTM"] * 100, 
    yield_table["Price"],
    marker="o"
    )
    
    plt.xlabel("Yield to Maturity %")
    plt.ylabel("Bond Price")
    plt.title("Bond Price vs Yield to Maturity (%)")
    plt.grid(True)

    plt.tight_layout()
    plt.savefig("figures/yield_sensitivity.png", dpi = 300)
    plt.close()

def plot_yield_shocks(shock_table):
    """
    Plots actual bond price changes against duration and duration + convexity approximations 
    """

    plt.figure(figsize=(8,5))
    plt.plot(
    shock_table["Shock"],
    shock_table["Actual"],
    marker='o',
    label="Actual"
    )

    plt.plot(
    shock_table["Shock"],
    shock_table["Duration"],
    marker='o',
    label="Duration"
    )
    plt.plot(
    shock_table["Shock"],
    shock_table["Duration + Convexity"],
    marker='o',
    label="Duration + Convexity"    
    )
    plt.xlabel("Yield Shock (BPS)")
    plt.ylabel("Price Change (%)")
    plt.title("Yield Shock Analysis")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig("figures/yield_shock_analysis_png", dpi = 300)


