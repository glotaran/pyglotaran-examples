| Optimization Result                       |          |
|-------------------------------------------|----------|
| Number of residual evaluation             | 11       |
| Number of residuals                       | 141873   |
| Number of free parameters                 | 9        |
| Number of conditionally linear parameters | 3412     |
| Degrees of freedom                        | 138452   |
| Chi Square                                | 8.93e+03 |
| Reduced Chi Square                        | 6.45e-02 |
| Root Mean Square Error (RMSE)             | 2.54e-01 |

| RMSE (per dataset)   |   weighted |   unweighted |
|----------------------|------------|--------------|
| 1.dataset1:          |   2.83e-01 |     4.10e-01 |
| 2.dataset2:          |   1.91e-01 |     2.83e-01 |

# Model

## Clp Relations

- **&nbsp;**
  - _Interval_: [[680, 1000]]
  - _Source_: c1
  - _Target_: c2
  - _Parameter_: rel.r1(1.00e+00, fixed)

- **&nbsp;**
  - _Interval_: [[680, 1000]]
  - _Source_: s1
  - _Target_: s2
  - _Parameter_: rel.r1(1.00e+00, fixed)


## Dataset Groups

- **default**
  - _Label_: default
  - _Residual Function_: variable_projection


## Weights

- **&nbsp;**
  - _Datasets_: ['dataset1']
  - _Global Interval_: [520, 540]
  - _Value_: 0.4

- **&nbsp;**
  - _Datasets_: ['dataset1']
  - _Global Interval_: [720, 1000]
  - _Value_: 0.5

- **&nbsp;**
  - _Datasets_: ['dataset2']
  - _Global Interval_: [520, 540]
  - _Value_: 0.4

- **&nbsp;**
  - _Datasets_: ['dataset2']
  - _Global Interval_: [720, 1000]
  - _Value_: 0.5


## K Matrix

- **km1fast**
  - _Label_: km1fast
  - _Matrix_: {('c2', 'c1'): 'rates.k21(4.43e-01±4.82e-03, t-value: 92, initial: 5.00e+00)', ('c3', 'c1'): 'rates.kocfast(6.38e-02±1.83e-02, t-value: 3.5, initial: 3.00e-01)', ('c3', 'c2'): 'rates.kocfast(6.38e-02±1.83e-02, t-value: 3.5, initial: 3.00e-01)', ('c3', 'c3'): 'rates.k33(1.42e-02=_rates.k3total(2.03e-02±5.83e-05, t-value: 349)_*(1-_rates.Tyield(3.00e-01, fixed)_))', ('c4', 'c3'): 'rates.k43(6.10e-03=_rates.k3total(2.03e-02±5.83e-05, t-value: 349)_*_rates.Tyield(3.00e-01, fixed)_)', ('c4', 'c4'): 'rates.k44(1.00e-05, fixed)'}

- **km1slow**
  - _Label_: km1slow
  - _Matrix_: {('c2', 'c1'): 'rates.k21(4.43e-01±4.82e-03, t-value: 92, initial: 5.00e+00)', ('c3', 'c1'): 'rates.kocslow(4.01e-02±1.72e-03, t-value: 23, initial: 4.00e-02)', ('c3', 'c2'): 'rates.kocslow(4.01e-02±1.72e-03, t-value: 23, initial: 4.00e-02)', ('c3', 'c3'): 'rates.k33(1.42e-02=_rates.k3total(2.03e-02±5.83e-05, t-value: 349)_*(1-_rates.Tyield(3.00e-01, fixed)_))', ('c4', 'c3'): 'rates.k43(6.10e-03=_rates.k3total(2.03e-02±5.83e-05, t-value: 349)_*_rates.Tyield(3.00e-01, fixed)_)', ('c4', 'c4'): 'rates.k44(1.00e-05, fixed)'}

- **km2fast**
  - _Label_: km2fast
  - _Matrix_: {('s2', 's1'): 'rates.k21(4.43e-01±4.82e-03, t-value: 92, initial: 5.00e+00)', ('s3', 's1'): 'rates.kcocfast(1.28e-01=_rates.kocfast(6.38e-02±1.83e-02, t-value: 3.5)_*2)', ('s3', 's2'): 'rates.kcocfast(1.28e-01=_rates.kocfast(6.38e-02±1.83e-02, t-value: 3.5)_*2)', ('s3', 's3'): 'rates.k33(1.42e-02=_rates.k3total(2.03e-02±5.83e-05, t-value: 349)_*(1-_rates.Tyield(3.00e-01, fixed)_))', ('s4', 's3'): 'rates.k43(6.10e-03=_rates.k3total(2.03e-02±5.83e-05, t-value: 349)_*_rates.Tyield(3.00e-01, fixed)_)', ('s4', 's4'): 'rates.k44(1.00e-05, fixed)'}

