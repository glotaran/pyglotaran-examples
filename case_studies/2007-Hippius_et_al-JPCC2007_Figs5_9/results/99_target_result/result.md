Optimization Result            |            |
-------------------------------|------------|
 Number of residual evaluation |         11 |
           Number of variables |          8 |
          Number of datapoints |  (115910,) |
            Degrees of freedom |     115902 |
                    Chi Square |   8.41e-02 |
            Reduced Chi Square |   7.26e-07 |
        Root Mean Square Error |   8.52e-04 |


# Model

_Type_: kinetic-spectrum

## Initial Concentration

* **input1**:
  * *Label*: input1
  * *Compartments*: ['s1', 's2', 's3', 's4']
  * *Parameters*: [inputs.1: **1.00000e+00** *(fixed)*, inputs.0: **0.00000e+00** *(fixed)*, inputs.0: **0.00000e+00** *(fixed)*, inputs.0: **0.00000e+00** *(fixed)*]
  * *Exclude From Normalize*: []

## K Matrix

* **km1**:
  * *Label*: km1
  * *Matrix*: 
    * *('s2', 's1')*: rates.k1: **1.21635e+00** *(fixed)*
    * *('s3', 's1')*: rates.k2: **7.80977e+00** *(fixed)*
    * *('s4', 's2')*: rates.k3: **8.78339e+00** *(StdErr: 0e+00 ,initial: 3.49811e-01)*
    * *('s4', 's3')*: rates.k4: **5.41857e-02** *(StdErr: 0e+00 ,initial: 4.27195e-02)*
    * *('s4', 's4')*: rates.k5: **1.74087e-02** *(StdErr: 0e+00 ,initial: 1.99982e-02)*
  

## Irf

* **irf1** (multi-gaussian):
  * *Label*: irf1
  * *Type*: multi-gaussian
  * *Center*: [irf.center: **1.17010e+00** *(StdErr: 0e+00 ,initial: 1.20844e+00)*]
  * *Width*: [irf.width: **1.10115e-01** *(StdErr: 0e+00 ,initial: 6.46305e-02)*]
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

