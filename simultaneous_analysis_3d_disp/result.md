| Optimization Result           |                                           |
|-------------------------------|-------------------------------------------|
| Number of residual evaluation | 4                                         |
| Number of variables           | 17                                        |
| Number of datapoints          | 91955                                     |
| Degrees of freedom            | 91938                                     |
| Chi Square                    | 1.47e-04                                  |
| Reduced Chi Square            | 1.60e-09                                  |
| Root Mean Square Error (RMSE) | 4.00e-05                                  |
| RMSE additional penalty       | [array([3.31503543e-08, 4.25307007e-08])] |

| RMSE (per dataset)   |   weighted |   unweighted |
|----------------------|------------|--------------|
| 1.dataset1:          |   3.54e-05 |     3.54e-05 |
| 2.dataset2:          |   4.41e-05 |     4.41e-05 |
| 3.dataset3:          |   4.01e-05 |     4.01e-05 |

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
      * ('s1', 's1'): rates.k1(5.00e-02±2.37e-08, initial: 4.99e-02)
      * ('s2', 's2'): rates.k2(2.31e+00±3.14e-07, initial: 2.31e+00)
      * ('s3', 's3'): rates.k3(5.09e-01±2.01e-07, initial: 5.09e-01)
  

## Initial Concentration

* **input1**:
    * *Label*: input1
    * *Compartments*: 
      * s1
      * s2
      * s3
    * *Parameters*: 
      * inputs.1(5.00e-01, fixed)
      * inputs.2(1.80e-01±8.29e-07, initial: 1.80e-01)
      * inputs.3(3.03e-01±1.82e-07, initial: 3.03e-01)
    * *Exclude From Normalize*: 
  
* **input2**:
    * *Label*: input2
    * *Compartments*: 
      * s1
      * s2
      * s3
    * *Parameters*: 
      * inputs.1(5.00e-01, fixed)
      * inputs.7(3.87e-01±9.60e-07, initial: 3.87e-01)
      * inputs.8(3.94e-01±2.05e-07, initial: 3.94e-01)
    * *Exclude From Normalize*: 
  
* **input3**:
    * *Label*: input3
    * *Compartments*: 
      * s1
      * s2
      * s3
    * *Parameters*: 
      * inputs.1(5.00e-01, fixed)
      * inputs.9(2.88e-01±9.23e-07, initial: 2.88e-01)
      * inputs.10(3.52e-01±1.92e-07, initial: 3.52e-01)
    * *Exclude From Normalize*: 
  

## Irf

* **irf1_with_dispersion** (spectral-multi-gaussian):
    * *Label*: irf1_with_dispersion
    * *Type*: spectral-multi-gaussian
    * *Center*: 
      * irf.center1(4.00e-01±3.93e-09, initial: 4.00e-01)
    * *Width*: 
      * irf.width(6.00e-02±2.41e-09, initial: 6.00e-02)
    * *Normalize*: True
    * *Backsweep*: False
    * *Dispersion Center*: irf.dispc(5.00e+02, fixed)
    * *Center Dispersion Coefficients*: 
      * irf.disp1(1.00e-02±9.02e-09, initial: 1.00e-02)
      * irf.disp2(1.00e-03±1.36e-08, initial: 1.00e-03)
    * *Width Dispersion Coefficients*: 
    * *Model Dispersion With Wavenumber*: False
  
* **irf2_with_dispersion** (spectral-multi-gaussian):
    * *Label*: irf2_with_dispersion
    * *Type*: spectral-multi-gaussian
    * *Center*: 
      * irf.center2(4.10e-01±3.56e-09, initial: 4.10e-01)
    * *Width*: 
      * irf.width(6.00e-02±2.41e-09, initial: 6.00e-02)
    * *Normalize*: True
    * *Backsweep*: False
    * *Dispersion Center*: irf.dispc(5.00e+02, fixed)
    * *Center Dispersion Coefficients*: 
      * irf.disp1(1.00e-02±9.02e-09, initial: 1.00e-02)
      * irf.disp2(1.00e-03±1.36e-08, initial: 1.00e-03)
    * *Width Dispersion Coefficients*: 
    * *Model Dispersion With Wavenumber*: False
  
* **irf3_with_dispersion** (spectral-multi-gaussian):
    * *Label*: irf3_with_dispersion
    * *Type*: spectral-multi-gaussian
    * *Center*: 
      * irf.center3(4.20e-01±3.65e-09, initial: 4.20e-01)
    * *Width*: 
      * irf.width(6.00e-02±2.41e-09, initial: 6.00e-02)
    * *Normalize*: True
    * *Backsweep*: False
    * *Dispersion Center*: irf.dispc(5.00e+02, fixed)
    * *Center Dispersion Coefficients*: 
      * irf.disp1(1.00e-02±9.02e-09, initial: 1.00e-02)
      * irf.disp2(1.00e-03±1.36e-08, initial: 1.00e-03)
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
    * *Irf*: irf1_with_dispersion
  
* **dataset2**:
    * *Label*: dataset2
    * *Group*: default
    * *Megacomplex*: 
      * complex1
    * *Scale*: scale.2(1.31e+00±1.90e-07, initial: 1.31e+00)
    * *Initial Concentration*: input2
    * *Irf*: irf2_with_dispersion
  
* **dataset3**:
    * *Label*: dataset3
    * *Group*: default
    * *Megacomplex*: 
      * complex1
    * *Scale*: scale.3(1.16e+00±1.02e-07, initial: 1.16e+00)
    * *Initial Concentration*: input3
    * *Irf*: irf3_with_dispersion
  

