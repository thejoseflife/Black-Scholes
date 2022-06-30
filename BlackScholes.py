from math import *
import math

# Standard normal distribution
def sdf(x):
    return (math.exp(-(x ** 2) / 2)) / math.sqrt(2 * math.pi);

# Cumulative distribution function
def cdf(x):
    return (1.0 + erf(x / sqrt(2.0))) / 2.0

# True for call, False for put
# s = stock price
# k = exercise price
# t = time in years
# v = volatility %
# r = risk-free interest rate %
# q = dividend yield %
def calculate_european_option(call, s, k, t, v, r, q):
    v /= 100.0
    r /= 100.0
    q /= 100.0

    cp = -1
    cp_string = " put "
    if call:
        cp = 1
        cp_string = " call "

    
    
    d1 = (math.log(s / k) + (r - q + (v ** 2) / 2) * t) / (v * math.sqrt(t))
    d2 = d1 - v * math.sqrt(t)
    
    cd1 = cdf(cp * d1)
    cd2 = cdf(cp * d2)

    # print("d1: " + str(d1))
    # print("d2: " + str(d2))
    # print("N(d1): " + str(cd1))
    # print("N(d2): " + str(cd2))
          
    value = (cp * s * math.exp(-q * t) * cd1) - (cp * k * math.exp(-r * t) * cd2)
    

    print("European" + cp_string + "value: " + str(value))
    print("Delta: " + str(delta(call, s, k, t, v, r, q)))
    print("Gamma: " + str(gamma(s, v, t, d1)))
    print("Vega: " + str(vega(s, t, d1)))
    print("Rho: " + str(rho(cp, k, t, r, d2)))
    print("Theta: " + str(theta(cp, s, k, t, v, r, q)))


def delta(call, s, k, t, v, r, q):
    d1 = (math.log(s / k) + (r - q  + (v ** 2) / 2) * t) / (v * math.sqrt(t))
    if call:
        return cdf(d1)
    return cdf(d1) - 1

def gamma(s, v, t, d1):
    return sdf(d1) / (s * v * math.sqrt(t))

def vega(s, t, d1):
    return 0.01 * s * sdf(d1) * math.sqrt(t)

def rho(cp, k, t, r, d2):
    return 0.01 * cp * k * t * math.exp(-r * t) * cdf(cp * d2)

def theta(cp, s, k, t, v, r, q):
    f = s * math.exp((r - q) * t)
    
    d1 = (math.log(f / k) + (0.5 * (v ** 2)) * t) / (v * math.sqrt(t))
    d2 = d1 - v * math.sqrt(t)
    lhs = -(s * sdf(d1) * v) / (2 * math.sqrt(t))
    rhs = r * k * math.exp(-r * t) * cdf(cp * d2)
    return (lhs - cp * rhs) / 365 
#
# Test values:
# $100 current price, $105 strike, 30% volatility
# 1 year until maturity, 5% risk-free rate, 1% dividend
#

calculate_european_option(True, 100.0, 105.0, 1.0, 30.0, 5.0, 1)
calculate_european_option(False, 100.0, 105.0, 1.0, 30.0, 5.0, 1)
