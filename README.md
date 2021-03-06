# Boundaries of quantum supremacy via random circuit sampling

## Abstract
Google's recent quantum supremacy experiment heralded a transition point where quantum 
computing performed a computational task, sampling of random quantum circuits,
beyond the reach of modern supercomputers. We examine the constraints of the observed 
quantum runtime advantage with an analytical extrapolation to larger circuits. At current 
error rates, we find a classical runtime advantage for circuits deeper than ~100 gates due 
to an exponential decrease in fidelity with increasing qubits and gates, while quantum 
runtimes bound the quantum advantage to ~300 qubits. However, reduced error rates 
exponentially expand the region of quantum advantage, emphasizing the importance of 
progress in this direction. Extrapolations of error rates suggest that the boundary of 
quantum supremacy via random circuit sampling coincides with the advent of error-corrected 
quantum computing.

## Code and data
Three code files contain the analysis of the main text:
* `fidelity.py`: Compute the empirical fidelity model. Data read from `fidelity_4a.csv` and `fidelity_4b.csv`,
which contains data from the original Google quantum supremacy experiment
(Arute, Frank, et al. "Quantum supremacy using a programmable superconducting processor." *Nature* 574.7779 (2019): 505-510).
* `main.nb`:
Contains the runtime analysis of cross-entropy benchmarking on quantum and classical devices.
* `fitter.py`: Perform exponential regression of experimental two-qubit gate error rates included in `error_rates.csv`.


## Citation

```
@misc{alex2020boundaries,
    title={Boundaries of quantum supremacy via random circuit sampling},
    author={Alexander Zlokapa and Sergio Boixo and Daniel Lidar},
    year={2020},
    eprint={2005.02464},
    archivePrefix={arXiv},
    primaryClass={quant-ph}
}
```
