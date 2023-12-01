activity diagram for
@startuml

|user|
start
:ask for trajectory;
|program|
:collect data;
if (found error?) then (yes)
|user|
:return error message;
stop
else (no)
|program|
:farvel;
endif
|user|
stop

@enduml