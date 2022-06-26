from numpy import log as ln
from math import *
import math

# Standard normal distribution
def sdf(x):
    top = math.exp(-0.5 * (x ** 2))
    bottom = math.sqrt(2 * math.pi)
    return top / bottom

# Cumulative distribution function
def cdf(x):
    return (1.0 + erf(x / sqrt(2.0))) / 2.0

# p = stock price
# ep = exercise price
# v = volatility %
# t = time in years
# r = risk-free interest rate %
# dividend yield %
def calculate_european_call(p, ep, v, t, r):
    v /= 100
    r /= 100
    
    d1 = (ln(p / ep) + (r + (v ** 2) / 2) * t) / (v * math.sqrt(t))
    
    d2 = d1 - v * math.sqrt(t)

    sd1 = sdf(d1)
    cd1 = cdf(d1)
    cd2 = cdf(d2)

    # print("d1: " + str(d1))
    # print("d2: " + str(d2))
    # print("N(d1): " + str(cd1))
    # print("N(d2): " + str(cd2))

    value = p * cdf(d1) - ep * math.exp(-r * t) * cdf(d2)
    print("European call value: $" + str(value))

    print("delta: " + str(cd1))

    rho = ep * t * math.exp(-r * t) * cd2
    print("rho: "+ str(rho))

    theta = -(p * sd1 * v) / (2 * math.sqrt(t)) - r * ep * math.exp(-r * t) * cd2
    print("theta: " + str(theta))

    gamma = sd1 / (p * v * math.sqrt(t))
    print("gamma: " + str(gamma))
    
    vega = p * sd1 * math.sqrt(t)
    print("vega: " + str(vega))

def calculate_european_put(p, ep, v, t, r):
    v /= 100
    r /= 100
    
    d1 = (ln(p / ep) + (r + (v ** 2) / 2) * t) / (v * math.sqrt(t))
    d2 = d1 - v * math.sqrt(t)

    sd1 = sdf(d1)
    cd1 = cdf(d1)
    pcd2 = cdf(-d2)

    # print("d1: " + str(d1))
    # print("d2: " + str(d2))
    # print("N(d1): " + str(cd1))
    # print("N(d2): " + str(cd2))
    
    theta = -(p * sd1 * v) / (2 * math.sqrt(t)) + r * ep * math.exp(-r * t) * pcd2

    value = ep * math.exp(-r * t) * cdf(-d2) - p * cdf(-d1)
    print("European put value: $" + str(value))
                    
    print("delta: " + str(cd1 - 1))

    rho = -ep * t * math.exp(-r * t) * pcd2
    print("rho: "+ str(rho))

    print("theta: " + str(theta))

    gamma = sd1 / (p * v * math.sqrt(t))
    print("gamma: " + str(gamma))
    
    vega = p * sd1 * math.sqrt(t)
    print("vega: " + str(vega))

# Test values:
# $100 current price, $105 strike, 30% volatility
# 1 year until maturity, 5% risk-free rate
calculate_european_call(100, 105, 30, 1, 5)
calculate_european_put(100, 105, 30, 1, 5)
