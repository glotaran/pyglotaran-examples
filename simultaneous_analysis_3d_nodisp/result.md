| Optimization Result           |                                                    |
|-------------------------------|----------------------------------------------------|
| Number of residual evaluation | 5                                                  |
| Number of parameters          | 13                                                 |
| Number of datapoints          | 91955                                              |
| Degrees of freedom            | 91942                                              |
| Chi Square                    | 6.78e+02                                           |
| Reduced Chi Square            | 7.37e-03                                           |
| Root Mean Square Error (RMSE) | 8.59e-02                                           |
| RMSE additional penalty       | [[1.0146291970158928e-06, 1.7906069842865692e-06]] |

| RMSE (per dataset)   |   weighted |   unweighted |
|----------------------|------------|--------------|
| 1.dataset1:          |   8.02e-02 |     8.92e-02 |
| 2.dataset2:          |   9.15e-02 |     1.02e-01 |
| 3.dataset3:          |   8.55e-02 |     9.51e-02 |

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
  

## Weights

* 
    * *Datasets*: ['dataset1', 'dataset2', 'dataset3']
    * *Global Interval*: 
      * 400
      * 450
    * *Value*: 0.5
  

## K Matrix

* **km1**:
    * *Label*: km1
    * *Matrix*: 
      * ('s1', 's1'): rates.k1(5.00e-02±6.98e-05, t-value: 716, initial: 5.00e-02)
      * ('s2', 's2'): rates.k2(2.00e+00±6.99e-04, t-value: 2858, initial: 2.00e+00)
      * ('s3', 's3'): rates.k3(5.00e-01±4.44e-04, t-value: 1125, initial: 5.00e-01)
  

## Initial Concentration

* **input1**:
    * *Label*: input1
    * *Compartments*: 
      * s1
      * s2
      * s3
    * *Parameters*: 
      * inputs.1(5.00e-01, fixed)
      * inputs.2(1.61e-01±8.34e-04, t-value: 193, initial: 1.61e-01)
      * inputs.3(3.11e-01±5.13e-04, t-value: 607, initial: 3.11e-01)
    * *Exclude From Normalize*: 
  
* **input2**:
    * *Label*: input2
    * *Compartments*: 
      * s1
      * s2
      * s3
    * *Parameters*: 
      * inputs.1(5.00e-01, fixed)
      * inputs.7(3.23e-01±5.42e-04, t-value: 595, initial: 3.22e-01)
      * inputs.8(4.15e-01±5.69e-04, t-value: 729, initial: 4.15e-01)
    * *Exclude From Normalize*: 
  
* **input3**:
    * *Label*: input3
    * *Compartments*: 
      * s1
      * s2
      * s3
    * *Parameters*: 
      * inputs.1(5.00e-01, fixed)
      * inputs.9(2.42e-01±6.29e-04, t-value: 385, initial: 2.42e-01)
      * inputs.10(3.63e-01±5.42e-04, t-value: 670, initial: 3.63e-01)
    * *Exclude From Normalize*: 
  

## Irf

* **irf1_no_dispersion** (spectral-multi-gaussian):
    * *Label*: irf1_no_dispersion
    * *Type*: spectral-multi-gaussian
    * *Center*: 
      * irf.center(4.00e-01±4.78e-06, t-value: 83619, initial: 4.00e-01)
    * *Width*: 
      * irf.width(6.00e-02±5.90e-06, t-value: 10166, initial: 6.00e-02)
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
    * *Irf*: irf1_no_dispersion
  
* **dataset2**:
    * *Label*: dataset2
    * *Group*: default
    * *Megacomplex*: 
      * complex1
    * *Scale*: scale.2(1.27e+00±7.94e-05, t-value: 16029, initial: 1.27e+00)
    * *Initial Concentration*: input2
    * *Irf*: irf1_no_dispersion
  
* **dataset3**:
    * *Label*: dataset3
    * *Group*: default
    * *Megacomplex*: 
      * complex1
    * *Scale*: scale.3(1.14e+00±5.63e-05, t-value: 20180, initial: 1.13e+00)
    * *Initial Concentration*: input3
    * *Irf*: irf1_no_dispersion
  

