| Optimization Result           |                                 |
|-------------------------------|---------------------------------|
| Number of residual evaluation | 4                               |
| Number of variables           | 17                              |
| Number of datapoints          | 91955                           |
| Degrees of freedom            | 91938                           |
| Chi Square                    | 1.47e-04                        |
| Reduced Chi Square            | 1.60e-09                        |
| Root Mean Square Error (RMSE) | 4.00e-05                        |
| RMSE additional penalty       | [3.30719558e-08 4.25250619e-08] |

| RMSE (per dataset)   |   weighted |   unweighted |
|----------------------|------------|--------------|
| 1.dataset1:          |   3.54e-05 |     3.54e-05 |
| 2.dataset2:          |   4.41e-05 |     4.41e-05 |
| 3.dataset3:          |   4.01e-05 |     4.01e-05 |

# Model

_Type_: kinetic-spectrum

## Initial Concentration

* **input1**:
  * *Label*: input1
  * *Compartments*: ['s1', 's2', 's3']
  * *Parameters*: [inputs.1: **5.00000e-01** *(fixed)*, inputs.2: **1.79632e-01** *(StdErr: 8e-07 ,initial: 1.80000e-01)*, inputs.3: **3.02972e-01** *(StdErr: 2e-07 ,initial: 3.03000e-01)*]
  * *Exclude From Normalize*: []
* **input2**:
  * *Label*: input2
  * *Compartments*: ['s1', 's2', 's3']
  * *Parameters*: [inputs.1: **5.00000e-01** *(fixed)*, inputs.7: **3.86863e-01** *(StdErr: 1e-06 ,initial: 3.87000e-01)*, inputs.8: **3.94087e-01** *(StdErr: 2e-07 ,initial: 3.94000e-01)*]
  * *Exclude From Normalize*: []
* **input3**:
  * *Label*: input3
  * *Compartments*: ['s1', 's2', 's3']
  * *Parameters*: [inputs.1: **5.00000e-01** *(fixed)*, inputs.9: **2.87686e-01** *(StdErr: 9e-07 ,initial: 2.88000e-01)*, inputs.10: **3.52197e-01** *(StdErr: 2e-07 ,initial: 3.52000e-01)*]
  * *Exclude From Normalize*: []

## K Matrix

* **km1**:
  * *Label*: km1
  * *Matrix*: 
    * *('s1', 's1')*: rates.k1: **4.99908e-02** *(StdErr: 2e-08 ,initial: 4.99000e-02)*
    * *('s2', 's2')*: rates.k2: **2.31059e+00** *(StdErr: 3e-07 ,initial: 2.31000e+00)*
    * *('s3', 's3')*: rates.k3: **5.09333e-01** *(StdErr: 2e-07 ,initial: 5.09000e-01)*
  

## Irf

* **irf1_with_dispersion** (spectral-multi-gaussian):
  * *Label*: irf1_with_dispersion
  * *Type*: spectral-multi-gaussian
  * *Center*: [irf.center1: **4.00005e-01** *(StdErr: 4e-09 ,initial: 4.00000e-01)*]
  * *Width*: [irf.width: **5.99808e-02** *(StdErr: 2e-09 ,initial: 5.99800e-02)*]
  * *Normalize*: True
  * *Backsweep*: False
  * *Dispersion Center*: irf.dispc: **5.00000e+02** *(fixed)*
  * *Center Dispersion*: [irf.disp1: **1.00000e-02** *(StdErr: 9e-09 ,initial: 1.00000e-02)*, irf.disp2: **1.00000e-03** *(StdErr: 1e-08 ,initial: 1.00000e-03)*]
  * *Width Dispersion*: []
  * *Model Dispersion With Wavenumber*: False
* **irf2_with_dispersion** (spectral-multi-gaussian):
  * *Label*: irf2_with_dispersion
  * *Type*: spectral-multi-gaussian
  * *Center*: [irf.center2: **4.10000e-01** *(StdErr: 4e-09 ,initial: 4.10000e-01)*]
  * *Width*: [irf.width: **5.99808e-02** *(StdErr: 2e-09 ,initial: 5.99800e-02)*]
  * *Normalize*: True
  * *Backsweep*: False
  * *Dispersion Center*: irf.dispc: **5.00000e+02** *(fixed)*
  * *Center Dispersion*: [irf.disp1: **1.00000e-02** *(StdErr: 9e-09 ,initial: 1.00000e-02)*, irf.disp2: **1.00000e-03** *(StdErr: 1e-08 ,initial: 1.00000e-03)*]
  * *Width Dispersion*: []
  * *Model Dispersion With Wavenumber*: False
* **irf3_with_dispersion** (spectral-multi-gaussian):
  * *Label*: irf3_with_dispersion
  * *Type*: spectral-multi-gaussian
  * *Center*: [irf.center3: **4.20000e-01** *(StdErr: 4e-09 ,initial: 4.20000e-01)*]
  * *Width*: [irf.width: **5.99808e-02** *(StdErr: 2e-09 ,initial: 5.99800e-02)*]
  * *Normalize*: True
  * *Backsweep*: False
  * *Dispersion Center*: irf.dispc: **5.00000e+02** *(fixed)*
  * *Center Dispersion*: [irf.disp1: **1.00000e-02** *(StdErr: 9e-09 ,initial: 1.00000e-02)*, irf.disp2: **1.00000e-03** *(StdErr: 1e-08 ,initial: 1.00000e-03)*]
  * *Width Dispersion*: []
  * *Model Dispersion With Wavenumber*: False

## Dataset

* **dataset1**:
  * *Label*: dataset1
  * *Megacomplex*: ['complex1']
  * *Scale*: scale.1: **1.00000e+00** *(fixed)*
  * *Initial Concentration*: input1
  * *Irf*: irf1_with_dispersion
* **dataset2**:
  * *Label*: dataset2
  * *Megacomplex*: ['complex1']
  * *Scale*: scale.2: **1.30557e+00** *(StdErr: 2e-07 ,initial: 1.30557e+00)*
  * *Initial Concentration*: input2
  * *Irf*: irf2_with_dispersion
* **dataset3**:
  * *Label*: dataset3
  * *Megacomplex*: ['complex1']
  * *Scale*: scale.3: **1.16354e+00** *(StdErr: 1e-07 ,initial: 1.16350e+00)*
  * *Initial Concentration*: input3
  * *Irf*: irf3_with_dispersion

## Megacomplex

* **complex1** (None):
  * *Label*: complex1
  * *K Matrix*: ['km1']

## Equal Area Penalties

* 
  * *Source*: s1
  * *Source Intervals*: [[300, 3000]]
  * *Target*: s2
  * *Target Intervals*: [[300, 3000]]
  * *Parameter*: area.1: **1.00000e+00** *(fixed)*
  * *Weight*: 0.1
* 
  * *Source*: s1
  * *Source Intervals*: [[300, 3000]]
  * *Target*: s3
  * *Target Intervals*: [[300, 3000]]
  * *Parameter*: area.1: **1.00000e+00** *(fixed)*
  * *Weight*: 0.1

