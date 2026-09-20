| Optimization Result                       |                                   |
|-------------------------------------------|-----------------------------------|
| Number of residual evaluation             | 23                                |
| Number of residuals                       | 11265                             |
| Number of free parameters                 | 3                                 |
| Number of conditionally linear parameters | 1408                              |
| Degrees of freedom                        | 9854                              |
| Chi Square                                | 9.80e+06                          |
| Reduced Chi Square                        | 9.95e+02                          |
| Root Mean Square Error (RMSE)             | 3.15e+01                          |
| RMSE additional penalty                   | [[np.float64(4.133294996656057)]] |

| RMSE (per dataset)   |   weighted |   unweighted |
|----------------------|------------|--------------|
| 1.dataset1:          |   3.00e+01 |     3.00e+01 |
| 2.dataset2:          |   5.80e-04 |     5.80e-04 |

# Model

## Clp Penalties

- **&nbsp;**
  - _Type_: equal_area
  - _Source_: s2
  - _Source Intervals_: [[0, 1000]]
  - _Target_: s1
  - _Target Intervals_: [[0, 1000]]
  - _Parameter_: area.1(3.46e+00, fixed)
  - _Weight_: 1e-06


## Clp Relations

- **&nbsp;**
  - _Interval_: [[0, 1000]]
  - _Source_: s1
  - _Target_: s4
  - _Parameter_: rel.r1(1.00e+00, fixed)

- **&nbsp;**
  - _Interval_: [[0, 1000]]
  - _Source_: s3
  - _Target_: s6
  - _Parameter_: rel.r1(1.00e+00, fixed)


## Dataset Groups

- **default**
  - _Label_: default
  - _Residual Function_: non_negative_least_squares


## K Matrix

- **km1**
  - _Label_: km1
  - _Matrix_: {('s1', 's4'): 'rates.k1(2.48e-01±3.24e-02, t-value: 7.6, initial: 2.10e-01)', ('s3', 's1'): 'rates.k2(1.60e-01±3.16e-02, t-value: 5.0, initial: 1.96e-01)', ('s2', 's1'): 'rates.k3(8.70e-02, fixed)', ('s5', 's2'): 'rates.k4(2.49e-01±3.29e-02, t-value: 7.6, initial: 2.67e-01)', ('s6', 's3'): 'rates.k5(6.40e-03, fixed)', ('s6', 's6'): 'rates.k6(1.30e-06, fixed)', ('s5', 's5'): 'rates.k6(1.30e-06, fixed)'}


## Megacomplex

- **complex1**
  - _Label_: complex1
  - _Dimension_: time
  - _Type_: decay
  - _K Matrix_: ['km1']

- **complex2**
  - _Label_: complex2
  - _Dimension_: time
  - _Type_: clp-guide
  - _Target_: s5


## Initial Concentration

- **input1**
  - _Label_: input1
  - _Compartments_: ['s1', 's2', 's3', 's4', 's5', 's6']
  - _Parameters_: ['inputs.s1(0.00e+00, fixed)', 'inputs.s1(0.00e+00, fixed)', 'inputs.s1(0.00e+00, fixed)', 'inputs.s2(1.00e+00, fixed)', 'inputs.s1(0.00e+00, fixed)', 'inputs.s1(0.00e+00, fixed)']
  - _Exclude From Normalize_: []


## Irf

- **irf1**
  - _Label_: irf1
  - _Normalize_: True
  - _Backsweep_: False
  - _Type_: gaussian
  - _Center_: irf.center(-1.00e-03, fixed)
  - _Width_: irf.width(4.15e-04, fixed)


## Dataset

- **dataset1**
  - _Label_: dataset1
  - _Group_: default
  - _Force Index Dependent_: False
  - _Megacomplex_: ['complex1']
  - _Scale_: scale.1(1.00e+00, fixed)
  - _Initial Concentration_: input1
  - _Irf_: irf1

- **dataset2**
  - _Label_: dataset2
  - _Group_: default
  - _Force Index Dependent_: False
  - _Megacomplex_: ['complex2']
  - _Scale_: scale.2(8.62e-01, fixed)


