| Optimization Result           |                                 |
|-------------------------------|---------------------------------|
| Number of residual evaluation | 8                               |
| Number of variables           | 17                              |
| Number of datapoints          | 92556                           |
| Degrees of freedom            | 92539                           |
| Chi Square                    | 1.49e-04                        |
| Reduced Chi Square            | 1.61e-09                        |
| Root Mean Square Error (RMSE) | 4.01e-05                        |
| RMSE additional penalty       | [2.69283191e-10 4.16454131e-07] |

| RMSE (per dataset)   |   weighted |   unweighted |
|----------------------|------------|--------------|
| 1.dataset1:          |   3.64e-05 |     3.64e-05 |
| 2.dataset2:          |   3.51e-05 |     3.51e-05 |
| 3.dataset3:          |   5.79e-05 |     5.79e-05 |
| 4.dataset4:          |   2.34e-05 |     2.34e-05 |
| 5.dataset5:          |   4.61e-05 |     4.61e-05 |
| 6.dataset6:          |   9.00e-06 |     9.00e-06 |

# Model

_Type_: kinetic-spectrum

## Initial Concentration

* **input1**:
  * *Label*: input1
  * *Compartments*: ['s1', 's2', 's3']
  * *Parameters*: [inputs.1: **5.00000e-01** *(fixed)*, inputs.2: **3.05578e-01** *(StdErr: 4e-07 ,initial: 5.10000e-02)*, inputs.3: **1.81049e-01** *(StdErr: 8e-07 ,initial: 2.52000e-01)*]
  * *Exclude From Normalize*: []
* **input2**:
  * *Label*: input2
  * *Compartments*: ['s1', 's2', 's3']
  * *Parameters*: [inputs.1: **5.00000e-01** *(fixed)*, inputs.7: **3.97441e-01** *(StdErr: 4e-07 ,initial: 5.21000e-02)*, inputs.8: **3.89975e-01** *(StdErr: 7e-07 ,initial: 2.20000e-01)*]
  * *Exclude From Normalize*: []
* **input3**:
  * *Label*: input3
  * *Compartments*: ['s1', 's2', 's3']
  * *Parameters*: [inputs.1: **5.00000e-01** *(fixed)*, inputs.9: **3.55235e-01** *(StdErr: 4e-07 ,initial: 5.22000e-02)*, inputs.10: **2.89950e-01** *(StdErr: 8e-07 ,initial: 2.20000e-01)*]
  * *Exclude From Normalize*: []

## K Matrix

* **km1**:
  * *Label*: km1
  * *Matrix*: 
    * *('s1', 's1')*: rates.k1: **4.99901e-02** *(StdErr: 2e-08 ,initial: 5.00000e-02)*
    * *('s2', 's2')*: rates.k2: **5.09192e-01** *(StdErr: 2e-07 ,initial: 5.00000e-01)*
    * *('s3', 's3')*: rates.k3: **2.31113e+00** *(StdErr: 3e-07 ,initial: 2.00000e+00)*
  

## Irf

* **irf1_with_dispersion** (spectral-multi-gaussian):
  * *Label*: irf1_with_dispersion
  * *Type*: spectral-multi-gaussian
  * *Center*: [irf.center1: **4.00005e-01** *(StdErr: 4e-09 ,initial: 4.00000e-01)*]
  * *Width*: [irf.width: **5.99808e-02** *(StdErr: 2e-09 ,initial: 6.00000e-02)*]
  * *Normalize*: True
  * *Backsweep*: False
  * *Dispersion Center*: irf.dispc: **5.00000e+02** *(fixed)*
  * *Center Dispersion*: [irf.disp1: **1.00000e-02** *(StdErr: 9e-09 ,initial: 1.00000e-02)*, irf.disp2: **1.00000e-03** *(StdErr: 1e-08 ,initial: 1.00000e-03)*]
  * *Width Dispersion*: []
  * *Model Dispersion With Wavenumber*: False
* **irf2_with_dispersion** (spectral-multi-gaussian):
  * *Label*: irf2_with_dispersion
  * *Type*: spectral-multi-gaussian
  * *Center*: [irf.center2: **4.10000e-01** *(StdErr: 4e-09 ,initial: 4.00000e-01)*]
  * *Width*: [irf.width: **5.99808e-02** *(StdErr: 2e-09 ,initial: 6.00000e-02)*]
  * *Normalize*: True
  * *Backsweep*: False
  * *Dispersion Center*: irf.dispc: **5.00000e+02** *(fixed)*
  * *Center Dispersion*: [irf.disp1: **1.00000e-02** *(StdErr: 9e-09 ,initial: 1.00000e-02)*, irf.disp2: **1.00000e-03** *(StdErr: 1e-08 ,initial: 1.00000e-03)*]
  * *Width Dispersion*: []
  * *Model Dispersion With Wavenumber*: False
* **irf3_with_dispersion** (spectral-multi-gaussian):
  * *Label*: irf3_with_dispersion
  * *Type*: spectral-multi-gaussian
  * *Center*: [irf.center3: **4.20000e-01** *(StdErr: 4e-09 ,initial: 4.00000e-01)*]
  * *Width*: [irf.width: **5.99808e-02** *(StdErr: 2e-09 ,initial: 6.00000e-02)*]
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
  * *Scale*: scale.1: **1.00000e+00** *(fixed)*
  * *Initial Concentration*: input1
  * *Irf*: irf1_with_dispersion
* **dataset3**:
  * *Label*: dataset3
  * *Megacomplex*: ['complex1']
  * *Scale*: scale.2: **1.30684e+00** *(StdErr: 1e-07 ,initial: 1.30000e+00)*
  * *Initial Concentration*: input2
  * *Irf*: irf2_with_dispersion
* **dataset4**:
  * *Label*: dataset4
  * *Megacomplex*: ['complex1']
  * *Scale*: scale.2: **1.30684e+00** *(StdErr: 1e-07 ,initial: 1.30000e+00)*
  * *Initial Concentration*: input2
  * *Irf*: irf2_with_dispersion
* **dataset5**:
  * *Label*: dataset5
  * *Megacomplex*: ['complex1']
  * *Scale*: scale.3: **1.16420e+00** *(StdErr: 6e-08 ,initial: 1.10000e+00)*
  * *Initial Concentration*: input3
  * *Irf*: irf3_with_dispersion
* **dataset6**:
  * *Label*: dataset6
  * *Megacomplex*: ['complex1']
  * *Scale*: scale.3: **1.16420e+00** *(StdErr: 6e-08 ,initial: 1.10000e+00)*
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
  * *Weight*: 0.01
* 
  * *Source*: s1
  * *Source Intervals*: [[300, 3000]]
  * *Target*: s3
  * *Target Intervals*: [[300, 3000]]
  * *Parameter*: area.1: **1.00000e+00** *(fixed)*
  * *Weight*: 0.01

