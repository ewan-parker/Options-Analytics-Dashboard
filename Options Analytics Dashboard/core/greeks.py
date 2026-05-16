import numpy as np
from scipy.stats import norm

def greeks(S, K, T, r, sigma):
    d1 = (np.log(S/K) + (r + sigma**2 * 0.5) * T) / (sigma * np.sqrt(T))
    d2 = d1 - (sigma * np.sqrt(T))

    delta_call = norm.cdf(d1)
    delta_put  = norm.cdf(d1) - 1

    gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))

    theta_call = (- (S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T)) - r * K * np.exp(-r*T) * norm.cdf(d2)) / 365

    vega = S * norm.pdf(d1) * np.sqrt(T) / 100

    return delta_call, delta_put, gamma, theta_call, vega
    