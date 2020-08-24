Optimization Result            |            |
-------------------------------|------------|
 Number of residual evaluation |          9 |
           Number of variables |          9 |
          Number of datapoints |   (45227,) |
            Degrees of freedom |      45218 |
                    Chi Square |   8.93e+07 |
            Reduced Chi Square |   1.97e+03 |
        Root Mean Square Error |   4.44e+01 |


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
    * *('s5', 's1')*: kinetic.2: **1.32873e+00** *(StdErr: 1e+00 ,initial: 9.56613e-02)*
    * *('s2', 's2')*: kinetic.3: **6.02947e-02** *(StdErr: 2e-04 ,initial: 6.01837e-02)*
    * *('s3', 's2')*: kinetic.4: **5.48462e-02** *(StdErr: 8e-04 ,initial: 1.27000e-01)*
    * *('s4', 's2')*: kinetic.5: **2.60597e-02** *(StdErr: 3e-04 ,initial: 2.61490e-02)*
    * *('s2', 's3')*: kinetic.6: **1.31307e-01** *(StdErr: 1e-03 ,initial: 5.70000e-02)*
    * *('s2', 's4')*: kinetic.7: **4.03148e-02** *(StdErr: 3e-04 ,initial: 4.50000e-02)*
    * *('s3', 's3')*: kinetic.8: **1.61728e-04** *(StdErr: 1e-06 ,initial: 1.60000e-04)*
    * *('s4', 's4')*: kinetic.8: **1.61728e-04** *(StdErr: 1e-06 ,initial: 1.60000e-04)*
    * *('s5', 's5')*: kinetic.8: **1.61728e-04** *(StdErr: 1e-06 ,initial: 1.60000e-04)*
  

## Irf

* **irf1** (gaussian):
  * *Label*: irf1
  * *Type*: gaussian
  * *Center*: irf.center: **-8.41472e+01** *(StdErr: 1e-01 ,initial: -8.38578e+01)*
  * *Width*: irf.width: **1.58651e+00** *(StdErr: 2e-02 ,initial: 1.61112e+00)*
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
  * *Interval*: [(650, 810)]
  * *Target*: s3
  * *Parameter*: area.1: **1.00000e+00** *(fixed)*
  * *Weight*: 0.0016
* 
  * *Compartment*: s2
  * *Interval*: [(650, 810)]
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
  * *Interval*: [(3, 680)]
* **zero**:
  * *Type*: zero
  * *Compartment*: s4
  * *Interval*: [(3, 690)]

