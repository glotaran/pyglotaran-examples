| Optimization Result                       |                                                                  |
|-------------------------------------------|------------------------------------------------------------------|
| Number of residual evaluation             | 6                                                                |
| Number of residuals                       | 45229                                                            |
| Number of free parameters                 | 8                                                                |
| Number of conditionally linear parameters | 161                                                              |
| Degrees of freedom                        | 45060                                                            |
| Chi Square                                | 9.01e+07                                                         |
| Reduced Chi Square                        | 2.00e+03                                                         |
| Root Mean Square Error (RMSE)             | 4.47e+01                                                         |
| RMSE additional penalty                   | [[np.float64(59.57133108911831), np.float64(44.56694180032681)]] |

# Model

## Clp Penalties

- **&nbsp;**
  - _Type_: equal_area
  - _Source_: s2
  - _Source Intervals_: [[100, 1000]]
  - _Target_: s3
  - _Target Intervals_: [[100, 1000]]
  - _Parameter_: area.1(1.00e+00, fixed)
  - _Weight_: 0.0016

- **&nbsp;**
  - _Type_: equal_area
  - _Source_: s2
  - _Source Intervals_: [[100, 1000]]
  - _Target_: s4
  - _Target Intervals_: [[100, 1000]]
  - _Parameter_: area.1(1.00e+00, fixed)
  - _Weight_: 0.0016


## Clp Constraints

- **&nbsp;**
  - _Interval_: [[1, 1000]]
  - _Target_: s1
  - _Type_: zero

- **&nbsp;**
  - _Interval_: [[1, 680]]
  - _Target_: s3
  - _Type_: zero

- **&nbsp;**
  - _Interval_: [[1, 690]]
  - _Target_: s4
  - _Type_: zero


## Dataset Groups

- **default**
  - _Label_: default
  - _Residual Function_: non_negative_least_squares


## K Matrix

- **km1**
  - _Label_: km1
  - _Matrix_: {('s2', 's1'): 'kinetic.1(2.00e+00, fixed)', ('s5', 's1'): 'kinetic.2(1.00e-01, fixed)', ('s2', 's2'): 'kinetic.3(6.31e-02±1.80e-04, t-value: 350, initial: 6.00e-02)', ('s3', 's2'): 'kinetic.4(2.71e-02±3.41e-04, t-value: 80, initial: 2.70e-02)', ('s4', 's2'): 'kinetic.5(5.66e-02±7.38e-04, t-value: 77, initial: 5.60e-02)', ('s2', 's3'): 'kinetic.6(3.97e-02±2.48e-04, t-value: 160, initial: 3.90e-02)', ('s2', 's4'): 'kinetic.7(1.33e-01±1.13e-03, t-value: 118, initial: 1.33e-01)', ('s3', 's3'): 'kinetic.8(1.63e-04±1.00e-06, t-value: 163, initial: 1.60e-04)', ('s4', 's4'): 'kinetic.8(1.63e-04±1.00e-06, t-value: 163, initial: 1.60e-04)', ('s5', 's5'): 'kinetic.8(1.63e-04±1.00e-06, t-value: 163, initial: 1.60e-04)'}


## Megacomplex

- **mc1**
  - _Label_: mc1
  - _Dimension_: time
  - _Type_: decay
  - _K Matrix_: ['km1']


## Initial Concentration

- **input1**
  - _Label_: input1
  - _Compartments_: ['s1', 's2', 's3', 's4', 's5']
  - _Parameters_: ['input.1(1.00e+00, fixed)', 'input.0(0.00e+00, fixed)', 'input.0(0.00e+00, fixed)', 'input.0(0.00e+00, fixed)', 'input.0(0.00e+00, fixed)']
  - _Exclude From Normalize_: []


## Irf

- **irf1**
  - _Label_: irf1
  - _Normalize_: True
  - _Backsweep_: True
  - _Backsweep Period_: irf.backsweep(1.32e+04, fixed)
  - _Type_: gaussian
  - _Center_: irf.center(-8.43e+01±3.05e-03, t-value: -27662, initial: -8.40e+01)
  - _Width_: irf.width(1.55e+00±3.24e-03, t-value: 479, initial: 1.55e+00)


## Dataset

- **dataset1**
  - _Label_: dataset1
  - _Group_: default
  - _Force Index Dependent_: False
  - _Megacomplex_: ['mc1']
  - _Initial Concentration_: input1
  - _Irf_: irf1


