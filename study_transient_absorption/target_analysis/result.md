| Optimization Result           |          |
|-------------------------------|----------|
| Number of residual evaluation | 10       |
| Number of variables           | 9        |
| Number of datapoints          | 115910   |
| Degrees of freedom            | 115901   |
| Chi Square                    | 4.66e-03 |
| Reduced Chi Square            | 4.02e-08 |
| Root Mean Square Error (RMSE) | 2.00e-04 |

# Model

_Type_: kinetic-spectrum

## Initial Concentration

* **input1**:
  * *Label*: input1
  * *Compartments*: ['s1', 's2', 's3', 's4', 's5']
  * *Parameters*: [inputs.1: **1.00000e+00** *(fixed)*, inputs.0: **0.00000e+00** *(fixed)*, inputs.0: **0.00000e+00** *(fixed)*, inputs.0: **0.00000e+00** *(fixed)*, inputs.iC: **1.00000e+00** *(fixed)*]
  * *Exclude From Normalize*: []

## K Matrix

* **km1**:
  * *Label*: km1
  * *Matrix*: 
    * *('s2', 's1')*: rates.k1: **1.51995e+00** *(fixed)*
    * *('s3', 's1')*: rates.k2: **7.97948e+00** *(fixed)*
    * *('s4', 's2')*: rates.k3: **3.60905e-01** *(StdErr: 3e-02 ,initial: 4.83972e-01)*
    * *('s4', 's3')*: rates.k4: **3.99494e-02** *(StdErr: 9e-03 ,initial: 3.68954e-02)*
    * *('s4', 's4')*: rates.k5: **2.00535e-02** *(StdErr: 4e-03 ,initial: 1.92859e-02)*
    * *('s5', 's5')*: rates.kC: **9.90000e+01** *(fixed)*
  

## Irf

* **irf1** (spectral-multi-gaussian):
  * *Label*: irf1
  * *Type*: spectral-multi-gaussian
  * *Center*: [irf.center: **1.20094e+00** *(StdErr: 8e-04 ,initial: 1.19809e+00)*]
  * *Width*: [irf.width: **6.12282e-02** *(StdErr: 2e-04 ,initial: 5.84300e-02)*]
  * *Normalize*: True
  * *Backsweep*: False
  * *Dispersion Center*: irf.dispc: **5.50000e+02** *(fixed)*
  * *Center Dispersion*: [irf.disp1: **2.89377e-01** *(StdErr: 2e-03 ,initial: 3.08957e-01)*, irf.disp2: **-7.68442e-02** *(StdErr: 1e-03 ,initial: -8.33899e-02)*, irf.disp3: **9.88958e-03** *(StdErr: 6e-04 ,initial: 4.70000e-03)*]
  * *Width Dispersion*: []
  * *Model Dispersion With Wavenumber*: False

## Dataset

* **dataset1**:
  * *Label*: dataset1
  * *Megacomplex*: ['cmplx1']
  * *Scale*: scale.1: **1.00000e+00** *(fixed)*
  * *Initial Concentration*: input1
  * *Irf*: irf1

## Megacomplex

* **cmplx1** (None):
  * *Label*: cmplx1
  * *K Matrix*: ['km1']

## Weights

* 
  * *Datasets*: ['dataset1']
  * *Global Interval*: [280, 550]
  * *Value*: 0.1
* 
  * *Datasets*: ['dataset1']
  * *Global Interval*: [720, 890]
  * *Value*: 0.1

## Spectral Relations

* 
  * *Compartment*: s2
  * *Target*: s3
  * *Parameter*: rel.r1: **1.00000e+00** *(fixed)*
  * *Interval*: [[0, 1000]]

