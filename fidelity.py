import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from scipy.optimize import curve_fit


plt.rc('axes', axisbelow=True)
plt.rc('text', usetex=True)
plt.rc('font',**{'family':'serif','serif':['CMU Serif'], 'size':8})

def model(x, a, b):
    m = x[0]
    n = x[1]
    return a*m*(1.5*n - 0.5*np.sqrt(n)) + b*n

pa_data = np.loadtxt('fidelity_4a.csv', delimiter=',')
pb_data = np.loadtxt('fidelity_4b.csv', delimiter=',')

def fit(data, p0):
    popt, pcov = curve_fit(model, (data[:, 0], data[:, 1]), np.log2(data[:, 2]), p0=p0)
    perr = 2*np.sqrt(np.diag(pcov))
    
    names = ['a', 'b', 'c', 'd']
    print('fidelity = c e^(amn + bm + cn)')

    for i in range(len(popt)):
        print(names[i], '=', popt[i], '±', perr[i])
    
    return popt, perr

data = np.zeros((len(pa_data) + len(pb_data), 3))
data[:, 0] = 14
data[:, 1] = 53

data[:len(pa_data), 1] = pa_data[:, 0]
data[:len(pa_data), 2] = pa_data[:, 1]

data[len(pa_data):, 0] = pb_data[:, 0]
data[len(pa_data):, 2] = pb_data[:, 1]

pa_data = data[:len(pa_data), :]
pb_data = data[len(pa_data):, :]

print(data)
f = fit(data, [-0.0017, -0.001])

c1 = 'tab:blue'
c2 = 'tab:red'

fig, ax2 = plt.subplots(figsize=(3.8, 3.8), constrained_layout=True)

plt.yscale('log')
plt.ylim((0.001, 0.5))
plt.grid(which='both', axis='y')

ax2.xaxis.set_major_locator(MaxNLocator(integer=True))
ax2.tick_params(axis='x', labelcolor=c2)

ax1 = ax2.twiny()
ax1.xaxis.set_major_locator(MaxNLocator(integer=True))
ax1.tick_params(axis='x', labelcolor=c1)

ax1.scatter(pa_data[:, 1], pa_data[:, 2], marker='x', color=c1, label=r'Google Sycamore samples')
ax2.scatter(pb_data[:, 0], pb_data[:, 2], marker='+', color=c2, label=r'Google Sycamore samples')

ax1.plot(pa_data[:, 1], 2**(model(np.transpose(pa_data[:, :2]), *(f[0]))), color='k', linewidth=1, label=r'Fitted error model $\mathcal{F}_\mathrm{XEB}(n, m=14)$')
ax2.plot(pb_data[:, 0], 2**(model(np.transpose(pb_data[:, :2]), *(f[0]))), linestyle='--', linewidth=1, color='k', label=r'Fitted error model $\mathcal{F}_\mathrm{XEB}(n=53, m)$')

handles, labels = ax1.get_legend_handles_labels()
labels, handles = zip(*sorted(zip(labels, handles), key=lambda t: t[0], reverse=True))
ax1.legend(handles, labels, loc='upper right', prop={'size': 7})

handles, labels = ax2.get_legend_handles_labels()
labels, handles = zip(*sorted(zip(labels, handles), key=lambda t: t[0], reverse=True))
ax2.legend(handles, labels, loc='lower left', prop={'size': 7})

ax1.set_xlabel(r'Number of qubits, $n$', color=c1)
ax2.set_ylabel(r'Cross-entropy benchmark fidelity, $\mathcal{F}_\mathrm{XEB}$')
# ax1.set_title(r'Verifiable circuits ($m=14$, variable $n$)')

ax2.set_xlabel(r'Number of cycles, $m$', color=c2)
ax2.set_xlim(10, 22)

plt.tight_layout()
plt.savefig('fidelity.pdf', format='pdf')