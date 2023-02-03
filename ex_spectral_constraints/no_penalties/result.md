| Optimization Result           |          |
|-------------------------------|----------|
| Number of residual evaluation | 2        |
| Number of parameters          | 4        |
| Number of datapoints          | 25551    |
| Degrees of freedom            | 25547    |
| Chi Square                    | 6.18e+01 |
| Reduced Chi Square            | 2.42e-03 |
| Root Mean Square Error (RMSE) | 4.92e-02 |

# Model

## Dataset Groups

- **default**
  - _Label_: default
  - _Residual Function_: variable_projection


## K Matrix

- **km1**
  - _Label_: km1
  - _Matrix_: {('s1', 's1'): 'rates.k1(2.50e-01±4.61e-05, t-value: 5421, initial: 2.50e-01)', ('s2', 's2'): 'rates.k2(1.00e+00±1.55e-04, t-value: 6450, initial: 1.00e+00)'}


## Megacomplex

- **complex1**
  - _Label_: complex1
  - _Dimension_: time
  - _Type_: decay
  - _K Matrix_: ['km1']


## Initial Concentration

- **input1**
  - _Label_: input1
  - _Compartments_: ['s1', 's2']
  - _Parameters_: ['inputs.s1(5.00e-01, fixed)', 'inputs.s2(5.00e-01, fixed)']
  - _Exclude From Normalize_: []


## Irf

- **irf1**
  - _Label_: irf1
  - _Normalize_: True
  - _Backsweep_: False
  - _Type_: gaussian
  - _Center_: irf.center(4.00e-01±5.60e-06, t-value: 71392, initial: 4.00e-01)
  - _Width_: irf.width(6.00e-02±7.53e-06, t-value: 7964, initial: 6.00e-02)


## Dataset

- **dataset1**
  - _Label_: dataset1
  - _Group_: default
  - _Force Index Dependent_: False
  - _Megacomplex_: ['complex1']
  - _Initial Concentration_: input1
  - _Irf_: irf1


