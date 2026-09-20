| Optimization Result                       |                                                                           |
|-------------------------------------------|---------------------------------------------------------------------------|
| Number of residual evaluation             | 86                                                                        |
| Number of residuals                       | 91955                                                                     |
| Number of free parameters                 | 16                                                                        |
| Number of conditionally linear parameters | 153                                                                       |
| Degrees of freedom                        | 91786                                                                     |
| Chi Square                                | 5.03e+03                                                                  |
| Reduced Chi Square                        | 5.48e-02                                                                  |
| Root Mean Square Error (RMSE)             | 2.34e-01                                                                  |
| RMSE additional penalty                   | [[np.float64(0.0038861541781443523), np.float64(0.00048749663137641623)]] |

| RMSE (per dataset)   |   weighted |   unweighted |
|----------------------|------------|--------------|
| 1.dataset1:          |   2.54e-01 |     2.54e-01 |
| 2.dataset2:          |   2.38e-01 |     4.76e-01 |
| 3.dataset3:          |   2.08e-01 |     8.30e+01 |

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
  - _Datasets_: ['dataset2']
  - _Global Interval_: [400, 600]
  - _Value_: 0.5

- **&nbsp;**
  - _Datasets_: ['dataset3']
  - _Global Interval_: [400, 600]
  - _Value_: 0.0025


## K Matrix

- **km1**
  - _Label_: km1
  - _Matrix_: {('s1', 's1'): 'rates.k1(5.00e-02±1.07e-05, t-value: 4670, initial: 5.00e-02)', ('s2', 's2'): 'rates.k2(1.99e+00±6.61e-03, t-value: 301, initial: 1.99e+00)', ('s3', 's3'): 'rates.k3(4.99e-01±9.21e-04, t-value: 542, initial: 4.99e-01)'}


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
  - _Parameters_: ['inputs.1(5.00e-01, fixed)', 'inputs.2(2.42e-01±2.42e-01, t-value: 1, initial: 2.42e-01)', 'inputs.3(3.63e-01±3.63e-01, t-value: 1, initial: 3.63e-01)']
  - _Exclude From Normalize_: []

- **input2**
  - _Label_: input2
  - _Compartments_: ['s1', 's2', 's3']
  - _Parameters_: ['inputs.1(5.00e-01, fixed)', 'inputs.7(1.61e-01±1.61e-01, t-value: 1, initial: 1.61e-01)', 'inputs.8(3.12e-01±3.12e-01, t-value: 1, initial: 3.12e-01)']
  - _Exclude From Normalize_: []

- **input3**
  - _Label_: input3
  - _Compartments_: ['s1', 's2', 's3']
  - _Parameters_: ['inputs.1(5.00e-01, fixed)', 'inputs.9(9.63e-02±9.63e-02, t-value: 1, initial: 9.62e-02)', 'inputs.10(2.08e-01±2.08e-01, t-value: 1, initial: 2.08e-01)']
  - _Exclude From Normalize_: []


## Irf

- **irf1_no_dispersion**
  - _Label_: irf1_no_dispersion
  - _Normalize_: True
  - _Backsweep_: False
  - _Type_: gaussian
  - _Center_: irf.center1(5.00e-01±2.03e-05, t-value: 24596, initial: 5.00e-01)
  - _Width_: irf.width1(6.00e-02±2.29e-05, t-value: 2619, initial: 6.00e-02)

- **irf2_no_dispersion**
  - _Label_: irf2_no_dispersion
  - _Normalize_: True
  - _Backsweep_: False
  - _Type_: gaussian
  - _Center_: irf.center2(4.00e-01±3.64e-05, t-value: 11002, initial: 4.00e-01)
  - _Width_: irf.width1(6.00e-02±2.29e-05, t-value: 2619, initial: 6.00e-02)

- **irf3_no_dispersion**
  - _Label_: irf3_no_dispersion
  - _Normalize_: True
  - _Backsweep_: False
  - _Type_: gaussian
  - _Center_: irf.center3(4.50e-01±1.26e-04, t-value: 3566, initial: 3.00e-01)
  - _Width_: irf.width2(1.20e-01±1.71e-04, t-value: 701, initial: 8.99e-02)


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
  - _Scale_: scale.2(8.80e-01±8.80e-01, t-value: 1, initial: 8.80e-01)
  - _Initial Concentration_: input2
  - _Irf_: irf2_no_dispersion

- **dataset3**
  - _Label_: dataset3
  - _Group_: default
  - _Force Index Dependent_: False
  - _Megacomplex_: ['complex1']
  - _Scale_: scale.3(7.27e+01±4.85e+02, t-value: 0.1, initial: 7.27e+01)
  - _Initial Concentration_: input3
  - _Irf_: irf3_no_dispersion


