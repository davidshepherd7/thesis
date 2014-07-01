#!/usr/bin/env python3

import sys

import scipy as sp
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from scipy import sin, cos, exp, log, pi, sqrt


def make_solution(dim, k, damping, c):
    """Return an exact solution to the llg equation with the requested parameters.
    """

    def solution(x, t): 
        t_scaled = t/(1 + damping**2)

        b = dim*k*k*damping*t_scaled;
        d = sqrt(sin(c)*sin(c)  +  exp(2*b)*cos(c)*cos(c));
        g = (1/damping) * log((d  +  exp(b)*cos(c)) /(1  +  cos(c)));

        return [(1/d) * sin(c) * cos(k*x + g),
                (1/d) * sin(c) * sin(k*x + g),
                (1/d) * cos(c) * exp(b)]

    return solution


def generate_time_plots(cs, save_path, tmax=3.0):

    # Make a figure
    fig, axes = plt.subplots(3, 1, sharex=True)

    # Plot for each c
    for c in cs:
        s = make_solution(1, 2*pi, 0.05, c)

        ts = sp.linspace(0, tmax, 1000)
        ms = [s(0, t) for t in ts]

        ms_split = list(zip(*ms))

        
        axes[0].plot(ts, ms_split[0], label=r"$"+str(c/pi)+r"\pi$")
        axes[1].plot(ts, ms_split[1])
        axes[2].plot(ts, ms_split[2])

    # label it
    axes[0].set_ylabel(r"$m_x$")
    axes[1].set_ylabel(r"$m_y$")
    axes[2].set_ylabel(r"$m_z$")

    axes[0].legend()
    axes[-1].set_xlabel(r"$t$")

    # save it
    fig.savefig(save_path, bbox_inches='tight',
                pad_inches=0.0, transparent=True)


def generate_animations():

    fig2 = plt.figure()

    s = make_solution(1, 2*pi, 0.1, pi/4)

    xs = sp.linspace(0, 1, 50)
    ts = sp.linspace(0, 10, 1000)
    
    ims = []
    for t in ts:
        ims.append(plt.plot(xs, [s(x, t)[0] for x in xs], 'k', label=str(t)))

    im_ani = animation.ArtistAnimation(fig2, ims, interval=50, blit=True)

    plt.show()



def main():

    # generate_time_plots(sp.array([0.1, 0.5, 0.7, 0.9, 0.99, 0.999])*(pi/2))
    generate_time_plots(sp.array([0.1, 0.5, 0.7])*(pi/2),
                        "./exact_solution_parameters.pdf")

    generate_time_plots(sp.array([0.5, 0.99, 0.999])*(pi/2),
                        "./exact_solution_parameters_complex.pdf",
                        tmax=5)

    # numerical errors generate some dynamics in this case:
    # generate_time_plots(sp.array([1])*(pi/2),
    #                     "./exact_solution_parameters_limit.pdf",
    #                     tmax=50)



    # fig2 = generate_animations()
        
    plt.show()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
