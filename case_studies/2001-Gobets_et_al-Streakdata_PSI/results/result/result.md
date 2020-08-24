Optimization Result            |            |
-------------------------------|------------|
 Number of residual evaluation |          7 |
           Number of variables |          6 |
          Number of datapoints |   (45227,) |
            Degrees of freedom |      45221 |
                    Chi Square |   8.75e+07 |
            Reduced Chi Square |   1.93e+03 |
        Root Mean Square Error |   4.40e+01 |


# Model

_Type_: kinetic-spectrum

## Initial Concentration

* **input1**:
  * *Label*: input1
  * *Compartments*: ['s1', 's2', 's3', 's4']
  * *Parameters*: [input.1: **1.00000e+00** *(fixed)*, input.0: **0.00000e+00** *(fixed)*, input.0: **0.00000e+00** *(fixed)*, input.0: **0.00000e+00** *(fixed)*]
  * *Exclude From Normalize*: []

## K Matrix

* **km1**:
  * *Label*: km1
  * *Matrix*: 
    * *('s2', 's1')*: kinetic.1: **2.24982e-01** *(StdErr: 7e-03 ,initial: 2.00000e-01)*
    * *('s3', 's2')*: kinetic.2: **6.80679e-02** *(StdErr: 8e-03 ,initial: 7.00000e-02)*
    * *('s4', 's3')*: kinetic.3: **2.12251e-02** *(StdErr: 2e-03 ,initial: 2.00000e-02)*
    * *('s4', 's4')*: kinetic.4: **1.59678e-04** *(StdErr: 6e-03 ,initial: 1.60000e-04)*
  

## Irf

* **irf1** (gaussian):
  * *Label*: irf1
  * *Type*: gaussian
  * *Center*: irf.center: **-8.38533e+01** *(StdErr: 3e-03 ,initial: -8.30000e+01)*
  * *Width*: irf.width: **1.60986e+00** *(StdErr: 3e-03 ,initial: 1.50000e+00)*
  * *Normalize*: False
  * *Backsweep*: True
  * *Backsweep Period*: irf.backsweep: **1.32000e+04** *(fixed)*

## Megacomplex

* **mc1**:
  * *Label*: mc1
  * *K Matrix*: ['km1']

## Dataset

* **dataset1**:
  * *Label*: dataset1
  * *Megacomplex*: ['mc1']
  * *Initial Concentration*: input1
  * *Irf*: irf1

