| Optimization Result           |                                           |
|-------------------------------|-------------------------------------------|
| Number of residual evaluation | 6                                         |
| Number of parameters          | 8                                         |
| Number of datapoints          | 45229                                     |
| Degrees of freedom            | 45221                                     |
| Chi Square                    | 9.01e+07                                  |
| Reduced Chi Square            | 1.99e+03                                  |
| Root Mean Square Error (RMSE) | 4.46e+01                                  |
| RMSE additional penalty       | [[59.571331186128596, 44.56693972679381]] |

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
  - _Matrix_: {('s2', 's1'): 'kinetic.1(2.00e+00, fixed)', ('s5', 's1'): 'kinetic.2(1.00e-01, fixed)', ('s2', 's2'): 'kinetic.3(6.31e-02±2.85e-03, t-value: 22, initial: 6.00e-02)', ('s3', 's2'): 'kinetic.4(2.71e-02±1.25e-02, t-value: 2.2, initial: 2.70e-02)', ('s4', 's2'): 'kinetic.5(5.66e-02±1.29e-02, t-value: 4.4, initial: 5.60e-02)', ('s2', 's3'): 'kinetic.6(3.97e-02±6.22e-03, t-value: 6.4, initial: 3.90e-02)', ('s2', 's4'): 'kinetic.7(1.33e-01±8.41e-03, t-value: 16, initial: 1.33e-01)', ('s3', 's3'): 'kinetic.8(1.63e-04±6.11e-03, t-value: 2.7e-02, initial: 1.60e-04)', ('s4', 's4'): 'kinetic.8(1.63e-04±6.11e-03, t-value: 2.7e-02, initial: 1.60e-04)', ('s5', 's5'): 'kinetic.8(1.63e-04±6.11e-03, t-value: 2.7e-02, initial: 1.60e-04)'}


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
  - _Center_: irf.center(-8.43e+01±3.04e-03, t-value: -27711, initial: -8.40e+01)
  - _Width_: irf.width(1.55e+00±3.24e-03, t-value: 480, initial: 1.55e+00)


## Dataset

- **dataset1**
  - _Label_: dataset1
  - _Group_: default
  - _Force Index Dependent_: False
  - _Megacomplex_: ['mc1']
  - _Initial Concentration_: input1
  - _Irf_: irf1


