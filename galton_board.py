from drop import Drop
import numpy as np


# class for the GaltonBoard
class GaltonBoard:
    __ball_placement = []
    __total_in_col = []
    __ball_drop = []
    __levels = None
    __num_of_balls = None

    # GaltonBoard constructor
    def __init__(self, levels, num_of_balls):
        self.__levels = levels
        self.__num_of_balls = num_of_balls
        self.__ball_placement = np.empty(shape=num_of_balls, dtype=int)
        self.__total_in_col = np.zeros(shape=levels + 1, dtype=int)
        self.__ball_drop = []

    # This method starts dropping given number balls in to the galton board
    def drop_balls(self):
        for x in range(self.__num_of_balls):
            new_drop = Drop(x, self.__levels)
            new_drop.start_drop()
            self.__ball_drop.append(new_drop)

    # This method sets the final placement of the ball in the galton boad
    def set_final_ball_placement(self, index):
        right_drop_tot = self.__ball_drop[index].get_right_drop_total()
        left_drop_tot = self.__ball_drop[index].get_left_drop_total()
        col = None

        # gets the column number that the ball should drop in to.
        if (right_drop_tot > left_drop_tot):
            col = int((self.__levels + 1) / 2 +
                      ((right_drop_tot - left_drop_tot) / 2))
        elif (left_drop_tot > right_drop_tot):
            col = int((self.__levels + 1) / 2 -
                      np.ceil((left_drop_tot - right_drop_tot) / 2))
        else:
            col = int(self.__levels / 2)

        self.__ball_placement[index] = col
        self.__total_in_col[col] += 1

    # This method returns the given ball placement in the galton board.
    def get_ball_placement_of_ball(self, index):
        return self.__ball_placement[index]

    # This method returns an array of all balls in what column of the galton
    # board
    def get_ball_placement_of_all_balls(self):
        return self.__ball_placement

    # This method returns total number of balls in the column of galton board
    def get_total_in_col(self, index):
        return self.__total_in_col[index]

    # This method return an array of number of balls in each column of the
    # galton board
    def get_all(self):
        return self.__total_in_col