| Optimization Result           |                         |
|-------------------------------|-------------------------|
| Number of residual evaluation | 103                     |
| Number of variables           | 16                      |
| Number of datapoints          | 91955                   |
| Degrees of freedom            | 91939                   |
| Chi Square                    | 5.03e+03                |
| Reduced Chi Square            | 5.47e-02                |
| Root Mean Square Error (RMSE) | 2.34e-01                |
| RMSE additional penalty       | [0.01165838 0.00146236] |

| RMSE (per dataset)   |   weighted |   unweighted |
|----------------------|------------|--------------|
| 1.dataset1:          |   2.54e-01 |     2.54e-01 |
| 2.dataset2:          |   2.38e-01 |     4.76e-01 |
| 3.dataset3:          |   2.08e-01 |     8.30e+01 |

# Model

_Type_: kinetic-spectrum

## Initial Concentration

* **input1**:
  * *Label*: input1
  * *Compartments*: ['s1', 's2', 's3']
  * *Parameters*: [inputs.1: **5.00000e-01** *(fixed)*, inputs.2: **2.42151e-01** *(StdErr: 1e+01 ,initial: 2.42290e-01)*, inputs.3: **3.63162e-01** *(StdErr: 3e+01 ,initial: 3.63180e-01)*]
  * *Exclude From Normalize*: []
* **input2**:
  * *Label*: input2
  * *Compartments*: ['s1', 's2', 's3']
  * *Parameters*: [inputs.1: **5.00000e-01** *(fixed)*, inputs.7: **1.61306e-01** *(StdErr: 1e+01 ,initial: 1.61370e-01)*, inputs.8: **3.11549e-01** *(StdErr: 3e+01 ,initial: 3.11570e-01)*]
  * *Exclude From Normalize*: []
* **input3**:
  * *Label*: input3
  * *Compartments*: ['s1', 's2', 's3']
  * *Parameters*: [inputs.1: **5.00000e-01** *(fixed)*, inputs.9: **9.62565e-02** *(StdErr: 1e+01 ,initial: 9.61700e-02)*, inputs.10: **2.07943e-01** *(StdErr: 3e+01 ,initial: 2.08060e-01)*]
  * *Exclude From Normalize*: []

## K Matrix

* **km1**:
  * *Label*: km1
  * *Matrix*: 
    * *('s1', 's1')*: rates.k1: **4.99629e-02** *(StdErr: 2e-04 ,initial: 4.99631e-02)*
    * *('s2', 's2')*: rates.k2: **1.99127e+00** *(StdErr: 3e-03 ,initial: 1.99170e+00)*
    * *('s3', 's3')*: rates.k3: **4.99018e-01** *(StdErr: 2e-03 ,initial: 4.99010e-01)*
  

## Irf

* **irf1_no_dispersion** (spectral-multi-gaussian):
  * *Label*: irf1_no_dispersion
  * *Type*: spectral-multi-gaussian
  * *Center*: [irf.center1: **4.99975e-01** *(StdErr: 4e-05 ,initial: 4.99983e-01)*]
  * *Width*: [irf.width1: **5.99548e-02** *(StdErr: 4e-04 ,initial: 5.99630e-02)*]
  * *Normalize*: True
  * *Backsweep*: False
  * *Center Dispersion*: []
  * *Width Dispersion*: []
  * *Model Dispersion With Wavenumber*: False
* **irf2_no_dispersion** (spectral-multi-gaussian):
  * *Label*: irf2_no_dispersion
  * *Type*: spectral-multi-gaussian
  * *Center*: [irf.center2: **4.00024e-01** *(StdErr: 9e-05 ,initial: 4.00024e-01)*]
  * *Width*: [irf.width1: **5.99548e-02** *(StdErr: 4e-04 ,initial: 5.99630e-02)*]
  * *Normalize*: True
  * *Backsweep*: False
  * *Center Dispersion*: []
  * *Width Dispersion*: []
  * *Model Dispersion With Wavenumber*: False
* **irf3_no_dispersion** (spectral-multi-gaussian):
  * *Label*: irf3_no_dispersion
  * *Type*: spectral-multi-gaussian
  * *Center*: [irf.center3: **4.49986e-01** *(StdErr: 3e-04 ,initial: 3.00091e-01)*]
  * *Width*: [irf.width2: **1.19729e-01** *(StdErr: 1e-03 ,initial: 8.99015e-02)*]
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
  * *Scale*: scale.2: **8.80050e-01** *(StdErr: 7e-01 ,initial: 8.80052e-01)*
  * *Initial Concentration*: input2
  * *Irf*: irf2_no_dispersion
* **dataset3**:
  * *Label*: dataset3
  * *Megacomplex*: ['complex1']
  * *Scale*: scale.3: **7.27381e+01** *(StdErr: 2e+00 ,initial: 7.27300e+01)*
  * *Initial Concentration*: input3
  * *Irf*: irf3_no_dispersion

## Megacomplex

* **complex1** (None):
  * *Label*: complex1
  * *K Matrix*: ['km1']

## Weights

* 
  * *Datasets*: ['dataset2']
  * *Global Interval*: [400, 600]
  * *Value*: 0.5
* 
  * *Datasets*: ['dataset3']
  * *Global Interval*: [400, 600]
  * *Value*: 0.0025

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

