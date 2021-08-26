| Optimization Result           |          |
|-------------------------------|----------|
| Number of residual evaluation | 11       |
| Number of variables           | 13       |
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

_Type_: kinetic-spectrum

## Initial Concentration

* **input1**:
  * *Label*: input1
  * *Compartments*: ['s1', 's2', 's3', 's4', 's5']
  * *Parameters*: [inputs.1: **1.00000e+00** *(fixed)*, inputs.0: **0.00000e+00** *(fixed)*, inputs.0: **0.00000e+00** *(fixed)*, inputs.0: **0.00000e+00** *(fixed)*, inputs.iC: **1.00000e+00** *(fixed)*]
  * *Exclude From Normalize*: []
* **input2**:
  * *Label*: input2
  * *Compartments*: ['s1', 's2', 's3', 's4', 's6']
  * *Parameters*: [inputs.1: **1.00000e+00** *(fixed)*, inputs.0: **0.00000e+00** *(fixed)*, inputs.0: **0.00000e+00** *(fixed)*, inputs.0: **0.00000e+00** *(fixed)*, inputs.iC: **1.00000e+00** *(fixed)*]
  * *Exclude From Normalize*: []

## K Matrix

* **km1**:
  * *Label*: km1
  * *Matrix*: 
    * *('s2', 's1')*: rates.k1: **8.26500e-01** *(fixed)*
    * *('s3', 's1')*: rates.k2: **8.76350e+00** *(fixed)*
    * *('s4', 's2')*: rates.k3: **2.39907e-01** *(StdErr: 3e-02 ,initial: 4.83972e-01)*
    * *('s4', 's3')*: rates.k4: **4.46740e-02** *(StdErr: 3e-03 ,initial: 3.68954e-02)*
    * *('s4', 's4')*: rates.k5: **1.86268e-02** *(StdErr: 2e-03 ,initial: 1.92859e-02)*
    * *('s5', 's5')*: rates.kC: **9.90000e+01** *(fixed)*
  
* **km2**:
  * *Label*: km2
  * *Matrix*: 
    * *('s2', 's1')*: rates.k1: **8.26500e-01** *(fixed)*
    * *('s3', 's1')*: rates.k2: **8.76350e+00** *(fixed)*
    * *('s4', 's2')*: rates.k3d2: **1.91837e+41** *(StdErr: 3e-17 ,initial: 7.00000e-01)*
    * *('s4', 's3')*: rates.k4d2: **1.06113e-01** *(StdErr: 4e-03 ,initial: 8.50000e-02)*
    * *('s4', 's4')*: rates.k5: **1.86268e-02** *(StdErr: 2e-03 ,initial: 1.92859e-02)*
    * *('s6', 's6')*: rates.kC: **9.90000e+01** *(fixed)*
  

## Irf

* **irf1** (spectral-multi-gaussian):
  * *Label*: irf1
  * *Type*: spectral-multi-gaussian
  * *Center*: [irf.center: **1.20087e+00** *(StdErr: 1e-03 ,initial: 1.19809e+00)*]
  * *Width*: [irf.width: **7.18333e-02** *(StdErr: 3e-04 ,initial: 5.84300e-02)*]
  * *Normalize*: True
  * *Backsweep*: False
  * *Dispersion Center*: irf.dispc: **5.50000e+02** *(fixed)*
  * *Center Dispersion*: [irf.disp1: **2.67436e-01** *(StdErr: 3e-03 ,initial: 3.08957e-01)*, irf.disp2: **-2.82969e-02** *(StdErr: 5e-03 ,initial: -8.33899e-02)*, irf.disp3: **-3.74524e-03** *(StdErr: 2e-03 ,initial: 4.70000e-03)*]
  * *Width Dispersion*: []
  * *Model Dispersion With Wavenumber*: False
* **irf2** (spectral-multi-gaussian):
  * *Label*: irf2
  * *Type*: spectral-multi-gaussian
  * *Center*: [irf2.center: **6.69247e-01** *(StdErr: 1e-03 ,initial: 7.00000e-01)*]
  * *Width*: [irf.width: **7.18333e-02** *(StdErr: 3e-04 ,initial: 5.84300e-02)*]
  * *Normalize*: True
  * *Backsweep*: False
  * *Dispersion Center*: irf.dispc: **5.50000e+02** *(fixed)*
  * *Center Dispersion*: [irf.disp1: **2.67436e-01** *(StdErr: 3e-03 ,initial: 3.08957e-01)*, irf.disp2: **-2.82969e-02** *(StdErr: 5e-03 ,initial: -8.33899e-02)*, irf.disp3: **-3.74524e-03** *(StdErr: 2e-03 ,initial: 4.70000e-03)*]
  * *Width Dispersion*: []
  * *Model Dispersion With Wavenumber*: False

## Dataset

* **dataset1**:
  * *Label*: dataset1
  * *Megacomplex*: ['cmplx1']
  * *Scale*: scale.1: **1.00000e+00** *(fixed)*
  * *Initial Concentration*: input1
  * *Irf*: irf1
* **dataset2**:
  * *Label*: dataset2
  * *Megacomplex*: ['cmplx2']
  * *Scale*: scale.2: **1.26043e+00** *(StdErr: 5e-04 ,initial: 1.30000e+00)*
  * *Initial Concentration*: input2
  * *Irf*: irf2

## Megacomplex

* **cmplx1** (None):
  * *Label*: cmplx1
  * *K Matrix*: ['km1']
* **cmplx2** (None):
  * *Label*: cmplx2
  * *K Matrix*: ['km2']

## Weights

* 
  * *Datasets*: ['dataset1', 'dataset2']
  * *Global Interval*: [280, 550]
  * *Value*: 0.1
* 
  * *Datasets*: ['dataset1', 'dataset2']
  * *Global Interval*: [720, 890]
  * *Value*: 0.2

## Spectral Relations

* 
  * *Compartment*: s2
  * *Target*: s3
  * *Parameter*: rel.r1: **1.00000e+00** *(fixed)*
  * *Interval*: [[0, 1000]]

