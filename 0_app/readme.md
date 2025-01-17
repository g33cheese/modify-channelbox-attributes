## **Introduction**
**App** is a rig performance evaluation tool. 

It applies randomized animation to rig controls, runs Maya's evaluation toolkit: validation to provide a performance read out in fps for the rig in DG, serial and parallel evaluation modes.

The App takes user specified input on how many times to run the eval toolkit validator and then averages the results in its output. Default will be 3 times. 
> The first set of values are always thrown out as Maya is doing some extra calculations/caching that causes disparity in its initial DG output. If user specifies 3 for the rig to be evaluated 3 times, it will actually be run four times.  
