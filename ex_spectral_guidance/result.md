| Optimization Result           |              |
|-------------------------------|--------------|
| Number of residual evaluation | 21           |
| Number of variables           | 6            |
| Number of datapoints          | 11265        |
| Degrees of freedom            | 11259        |
| Chi Square                    | 9.80e+06     |
| Reduced Chi Square            | 8.71e+02     |
| Root Mean Square Error (RMSE) | 2.95e+01     |
| RMSE additional penalty       | [4.06507309] |

| RMSE (per dataset)   |   weighted |   unweighted |
|----------------------|------------|--------------|
| 1.dataset1:          |   3.00e+01 |     3.00e+01 |
| 2.dataset2:          |   5.59e-04 |     5.59e-04 |

# Model

_Type_: kinetic-spectrum

## Initial Concentration

* **input1**:
  * *Label*: input1
  * *Compartments*: ['s1', 's2', 's3', 's4', 's5', 's6']
  * *Parameters*: [inputs.s1: **0.00000e+00** *(fixed)*, inputs.s1: **0.00000e+00** *(fixed)*, inputs.s1: **0.00000e+00** *(fixed)*, inputs.s2: **1.00000e+00** *(fixed)*, inputs.s1: **0.00000e+00** *(fixed)*, inputs.s1: **0.00000e+00** *(fixed)*]
  * *Exclude From Normalize*: []
* **input2**:
  * *Label*: input2
  * *Compartments*: ['s5']
  * *Parameters*: [inputs.s2: **1.00000e+00** *(fixed)*]
  * *Exclude From Normalize*: []

## K Matrix

* **km1**:
  * *Label*: km1
  * *Matrix*: 
    * *('s1', 's4')*: rates.k1: **2.46938e-01** *(StdErr: 4e-02 ,initial: 2.10000e-01)*
    * *('s3', 's1')*: rates.k2: **1.59884e-01** *(StdErr: 8e-02 ,initial: 1.95500e-01)*
    * *('s2', 's1')*: rates.k3: **8.70000e-02** *(fixed)*
    * *('s5', 's2')*: rates.k4: **2.49146e-01** *(StdErr: 2e-02 ,initial: 2.67000e-01)*
    * *('s6', 's3')*: rates.k5: **6.43174e-03** *(StdErr: 2e-01 ,initial: 6.40000e-03)*
    * *('s6', 's6')*: rates.k6: **1.33179e-06** *(StdErr: 4e-01 ,initial: 1.30000e-06)*
    * *('s5', 's5')*: rates.k6: **1.33179e-06** *(StdErr: 4e-01 ,initial: 1.30000e-06)*
  
* **km2**:
  * *Label*: km2
  * *Matrix*: 
    * *('s5', 's5')*: rates.k6: **1.33179e-06** *(StdErr: 4e-01 ,initial: 1.30000e-06)*
  

## Irf

* **irf1** (spectral-multi-gaussian):
  * *Label*: irf1
  * *Type*: spectral-multi-gaussian
  * *Center*: [irf.center: **-1.00000e-03** *(fixed)*]
  * *Width*: [irf.width: **4.15256e-04** *(fixed)*]
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
  * *Megacomplex*: ['complex2']
  * *Scale*: scale.2: **8.55560e-01** *(StdErr: 2e+00 ,initial: 8.62000e-01)*
  * *Initial Concentration*: input2

## Megacomplex

* **complex1** (None):
  * *Label*: complex1
  * *K Matrix*: ['km1']
* **complex2** (None):
  * *Label*: complex2
  * *K Matrix*: ['km2']

## Equal Area Penalties

* 
  * *Source*: s2
  * *Source Intervals*: [[0, 1000]]
  * *Target*: s1
  * *Target Intervals*: [[0, 1000]]
  * *Parameter*: area.1: **3.46340e+00** *(fixed)*
  * *Weight*: 1e-06

## Spectral Relations

* 
  * *Compartment*: s1
  * *Target*: s4
  * *Parameter*: rel.r1: **1.00000e+00** *(fixed)*
  * *Interval*: [[0, 1000]]
* 
  * *Compartment*: s3
  * *Target*: s6
  * *Parameter*: rel.r1: **1.00000e+00** *(fixed)*
  * *Interval*: [[0, 1000]]

