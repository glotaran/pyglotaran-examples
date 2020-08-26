Optimization Result            |            |
-------------------------------|------------|
 Number of residual evaluation |          5 |
           Number of variables |          8 |
          Number of datapoints |  (115910,) |
            Degrees of freedom |     115902 |
                    Chi Square |   6.43e-02 |
            Reduced Chi Square |   5.55e-07 |
        Root Mean Square Error |   7.45e-04 |


# Model

_Type_: kinetic-spectrum

## Initial Concentration

* **input1**:
  * *Label*: input1
  * *Compartments*: ['s1', 's2', 's3']
  * *Parameters*: [inputs.1: **1.00000e+00** *(fixed)*, inputs.0: **0.00000e+00** *(fixed)*, inputs.0: **0.00000e+00** *(fixed)*]
  * *Exclude From Normalize*: []

## K Matrix

* **km1**:
  * *Label*: km1
  * *Matrix*: 
    * *('s2', 's1')*: rates.k1: **1.60053e+00** *(StdErr: 2e-02 ,initial: 5.00000e-01)*
    * *('s3', 's2')*: rates.k2: **5.37349e-02** *(StdErr: 1e-02 ,initial: 5.00000e-02)*
    * *('s3', 's3')*: rates.k3: **1.81293e-02** *(StdErr: 4e-03 ,initial: 1.00000e-02)*
  

## Irf

* **irf1** (spectral-gaussian):
  * *Label*: irf1
  * *Type*: spectral-gaussian
  * *Center*: irf.center: **1.15512e+00** *(StdErr: 4e-04 ,initial: 1.00000e+00)*
  * *Width*: irf.width: **6.48918e-02** *(StdErr: 4e-04 ,initial: 2.00000e-01)*
  * *Normalize*: False
  * *Backsweep*: False
  * *Dispersion Center*: irf.dispc: **5.30000e+02** *(fixed)*
  * *Center Dispersion*: [irf.disp1: **3.42944e-01** *(StdErr: 9e-04 ,initial: 3.00000e-01)*, irf.disp2: **-1.09607e-01** *(StdErr: 7e-04 ,initial: -1.00000e-01)*, irf.disp3: **1.80009e-02** *(StdErr: 2e-04 ,initial: 1.00000e-02)*]
  * *Width Dispersion*: []
  * *Model Dispersion With Wavenumber*: False

## Megacomplex

* **cmplx1**:
  * *Label*: cmplx1
  * *K Matrix*: ['km1']

## Dataset

* **dataset1**:
  * *Label*: dataset1
  * *Megacomplex*: ['cmplx1']
  * *Initial Concentration*: input1
  * *Irf*: irf1

