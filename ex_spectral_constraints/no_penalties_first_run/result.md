| Optimization Result           |          |
|-------------------------------|----------|
| Number of residual evaluation | 5        |
| Number of parameters          | 4        |
| Number of datapoints          | 25551    |
| Degrees of freedom            | 25547    |
| Chi Square                    | 6.18e+01 |
| Reduced Chi Square            | 2.42e-03 |
| Root Mean Square Error (RMSE) | 4.92e-02 |

# Model

_Megacomplex Types_: decay

## Dataset Groups

* **default**:
  * *Label*: default
  * *residual_function*: variable_projection
  * *link_clp*: None

## K Matrix

* **km1**:
    * *Label*: km1
    * *Matrix*: 
      * ('s1', 's1'): rates.k1(2.50e-01±4.61e-05, t-value: 5421, initial: 2.00e-01)
      * ('s2', 's2'): rates.k2(1.00e+00±1.55e-04, t-value: 6450, initial: 1.10e+00)
  

## Initial Concentration

* **input1**:
    * *Label*: input1
    * *Compartments*: 
      * s1
      * s2
    * *Parameters*: 
      * inputs.s1(5.00e-01, fixed)
      * inputs.s2(5.00e-01, fixed)
    * *Exclude From Normalize*: 
  

## Irf

* **irf1** (spectral-multi-gaussian):
    * *Label*: irf1
    * *Type*: spectral-multi-gaussian
    * *Center*: 
      * irf.center(4.00e-01±5.60e-06, t-value: 71392, initial: 4.00e-01)
    * *Width*: 
      * irf.width(6.00e-02±7.53e-06, t-value: 7964, initial: 5.00e-02)
    * *Normalize*: True
    * *Backsweep*: False
    * *Center Dispersion Coefficients*: 
    * *Width Dispersion Coefficients*: 
    * *Model Dispersion With Wavenumber*: False
  

## Megacomplex

* **complex1** (None):
    * *Label*: complex1
    * *Dimension*: time
    * *K Matrix*: 
      * km1
  

## Dataset

* **dataset1**:
    * *Label*: dataset1
    * *Group*: default
    * *Megacomplex*: 
      * complex1
    * *Initial Concentration*: input1
    * *Irf*: irf1
  

