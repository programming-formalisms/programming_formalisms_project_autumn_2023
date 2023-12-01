
- User wants to start
- predetermined number of generations? or death, whichever comes first.
- press the start button
- simulation runs
- simulation ends: 3 subcases? 1. when the user decides to stop, 2. when a time limit is reached, 3. when nutrients are exhausted
- results printed to screen

```plantuml

skin rose
title Repeat - Use-case Diagram

start
repeat
  :Start simulations;
  :Initialize earth;
  repeat
  :Calculate position;
  :Sense environment;
  :Decide motion;
  :Move to new postion;
  repeat while(there are resources left And limit time is not reached)
    :Print results to screen;
    :Print results to file;
    :Plot the figure;
    :Ask if the user would like "to play again?";
  repeat while(User selects "yes");
stop

```
