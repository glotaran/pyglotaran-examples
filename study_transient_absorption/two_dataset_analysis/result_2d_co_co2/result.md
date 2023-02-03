| Optimization Result           |          |
|-------------------------------|----------|
| Number of residual evaluation | 11       |
| Number of parameters          | 13       |
| Number of datapoints          | 141873   |
| Degrees of freedom            | 141860   |
| Chi Square                    | 1.40e+04 |
| Reduced Chi Square            | 9.87e-02 |
| Root Mean Square Error (RMSE) | 3.14e-01 |

| RMSE (per dataset)   |   weighted |   unweighted |
|----------------------|------------|--------------|
| 1.dataset1:          |   3.13e-01 |     5.69e-01 |
| 2.dataset2:          |   3.16e-01 |     5.79e-01 |

# Model

## Clp Relations

- **&nbsp;**
  - _Interval_: [[0, 1000]]
  - _Source_: s2
  - _Target_: s3
  - _Parameter_: rel.r1(1.00e+00, fixed)


## Dataset Groups

- **default**
  - _Label_: default
  - _Residual Function_: variable_projection


## Weights

- **&nbsp;**
  - _Datasets_: ['dataset1', 'dataset2']
  - _Global Interval_: [280, 550]
  - _Value_: 0.1

- **&nbsp;**
  - _Datasets_: ['dataset1', 'dataset2']
  - _Global Interval_: [720, 890]
  - _Value_: 0.2


## K Matrix

- **km1**
  - _Label_: km1
  - _Matrix_: {('s2', 's1'): 'rates.k1(8.27e-01, fixed)', ('s3', 's1'): 'rates.k2(8.76e+00, fixed)', ('s4', 's2'): 'rates.k3(2.40e-01±3.03e-02, t-value: 7.9, initial: 4.84e-01)', ('s4', 's3'): 'rates.k4(4.47e-02±3.03e-03, t-value: 15, initial: 3.69e-02)', ('s4', 's4'): 'rates.k5(1.86e-02±1.52e-03, t-value: 12, initial: 1.93e-02)', ('s5', 's5'): 'rates.kC(9.90e+01, fixed)'}

- **km2**
  - _Label_: km2
  - _Matrix_: {('s2', 's1'): 'rates.k1(8.27e-01, fixed)', ('s3', 's1'): 'rates.k2(8.76e+00, fixed)', ('s4', 's2'): 'rates.k3d2(1.49e+20±3.35e-17, t-value: 4447293103559744241953961144355913728, initial: 7.00e-01)', ('s4', 's3'): 'rates.k4d2(1.06e-01±3.65e-03, t-value: 29, initial: 8.50e-02)', ('s4', 's4'): 'rates.k5(1.86e-02±1.52e-03, t-value: 12, initial: 1.93e-02)', ('s6', 's6'): 'rates.kC(9.90e+01, fixed)'}


## Megacomplex

- **cmplx1**
  - _Label_: cmplx1
  - _Dimension_: time
  - _Type_: decay
  - _K Matrix_: ['km1']

- **cmplx2**
  - _Label_: cmplx2
  - _Dimension_: time
  - _Type_: decay
  - _K Matrix_: ['km2']


## Initial Concentration

- **input1**
  - _Label_: input1
  - _Compartments_: ['s1', 's2', 's3', 's4', 's5']
  - _Parameters_: ['inputs.1(1.00e+00, fixed)', 'inputs.0(0.00e+00, fixed)', 'inputs.0(0.00e+00, fixed)', 'inputs.0(0.00e+00, fixed)', 'inputs.iC(1.00e+00, fixed)']
  - _Exclude From Normalize_: []

- **input2**
  - _Label_: input2
  - _Compartments_: ['s1', 's2', 's3', 's4', 's6']
  - _Parameters_: ['inputs.1(1.00e+00, fixed)', 'inputs.0(0.00e+00, fixed)', 'inputs.0(0.00e+00, fixed)', 'inputs.0(0.00e+00, fixed)', 'inputs.iC(1.00e+00, fixed)']
  - _Exclude From Normalize_: []


## Irf

- **irf1**
  - _Label_: irf1
  - _Center_: ['irf.center(1.20e+00±1.12e-03, t-value: 1076, initial: 1.20e+00)']
  - _Width_: ['irf.width(7.18e-02±2.54e-04, t-value: 282, initial: 5.84e-02)']
  - _Normalize_: True
  - _Backsweep_: False
  - _Type_: spectral-multi-gaussian
  - _Dispersion Center_: irf.dispc(5.50e+02, fixed)
  - _Center Dispersion Coefficients_: ['irf.disp1(2.67e-01±3.43e-03, t-value: 78, initial: 3.09e-01)', 'irf.disp2(-2.83e-02±4.57e-03, t-value: -6.2, initial: -8.34e-02)', 'irf.disp3(-3.75e-03±1.89e-03, t-value: -2.0, initial: 4.70e-03)']
  - _Width Dispersion Coefficients_: []
  - _Model Dispersion With Wavenumber_: False

- **irf2**
  - _Label_: irf2
  - _Center_: ['irf2.center(6.69e-01±1.06e-03, t-value: 631, initial: 7.00e-01)']
  - _Width_: ['irf.width(7.18e-02±2.54e-04, t-value: 282, initial: 5.84e-02)']
  - _Normalize_: True
  - _Backsweep_: False
  - _Type_: spectral-multi-gaussian
  - _Dispersion Center_: irf.dispc(5.50e+02, fixed)
  - _Center Dispersion Coefficients_: ['irf.disp1(2.67e-01±3.43e-03, t-value: 78, initial: 3.09e-01)', 'irf.disp2(-2.83e-02±4.57e-03, t-value: -6.2, initial: -8.34e-02)', 'irf.disp3(-3.75e-03±1.89e-03, t-value: -2.0, initial: 4.70e-03)']
  - _Width Dispersion Coefficients_: []
  - _Model Dispersion With Wavenumber_: False


## Dataset

- **dataset1**
  - _Label_: dataset1
  - _Group_: default
  - _Force Index Dependent_: False
  - _Megacomplex_: ['cmplx1']
  - _Scale_: scale.1(1.00e+00, fixed)
  - _Initial Concentration_: input1
  - _Irf_: irf1

- **dataset2**
  - _Label_: dataset2
  - _Group_: default
  - _Force Index Dependent_: False
  - _Megacomplex_: ['cmplx2']
  - _Scale_: scale.2(1.26e+00±4.94e-04, t-value: 2550, initial: 1.30e+00)
  - _Initial Concentration_: input2
  - _Irf_: irf2


