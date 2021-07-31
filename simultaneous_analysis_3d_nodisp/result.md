| Optimization Result           |                                 |
|-------------------------------|---------------------------------|
| Number of residual evaluation | 5                               |
| Number of variables           | 13                              |
| Number of datapoints          | 91955                           |
| Degrees of freedom            | 91942                           |
| Chi Square                    | 6.78e+02                        |
| Reduced Chi Square            | 7.37e-03                        |
| Root Mean Square Error (RMSE) | 8.59e-02                        |
| RMSE additional penalty       | [1.30065822e-05 1.08228374e-05] |

| RMSE (per dataset)   |   weighted |   unweighted |
|----------------------|------------|--------------|
| 1.dataset1:          |   8.02e-02 |     8.92e-02 |
| 2.dataset2:          |   9.15e-02 |     1.02e-01 |
| 3.dataset3:          |   8.55e-02 |     9.51e-02 |

# Model

_Type_: kinetic-spectrum

## Initial Concentration

* **input1**:
  * *Label*: input1
  * *Compartments*: ['s1', 's2', 's3']
  * *Parameters*: [inputs.1: **5.00000e-01** *(fixed)*, inputs.2: **1.61292e-01** *(StdErr: 9e-04 ,initial: 1.61000e-01)*, inputs.3: **3.11391e-01** *(StdErr: 5e-04 ,initial: 3.11000e-01)*]
  * *Exclude From Normalize*: []
* **input2**:
  * *Label*: input2
  * *Compartments*: ['s1', 's2', 's3']
  * *Parameters*: [inputs.1: **5.00000e-01** *(fixed)*, inputs.7: **3.22561e-01** *(StdErr: 6e-04 ,initial: 3.22000e-01)*, inputs.8: **4.15097e-01** *(StdErr: 5e-04 ,initial: 4.15000e-01)*]
  * *Exclude From Normalize*: []
* **input3**:
  * *Label*: input3
  * *Compartments*: ['s1', 's2', 's3']
  * *Parameters*: [inputs.1: **5.00000e-01** *(fixed)*, inputs.9: **2.41926e-01** *(StdErr: 7e-04 ,initial: 2.42000e-01)*, inputs.10: **3.63243e-01** *(StdErr: 5e-04 ,initial: 3.63000e-01)*]
  * *Exclude From Normalize*: []

## K Matrix

* **km1**:
  * *Label*: km1
  * *Matrix*: 
    * *('s1', 's1')*: rates.k1: **4.99901e-02** *(StdErr: 7e-05 ,initial: 5.00000e-02)*
    * *('s2', 's2')*: rates.k2: **1.99742e+00** *(StdErr: 7e-04 ,initial: 2.00000e+00)*
    * *('s3', 's3')*: rates.k3: **4.99647e-01** *(StdErr: 4e-04 ,initial: 5.00000e-01)*
  

## Irf

* **irf1_no_dispersion** (spectral-multi-gaussian):
  * *Label*: irf1_no_dispersion
  * *Type*: spectral-multi-gaussian
  * *Center*: [irf.center: **4.00008e-01** *(StdErr: 5e-06 ,initial: 4.00000e-01)*]
  * *Width*: [irf.width: **5.99786e-02** *(StdErr: 6e-06 ,initial: 5.99800e-02)*]
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
  * *Irf*: irf1_no_dispersion
* **dataset2**:
  * *Label*: dataset2
  * *Megacomplex*: ['complex1']
  * *Scale*: scale.2: **1.27238e+00** *(StdErr: 6e-05 ,initial: 1.27000e+00)*
  * *Initial Concentration*: input2
  * *Irf*: irf1_no_dispersion
* **dataset3**:
  * *Label*: dataset3
  * *Megacomplex*: ['complex1']
  * *Scale*: scale.3: **1.13619e+00** *(StdErr: 5e-05 ,initial: 1.13000e+00)*
  * *Initial Concentration*: input3
  * *Irf*: irf1_no_dispersion

## Megacomplex

* **complex1** (None):
  * *Label*: complex1
  * *K Matrix*: ['km1']

## Weights

* 
  * *Datasets*: ['dataset1', 'dataset2', 'dataset3']
  * *Global Interval*: [400, 450]
  * *Value*: 0.5

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

