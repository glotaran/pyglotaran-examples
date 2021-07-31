| Optimization Result           |                           |
|-------------------------------|---------------------------|
| Number of residual evaluation | 6                         |
| Number of variables           | 8                         |
| Number of datapoints          | 45229                     |
| Degrees of freedom            | 45221                     |
| Chi Square                    | 9.01e+07                  |
| Reduced Chi Square            | 1.99e+03                  |
| Root Mean Square Error (RMSE) | 4.46e+01                  |
| RMSE additional penalty       | [59.57132818 44.56694497] |

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
    * *('s2', 's2')*: kinetic.3: **6.30601e-02** *(StdErr: 3e-03 ,initial: 6.00000e-02)*
    * *('s3', 's2')*: kinetic.4: **2.71413e-02** *(StdErr: 1e-02 ,initial: 2.70000e-02)*
    * *('s4', 's2')*: kinetic.5: **5.66092e-02** *(StdErr: 1e-02 ,initial: 5.60000e-02)*
    * *('s2', 's3')*: kinetic.6: **3.96686e-02** *(StdErr: 6e-03 ,initial: 3.90000e-02)*
    * *('s2', 's4')*: kinetic.7: **1.33279e-01** *(StdErr: 8e-03 ,initial: 1.33000e-01)*
    * *('s3', 's3')*: kinetic.8: **1.63160e-04** *(StdErr: 6e-03 ,initial: 1.60000e-04)*
    * *('s4', 's4')*: kinetic.8: **1.63160e-04** *(StdErr: 6e-03 ,initial: 1.60000e-04)*
    * *('s5', 's5')*: kinetic.8: **1.63160e-04** *(StdErr: 6e-03 ,initial: 1.60000e-04)*
  

## Irf

* **irf1** (gaussian):
  * *Label*: irf1
  * *Type*: gaussian
  * *Center*: irf.center: **-8.43113e+01** *(StdErr: 3e-03 ,initial: -8.40000e+01)*
  * *Width*: irf.width: **1.55406e+00** *(StdErr: 3e-03 ,initial: 1.55000e+00)*
  * *Normalize*: True
  * *Backsweep*: True
  * *Backsweep Period*: irf.backsweep: **1.32000e+04** *(fixed)*

## Dataset

* **dataset1**:
  * *Label*: dataset1
  * *Megacomplex*: ['mc1']
  * *Initial Concentration*: input1
  * *Irf*: irf1

## Megacomplex

* **mc1** (None):
  * *Label*: mc1
  * *K Matrix*: ['km1']

## Equal Area Penalties

* 
  * *Source*: s2
  * *Source Intervals*: [[100, 1000]]
  * *Target*: s3
  * *Target Intervals*: [[100, 1000]]
  * *Parameter*: area.1: **1.00000e+00** *(fixed)*
  * *Weight*: 0.0016
* 
  * *Source*: s2
  * *Source Intervals*: [[100, 1000]]
  * *Target*: s4
  * *Target Intervals*: [[100, 1000]]
  * *Parameter*: area.1: **1.00000e+00** *(fixed)*
  * *Weight*: 0.0016

## Spectral Constraints

* **zero**:
  * *Type*: zero
  * *Compartment*: s1
  * *Interval*: [[1, 1000]]
* **zero**:
  * *Type*: zero
  * *Compartment*: s3
  * *Interval*: [[1, 680]]
* **zero**:
  * *Type*: zero
  * *Compartment*: s4
  * *Interval*: [[1, 690]]

