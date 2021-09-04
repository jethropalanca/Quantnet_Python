'''
Conduct Multithreading on your Monty Hall Simulation (BONUS)
'''

'''
import threading
import queue
import time
from montyHall import montyGameFile


# Run Simulation for Monty Hall
# if inputs to this f is more than 1, add more to the arguments tuple...

# ATTEMPT 1: FAIL.

def getThread(q, thread):
    q.put(thread)


def thread_task(strategy, simulation, input):
    s = time.time()  # how long process takes
    game = montyGameFile.montyGame()
    list = [game.playGame(strategy) for _ in range(simulation)]

    listResults = [sum(item) / len(item) for item in list]
    aveFinal = 100 * (sum(listResults) / len(listResults))
    e = time.time()

    print(f'\n# of Process: {input}.')
    print(f'# of Simulations per Process: {simulation}')
    print(f'Total Simulations (Process * Simulations per Process) = {simulation * input}. Error from 10m = ({((simulation * input) / 10000000) - 1:.6f}%).')
    print(f'Average of the results: {aveFinal:.6f}%')

    print(f'Time taken: {e - s:.6f} seconds\n')

    # Thread.
    #########################
    if __name__ == '__main__':

        # Input (Number of Partitions)
        input = 5

        # Number of Times
        simulationTest = round(
            10000000 / input)  # KEY STEP! So that number of target simulations is not increasing with number of process / input
        simulations = simulationTest if (simulationTest * input >= 10000000) else round(10000000 / input) + 1

        # Multi-Threading
        for i in range(input):
            t = threading.Thread(target=thread_task, args=(2, simulations, input))  # target = kwarg, function that you want the process to call (doWork). args -> Passed into doWork
            t.start()  # kwarg can be as many as you need. Returns a HANDLE for each start.
            t.join()
            
'''

import threading
import queue
import time
from montyHall import montyGameFile


# geeksforgeeks:
# A thread contains all this information in a Thread Control Block (TCB):
# Thread Identifier... Unique id (TID) is assigned to every new thread.
# Stack pointer... Points to thread’s stack in the process. Stack contains the local variables under thread’s scope.
# Program counter... a register which stores the address of the instruction currently being executed by thread.
# Thread state... can be running, ready, waiting, start or done.
# Thread’s register set... registers assigned to thread for computations.
# Parent process Pointer... A pointer to the Process control block (PCB) of the process that the thread lives on.


# Run Simulation for Monty Hall
# if inputs to this f is more than 1, add more to the arguments tuple...
def montyHallSim(strategy, simulation):
    game = montyGameFile.montyGame()
    listBool = [game.playGame(strategy) for i in range(simulation)]
    return listBool


# Function to interact with input queue and output queue
# Also Starts an INFINITE LOOP. At each iteration, calls get on input queue
def doWork(q):  # Input_queue and output_queue
    f, args = q.get(timeout=1)  # Unpacking the tuple (function name, parameters). Don't want it to block. If anytime time takes more than 1, stop process.
    res = f(*args)  # Call function with list of arguments
    q.put(res)


