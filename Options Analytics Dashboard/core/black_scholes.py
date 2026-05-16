import numpy as np
from scipy.stats import norm

def bs_price(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + sigma**2 * 0.5) * T) / (sigma * np.sqrt(T))
    d2 = d1 - (sigma * np.sqrt(T))

    call = S * norm.cdf(d1) - K * (np.exp(-r*T) * norm.cdf(d2))
    put  = K * np.exp(-r*T) * norm.cdf(-d2) - S * norm.cdf(-d1)

    return call, put