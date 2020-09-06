Optimization Result            |            |
-------------------------------|------------|
 Number of residual evaluation |         11 |
           Number of variables |          9 |
          Number of datapoints |  (115910,) |
            Degrees of freedom |     115901 |
                    Chi Square |   5.65e-02 |
            Reduced Chi Square |   4.88e-07 |
        Root Mean Square Error |   6.98e-04 |


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
    * *('s2', 's1')*: rates.k1: **1.61022e+00** *(fixed)*
    * *('s3', 's1')*: rates.k2: **5.89945e+00** *(fixed)*
    * *('s4', 's2')*: rates.k3: **4.83972e-01** *(StdErr: 4e-02 ,initial: 5.83815e-01)*
    * *('s4', 's3')*: rates.k4: **3.68954e-02** *(StdErr: 2e-02 ,initial: 4.64272e-02)*
    * *('s4', 's4')*: rates.k5: **1.92108e-02** *(StdErr: 8e-03 ,initial: 1.92859e-02)*
    * *('s5', 's5')*: rates.kC: **9.90000e+01** *(fixed)*
  

## Irf

* **irf1** (spectral-multi-gaussian):
  * *Label*: irf1
  * *Type*: spectral-multi-gaussian
  * *Center*: [irf.center: **1.19809e+00** *(StdErr: 7e-04 ,initial: 1.20878e+00)*]
  * *Width*: [irf.width: **5.84337e-02** *(StdErr: 4e-04 ,initial: 6.08457e-02)*]
  * *Normalize*: False
  * *Backsweep*: False
  * *Dispersion Center*: irf.dispc: **5.50000e+02** *(fixed)*
  * *Center Dispersion*: [irf.disp1: **3.08957e-01** *(StdErr: 2e-03 ,initial: 3.02102e-01)*, irf.disp2: **-8.33900e-02** *(StdErr: 8e-04 ,initial: -7.74943e-02)*, irf.disp3: **4.66667e-03** *(StdErr: 4e-04 ,initial: 3.75955e-03)*]
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

## Spectral Relations

* 
  * *Compartment*: s2
  * *Target*: s3
  * *Parameter*: rel.r1: **1.00000e+00** *(fixed)*
  * *Interval*: [(0, 1000)]