- **km2slow**
  - _Label_: km2slow
  - _Matrix_: {('s2', 's1'): 'rates.k21(4.43e-01±4.82e-03, t-value: 92, initial: 5.00e+00)', ('s3', 's1'): 'rates.kcocslow(8.03e-02=_rates.kocslow(4.01e-02±1.72e-03, t-value: 23)_*2)', ('s3', 's2'): 'rates.kcocslow(8.03e-02=_rates.kocslow(4.01e-02±1.72e-03, t-value: 23)_*2)', ('s3', 's3'): 'rates.k33(1.42e-02=_rates.k3total(2.03e-02±5.83e-05, t-value: 349)_*(1-_rates.Tyield(3.00e-01, fixed)_))', ('s4', 's3'): 'rates.k43(6.10e-03=_rates.k3total(2.03e-02±5.83e-05, t-value: 349)_*_rates.Tyield(3.00e-01, fixed)_)', ('s4', 's4'): 'rates.k44(1.00e-05, fixed)'}


## Megacomplex

- **mc1fast**
  - _Label_: mc1fast
  - _Dimension_: time
  - _Type_: decay
  - _K Matrix_: ['km1fast']

- **mc1slow**
  - _Label_: mc1slow
  - _Dimension_: time
  - _Type_: decay
  - _K Matrix_: ['km1slow']

- **artifact1**
  - _Label_: artifact1
  - _Dimension_: time
  - _Type_: coherent-artifact
  - _Order_: 3

- **mc2fast**
  - _Label_: mc2fast
  - _Dimension_: time
  - _Type_: decay
  - _K Matrix_: ['km2fast']

- **mc2slow**
  - _Label_: mc2slow
  - _Dimension_: time
  - _Type_: decay
  - _K Matrix_: ['km2slow']

- **artifact2**
  - _Label_: artifact2
  - _Dimension_: time
  - _Type_: coherent-artifact
  - _Order_: 3


## Initial Concentration

- **input1**
  - _Label_: input1
  - _Compartments_: ['c1', 'c2', 'c3', 'c4']
  - _Parameters_: ['input.1(1.00e+00, fixed)', 'input.0(0.00e+00, fixed)', 'input.0(0.00e+00, fixed)', 'input.0(0.00e+00, fixed)']
  - _Exclude From Normalize_: []

- **input2**
  - _Label_: input2
  - _Compartments_: ['s1', 's2', 's3', 's4']
  - _Parameters_: ['input.1(1.00e+00, fixed)', 'input.0(0.00e+00, fixed)', 'input.0(0.00e+00, fixed)', 'input.0(0.00e+00, fixed)']
  - _Exclude From Normalize_: []


## Irf

- **irf1**
  - _Label_: irf1
  - _Center_: ['irf.center1(1.22e+00±4.97e-04, t-value: 2451, initial: 1.21e+00)']
  - _Width_: ['irf.width1(5.18e-02±2.58e-04, t-value: 201, initial: 5.05e-02)']
  - _Normalize_: True
  - _Backsweep_: False
  - _Type_: spectral-multi-gaussian
  - _Dispersion Center_: irf.common_dispcenter(5.50e+02, fixed)
  - _Center Dispersion Coefficients_: ['irf.data1_disp1(-8.40e-01, fixed)', 'irf.data1_disp2(-3.55e-01, fixed)']
  - _Width Dispersion Coefficients_: []
  - _Model Dispersion With Wavenumber_: True

- **irf2**
  - _Label_: irf2
  - _Center_: ['irf.center2(6.89e-01±3.57e-04, t-value: 1927, initial: 6.90e-01)']
  - _Width_: ['irf.width2(5.98e-02±2.11e-04, t-value: 284, initial: 6.20e-02)']
  - _Normalize_: True
  - _Backsweep_: False
  - _Type_: spectral-multi-gaussian
  - _Dispersion Center_: irf.common_dispcenter(5.50e+02, fixed)
  - _Center Dispersion Coefficients_: ['irf.data1_disp1(-8.40e-01, fixed)', 'irf.data1_disp2(-3.55e-01, fixed)']
  - _Width Dispersion Coefficients_: []
  - _Model Dispersion With Wavenumber_: True


## Dataset

- **dataset1**
  - _Label_: dataset1
  - _Group_: default
  - _Force Index Dependent_: False
  - _Megacomplex_: ['mc1fast', 'mc1slow', 'artifact1']
  - _Megacomplex Scale_: ['mc_scale.1(-1.97e-01=1-_mc_scale.2(1.20e+00±2.01e-01, t-value: 5.9)_)', 'mc_scale.2(1.20e+00±2.01e-01, t-value: 5.9, initial: 9.10e-01)', 'input.1(1.00e+00, fixed)']
  - _Initial Concentration_: input1
  - _Irf_: irf1

- **dataset2**
  - _Label_: dataset2
  - _Group_: default
  - _Force Index Dependent_: False
  - _Megacomplex_: ['mc2fast', 'mc2slow', 'artifact2']
  - _Megacomplex Scale_: ['mc_scale.1(-1.97e-01=1-_mc_scale.2(1.20e+00±2.01e-01, t-value: 5.9)_)', 'mc_scale.2(1.20e+00±2.01e-01, t-value: 5.9, initial: 9.10e-01)', 'input.1(1.00e+00, fixed)']
  - _Initial Concentration_: input2
  - _Irf_: irf2


