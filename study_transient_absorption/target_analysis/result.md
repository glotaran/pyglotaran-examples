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

_Megacomplex Types_: decay

## Dataset Groups

* **default**:
  * *Label*: default
  * *residual_function*: variable_projection
  * *link_clp*: None

## Clp Relations

* 
    * *Interval*: 
      * [0, 1000]
    * *Source*: s2
    * *Target*: s3
    * *Parameter*: rel.r1(1.00e+00, fixed)
  

## Weights

* 
    * *Datasets*: ['dataset1']
    * *Global Interval*: 
      * 280
      * 550
    * *Value*: 0.1
  
* 
    * *Datasets*: ['dataset1']
    * *Global Interval*: 
      * 720
      * 890
    * *Value*: 0.1
  

## K Matrix

* **km1**:
    * *Label*: km1
    * *Matrix*: 
      * ('s2', 's1'): rates.k1(1.52e+00=_b.1(1.60e-01±1.27e-02, t-value: 13)_ * _rates.k1sum(9.50e+00, fixed)_)
      * ('s3', 's1'): rates.k2(7.98e+00=_b.2(8.40e-01=1.0 - _b.1(1.60e-01±1.27e-02, t-value: 13)_)_ * _rates.k1sum(9.50e+00, fixed)_)
      * ('s4', 's2'): rates.k3(3.61e-01±2.57e-02, t-value: 14, initial: 4.84e-01)
      * ('s4', 's3'): rates.k4(3.99e-02±9.01e-03, t-value: 4.4, initial: 3.69e-02)
      * ('s4', 's4'): rates.k5(2.01e-02±3.98e-03, t-value: 5.0, initial: 1.93e-02)
      * ('s5', 's5'): rates.kC(9.90e+01, fixed)
  

## Initial Concentration

* **input1**:
    * *Label*: input1
    * *Compartments*: 
      * s1
      * s2
      * s3
      * s4
      * s5
    * *Parameters*: 
      * inputs.1(1.00e+00, fixed)
      * inputs.0(0.00e+00, fixed)
      * inputs.0(0.00e+00, fixed)
      * inputs.0(0.00e+00, fixed)
      * inputs.iC(1.00e+00, fixed)
    * *Exclude From Normalize*: 
  

## Irf

* **irf1** (spectral-multi-gaussian):
    * *Label*: irf1
    * *Type*: spectral-multi-gaussian
    * *Center*: 
      * irf.center(1.20e+00±7.74e-04, t-value: 1553, initial: 1.20e+00)
    * *Width*: 
      * irf.width(6.12e-02±2.41e-04, t-value: 254, initial: 5.84e-02)
    * *Normalize*: True
    * *Backsweep*: False
    * *Dispersion Center*: irf.dispc(5.50e+02, fixed)
    * *Center Dispersion Coefficients*: 
      * irf.disp1(2.89e-01±1.73e-03, t-value: 168, initial: 3.09e-01)
      * irf.disp2(-7.68e-02±1.38e-03, t-value: -5.6e+01, initial: -8.34e-02)
      * irf.disp3(9.89e-03±5.63e-04, t-value: 18, initial: 4.70e-03)
    * *Width Dispersion Coefficients*: 
    * *Model Dispersion With Wavenumber*: False
  

## Megacomplex

* **cmplx1** (None):
    * *Label*: cmplx1
    * *Dimension*: time
    * *K Matrix*: 
      * km1
  

## Dataset

* **dataset1**:
    * *Label*: dataset1
    * *Group*: default
    * *Megacomplex*: 
      * cmplx1
    * *Scale*: scale.1(1.00e+00, fixed)
    * *Initial Concentration*: input1
    * *Irf*: irf1
  

