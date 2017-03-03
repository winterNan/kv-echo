# echo-keyvalue
A scalable and efficient key-value store for non-volatile memory (NVM). 

Exploring storage class memory with key value stores. 
Katelin A. Bailey, Peter Hornyack, Luis Ceze, Steven D. Gribble, and Henry M. Levy
Workshop on Interactions of NVM/FLASH with Operating Systems and Workloads (INFLOW '13)

# To build
~~~
    $ cd echo/src
    $ ./make_echo
~~~

# To run :

~~~
    $ cd echo/src
    $ ./run_echo --small [--trace]
~~~

Echo will create a persistent heap in /dev/shm.
To collect the trace of accesses to persistent memory,
make sure you have debugfs mounted in Linux.
