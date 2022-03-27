| Optimization Result           |                                           |
|-------------------------------|-------------------------------------------|
| Number of residual evaluation | 8                                         |
| Number of variables           | 17                                        |
| Number of datapoints          | 92556                                     |
| Degrees of freedom            | 92539                                     |
| Chi Square                    | 1.49e-04                                  |
| Reduced Chi Square            | 1.61e-09                                  |
| Root Mean Square Error (RMSE) | 4.01e-05                                  |
| RMSE additional penalty       | [array([1.29621185e-10, 4.17240735e-07])] |

| RMSE (per dataset)   |   weighted |   unweighted |
|----------------------|------------|--------------|
| 1.dataset1:          |   3.64e-05 |     3.64e-05 |
| 2.dataset2:          |   3.51e-05 |     3.51e-05 |
| 3.dataset3:          |   5.79e-05 |     5.79e-05 |
| 4.dataset4:          |   2.34e-05 |     2.34e-05 |
| 5.dataset5:          |   4.61e-05 |     4.61e-05 |
| 6.dataset6:          |   9.00e-06 |     9.00e-06 |

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
    * *Weight*: 0.01
  
* 
    * *Source*: s1
    * *Source Intervals*: 
      * [300, 3000]
    * *Target*: s3
    * *Target Intervals*: 
      * [300, 3000]
    * *Parameter*: area.1(1.00e+00, fixed)
    * *Weight*: 0.01
  

## K Matrix

* **km1**:
    * *Label*: km1
    * *Matrix*: 
      * ('s1', 's1'): rates.k1(5.00e-02±2.37e-08, initial: 5.00e-02)
      * ('s2', 's2'): rates.k2(5.09e-01±2.00e-07, initial: 5.00e-01)
      * ('s3', 's3'): rates.k3(2.31e+00±3.11e-07, initial: 2.00e+00)
  

## Initial Concentration

* **input1**:
    * *Label*: input1
    * *Compartments*: 
      * s1
      * s2
      * s3
    * *Parameters*: 
      * inputs.1(5.00e-01, fixed)
      * inputs.2(3.06e-01±3.90e-07, initial: 5.10e-02)
      * inputs.3(1.81e-01±8.18e-07, initial: 2.52e-01)
    * *Exclude From Normalize*: 
  
* **input2**:
    * *Label*: input2
    * *Compartments*: 
      * s1
      * s2
      * s3
    * *Parameters*: 
      * inputs.1(5.00e-01, fixed)
      * inputs.7(3.97e-01±4.01e-07, initial: 5.21e-02)
      * inputs.8(3.90e-01±7.28e-07, initial: 2.20e-01)
    * *Exclude From Normalize*: 
  
* **input3**:
    * *Label*: input3
    * *Compartments*: 
      * s1
      * s2
      * s3
    * *Parameters*: 
      * inputs.1(5.00e-01, fixed)
      * inputs.9(3.55e-01±3.94e-07, initial: 5.22e-02)
      * inputs.10(2.90e-01±7.50e-07, initial: 2.20e-01)
    * *Exclude From Normalize*: 
  

## Irf

* **irf1_with_dispersion** (spectral-multi-gaussian):
    * *Label*: irf1_with_dispersion
    * *Type*: spectral-multi-gaussian
    * *Center*: 
      * irf.center1(4.00e-01±3.92e-09, initial: 4.00e-01)
    * *Width*: 
      * irf.width(6.00e-02±2.40e-09, initial: 6.00e-02)
    * *Normalize*: True
    * *Backsweep*: False
    * *Dispersion Center*: irf.dispc(5.00e+02, fixed)
    * *Center Dispersion Coefficients*: 
      * irf.disp1(1.00e-02±9.01e-09, initial: 1.00e-02)
      * irf.disp2(1.00e-03±1.36e-08, initial: 1.00e-03)
    * *Width Dispersion Coefficients*: 
    * *Model Dispersion With Wavenumber*: False
  
* **irf2_with_dispersion** (spectral-multi-gaussian):
    * *Label*: irf2_with_dispersion
    * *Type*: spectral-multi-gaussian
    * *Center*: 
      * irf.center2(4.10e-01±3.50e-09, initial: 4.00e-01)
    * *Width*: 
      * irf.width(6.00e-02±2.40e-09, initial: 6.00e-02)
    * *Normalize*: True
    * *Backsweep*: False
    * *Dispersion Center*: irf.dispc(5.00e+02, fixed)
    * *Center Dispersion Coefficients*: 
      * irf.disp1(1.00e-02±9.01e-09, initial: 1.00e-02)
      * irf.disp2(1.00e-03±1.36e-08, initial: 1.00e-03)
    * *Width Dispersion Coefficients*: 
    * *Model Dispersion With Wavenumber*: False
  
* **irf3_with_dispersion** (spectral-multi-gaussian):
    * *Label*: irf3_with_dispersion
    * *Type*: spectral-multi-gaussian
    * *Center*: 
      * irf.center3(4.20e-01±3.64e-09, initial: 4.00e-01)
    * *Width*: 
      * irf.width(6.00e-02±2.40e-09, initial: 6.00e-02)
    * *Normalize*: True
    * *Backsweep*: False
    * *Dispersion Center*: irf.dispc(5.00e+02, fixed)
    * *Center Dispersion Coefficients*: 
      * irf.disp1(1.00e-02±9.01e-09, initial: 1.00e-02)
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
    * *Scale*: scale.1(1.00e+00, fixed)
    * *Initial Concentration*: input1
    * *Irf*: irf1_with_dispersion
  
* **dataset3**:
    * *Label*: dataset3
    * *Group*: default
    * *Megacomplex*: 
      * complex1
    * *Scale*: scale.2(1.31e+00±1.04e-07, initial: 1.30e+00)
    * *Initial Concentration*: input2
    * *Irf*: irf2_with_dispersion
  
* **dataset4**:
    * *Label*: dataset4
    * *Group*: default
    * *Megacomplex*: 
      * complex1
    * *Scale*: scale.2(1.31e+00±1.04e-07, initial: 1.30e+00)
    * *Initial Concentration*: input2
    * *Irf*: irf2_with_dispersion
  
* **dataset5**:
    * *Label*: dataset5
    * *Group*: default
    * *Megacomplex*: 
      * complex1
    * *Scale*: scale.3(1.16e+00±5.78e-08, initial: 1.10e+00)
    * *Initial Concentration*: input3
    * *Irf*: irf3_with_dispersion
  
* **dataset6**:
    * *Label*: dataset6
    * *Group*: default
    * *Megacomplex*: 
      * complex1
    * *Scale*: scale.3(1.16e+00±5.78e-08, initial: 1.10e+00)
    * *Initial Concentration*: input3
    * *Irf*: irf3_with_dispersion
  

