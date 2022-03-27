| Optimization Result           |                       |
|-------------------------------|-----------------------|
| Number of residual evaluation | 23                    |
| Number of variables           | 6                     |
| Number of datapoints          | 11265                 |
| Degrees of freedom            | 11259                 |
| Chi Square                    | 9.81e+06              |
| Reduced Chi Square            | 8.71e+02              |
| Root Mean Square Error (RMSE) | 2.95e+01              |
| RMSE additional penalty       | [array([8.60398997])] |

| RMSE (per dataset)   |   weighted |   unweighted |
|----------------------|------------|--------------|
| 1.dataset1:          |   3.00e+01 |     3.00e+01 |
| 2.dataset2:          |   5.71e-04 |     5.71e-04 |

# Model

_Megacomplex Types_: decay

## Dataset Groups

* **default**:
  * *Label*: default
  * *residual_function*: non_negative_least_squares
  * *link_clp*: None

## Clp Area Penalties

* 
    * *Source*: s2
    * *Source Intervals*: 
      * [0, 1000]
    * *Target*: s1
    * *Target Intervals*: 
      * [0, 1000]
    * *Parameter*: area.1(3.46e+00, fixed)
    * *Weight*: 1e-06
  

## Clp Relations

* 
    * *Interval*: 
      * [0, 1000]
    * *Source*: s1
    * *Target*: s4
    * *Parameter*: rel.r1(1.00e+00, fixed)
  
* 
    * *Interval*: 
      * [0, 1000]
    * *Source*: s3
    * *Target*: s6
    * *Parameter*: rel.r1(1.00e+00, fixed)
  

## K Matrix

* **km1**:
    * *Label*: km1
    * *Matrix*: 
      * ('s1', 's4'): rates.k1(2.50e-01±2.97e-01, initial: 2.10e-01)
      * ('s3', 's1'): rates.k2(1.57e-01±9.12e-02, initial: 1.96e-01)
      * ('s2', 's1'): rates.k3(8.70e-02, fixed)
      * ('s5', 's2'): rates.k4(2.49e-01±3.31e-01, initial: 2.67e-01)
      * ('s6', 's3'): rates.k5(6.44e-03±1.57e+00, initial: 6.40e-03)
      * ('s6', 's6'): rates.k6(1.34e-06±4.00e-01, initial: 1.30e-06)
      * ('s5', 's5'): rates.k6(1.34e-06±4.00e-01, initial: 1.30e-06)
  
* **km2**:
    * *Label*: km2
    * *Matrix*: 
      * ('s5', 's5'): rates.k6(1.34e-06±4.00e-01, initial: 1.30e-06)
  

## Initial Concentration

* **input1**:
    * *Label*: input1
    * *Compartments*: 
      * s1
      * s2
      * s3
      * s4
      * s5
      * s6
    * *Parameters*: 
      * inputs.s1(0.00e+00, fixed)
      * inputs.s1(0.00e+00, fixed)
      * inputs.s1(0.00e+00, fixed)
      * inputs.s2(1.00e+00, fixed)
      * inputs.s1(0.00e+00, fixed)
      * inputs.s1(0.00e+00, fixed)
    * *Exclude From Normalize*: 
  
* **input2**:
    * *Label*: input2
    * *Compartments*: 
      * s5
    * *Parameters*: 
      * inputs.s2(1.00e+00, fixed)
    * *Exclude From Normalize*: 
  

## Irf

* **irf1** (spectral-multi-gaussian):
    * *Label*: irf1
    * *Type*: spectral-multi-gaussian
    * *Center*: 
      * irf.center(-1.00e-03, fixed)
    * *Width*: 
      * irf.width(4.15e-04, fixed)
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
  
* **complex2** (None):
    * *Label*: complex2
    * *Dimension*: time
    * *K Matrix*: 
      * km2
  

## Dataset

* **dataset1**:
    * *Label*: dataset1
    * *Group*: default
    * *Megacomplex*: 
      * complex1
    * *Scale*: scale.1(1.00e+00, fixed)
    * *Initial Concentration*: input1
    * *Irf*: irf1
  
* **dataset2**:
    * *Label*: dataset2
    * *Group*: default
    * *Megacomplex*: 
      * complex2
    * *Scale*: scale.2(8.53e-01±1.63e+00, initial: 8.62e-01)
    * *Initial Concentration*: input2
  

