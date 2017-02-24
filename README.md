# echo-keyvalue
The research prototype of a versioned key-value store for non-volatile main-memory. 
We thank Katelin Bailey, Luis Ceze and Hank Levy for allowing us to use this code.
For more information on the echo keyvalue store, please read the original paper-

Katelin A. Bailey, Peter Hornyack, Luis Ceze, Steven D. Gribble, and Henry M.
Levy. 2013. Exploring storage class memory with key value stores. In
Proceedings of the 1st Workshop on Interactions of NVM/FLASH with Operating
Systems and Workloads (INFLOW '13). ACM, New York, NY, USA, , Article 4 , 8
pages. DOI=http://dx.doi.org/10.1145/2527792.2527799


## Easy install and run
Use our install and run scripts to make your lives easier!

We have provided a simple install.py which handles installation and cleans of
the individual workloads. To clean and/or build nstore, simply do:

    python install.py [--build] [--clean]

For running echo, use the following commandline
    run.py [-h] [--sim_size SIM_SIZE] echo

Supported simulation sizes: test, small, medium, large


