activity diagram for
@startuml

user --> (track trajectory)
(track trajectory) --> (visualize) : includes
(visualize) --> (show bacteria) : includes
(visualize) --> (show nutrient distribution) : includes
user --> (show results)
(visualize) -> (show results) : includes
user --> (error messages)
user --> (start simulation)
(error messages) -> (show results): includes

@enduml