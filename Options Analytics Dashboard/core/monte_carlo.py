import numpy as np

def mc_price(S, K, T, r, sigma, simulations=10_000):
    Z = np.random.standard_normal(simulations)

    S_T = S * np.exp((r - 0.5 * sigma**2) * T + sigma * np.sqrt(T) * Z)

    call_payoffs = np.maximum(S_T - K, 0)
    put_payoffs  = np.maximum(K - S_T, 0)

    call = np.exp(-r * T) * np.mean(call_payoffs)
    put  = np.exp(-r * T) * np.mean(put_payoffs)

    return call, put, S_T