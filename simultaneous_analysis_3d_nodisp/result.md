| Optimization Result                       |                                                                            |
|-------------------------------------------|----------------------------------------------------------------------------|
| Number of residual evaluation             | 5                                                                          |
| Number of residuals                       | 91955                                                                      |
| Number of free parameters                 | 13                                                                         |
| Number of conditionally linear parameters | 153                                                                        |
| Degrees of freedom                        | 91789                                                                      |
| Chi Square                                | 6.78e+02                                                                   |
| Reduced Chi Square                        | 7.39e-03                                                                   |
| Root Mean Square Error (RMSE)             | 8.59e-02                                                                   |
| RMSE additional penalty                   | [[np.float64(1.0249816568830283e-06), np.float64(1.7612652300158516e-06)]] |

| RMSE (per dataset)   |   weighted |   unweighted |
|----------------------|------------|--------------|
| 1.dataset1:          |   8.02e-02 |     8.92e-02 |
| 2.dataset2:          |   9.15e-02 |     1.02e-01 |
| 3.dataset3:          |   8.55e-02 |     9.51e-02 |

# Model

## Clp Penalties

- **&nbsp;**
  - _Type_: equal_area
  - _Source_: s1
  - _Source Intervals_: [[300, 3000]]
  - _Target_: s2
  - _Target Intervals_: [[300, 3000]]
  - _Parameter_: area.1(1.00e+00, fixed)
  - _Weight_: 0.1

- **&nbsp;**
  - _Type_: equal_area
  - _Source_: s1
  - _Source Intervals_: [[300, 3000]]
  - _Target_: s3
  - _Target Intervals_: [[300, 3000]]
  - _Parameter_: area.1(1.00e+00, fixed)
  - _Weight_: 0.1


## Dataset Groups

- **default**
  - _Label_: default
  - _Residual Function_: non_negative_least_squares


## Weights

- **&nbsp;**
  - _Datasets_: ['dataset1', 'dataset2', 'dataset3']
  - _Global Interval_: [400, 450]
  - _Value_: 0.5


## K Matrix

- **km1**
  - _Label_: km1
  - _Matrix_: {('s1', 's1'): 'rates.k1(5.00e-02±3.49e-06, t-value: 14315, initial: 5.00e-02)', ('s2', 's2'): 'rates.k2(2.00e+00±1.40e-03, t-value: 1429, initial: 2.00e+00)', ('s3', 's3'): 'rates.k3(5.00e-01±2.22e-04, t-value: 2248, initial: 5.00e-01)'}


## Megacomplex

- **complex1**
  - _Label_: complex1
  - _Dimension_: time
  - _Type_: decay
  - _K Matrix_: ['km1']


## Initial Concentration

- **input1**
  - _Label_: input1
  - _Compartments_: ['s1', 's2', 's3']
  - _Parameters_: ['inputs.1(5.00e-01, fixed)', 'inputs.2(1.61e-01±1.34e-04, t-value: 1199, initial: 1.61e-01)', 'inputs.3(3.11e-01±1.60e-04, t-value: 1946, initial: 3.11e-01)']
  - _Exclude From Normalize_: []

- **input2**
  - _Label_: input2
  - _Compartments_: ['s1', 's2', 's3']
  - _Parameters_: ['inputs.1(5.00e-01, fixed)', 'inputs.7(3.23e-01±1.75e-04, t-value: 1846, initial: 3.22e-01)', 'inputs.8(4.15e-01±2.37e-04, t-value: 1755, initial: 4.15e-01)']
  - _Exclude From Normalize_: []

- **input3**
  - _Label_: input3
  - _Compartments_: ['s1', 's2', 's3']
  - _Parameters_: ['inputs.1(5.00e-01, fixed)', 'inputs.9(2.42e-01±1.52e-04, t-value: 1591, initial: 2.42e-01)', 'inputs.10(3.63e-01±1.97e-04, t-value: 1842, initial: 3.63e-01)']
  - _Exclude From Normalize_: []


## Irf

- **irf1_no_dispersion**
  - _Label_: irf1_no_dispersion
  - _Normalize_: True
  - _Backsweep_: False
  - _Type_: gaussian
  - _Center_: irf.center(4.00e-01±4.79e-06, t-value: 83550, initial: 4.00e-01)
  - _Width_: irf.width(6.00e-02±5.90e-06, t-value: 10157, initial: 6.00e-02)


## Dataset

- **dataset1**
  - _Label_: dataset1
  - _Group_: default
  - _Force Index Dependent_: False
  - _Megacomplex_: ['complex1']
  - _Scale_: scale.1(1.00e+00, fixed)
  - _Initial Concentration_: input1
  - _Irf_: irf1_no_dispersion

- **dataset2**
  - _Label_: dataset2
  - _Group_: default
  - _Force Index Dependent_: False
  - _Megacomplex_: ['complex1']
  - _Scale_: scale.2(1.27e+00±7.94e-05, t-value: 16027, initial: 1.27e+00)
  - _Initial Concentration_: input2
  - _Irf_: irf1_no_dispersion

- **dataset3**
  - _Label_: dataset3
  - _Group_: default
  - _Force Index Dependent_: False
  - _Megacomplex_: ['complex1']
  - _Scale_: scale.3(1.14e+00±5.63e-05, t-value: 20166, initial: 1.13e+00)
  - _Initial Concentration_: input3
  - _Irf_: irf1_no_dispersion


