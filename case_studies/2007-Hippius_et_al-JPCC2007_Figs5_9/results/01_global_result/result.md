Optimization Result            |            |
-------------------------------|------------|
 Number of residual evaluation |         11 |
           Number of variables |          5 |
          Number of datapoints |  (115910,) |
            Degrees of freedom |     115905 |
                    Chi Square |   1.05e-01 |
            Reduced Chi Square |   9.09e-07 |
        Root Mean Square Error |   9.54e-04 |


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
    * *('s2', 's1')*: rates.k1: **5.66581e+00** *(StdErr: 1e-02 ,initial: 5.00000e-01)*
    * *('s3', 's2')*: rates.k2: **5.67378e-02** *(StdErr: 1e-02 ,initial: 5.00000e-02)*
    * *('s3', 's3')*: rates.k3: **1.75478e-02** *(StdErr: 4e-03 ,initial: 1.00000e-02)*
  

## Irf

* **irf1** (gaussian):
  * *Label*: irf1
  * *Type*: gaussian
  * *Center*: irf.center: **1.21928e+00** *(StdErr: 1e-03 ,initial: 1.00000e+00)*
  * *Width*: irf.width: **1.48947e-01** *(StdErr: 9e-04 ,initial: 2.00000e-01)*
  * *Normalize*: False
  * *Backsweep*: False

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

