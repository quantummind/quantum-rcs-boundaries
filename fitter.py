import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score
import datetime

def func(x, a, b):
    return a + b*x

def exp_regression(x, y):
    p, _ = curve_fit(func, x, np.log(y))
    p[0] = np.exp(p[0])
    return p
    
def r2(coeffs, x, y):
    return r2_score(np.log(y), np.log(out[0]*np.exp(out[1]*x)))

# calculate exponential fit for TN
tn = pd.read_csv('tn_n53.csv')
out = exp_regression(tn.m, tn.time)
print('tn coefficients', out)
print('R^2', r2(out, tn.m, tn.time))
print()

# calculate exponential fit for error rate extrapolation
# report as annual decay (i.e. error rate decreases by fixed factor every year)
errors = pd.read_csv('error_rates.csv')
x = pd.to_datetime(errors.iloc[:, 0]).astype(int)
y = errors.iloc[:, 1]
out = exp_regression(x, y)
print('annual error rate decay', np.exp(out[1]*pd.Timedelta(datetime.timedelta(days=365.2422)).delta))
print('R^2', r2(out, x, y))