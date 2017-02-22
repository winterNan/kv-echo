# echo-keyvalue
The research prototype of a versioned key-value store for non-volatile main-memory. 

## Easy install and run
Use our install and run scripts to make your lives easier!

We have provided a simple install.py which handles installation and cleans of
the individual workloads. To clean and/or build nstore, simply do:

    python install.py [--build] [--clean]

For running either ycsb or tpcc workload with nstore,
    run.py [-h] [--sim_size SIM_SIZE]

Supported simulation sizes: test, small, medium, large


