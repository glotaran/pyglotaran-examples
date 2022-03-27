| Optimization Result           |                                           |
|-------------------------------|-------------------------------------------|
| Number of residual evaluation | 103                                       |
| Number of variables           | 16                                        |
| Number of datapoints          | 91955                                     |
| Degrees of freedom            | 91939                                     |
| Chi Square                    | 5.03e+03                                  |
| Reduced Chi Square            | 5.47e-02                                  |
| Root Mean Square Error (RMSE) | 2.34e-01                                  |
| RMSE additional penalty       | [array([8.24456947e-09, 1.79876224e-08])] |

| RMSE (per dataset)   |   weighted |   unweighted |
|----------------------|------------|--------------|
| 1.dataset1:          |   2.54e-01 |     2.54e-01 |
| 2.dataset2:          |   2.38e-01 |     4.76e-01 |
| 3.dataset3:          |   2.08e-01 |     8.30e+01 |

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
    * *Datasets*: ['dataset2']
    * *Global Interval*: 
      * 400
      * 600
    * *Value*: 0.5
  
* 
    * *Datasets*: ['dataset3']
    * *Global Interval*: 
      * 400
      * 600
    * *Value*: 0.0025
  

## K Matrix

* **km1**:
    * *Label*: km1
    * *Matrix*: 
      * ('s1', 's1'): rates.k1(5.00e-02±2.14e-04, initial: 5.00e-02)
      * ('s2', 's2'): rates.k2(1.99e+00±3.31e-03, initial: 1.99e+00)
      * ('s3', 's3'): rates.k3(4.99e-01±1.84e-03, initial: 4.99e-01)
  

## Initial Concentration

* **input1**:
    * *Label*: input1
    * *Compartments*: 
      * s1
      * s2
      * s3
    * *Parameters*: 
      * inputs.1(5.00e-01, fixed)
      * inputs.2(2.42e-01±1.39e+01, initial: 2.42e-01)
      * inputs.3(3.63e-01±2.26e+01, initial: 3.63e-01)
    * *Exclude From Normalize*: 
  
* **input2**:
    * *Label*: input2
    * *Compartments*: 
      * s1
      * s2
      * s3
    * *Parameters*: 
      * inputs.1(5.00e-01, fixed)
      * inputs.7(1.61e-01±1.39e+01, initial: 1.61e-01)
      * inputs.8(3.12e-01±2.26e+01, initial: 3.12e-01)
    * *Exclude From Normalize*: 
  
* **input3**:
    * *Label*: input3
    * *Compartments*: 
      * s1
      * s2
      * s3
    * *Parameters*: 
      * inputs.1(5.00e-01, fixed)
      * inputs.9(9.63e-02±1.39e+01, initial: 9.62e-02)
      * inputs.10(2.08e-01±2.26e+01, initial: 2.08e-01)
    * *Exclude From Normalize*: 
  

## Irf

* **irf1_no_dispersion** (spectral-multi-gaussian):
    * *Label*: irf1_no_dispersion
    * *Type*: spectral-multi-gaussian
    * *Center*: 
      * irf.center1(5.00e-01±4.06e-05, initial: 5.00e-01)
    * *Width*: 
      * irf.width1(6.00e-02±3.81e-04, initial: 6.00e-02)
    * *Normalize*: True
    * *Backsweep*: False
    * *Center Dispersion Coefficients*: 
    * *Width Dispersion Coefficients*: 
    * *Model Dispersion With Wavenumber*: False
  
* **irf2_no_dispersion** (spectral-multi-gaussian):
    * *Label*: irf2_no_dispersion
    * *Type*: spectral-multi-gaussian
    * *Center*: 
      * irf.center2(4.00e-01±9.08e-05, initial: 4.00e-01)
    * *Width*: 
      * irf.width1(6.00e-02±3.81e-04, initial: 6.00e-02)
    * *Normalize*: True
    * *Backsweep*: False
    * *Center Dispersion Coefficients*: 
    * *Width Dispersion Coefficients*: 
    * *Model Dispersion With Wavenumber*: False
  
* **irf3_no_dispersion** (spectral-multi-gaussian):
    * *Label*: irf3_no_dispersion
    * *Type*: spectral-multi-gaussian
    * *Center*: 
      * irf.center3(4.50e-01±2.80e-04, initial: 3.00e-01)
    * *Width*: 
      * irf.width2(1.20e-01±1.42e-03, initial: 8.99e-02)
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
    * *Scale*: scale.2(8.80e-01±7.22e-01, initial: 8.80e-01)
    * *Initial Concentration*: input2
    * *Irf*: irf2_no_dispersion
  
* **dataset3**:
    * *Label*: dataset3
    * *Group*: default
    * *Megacomplex*: 
      * complex1
    * *Scale*: scale.3(7.27e+01±1.86e+00, initial: 7.27e+01)
    * *Initial Concentration*: input3
    * *Irf*: irf3_no_dispersion
  

