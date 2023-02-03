| Optimization Result           |                                                 |
|-------------------------------|-------------------------------------------------|
| Number of residual evaluation | 8                                               |
| Number of parameters          | 17                                              |
| Number of datapoints          | 92556                                           |
| Degrees of freedom            | 92539                                           |
| Chi Square                    | 1.49e-04                                        |
| Reduced Chi Square            | 1.61e-09                                        |
| Root Mean Square Error (RMSE) | 4.01e-05                                        |
| RMSE additional penalty       | [[4.00875114792143e-08, 4.683422957896255e-08]] |

| RMSE (per dataset)   |   weighted |   unweighted |
|----------------------|------------|--------------|
| 1.dataset1:          |   3.64e-05 |     3.64e-05 |
| 2.dataset2:          |   3.51e-05 |     3.51e-05 |
| 3.dataset3:          |   5.79e-05 |     5.79e-05 |
| 4.dataset4:          |   2.34e-05 |     2.34e-05 |
| 5.dataset5:          |   4.61e-05 |     4.61e-05 |
| 6.dataset6:          |   9.00e-06 |     9.00e-06 |

# Model

## Clp Penalties

- **&nbsp;**
  - _Type_: equal_area
  - _Source_: s1
  - _Source Intervals_: [[300, 3000]]
  - _Target_: s2
  - _Target Intervals_: [[300, 3000]]
  - _Parameter_: area.1(1.00e+00, fixed)
  - _Weight_: 0.01

- **&nbsp;**
  - _Type_: equal_area
  - _Source_: s1
  - _Source Intervals_: [[300, 3000]]
  - _Target_: s3
  - _Target Intervals_: [[300, 3000]]
  - _Parameter_: area.1(1.00e+00, fixed)
  - _Weight_: 0.01


## Dataset Groups

- **default**
  - _Label_: default
  - _Residual Function_: non_negative_least_squares


## K Matrix

- **km1**
  - _Label_: km1
  - _Matrix_: {('s1', 's1'): 'rates.k1(5.00e-02±2.37e-08, t-value: 2108831, initial: 5.00e-02)', ('s2', 's2'): 'rates.k2(5.09e-01±2.00e-07, t-value: 2552274, initial: 5.00e-01)', ('s3', 's3'): 'rates.k3(2.31e+00±3.11e-07, t-value: 7423333, initial: 2.00e+00)'}


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
  - _Parameters_: ['inputs.1(5.00e-01, fixed)', 'inputs.2(3.03e-01±1.06e-06, t-value: 286638, initial: 5.10e-02)', 'inputs.3(1.80e-01±2.27e-06, t-value: 78942, initial: 2.52e-01)']
  - _Exclude From Normalize_: []

- **input2**
  - _Label_: input2
  - _Compartments_: ['s1', 's2', 's3']
  - _Parameters_: ['inputs.1(5.00e-01, fixed)', 'inputs.7(3.94e-01±1.06e-06, t-value: 371345, initial: 5.21e-02)', 'inputs.8(3.87e-01±2.24e-06, t-value: 172739, initial: 2.20e-01)']
  - _Exclude From Normalize_: []

- **input3**
  - _Label_: input3
  - _Compartments_: ['s1', 's2', 's3']
  - _Parameters_: ['inputs.1(5.00e-01, fixed)', 'inputs.9(3.52e-01±1.06e-06, t-value: 332666, initial: 5.22e-02)', 'inputs.10(2.88e-01±2.25e-06, t-value: 127941, initial: 2.20e-01)']
  - _Exclude From Normalize_: []


## Irf

- **irf1_with_dispersion**
  - _Label_: irf1_with_dispersion
  - _Center_: ['irf.center1(4.00e-01±3.92e-09, t-value: 102061193, initial: 4.00e-01)']
  - _Width_: ['irf.width(6.00e-02±2.40e-09, t-value: 24959078, initial: 6.00e-02)']
  - _Normalize_: True
  - _Backsweep_: False
  - _Type_: spectral-multi-gaussian
  - _Dispersion Center_: irf.dispc(5.00e+02, fixed)
  - _Center Dispersion Coefficients_: ['irf.disp1(1.00e-02±9.01e-09, t-value: 1109677, initial: 1.00e-02)', 'irf.disp2(1.00e-03±1.36e-08, t-value: 73426, initial: 1.00e-03)']
  - _Width Dispersion Coefficients_: []
  - _Model Dispersion With Wavenumber_: False

- **irf2_with_dispersion**
  - _Label_: irf2_with_dispersion
  - _Center_: ['irf.center2(4.10e-01±3.50e-09, t-value: 117073070, initial: 4.00e-01)']
  - _Width_: ['irf.width(6.00e-02±2.40e-09, t-value: 24959078, initial: 6.00e-02)']
  - _Normalize_: True
  - _Backsweep_: False
  - _Type_: spectral-multi-gaussian
  - _Dispersion Center_: irf.dispc(5.00e+02, fixed)
  - _Center Dispersion Coefficients_: ['irf.disp1(1.00e-02±9.01e-09, t-value: 1109677, initial: 1.00e-02)', 'irf.disp2(1.00e-03±1.36e-08, t-value: 73426, initial: 1.00e-03)']
  - _Width Dispersion Coefficients_: []
  - _Model Dispersion With Wavenumber_: False

- **irf3_with_dispersion**
  - _Label_: irf3_with_dispersion
  - _Center_: ['irf.center3(4.20e-01±3.64e-09, t-value: 115284489, initial: 4.00e-01)']
  - _Width_: ['irf.width(6.00e-02±2.40e-09, t-value: 24959078, initial: 6.00e-02)']
  - _Normalize_: True
  - _Backsweep_: False
  - _Type_: spectral-multi-gaussian
  - _Dispersion Center_: irf.dispc(5.00e+02, fixed)
  - _Center Dispersion Coefficients_: ['irf.disp1(1.00e-02±9.01e-09, t-value: 1109677, initial: 1.00e-02)', 'irf.disp2(1.00e-03±1.36e-08, t-value: 73426, initial: 1.00e-03)']
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
  - _Scale_: scale.1(1.00e+00, fixed)
  - _Initial Concentration_: input1
  - _Irf_: irf1_with_dispersion

- **dataset3**
  - _Label_: dataset3
  - _Group_: default
  - _Force Index Dependent_: False
  - _Megacomplex_: ['complex1']
  - _Scale_: scale.2(1.31e+00±3.44e-07, t-value: 3793402, initial: 1.30e+00)
  - _Initial Concentration_: input2
  - _Irf_: irf2_with_dispersion

- **dataset4**
  - _Label_: dataset4
  - _Group_: default
  - _Force Index Dependent_: False
  - _Megacomplex_: ['complex1']
  - _Scale_: scale.2(1.31e+00±3.44e-07, t-value: 3793402, initial: 1.30e+00)
  - _Initial Concentration_: input2
  - _Irf_: irf2_with_dispersion

- **dataset5**
  - _Label_: dataset5
  - _Group_: default
  - _Force Index Dependent_: False
  - _Megacomplex_: ['complex1']
  - _Scale_: scale.3(1.16e+00±1.80e-07, t-value: 6462359, initial: 1.10e+00)
  - _Initial Concentration_: input3
  - _Irf_: irf3_with_dispersion

- **dataset6**
  - _Label_: dataset6
  - _Group_: default
  - _Force Index Dependent_: False
  - _Megacomplex_: ['complex1']
  - _Scale_: scale.3(1.16e+00±1.80e-07, t-value: 6462359, initial: 1.10e+00)
  - _Initial Concentration_: input3
  - _Irf_: irf3_with_dispersion


