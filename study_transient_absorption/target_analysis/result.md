| Optimization Result           |          |
|-------------------------------|----------|
| Number of residual evaluation | 10       |
| Number of parameters          | 9        |
| Number of datapoints          | 115910   |
| Degrees of freedom            | 115901   |
| Chi Square                    | 4.66e-03 |
| Reduced Chi Square            | 4.02e-08 |
| Root Mean Square Error (RMSE) | 2.00e-04 |

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
  - _Datasets_: ['dataset1']
  - _Global Interval_: [280, 550]
  - _Value_: 0.1

- **&nbsp;**
  - _Datasets_: ['dataset1']
  - _Global Interval_: [720, 890]
  - _Value_: 0.1


## K Matrix

- **km1**
  - _Label_: km1
  - _Matrix_: {('s2', 's1'): 'rates.k1(1.52e+00=_b.1(1.60e-01±1.27e-02, t-value: 13)_ * _rates.k1sum(9.50e+00, fixed)_)', ('s3', 's1'): 'rates.k2(7.98e+00=_b.2(8.40e-01=1.0 - _b.1(1.60e-01±1.27e-02, t-value: 13)_)_ * _rates.k1sum(9.50e+00, fixed)_)', ('s4', 's2'): 'rates.k3(3.61e-01±2.57e-02, t-value: 14, initial: 4.84e-01)', ('s4', 's3'): 'rates.k4(3.99e-02±9.01e-03, t-value: 4.4, initial: 3.69e-02)', ('s4', 's4'): 'rates.k5(2.01e-02±3.98e-03, t-value: 5.0, initial: 1.93e-02)', ('s5', 's5'): 'rates.kC(9.90e+01, fixed)'}


## Megacomplex

- **cmplx1**
  - _Label_: cmplx1
  - _Dimension_: time
  - _Type_: decay
  - _K Matrix_: ['km1']


## Initial Concentration

- **input1**
  - _Label_: input1
  - _Compartments_: ['s1', 's2', 's3', 's4', 's5']
  - _Parameters_: ['inputs.1(1.00e+00, fixed)', 'inputs.0(0.00e+00, fixed)', 'inputs.0(0.00e+00, fixed)', 'inputs.0(0.00e+00, fixed)', 'inputs.iC(1.00e+00, fixed)']
  - _Exclude From Normalize_: []


## Irf

- **irf1**
  - _Label_: irf1
  - _Center_: ['irf.center(1.20e+00±7.74e-04, t-value: 1553, initial: 1.20e+00)']
  - _Width_: ['irf.width(6.12e-02±2.41e-04, t-value: 254, initial: 5.84e-02)']
  - _Normalize_: True
  - _Backsweep_: False
  - _Type_: spectral-multi-gaussian
  - _Dispersion Center_: irf.dispc(5.50e+02, fixed)
  - _Center Dispersion Coefficients_: ['irf.disp1(2.89e-01±1.73e-03, t-value: 168, initial: 3.09e-01)', 'irf.disp2(-7.68e-02±1.38e-03, t-value: -56, initial: -8.34e-02)', 'irf.disp3(9.89e-03±5.63e-04, t-value: 18, initial: 4.70e-03)']
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


