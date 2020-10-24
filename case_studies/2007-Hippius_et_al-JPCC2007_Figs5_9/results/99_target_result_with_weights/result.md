Optimization Result            |            |
-------------------------------|------------|
 Number of residual evaluation |       1000 |
           Number of variables |          9 |
          Number of datapoints |       (1,) |
            Degrees of freedom |          1 |
                    Chi Square |  1.00e-250 |
            Reduced Chi Square |       -inf |
        Root Mean Square Error |        nan |


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
    * *('s2', 's1')*: rates.k1: **1.37545e+00** *(fixed)*
    * *('s3', 's1')*: rates.k2: **6.90640e+00** *(fixed)*
    * *('s4', 's2')*: rates.k3: **2.83873e-01** *(StdErr: 0e+00 ,initial: 4.83972e-01)*
    * *('s4', 's3')*: rates.k4: **3.78511e-02** *(StdErr: 0e+00 ,initial: 3.68954e-02)*
    * *('s4', 's4')*: rates.k5: **2.05819e-02** *(StdErr: 0e+00 ,initial: 1.92859e-02)*
    * *('s5', 's5')*: rates.kC: **9.90000e+01** *(fixed)*
  

## Irf

* **irf1** (spectral-multi-gaussian):
  * *Label*: irf1
  * *Type*: spectral-multi-gaussian
  * *Center*: [irf.center: **1.19591e+00** *(StdErr: 0e+00 ,initial: 1.19809e+00)*]
  * *Width*: [irf.width: **6.30974e-02** *(StdErr: 0e+00 ,initial: 5.84300e-02)*]
  * *Normalize*: False
  * *Backsweep*: False
  * *Dispersion Center*: irf.dispc: **5.50000e+02** *(fixed)*
  * *Center Dispersion*: [irf.disp1: **3.00003e-01** *(StdErr: 0e+00 ,initial: 3.08957e-01)*, irf.disp2: **-7.06533e-02** *(StdErr: 0e+00 ,initial: -8.33899e-02)*, irf.disp3: **2.33938e-03** *(StdErr: 0e+00 ,initial: 4.70000e-03)*]
  * *Width Dispersion*: []
  * *Model Dispersion With Wavenumber*: False

## Dataset

* **dataset1**:
  * *Label*: dataset1
  * *Megacomplex*: ['cmplx1']
  * *Initial Concentration*: input1
  * *Irf*: irf1

## Megacomplex

* **cmplx1**:
  * *Label*: cmplx1
  * *K Matrix*: ['km1']

## Weights

* 
  * *Datasets*: ['dataset1']
  * *Global Interval*: (280, 550)
  * *Value*: 0.1
* 
  * *Datasets*: ['dataset1']
  * *Global Interval*: (720, 890)
  * *Value*: 0.2

## Spectral Relations

* 
  * *Compartment*: s2
  * *Target*: s3
  * *Parameter*: rel.r1: **1.00000e+00** *(fixed)*
  * *Interval*: [(0, 1000)]

