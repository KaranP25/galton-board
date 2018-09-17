from galton_board import GaltonBoard
from simulation import PlotSimulation
import numpy as np
import time
import sys


# main method to run the code
def run_main(ball, levels):
    print("Dropping ", ball, " balls in to the galton board")
    print("Board creation in process...")

    start_time = time.time()
    galton_board = GaltonBoard(levels, ball)  # creates a GaltonBoard object
    galton_board.drop_balls()
    for x in range(ball):
        galton_board.set_final_ball_placement(x)

    end_time = time.time()
    runtime = end_time - start_time  # get the runtime of generatrd data

    print("Board created!")
    print("Time it took: %5.2f" % (runtime), "sec") if(
        runtime > 1) else print("Time it took: %5.2f" % (runtime * 1000), "ms")

    # show the final result on the board
    print("Board result: ", galton_board.get_all())
    print("Generating simulation...")

    plot_sTime = time.time()
    # creating a graphical simulation based on generated data
    max = np.amax(galton_board.get_all())
    simulate = PlotSimulation(ball, levels, max)
    simulate.set_plot_sequence(galton_board.get_ball_placement_of_all_balls())
    simulate.start_making_plot_seq()
    print("Simulation created!")
    plot_eTime = time.time()
    runtime_plot = plot_eTime - plot_sTime
    print("Time it took to plot: %5.2f" % (runtime_plot), "sec") if(runtime_plot > 1) else print("Time it took to plot: %5.2f" % (runtime_plot * 1000), "ms")
    simulate.plot_simulation()  # starts plotting the simulation on graph


# Gets a integer argument of the exercise number
if (len(sys.argv) > 1):
    k = str(sys.argv[1])
    try:
        print("Running Exercise: ", str(k))
        input = int(sys.argv[1])
        if (input > 6 or input <= 0):
            print("Input argument of Exercise #: ", input, " doesn't exist.")
            sys.exit(0)
    except ValueError:
        print("Input argument is not an integer, put a integer argument.")
        sys.exit(0)

    if(int(sys.argv[1]) == 1):
        balls = 100
    elif(int(sys.argv[1]) == 2):
        balls = 1000
    elif(int(sys.argv[1]) == 3):
        balls = 10000
    elif(int(sys.argv[1]) == 4):
        balls = 50000
    elif(int(sys.argv[1]) == 5):
        balls = 100000
    elif(int(sys.argv[1]) == 6):
        balls = 1000000

    levels = 18 # predefined level for the exercise
    run_main(balls, levels)

else:
    # Asking user for input if given no argument in cmd/terminal
    # also checking if user input is valid
    while True:
        try:
            levels = int(
                input("Enter the number of drop levels and board column(e.g: 14): "))
        except ValueError:
            print("Invalid input. Try Again")
        else:
            break

    while True:
        try:
            balls = int(
                input("Enter the number of balls to drop(e.g: 1000): "))
        except ValueError:
            print("Invalid input. Try Again")
        else:
            break

    run_main(balls, levels)