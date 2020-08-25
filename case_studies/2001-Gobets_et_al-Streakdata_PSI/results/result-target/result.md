Optimization Result            |            |
-------------------------------|------------|
 Number of residual evaluation |         10 |
           Number of variables |          8 |
          Number of datapoints |   (45227,) |
            Degrees of freedom |      45219 |
                    Chi Square |   8.94e+07 |
            Reduced Chi Square |   1.98e+03 |
        Root Mean Square Error |   4.45e+01 |


# Model

_Type_: kinetic-spectrum

## Initial Concentration

* **input1**:
  * *Label*: input1
  * *Compartments*: ['s1', 's2', 's3', 's4', 's5']
  * *Parameters*: [input.1: **1.00000e+00** *(fixed)*, input.0: **0.00000e+00** *(fixed)*, input.0: **0.00000e+00** *(fixed)*, input.0: **0.00000e+00** *(fixed)*, input.0: **0.00000e+00** *(fixed)*]
  * *Exclude From Normalize*: []

## K Matrix

* **km1**:
  * *Label*: km1
  * *Matrix*: 
    * *('s2', 's1')*: kinetic.1: **2.00000e+00** *(fixed)*
    * *('s5', 's1')*: kinetic.2: **1.00000e-01** *(fixed)*
    * *('s2', 's2')*: kinetic.3: **6.06092e-02** *(StdErr: 4e-03 ,initial: 6.01837e-02)*
    * *('s3', 's2')*: kinetic.4: **5.59054e-02** *(StdErr: 1e-02 ,initial: 1.27000e-01)*
    * *('s4', 's2')*: kinetic.5: **2.60049e-02** *(StdErr: 1e-02 ,initial: 2.61490e-02)*
    * *('s2', 's3')*: kinetic.6: **1.31238e-01** *(StdErr: 9e-03 ,initial: 5.70000e-02)*
    * *('s2', 's4')*: kinetic.7: **4.02575e-02** *(StdErr: 6e-03 ,initial: 4.50000e-02)*
    * *('s3', 's3')*: kinetic.8: **1.61193e-04** *(StdErr: 6e-03 ,initial: 1.60000e-04)*
    * *('s4', 's4')*: kinetic.8: **1.61193e-04** *(StdErr: 6e-03 ,initial: 1.60000e-04)*
    * *('s5', 's5')*: kinetic.8: **1.61193e-04** *(StdErr: 6e-03 ,initial: 1.60000e-04)*
  

## Irf

* **irf1** (gaussian):
  * *Label*: irf1
  * *Type*: gaussian
  * *Center*: irf.center: **-8.43123e+01** *(StdErr: 3e-03 ,initial: -8.38578e+01)*
  * *Width*: irf.width: **1.55189e+00** *(StdErr: 3e-03 ,initial: 1.61112e+00)*
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

## Equal Area Penalties

* 
  * *Compartment*: s2
  * *Interval*: (100, '1000)')
  * *Target*: s3
  * *Parameter*: area.1: **1.00000e+00** *(fixed)*
  * *Weight*: 0.0016
* 
  * *Compartment*: s2
  * *Interval*: (100, 1000)
  * *Target*: s4
  * *Parameter*: area.1: **1.00000e+00** *(fixed)*
  * *Weight*: 0.0016

## Spectral Constraints

* **zero**:
  * *Type*: zero
  * *Compartment*: s1
  * *Interval*: [(1, 1000)]
* **zero**:
  * *Type*: zero
  * *Compartment*: s3
  * *Interval*: [(1, 680)]
* **zero**:
  * *Type*: zero
  * *Compartment*: s4
  * *Interval*: [(1, 690)]

