
# Class diagrams

- ThresholdConc
- Environment
- Bacteria
- Position


```plantuml
class "Bacteria" as class1
class class2 as "Position"
class class3 as "ThresholdConc"

class class4 as "Environment"
class class5 as "SpinDirection"

class1 *-- class2 : describes
class1 *-- class3 : describes
class1 *-- class5 : describes

class4 o-- class1 : contains

class4 : get_bacteria_positions()


```
