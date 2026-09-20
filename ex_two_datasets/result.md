| Optimization Result                       |                                                                           |
|-------------------------------------------|---------------------------------------------------------------------------|
| Number of residual evaluation             | 18                                                                        |
| Number of residuals                       | 51104                                                                     |
| Number of free parameters                 | 10                                                                        |
| Number of conditionally linear parameters | 153                                                                       |
| Degrees of freedom                        | 50941                                                                     |
| Chi Square                                | 3.14e+02                                                                  |
| Reduced Chi Square                        | 6.16e-03                                                                  |
| Root Mean Square Error (RMSE)             | 7.85e-02                                                                  |
| RMSE additional penalty                   | [[np.float64(2.4736226259847174e-05), np.float64(3.904897312168032e-07)]] |

| RMSE (per dataset)   |   weighted |   unweighted |
|----------------------|------------|--------------|
| 1.dataset1:          |   6.75e-02 |     6.75e-02 |
| 2.dataset2:          |   8.79e-02 |     8.79e-02 |

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


## K Matrix

- **km1**
  - _Label_: km1
  - _Matrix_: {('s1', 's1'): 'rates.k1(2.50e-01±1.65e-04, t-value: 1511, initial: 1.99e-01)', ('s2', 's2'): 'rates.k2(5.00e-01±9.69e-04, t-value: 516, initial: 5.00e-01)', ('s3', 's3'): 'rates.k3(1.00e+00±1.00e+00, t-value: 1, initial: 1.10e+00)'}


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
  - _Parameters_: ['inputs.1(5.00e-01, fixed)', 'inputs.2(6.25e-01±1.17e-02, t-value: 53, initial: 2.51e-01)', 'inputs.3(6.44e-01±4.06e-03, t-value: 159, initial: 2.52e-01)']
  - _Exclude From Normalize_: []

- **input2**
  - _Label_: input2
  - _Compartments_: ['s1', 's2', 's3']
  - _Parameters_: ['inputs.1(5.00e-01, fixed)', 'inputs.7(3.12e-01±5.41e-03, t-value: 58, initial: 2.10e-01)', 'inputs.8(1.61e-01±1.05e-03, t-value: 153, initial: 2.20e-01)']
  - _Exclude From Normalize_: []


## Irf

- **irf1**
  - _Label_: irf1
  - _Normalize_: True
  - _Backsweep_: False
  - _Type_: gaussian
  - _Center_: irf.center(4.00e-01±4.66e-06, t-value: 85824, initial: 5.00e-01)
  - _Width_: irf.width(6.00e-02±6.33e-06, t-value: 9467, initial: 1.00e-01)

- **irf1_no_dispersion**
  - _Label_: irf1_no_dispersion
  - _Normalize_: True
  - _Backsweep_: False
  - _Type_: gaussian
  - _Center_: irf.center(4.00e-01±4.66e-06, t-value: 85824, initial: 5.00e-01)
  - _Width_: irf.width(6.00e-02±6.33e-06, t-value: 9467, initial: 1.00e-01)


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
  - _Megacomplex_: ['complex1']
  - _Scale_: scale.2(1.10e+00±4.55e-04, t-value: 2417, initial: 1.20e+00)
  - _Initial Concentration_: input2
  - _Irf_: irf1


