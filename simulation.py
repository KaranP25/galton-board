import matplotlib
#import warnings
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from matplotlib import animation
import numpy as np
np.set_printoptions(threshold=np.nan)  # prints full array


# class for plotting simulation of the galton board
class PlotSimulation():
    fig = None
    _max_in_col = None
    _x = None
    _y = None
    _num_of_balls = None
    _levels = None
    _ball_seq = None
    data = None

    # # Setting up the exporting of the simulation/plot to a video file
    # Writer = animation.writers['ffmpeg']
    # writer = Writer(fps=180, metadata=dict(artist='Me'), bitrate=500)
    # warnings.filterwarnings("ignore", category=UserWarning,
    # module="matplotlib") ## filters warnings from the terinal

    # constructor
    def __init__(self, num_of_balls, levels, max_in_col):
        self.fig = plt.figure(figsize=(10, 8))
        self._x = np.arange(1, levels + 2)
        self._y = np.zeros(levels + 1, dtype=float)
        self._num_of_balls = num_of_balls
        self._levels = levels
        self._max_in_col = max_in_col
        self.data = []

    # This method sets the sequence of the ball dropping in which column
    def set_plot_sequence(self, ball_seq_of_ball):
        self._ball_seq = ball_seq_of_ball

    # This method returns a array that is evenly spaced out after increasing
    # by 1 in given column number
    def plot_data_change(self, curr_data, col):
        #print('@@@@@@@@: ', curr_data)
        datax = np.column_stack([np.linspace(curr_data[yi], curr_data[yi] + 1, 5 if(self._num_of_balls <= 1001) else 2) if yi ==
                                 col else np.linspace(curr_data[yi], curr_data[yi], 5 if(self._num_of_balls <= 1001) else 2) for yi in range(len(curr_data))])
        return datax

    # This method starts making the sequence of the plot animation as the
    # balls drop
    def start_making_plot_seq(self):
        self.data = self.plot_data_change(self._y, self._ball_seq[0])
        if(self._num_of_balls <= 1000):
            for xd in range(1, (len(self._ball_seq))):
                y = self.data[len(self.data) - 1, :]
                s = self.plot_data_change(y, self._ball_seq[xd])
                self.data = np.append(self.data, s, axis=0)
        else:
            for xd in range(1, len(self._ball_seq)):
                temp = np.array(self.data[len(self.data) - 1, :])
                temp[self._ball_seq[xd]] += 1
                self.data = np.append(self.data, [temp], axis=0)
        # print(len(data))

    # This method plots the data on a matplotlib graph
    def plot_simulation(self):
        try:
            print("Graphical Simulation in process...")
            rects = plt.bar(self._x, self.data[len(
                self.data) - 1, :], color='#1b685b')

            plt.ylim(0, self._max_in_col + 5)
            plt.title('%s Balls Dropping Simulation' %
                      self._num_of_balls, fontsize=28, style='italic')
            # Used to animate the plot

            def animate(i):
                rok = self.data[len(self.data) - 1, :]
                for rect, yi in zip(rects, self.data[i]):
                    rect.set_height(yi)
                return rects

            anim = animation.FuncAnimation(self.fig, animate, frames=len(
                self.data), interval=1, blit=True, repeat=False)

            # anim.save('%s.mp4' % self._num_of_balls , writer="writer") # for
            # exporting plot

            plt.show()
            plt.close()

            if plt.get_fignums():
                print("Running Plot")
            else:
                print("Plotting window closed")

        except:
            plt.close('all')
            print("\n PLOTTING WINDOW CLOSED")