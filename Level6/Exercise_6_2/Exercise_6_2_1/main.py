'''
Conduct Multiprocessing on your Monty Hall Simulation
I built this program using my notes as I watched the videos multiple times so please excuse the notes...
'''

import multiprocessing # 1st step: RUN MULTIPLE PROCESSES IN A SINGLE PROCESS.
import time
from montyHall import montyGameFile

# Not multiple threads. multiple PROCESSES (open 5 pychcarms)

# Run Simulation for Monty Hall
# if inputs to this f is more than 1, add more to the arguments tuple...
def montyHallSim(strategy, simulation):
    game = montyGameFile.montyGame()
    listBool = [game.playGame(strategy) for i in range(simulation)]
    return listBool


# Function to interact with input queue and output queue (main process)
# Also Starts an INFINITE LOOP. At each iteration, calls get on input queue
def doWork(input, output): # Input_queue and output_queue
    f, args = input.get(timeout=1) # Unpacking the tuple (function name, parameters). Fully created before processes start. Don't want it to block. If anytime time takes more than 1, stop process.
    res = f(*args) # Call function with list of arguments
    # len(res)... Do this instead below.
    output.put(res)
    # output.put('Done') # In the do work, also seen in the main process
    # Removed as a potential site of slowness (per QuantNet)


def main():
    # Number of Times
    # simulations = 5 # 2000000 WRONG. This should be 10m/processes
    process = [5,3,7,9,11,20,25]

    # (1) Multi-processing:
    ## Start (creates CHILD process) -> Returns a handle (keep this, for stopping later) -> terminate (to save resources; terminates even if still unfinished)
    ## Lecture Modification for RACE CONDITION: List of list(len of the results list in the MAIN process... As soon as len of results = len of original input queue, DONE)

    ### Nutshell: (1) PROGRAM -> Spawn Processes. (2) Children Comms with Main. (3) Main PROGRAM Aggregates
    # GRID COMPUTING - Similar. Multiple Usage. Delegate calc to the grid. Code run by many different computers.

    trial = 0
    for input in process:
        simulationTest = round(10000000/input) # KEY STEP! So that number of target simulations is not increasing with number of process / input
        simulations = simulationTest if (simulationTest * input >= 10000000) else round(10000000/input) + 1

        ###: I. QUEUE II. PROCESS

        # STEP 1: Create Queue Objects
        # POI 1 - QUEUE. Threadsafe / Process-safe. Visible to any process with a handle to this queue
        input_queue = multiprocessing.Queue() # WHAT WE WANT THE PROCESSES TO DO
        output_queue = multiprocessing.Queue() # RESULTS after all the processes finish

        # STEP 2: Process to put on to the Queue
        s = time.time() # how long process takes
        for i in range(input):
            input_queue.put((montyHallSim, (2, simulations)))  # QUEUE (FIFO) ... STACK (LIFO)


        #################################
        ####### Main Process Code #######
        #################################

        # STEP 3: Create n Child Processes. Start FIVE Processes. Function gets called upon starting.
        processList = []  # for join/terminate per tips and tricks
        for i in range(input):
            p = multiprocessing.Process(target=doWork, args = (input_queue, output_queue)) # target = kwarg, function that you want the process to call (doWork). args -> Passed into doWork
            p.start() # kwarg can be as many as you need. Returns a HANDLE for each start.
            processList.append(p)

        # Step 4 (Creates Infinite Loop, monitors output queue). Starts off as empty.
        ## Other processes ARE RUNNING in the background...

        res = []
        while(True):
            # If this is here, will never start
            # r = output_queue.get() # STARTS OFF AS BLOCK. Takes something off of the queue. Just stays here until output queue contains something... Eventually will contain something as it is MULTIPROCESSING
            if len(res) != input: # If contains the word done, DONE (found in do-work process, can be modified to prevent racing problem)
                r = output_queue.get() # [11th hour fix whooo] GET ONLY WHEN NOT EQUAL TO PROCESS. Stop when equal...
                res.append(r) # when it finally contains something, add that to list of results.
            else:
                break

        # Step 5 (stack: difference between terminate/join):
        for process in processList:
            process.join() # Wait till finished, then terminate.

        # FINAL STEP: Print Results
        listResults = [sum(list) / len(list) for list in res]
        aveFinal = 100 * (sum(listResults) / len(listResults))

        e = time.time()

        print(f'Trial #{trial+1}')
        trial = trial + 1

        print(f'# of Process: {input}.')
        print(f'# of Simulations per Process: {simulations}')
        print(f'Total Simulations (Process * Simulations per Process) = {simulations * input}. Error from 10m = ({((simulations * input)/10000000) - 1:.6f}%).')
        print(f'Average of the results: {aveFinal:.6f}%')
        print(f'Time taken: {e-s:.6f} seconds\n')


        # Results Discussion (Try DECREASING (2) and INCREASING (3)):

        # Trial #1
        # # of Process: 5.
        # # of Simulations per Process: 2000000
        # Total Simulations (Process * Simulations per Process) = 10000000. Error from 10m = (0.000000%).
        # Average of the results: 66.668180%
        # Time taken: 42.695091 seconds
        #
        # Trial #2
        # # of Process: 3.
        # # of Simulations per Process: 3333334
        # Total Simulations (Process * Simulations per Process) = 10000002. Error from 10m = (0.000000%).
        # Average of the results: 66.654097%
        # Time taken: 53.569706 seconds
        #
        # Trial #3
        # # of Process: 7.
        # # of Simulations per Process: 1428572
        # Total Simulations (Process * Simulations per Process) = 10000004. Error from 10m = (0.000000%).
        # Average of the results: 66.654243%
        # Time taken: 39.631760 seconds
        #
        # Trial #4
        # # of Process: 9.
        # # of Simulations per Process: 1111112
        # Total Simulations (Process * Simulations per Process) = 10000008. Error from 10m = (0.000001%).
        # Average of the results: 66.680557%
        # Time taken: 38.637873 seconds
        #
        # Trial #5
        # # of Process: 11.
        # # of Simulations per Process: 909091
        # Total Simulations (Process * Simulations per Process) = 10000001. Error from 10m = (0.000000%).
        # Average of the results: 66.698073%
        # Time taken: 38.999461 seconds
        #
        # Trial #6
        # # of Process: 20.
        # # of Simulations per Process: 500000
        # Total Simulations (Process * Simulations per Process) = 10000000. Error from 10m = (0.000000%).
        # Average of the results: 66.677190%
        # Time taken: 40.099970 seconds
        #
        # Trial #7
        # # of Process: 25.
        # # of Simulations per Process: 400000
        # Total Simulations (Process * Simulations per Process) = 10000000. Error from 10m = (0.000000%).
        # Average of the results: 66.687160%
        # Time taken: 40.623043 seconds

    print('VERDICT: Optimal Runtime = 40 Seconds < 150 - 180 seconds in 6_1_3.')



#########################
if __name__ == '__main__':
    main()
