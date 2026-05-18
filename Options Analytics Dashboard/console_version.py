from data.market import get_stock_info, get_risk_free_rate, get_expiries, get_option_chain, time_to_expiry
from core.black_scholes import bs_price
from core.greeks import greeks

ticker = input("Enter ticker: ").upper()

info = get_stock_info(ticker)
if info is None:
    print("Stock Not Found :(")
    exit()

S = info["price"]
print(f"\n{info['name']} — ${S}")

r = get_risk_free_rate()
print(f"Risk-free rate: {r:.2%}")

expiries = get_expiries(ticker)
print("\nAvailable expiries:")
for i, date in enumerate(expiries[:5]):   # show first 5
    print(f"  {i}: {date}")

choice = int(input("Pick expiry number: "))
expiry = expiries[choice]
T = time_to_expiry(expiry)

calls, puts = get_option_chain(ticker, expiry)
print("\nAvailable strikes:")
strikes = calls["strike"].tolist()
for i, strike in enumerate(strikes):
    print(f"  {i}: ${strike}")

choice = int(input("Pick strike number: "))
K = strikes[choice]

sigma = calls.iloc[choice]["impliedVolatility"]
print(f"\nImplied volatility: {sigma:.2%}")

call, put = bs_price(S, K, T, r, sigma)

delta_call, delta_put, gamma, theta_call, vega = greeks(S, K, T, r, sigma)

print(f"\n--- Black-Scholes Results ---")
print(f"Call Price: ${call:.2f}")
print(f"Put Price:  ${put:.2f}")

print(f"\n--- Greeks ---")
print(f"Delta (call): {delta_call:.4f}")
print(f"Delta (put):  {delta_put:.4f}")
print(f"Gamma:        {gamma:.4f}")
print(f"Theta:        {theta_call:.4f}")
print(f"Vega:         {vega:.4f}")