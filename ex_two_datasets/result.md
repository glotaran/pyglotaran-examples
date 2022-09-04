| Optimization Result           |                                                    |
|-------------------------------|----------------------------------------------------|
| Number of residual evaluation | 18                                                 |
| Number of parameters          | 10                                                 |
| Number of datapoints          | 51104                                              |
| Degrees of freedom            | 51094                                              |
| Chi Square                    | 3.14e+02                                           |
| Reduced Chi Square            | 6.15e-03                                           |
| Root Mean Square Error (RMSE) | 7.84e-02                                           |
| RMSE additional penalty       | [[1.5393246485473355e-05, 2.1872520392207664e-06]] |

| RMSE (per dataset)   |   weighted |   unweighted |
|----------------------|------------|--------------|
| 1.dataset1:          |   6.75e-02 |     6.75e-02 |
| 2.dataset2:          |   8.79e-02 |     8.79e-02 |

# Model

_Megacomplex Types_: decay

## Dataset Groups

* **default**:
  * *Label*: default
  * *residual_function*: non_negative_least_squares
  * *link_clp*: None

## Clp Area Penalties

* 
    * *Source*: s1
    * *Source Intervals*: 
      * [300, 3000]
    * *Target*: s2
    * *Target Intervals*: 
      * [300, 3000]
    * *Parameter*: area.1(1.00e+00, fixed)
    * *Weight*: 0.1
  
* 
    * *Source*: s1
    * *Source Intervals*: 
      * [300, 3000]
    * *Target*: s3
    * *Target Intervals*: 
      * [300, 3000]
    * *Parameter*: area.1(1.00e+00, fixed)
    * *Weight*: 0.1
  

## K Matrix

* **km1**:
    * *Label*: km1
    * *Matrix*: 
      * ('s1', 's1'): rates.k1(2.50e-01±6.60e-04, t-value: 378, initial: 1.99e-01)
      * ('s2', 's2'): rates.k2(5.00e-01±1.93e-03, t-value: 259, initial: 5.00e-01)
      * ('s3', 's3'): rates.k3(1.00e+00±9.85e-04, t-value: 1015, initial: 1.10e+00)
  

## Initial Concentration

* **input1**:
    * *Label*: input1
    * *Compartments*: 
      * s1
      * s2
      * s3
    * *Parameters*: 
      * inputs.1(5.00e-01, fixed)
      * inputs.2(6.25e-01±1.96e-02, t-value: 32, initial: 2.51e-01)
      * inputs.3(6.44e-01±6.60e-03, t-value: 98, initial: 2.52e-01)
    * *Exclude From Normalize*: 
  
* **input2**:
    * *Label*: input2
    * *Compartments*: 
      * s1
      * s2
      * s3
    * *Parameters*: 
      * inputs.1(5.00e-01, fixed)
      * inputs.7(3.12e-01±1.81e-02, t-value: 17, initial: 2.10e-01)
      * inputs.8(1.61e-01±6.85e-03, t-value: 23, initial: 2.20e-01)
    * *Exclude From Normalize*: 
  

## Irf

* **irf1** (spectral-multi-gaussian):
    * *Label*: irf1
    * *Type*: spectral-multi-gaussian
    * *Center*: 
      * irf.center(4.00e-01±4.65e-06, t-value: 85952, initial: 5.00e-01)
    * *Width*: 
      * irf.width(6.00e-02±6.33e-06, t-value: 9481, initial: 1.00e-01)
    * *Normalize*: True
    * *Backsweep*: False
    * *Center Dispersion Coefficients*: 
    * *Width Dispersion Coefficients*: 
    * *Model Dispersion With Wavenumber*: False
  
* **irf1_no_dispersion** (spectral-multi-gaussian):
    * *Label*: irf1_no_dispersion
    * *Type*: spectral-multi-gaussian
    * *Center*: 
      * irf.center(4.00e-01±4.65e-06, t-value: 85952, initial: 5.00e-01)
    * *Width*: 
      * irf.width(6.00e-02±6.33e-06, t-value: 9481, initial: 1.00e-01)
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
    * *Scale*: scale.1(1.00e+00, fixed)
    * *Initial Concentration*: input1
    * *Irf*: irf1
  
* **dataset2**:
    * *Label*: dataset2
    * *Group*: default
    * *Megacomplex*: 
      * complex1
    * *Scale*: scale.2(1.10e+00±4.20e-04, t-value: 2621, initial: 1.20e+00)
    * *Initial Concentration*: input2
    * *Irf*: irf1
  

