| Optimization Result           |          |
|-------------------------------|----------|
| Number of residual evaluation | 11       |
| Number of parameters          | 13       |
| Number of datapoints          | 141873   |
| Degrees of freedom            | 141860   |
| Chi Square                    | 1.40e+04 |
| Reduced Chi Square            | 9.87e-02 |
| Root Mean Square Error (RMSE) | 3.14e-01 |

| RMSE (per dataset)   |   weighted |   unweighted |
|----------------------|------------|--------------|
| 1.dataset1:          |   3.13e-01 |     5.69e-01 |
| 2.dataset2:          |   3.16e-01 |     5.79e-01 |

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
    * *Datasets*: ['dataset1', 'dataset2']
    * *Global Interval*: 
      * 280
      * 550
    * *Value*: 0.1
  
* 
    * *Datasets*: ['dataset1', 'dataset2']
    * *Global Interval*: 
      * 720
      * 890
    * *Value*: 0.2
  

## K Matrix

* **km1**:
    * *Label*: km1
    * *Matrix*: 
      * ('s2', 's1'): rates.k1(8.27e-01, fixed)
      * ('s3', 's1'): rates.k2(8.76e+00, fixed)
      * ('s4', 's2'): rates.k3(2.40e-01±3.03e-02, t-value: 7.9, initial: 4.84e-01)
      * ('s4', 's3'): rates.k4(4.47e-02±3.03e-03, t-value: 15, initial: 3.69e-02)
      * ('s4', 's4'): rates.k5(1.86e-02±1.52e-03, t-value: 12, initial: 1.93e-02)
      * ('s5', 's5'): rates.kC(9.90e+01, fixed)
  
* **km2**:
    * *Label*: km2
    * *Matrix*: 
      * ('s2', 's1'): rates.k1(8.27e-01, fixed)
      * ('s3', 's1'): rates.k2(8.76e+00, fixed)
      * ('s4', 's2'): rates.k3d2(3.82e+27±1.40e+07, t-value: 272559207423450152960, initial: 7.00e-01)
      * ('s4', 's3'): rates.k4d2(1.06e-01±3.65e-03, t-value: 29, initial: 8.50e-02)
      * ('s4', 's4'): rates.k5(1.86e-02±1.52e-03, t-value: 12, initial: 1.93e-02)
      * ('s6', 's6'): rates.kC(9.90e+01, fixed)
  

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
  
* **input2**:
    * *Label*: input2
    * *Compartments*: 
      * s1
      * s2
      * s3
      * s4
      * s6
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
      * irf.center(1.20e+00±1.12e-03, t-value: 1076, initial: 1.20e+00)
    * *Width*: 
      * irf.width(7.18e-02±2.54e-04, t-value: 282, initial: 5.84e-02)
    * *Normalize*: True
    * *Backsweep*: False
    * *Dispersion Center*: irf.dispc(5.50e+02, fixed)
    * *Center Dispersion Coefficients*: 
      * irf.disp1(2.67e-01±3.43e-03, t-value: 78, initial: 3.09e-01)
      * irf.disp2(-2.83e-02±4.57e-03, t-value: -6.2e+00, initial: -8.34e-02)
      * irf.disp3(-3.75e-03±1.89e-03, t-value: -2.0e+00, initial: 4.70e-03)
    * *Width Dispersion Coefficients*: 
    * *Model Dispersion With Wavenumber*: False
  
* **irf2** (spectral-multi-gaussian):
    * *Label*: irf2
    * *Type*: spectral-multi-gaussian
    * *Center*: 
      * irf2.center(6.69e-01±1.06e-03, t-value: 631, initial: 7.00e-01)
    * *Width*: 
      * irf.width(7.18e-02±2.54e-04, t-value: 282, initial: 5.84e-02)
    * *Normalize*: True
    * *Backsweep*: False
    * *Dispersion Center*: irf.dispc(5.50e+02, fixed)
    * *Center Dispersion Coefficients*: 
      * irf.disp1(2.67e-01±3.43e-03, t-value: 78, initial: 3.09e-01)
      * irf.disp2(-2.83e-02±4.57e-03, t-value: -6.2e+00, initial: -8.34e-02)
      * irf.disp3(-3.75e-03±1.89e-03, t-value: -2.0e+00, initial: 4.70e-03)
    * *Width Dispersion Coefficients*: 
    * *Model Dispersion With Wavenumber*: False
  

## Megacomplex

* **cmplx1** (None):
    * *Label*: cmplx1
    * *Dimension*: time
    * *K Matrix*: 
      * km1
  
* **cmplx2** (None):
    * *Label*: cmplx2
    * *Dimension*: time
    * *K Matrix*: 
      * km2
  

## Dataset

* **dataset1**:
    * *Label*: dataset1
    * *Group*: default
    * *Megacomplex*: 
      * cmplx1
    * *Scale*: scale.1(1.00e+00, fixed)
    * *Initial Concentration*: input1
    * *Irf*: irf1
  
* **dataset2**:
    * *Label*: dataset2
    * *Group*: default
    * *Megacomplex*: 
      * cmplx2
    * *Scale*: scale.2(1.26e+00±4.94e-04, t-value: 2550, initial: 1.30e+00)
    * *Initial Concentration*: input2
    * *Irf*: irf2
  