def main():
    # Number of Times
    # simulations = 5 # 2000000 WRONG. This should be 10m/thread
    thread = [5, 3, 9, 20, 25] # Less threads as this takes longer.

    trial = 0
    for input in thread:

        # Get # of Simulations
        simulationTest = round(10000000 / input)  # KEY STEP! So that number of target simulations is not increasing with number of process / input
        simulations = simulationTest if (simulationTest * input >= 10000000) else round(10000000 / input) + 1

        # STEP 1: Create Queue Objects
        # POI 1 - QUEUE. Threadsafe / Process-safe. Visible to any process with a handle to this queue
        q = queue.Queue()  # WHAT WE WANT THE PROCESSES TO DO. 1 queue allowed the process to execute vs having an input and output queue (trial and error)

        # STEP 2: Process to put on to the Queue
        s = time.time()  # how long process takes
        for i in range(input):
            q.put((montyHallSim, (2, simulations)))  # QUEUE (FIFO) ... STACK (LIFO)

        #################################
        ####### Main Thread Code #######
        #################################

        # STEP 3: Create n Child Threads. Start FIVE Threads. Function gets called upon starting.
        threads = []  # for join/terminate per tips and tricks
        for i in range(input):
            t = threading.Thread(target=doWork, args=(q,))  # target = kwarg, function that you want the thread to call (doWork). args -> Passed into doWork
            t.start()  # kwarg can be as many as you need. Returns a HANDLE for each start.
            threads.append(t)

        # Step 4 (Creates Infinite Loop, monitors output queue). Starts off as empty.

        res = []
        while (True):
            # If this is here, will never start
            # r = output_queue.get() # STARTS OFF AS BLOCK. Takes something off of the queue. Just stays here until output queue contains something... Eventually will contain something as it is multi-threading
            if len(res) != input:  # If contains the word done, DONE (found in do-work, can be modified to prevent racing problem)
                r = q.get()  # [11th hour fix whooo] GET ONLY WHEN NOT EQUAL TO thread. Stop when equal...
                res.append(r)  # when it finally contains something, add that to list of results.
            else:
                break

        # Step 5
        # Step 5 (stack: difference between terminate/join):
        # for t in threading.enumerate():
        #     t.join()  # Wait till finished, then terminate.
        q.task_done()

        # FINAL STEP: Print Results
        listResults = [sum(list) / len(list) for list in res]
        aveFinal = 100 * (sum(listResults) / len(listResults))

        e = time.time()

        print(f'Trial #{trial + 1}')
        trial = trial + 1

        print(f'# of Threads: {input}.')
        print(f'# of Simulations per Threads: {simulations}')
        print(f'Total Simulations (Threads * Simulations per Threads) = {simulations * input}. Error from 10m = ({((simulations * input) / 10000000) - 1:.6f}%).')
        print(f'Average of the results: {aveFinal:.6f}%')
        print(f'Time taken: {e - s:.6f} seconds\n')


    # Results Discussion (Try DECREASING (2) and INCREASING (3)):

    # Trial #1
    # # of Threads: 5.
    # # of Simulations per Threads: 2000000
    # Total Simulations (Threads * Simulations per Threads) = 10000000. Error from 10m = (0.000000%).
    # Average of the results: 66.679660%
    # Time taken: 124.206677 seconds
    #
    # Trial #2
    # # of Threads: 3.
    # # of Simulations per Threads: 3333334
    # Total Simulations (Threads * Simulations per Threads) = 10000002. Error from 10m = (0.000000%).
    # Average of the results: 66.674717%
    # Time taken: 117.118245 seconds
    #
    # Trial #3
    # # of Threads: 7.
    # # of Simulations per Threads: 1428572
    # Total Simulations (Threads * Simulations per Threads) = 10000004. Error from 10m = (0.000000%).
    # Average of the results: 66.637483%
    # Time taken: 115.596147 seconds
    #
    # Trial #4
    # # of Threads: 9.
    # # of Simulations per Threads: 1111112
    # Total Simulations (Threads * Simulations per Threads) = 10000008. Error from 10m = (0.000001%).
    # Average of the results: 66.682377%
    # Time taken: 137.315382 seconds
    #
    # Trial #5
    # # of Threads: 11.
    # # of Simulations per Threads: 909091
    # Total Simulations (Threads * Simulations per Threads) = 10000001. Error from 10m = (0.000000%).
    # Average of the results: 66.672083%
    # Time taken: 119.960525 seconds
    #
    # Trial #6
    # # of Threads: 20.
    # # of Simulations per Threads: 500000
    # Total Simulations (Threads * Simulations per Threads) = 10000000. Error from 10m = (0.000000%).
    # Average of the results: 66.641340%
    # Time taken: 120.251590 seconds
    #
    # Trial #7
    # # of Threads: 25.
    # # of Simulations per Threads: 400000
    # Total Simulations (Threads * Simulations per Threads) = 10000000. Error from 10m = (0.000000%).
    # Average of the results: 66.656170%
    # Time taken: 120.279265 seconds

    # Comparison with Multi-processing:
    # (1) 3x Slower (120 seconds vs. 40 seconds for Multi-processing). This shows how multi-threading is merely an illusion and shows the drag of GIL.
    # (2) Also plateaus after a certain point (120 seconds optimal run time)
    # (3) Not as consistent: We got 137 seconds run time for 9 Threads when we have less for other runs greater than 5.

    print('VERDICT: Optimal Runtime = 120 Seconds < 150 - 180 seconds in 6_1_3.')


#########################
if __name__ == '__main__':
    main()




