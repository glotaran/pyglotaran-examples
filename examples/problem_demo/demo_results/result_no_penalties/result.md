Optimization Result            |            |
-------------------------------|------------|
 Number of residual evaluation |          5 |
           Number of variables |          4 |
          Number of datapoints |   (25551,) |
            Degrees of freedom |      25547 |
                    Chi Square |   6.18e+01 |
            Reduced Chi Square |   2.42e-03 |
        Root Mean Square Error |   4.92e-02 |


# Model

_Type_: kinetic-spectrum

## Initial Concentration

* **j1**:
  * *Label*: j1
  * *Compartments*: ['s1', 's2']
  * *Parameters*: [i.1: **5.00000e-01** *(fixed)*, i.2: **5.00000e-01** *(fixed)*]
  * *Exclude From Normalize*: []

## K Matrix

* **k1**:
  * *Label*: k1
  * *Matrix*: 
    * *('s1', 's1')*: kinetic.1: **2.50031e-01** *(StdErr: 0e+00 ,initial: 2.00000e-01)*
    * *('s2', 's2')*: kinetic.2: **9.99947e-01** *(StdErr: 0e+00 ,initial: 1.10000e+00)*
  

## Irf

* **irf1** (gaussian):
  * *Label*: irf1
  * *Type*: gaussian
  * *Center*: irf.1: **4.00002e-01** *(StdErr: 0e+00 ,initial: 4.00000e-01)*
  * *Width*: irf.2: **5.99785e-02** *(StdErr: 0e+00 ,initial: 5.00000e-02)*
  * *Normalize*: False
  * *Backsweep*: False

## Dataset

* **dataset1**:
  * *Label*: dataset1
  * *Megacomplex*: ['mc1']
  * *Initial Concentration*: j1
  * *Irf*: irf1

## Megacomplex

* **mc1**:
  * *Label*: mc1
  * *K Matrix*: ['k1']

