| Optimization Result           |          |
|-------------------------------|----------|
| Number of residual evaluation | 1        |
| Number of parameters          | 4        |
| Number of datapoints          | 138301   |
| Degrees of freedom            | 138297   |
| Chi Square                    | 1.63e+04 |
| Reduced Chi Square            | 1.18e-01 |
| Root Mean Square Error (RMSE) | 3.43e-01 |

# Model

## Dataset Groups

- **default**
  - _Label_: default
  - _Residual Function_: variable_projection


## K Matrix

- **k1**
  - _Label_: k1
  - _Matrix_: {('hotS1', 'S2'): 'kinetic.1(5.97e+00, fixed)', ('S1', 'hotS1'): 'kinetic.2(2.64e+00, fixed)', ('S1', 'S1'): 'kinetic.3(1.11e-01, fixed)'}


## Megacomplex

- **doas**
  - _Label_: doas
  - _Dimension_: time
  - _Type_: damped-oscillation
  - _Labels_: ['osc1', 'osc2', 'osc3', 'osc4', 'osc5', 'osc6', 'osc7', 'osc8', 'osc9', 'osc10', 'osc11', 'osc12', 'osc13', 'osc14', 'osc15', 'osc16', 'osc17', 'osc18', 'osc19']
  - _Frequencies_: ['osc.freq.1(1.52e+03, fixed)', 'osc.freq.2(1.19e+03, fixed)', 'osc.freq.3(1.16e+03, fixed)', 'osc.freq.4(1.00e+03, fixed)', 'osc.freq.5(9.83e+02, fixed)', 'osc.freq.6(8.04e+02, fixed)', 'osc.freq.7(7.22e+02, fixed)', 'osc.freq.8(5.00e+02, fixed)', 'osc.freq.9(3.98e+02, fixed)', 'osc.freq.10(2.94e+02, fixed)', 'osc.freq.11(2.52e+02, fixed)', 'osc.freq.12(9.73e+01, fixed)', 'osc.freq.13(3.45e+01, fixed)', 'osc.freq.14(6.30e+02, fixed)', 'osc.freq.15(1.44e+03, fixed)', 'osc.freq.16(2.45e+03, fixed)', 'osc.freq.17(1.44e+03, fixed)', 'osc.freq.18(1.45e+03, fixed)', 'osc.freq.19(1.40e+03, fixed)']
  - _Rates_: ['osc.rates.1(1.54e+00, fixed)', 'osc.rates.2(2.81e+00, fixed)', 'osc.rates.3(1.07e+00, fixed)', 'osc.rates.4(1.66e+00, fixed)', 'osc.rates.5(5.95e+00, fixed)', 'osc.rates.6(2.00e-01, fixed)', 'osc.rates.7(2.05e-01, fixed)', 'osc.rates.8(8.87e-01, fixed)', 'osc.rates.9(8.01e-01, fixed)', 'osc.rates.10(1.83e+00, fixed)', 'osc.rates.11(1.09e+00, fixed)', 'osc.rates.12(3.18e-01, fixed)', 'osc.rates.13(2.03e+00, fixed)', 'osc.rates.14(2.00e+01, fixed)', 'osc.rates.15(-7.98e+00, fixed)', 'osc.rates.16(-8.30e+00, fixed)', 'osc.rates.17(-6.17e+00, fixed)', 'osc.rates.18(-7.08e+00, fixed)', 'osc.rates.19(-8.00e+00, fixed)']

- **decay**
  - _Label_: decay
  - _Dimension_: time
  - _Type_: decay
  - _K Matrix_: ['k1']

- **artifact**
  - _Label_: artifact
  - _Dimension_: time
  - _Type_: coherent-artifact
  - _Order_: 3
  - _Width_: artifact.CAwidth(1.88e-02±6.70e-04, t-value: 28, initial: 1.88e-02)


## Initial Concentration

- **j1**
  - _Label_: j1
  - _Compartments_: ['S2', 'hotS1', 'S1']
  - _Parameters_: ['j.1(1.00e+00, fixed)', 'j.0(0.00e+00, fixed)', 'j.0(0.00e+00, fixed)']
  - _Exclude From Normalize_: []


## Irf

- **irf1**
  - _Label_: irf1
  - _Normalize_: True
  - _Backsweep_: False
  - _Dispersion Center_: irf.dispcenter(6.00e+02, fixed)
  - _Center Dispersion Coefficients_: ['irf.disp1(-2.11e-02±8.29e-05, t-value: -255, initial: -2.11e-02)', 'irf.disp2(1.07e-02±4.48e-04, t-value: 24, initial: 1.07e-02)']
  - _Width Dispersion Coefficients_: []
  - _Model Dispersion With Wavenumber_: True
  - _Type_: spectral-gaussian
  - _Center_: irf.center(1.27e-02±1.58e-05, t-value: 807, initial: 1.27e-02)
  - _Width_: irf.width(6.00e-03, fixed)


## Dataset

- **dataset1**
  - _Label_: dataset1
  - _Group_: default
  - _Force Index Dependent_: False
  - _Megacomplex_: ['doas', 'decay', 'artifact']
  - _Initial Concentration_: j1
  - _Irf_: irf1


