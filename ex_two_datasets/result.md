| Optimization Result           |                                 |
|-------------------------------|---------------------------------|
| Number of residual evaluation | 13                              |
| Number of variables           | 10                              |
| Number of datapoints          | 51104                           |
| Degrees of freedom            | 51094                           |
| Chi Square                    | 3.14e+02                        |
| Reduced Chi Square            | 6.15e-03                        |
| Root Mean Square Error (RMSE) | 7.84e-02                        |
| RMSE additional penalty       | [8.03437706e-07 4.77945741e-07] |

| RMSE (per dataset)   |   weighted |   unweighted |
|----------------------|------------|--------------|
| 1.dataset1:          |   6.75e-02 |     6.75e-02 |
| 2.dataset2:          |   8.79e-02 |     8.79e-02 |

# Model

_Type_: kinetic-spectrum

## Initial Concentration

* **input1**:
  * *Label*: input1
  * *Compartments*: ['s1', 's2', 's3']
  * *Parameters*: [inputs.1: **5.00000e-01** *(fixed)*, inputs.2: **6.25101e-01** *(StdErr: 2e-02 ,initial: 2.51000e-01)*, inputs.3: **6.44003e-01** *(StdErr: 6e-03 ,initial: 2.52000e-01)*]
  * *Exclude From Normalize*: []
* **input2**:
  * *Label*: input2
  * *Compartments*: ['s1', 's2', 's3']
  * *Parameters*: [inputs.1: **5.00000e-01** *(fixed)*, inputs.7: **3.12492e-01** *(StdErr: 2e-02 ,initial: 2.10000e-01)*, inputs.8: **1.60788e-01** *(StdErr: 6e-03 ,initial: 2.20000e-01)*]
  * *Exclude From Normalize*: []

## K Matrix

* **km1**:
  * *Label*: km1
  * *Matrix*: 
    * *('s1', 's1')*: rates.k1: **2.49920e-01** *(StdErr: 7e-04 ,initial: 1.99000e-01)*
    * *('s2', 's2')*: rates.k2: **5.00182e-01** *(StdErr: 2e-03 ,initial: 5.00000e-01)*
    * *('s3', 's3')*: rates.k3: **1.00046e+00** *(StdErr: 1e-03 ,initial: 1.10000e+00)*
  

## Irf

* **irf1** (spectral-multi-gaussian):
  * *Label*: irf1
  * *Type*: spectral-multi-gaussian
  * *Center*: [irf.center: **4.00004e-01** *(StdErr: 5e-06 ,initial: 5.00000e-01)*]
  * *Width*: [irf.width: **5.99716e-02** *(StdErr: 6e-06 ,initial: 1.00000e-01)*]
  * *Normalize*: True
  * *Backsweep*: False
  * *Center Dispersion*: []
  * *Width Dispersion*: []
  * *Model Dispersion With Wavenumber*: False
* **irf1_no_dispersion** (spectral-multi-gaussian):
  * *Label*: irf1_no_dispersion
  * *Type*: spectral-multi-gaussian
  * *Center*: [irf.center: **4.00004e-01** *(StdErr: 5e-06 ,initial: 5.00000e-01)*]
  * *Width*: [irf.width: **5.99716e-02** *(StdErr: 6e-06 ,initial: 1.00000e-01)*]
  * *Normalize*: True
  * *Backsweep*: False
  * *Center Dispersion*: []
  * *Width Dispersion*: []
  * *Model Dispersion With Wavenumber*: False

## Dataset

* **dataset1**:
  * *Label*: dataset1
  * *Megacomplex*: ['complex1']
  * *Scale*: scale.1: **1.00000e+00** *(fixed)*
  * *Initial Concentration*: input1
  * *Irf*: irf1
* **dataset2**:
  * *Label*: dataset2
  * *Megacomplex*: ['complex1']
  * *Scale*: scale.2: **1.10058e+00** *(StdErr: 4e-04 ,initial: 1.20000e+00)*
  * *Initial Concentration*: input2
  * *Irf*: irf1

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

