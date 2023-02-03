| Optimization Result           |                                                   |
|-------------------------------|---------------------------------------------------|
| Number of residual evaluation | 4                                                 |
| Number of parameters          | 17                                                |
| Number of datapoints          | 91955                                             |
| Degrees of freedom            | 91938                                             |
| Chi Square                    | 1.47e-04                                          |
| Reduced Chi Square            | 1.60e-09                                          |
| Root Mean Square Error (RMSE) | 4.00e-05                                          |
| RMSE additional penalty       | [[2.0147494979028126e-07, 3.169370756950229e-08]] |

| RMSE (per dataset)   |   weighted |   unweighted |
|----------------------|------------|--------------|
| 1.dataset1:          |   3.54e-05 |     3.54e-05 |
| 2.dataset2:          |   4.41e-05 |     4.41e-05 |
| 3.dataset3:          |   4.01e-05 |     4.01e-05 |

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
  - _Matrix_: {('s1', 's1'): 'rates.k1(5.00e-02±2.37e-08, t-value: 2109203, initial: 4.99e-02)', ('s2', 's2'): 'rates.k2(2.31e+00±3.14e-07, t-value: 7362697, initial: 2.31e+00)', ('s3', 's3'): 'rates.k3(5.09e-01±2.01e-07, t-value: 2539982, initial: 5.09e-01)'}


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
  - _Parameters_: ['inputs.1(5.00e-01, fixed)', 'inputs.2(1.80e-01±9.16e-07, t-value: 196096, initial: 1.80e-01)', 'inputs.3(3.03e-01±2.08e-07, t-value: 1459804, initial: 3.03e-01)']
  - _Exclude From Normalize_: []

- **input2**
  - _Label_: input2
  - _Compartments_: ['s1', 's2', 's3']
  - _Parameters_: ['inputs.1(5.00e-01, fixed)', 'inputs.7(3.87e-01±1.04e-06, t-value: 373422, initial: 3.87e-01)', 'inputs.8(3.94e-01±2.28e-07, t-value: 1731211, initial: 3.94e-01)']
  - _Exclude From Normalize_: []

- **input3**
  - _Label_: input3
  - _Compartments_: ['s1', 's2', 's3']
  - _Parameters_: ['inputs.1(5.00e-01, fixed)', 'inputs.9(2.88e-01±1.00e-06, t-value: 287284, initial: 2.88e-01)', 'inputs.10(3.52e-01±2.16e-07, t-value: 1629117, initial: 3.52e-01)']
  - _Exclude From Normalize_: []


## Irf

- **irf1_with_dispersion**
  - _Label_: irf1_with_dispersion
  - _Center_: ['irf.center1(4.00e-01±3.93e-09, t-value: 101889622, initial: 4.00e-01)']
  - _Width_: ['irf.width(6.00e-02±2.41e-09, t-value: 24852005, initial: 6.00e-02)']
  - _Normalize_: True
  - _Backsweep_: False
  - _Type_: spectral-multi-gaussian
  - _Dispersion Center_: irf.dispc(5.00e+02, fixed)
  - _Center Dispersion Coefficients_: ['irf.disp1(1.00e-02±9.02e-09, t-value: 1109246, initial: 1.00e-02)', 'irf.disp2(1.00e-03±1.36e-08, t-value: 73442, initial: 1.00e-03)']
  - _Width Dispersion Coefficients_: []
  - _Model Dispersion With Wavenumber_: False

- **irf2_with_dispersion**
  - _Label_: irf2_with_dispersion
  - _Center_: ['irf.center2(4.10e-01±3.56e-09, t-value: 115269628, initial: 4.10e-01)']
  - _Width_: ['irf.width(6.00e-02±2.41e-09, t-value: 24852005, initial: 6.00e-02)']
  - _Normalize_: True
  - _Backsweep_: False
  - _Type_: spectral-multi-gaussian
  - _Dispersion Center_: irf.dispc(5.00e+02, fixed)
  - _Center Dispersion Coefficients_: ['irf.disp1(1.00e-02±9.02e-09, t-value: 1109246, initial: 1.00e-02)', 'irf.disp2(1.00e-03±1.36e-08, t-value: 73442, initial: 1.00e-03)']
  - _Width Dispersion Coefficients_: []
  - _Model Dispersion With Wavenumber_: False

- **irf3_with_dispersion**
  - _Label_: irf3_with_dispersion
  - _Center_: ['irf.center3(4.20e-01±3.65e-09, t-value: 114962212, initial: 4.20e-01)']
  - _Width_: ['irf.width(6.00e-02±2.41e-09, t-value: 24852005, initial: 6.00e-02)']
  - _Normalize_: True
  - _Backsweep_: False
  - _Type_: spectral-multi-gaussian
  - _Dispersion Center_: irf.dispc(5.00e+02, fixed)
  - _Center Dispersion Coefficients_: ['irf.disp1(1.00e-02±9.02e-09, t-value: 1109246, initial: 1.00e-02)', 'irf.disp2(1.00e-03±1.36e-08, t-value: 73442, initial: 1.00e-03)']
  - _Width Dispersion Coefficients_: []
  - _Model Dispersion With Wavenumber_: False


## Dataset

- **dataset1**
  - _Label_: dataset1
  - _Group_: default
  - _Force Index Dependent_: False
  - _Megacomplex_: ['complex1']
  - _Scale_: scale.1(1.00e+00, fixed)
  - _Initial Concentration_: input1
  - _Irf_: irf1_with_dispersion

- **dataset2**
  - _Label_: dataset2
  - _Group_: default
  - _Force Index Dependent_: False
  - _Megacomplex_: ['complex1']
  - _Scale_: scale.2(1.31e+00±2.00e-07, t-value: 6535426, initial: 1.31e+00)
  - _Initial Concentration_: input2
  - _Irf_: irf2_with_dispersion

- **dataset3**
  - _Label_: dataset3
  - _Group_: default
  - _Force Index Dependent_: False
  - _Megacomplex_: ['complex1']
  - _Scale_: scale.3(1.16e+00±1.07e-07, t-value: 10908165, initial: 1.16e+00)
  - _Initial Concentration_: input3
  - _Irf_: irf3_with_dispersion


