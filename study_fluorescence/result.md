| Optimization Result           |                                     |
|-------------------------------|-------------------------------------|
| Number of residual evaluation | 6                                   |
| Number of variables           | 8                                   |
| Number of datapoints          | 45229                               |
| Degrees of freedom            | 45221                               |
| Chi Square                    | 9.01e+07                            |
| Reduced Chi Square            | 1.99e+03                            |
| Root Mean Square Error (RMSE) | 4.46e+01                            |
| RMSE additional penalty       | [array([59.57133119, 44.56693775])] |

# Model

_Megacomplex Types_: decay

## Dataset Groups

* **default**:
  * *Label*: default
  * *residual_function*: non_negative_least_squares
  * *link_clp*: None

## Clp Area Penalties

* 
    * *Source*: s2
    * *Source Intervals*: 
      * [100, 1000]
    * *Target*: s3
    * *Target Intervals*: 
      * [100, 1000]
    * *Parameter*: area.1(1.00e+00, fixed)
    * *Weight*: 0.0016
  
* 
    * *Source*: s2
    * *Source Intervals*: 
      * [100, 1000]
    * *Target*: s4
    * *Target Intervals*: 
      * [100, 1000]
    * *Parameter*: area.1(1.00e+00, fixed)
    * *Weight*: 0.0016
  

## Clp Constraints

* 
    * *Interval*: 
      * [1, 1000]
    * *Target*: s1
  
* 
    * *Interval*: 
      * [1, 680]
    * *Target*: s3
  
* 
    * *Interval*: 
      * [1, 690]
    * *Target*: s4
  

## K Matrix

* **km1**:
    * *Label*: km1
    * *Matrix*: 
      * ('s2', 's1'): kinetic.1(2.00e+00, fixed)
      * ('s5', 's1'): kinetic.2(1.00e-01, fixed)
      * ('s2', 's2'): kinetic.3(6.31e-02±2.85e-03, initial: 6.00e-02)
      * ('s3', 's2'): kinetic.4(2.71e-02±1.25e-02, initial: 2.70e-02)
      * ('s4', 's2'): kinetic.5(5.66e-02±1.29e-02, initial: 5.60e-02)
      * ('s2', 's3'): kinetic.6(3.97e-02±6.22e-03, initial: 3.90e-02)
      * ('s2', 's4'): kinetic.7(1.33e-01±8.41e-03, initial: 1.33e-01)
      * ('s3', 's3'): kinetic.8(1.63e-04±6.11e-03, initial: 1.60e-04)
      * ('s4', 's4'): kinetic.8(1.63e-04±6.11e-03, initial: 1.60e-04)
      * ('s5', 's5'): kinetic.8(1.63e-04±6.11e-03, initial: 1.60e-04)
  

## Initial Concentration

* **input1**:
    * *Label*: input1
    * *Compartments*: 
      * s1
      * s2
      * s3
      * s4
      * s5
    * *Parameters*: 
      * input.1(1.00e+00, fixed)
      * input.0(0.00e+00, fixed)
      * input.0(0.00e+00, fixed)
      * input.0(0.00e+00, fixed)
      * input.0(0.00e+00, fixed)
    * *Exclude From Normalize*: 
  

## Irf

* **irf1** (gaussian):
    * *Label*: irf1
    * *Type*: gaussian
    * *Center*: irf.center(-8.43e+01±3.04e-03, initial: -8.40e+01)
    * *Width*: irf.width(1.55e+00±3.24e-03, initial: 1.55e+00)
    * *Normalize*: True
    * *Backsweep*: True
    * *Backsweep Period*: irf.backsweep(1.32e+04, fixed)
  

## Megacomplex

* **mc1** (None):
    * *Label*: mc1
    * *Dimension*: time
    * *K Matrix*: 
      * km1
  

## Dataset

* **dataset1**:
    * *Label*: dataset1
    * *Group*: default
    * *Megacomplex*: 
      * mc1
    * *Initial Concentration*: input1
    * *Irf*: irf1
  

