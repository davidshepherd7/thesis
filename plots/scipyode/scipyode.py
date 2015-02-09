#!/usr/bin/env python3

import sys
import argparse
import os
import os.path

import scipy as sp
import scipy.integrate
from scipy.integrate import ode as spode
from scipy.integrate import odeint as spodeint
import matplotlib.pyplot as plt
from matplotlib.pyplot import show, subplots

from os.path import join as pjoin

def f(t, y, omega, beta):
    return -beta * sp.exp(-beta * t) * sp.sin(omega * t) \
        + omega * sp.exp(-beta * t) * sp.cos(omega * t)


def y_exact(t, omega, beta):
    return sp.exp(-beta*t) * sp.sin(omega*t)

initial_dt = 0.1
tol = 5e-5 # 5* oomph's tol to account for safety factor in VODE
omega = 2
beta = 0.1
y0 = 0
tmax = 20


# This is kind of useless because it can't output step sizes...
def main_ode():

    r = spode(f)
    r.set_integrator("vode",
                     rtol=tol,
                     # atol=1e-14, # No atol
                     method="bdf",
                     with_jacobian=False,
                     first_step=initial_dt,
                     order=2
    )
    r.set_f_params(omega, beta)
    r.set_initial_value(y0)

    # We have to use step=True inside a while loop to get all the time step
    # information out of VODE.
    ts = []
    ys = []
    while r.t < tmax:
        r.integrate(tmax, step=True)
        ts.append(r.t)
        ys.append(r.y)

    yerr = [abs(y_exact(t, omega, beta) - y) for t,y in zip(ts, ys)]
    dts = [t2 - t1 for t1, t2 in zip(ts[:-1], ts[1:])]

    fig, ax = subplots(3, 1, sharex=True)

    k = 'g'
    ax[0].plot(ts, yerr, k, label='VODE')
    ax[1].plot(ts[1:], dts, k)
    ax[2].plot(ts, ys, k)



    # Load and plot oomph-lib data
    with open("clean-trace") as oomph_file:
        lines = oomph_file.read().splitlines()

    headers = lines[0].split()
    body = [l.split() for l in lines[1:]]

    oomph_ts = [b[0] for b in body]
    oomph_dts = [b[1] for b in body]
    oomph_errs = [b[2] for b in body]
    oomph_ys = [b[3] for b in body]

    k = 'r'
    ax[0].plot(oomph_ts, oomph_errs, k, label='oomph-lib')
    ax[1].plot(oomph_ts, oomph_dts, k)
    ax[2].plot(oomph_ts, oomph_ys, k)


    # Prettify plot
    ax[0].set_xlim([0, 20])
    ax[2].set_xlabel('$t$')
    ax[0].set_ylabel('$|y(t_n) - y_n|$')
    ax[1].set_ylabel('$\Delta_n$')
    ax[2].set_ylabel('$y_n$')
    ax[0].legend()

    fig.savefig("vode-bdf2.pdf",
                bbox_inches='tight',
                pad_inches=0.0,
                transparent=True)

    # plt.show()

    return 0


if __name__ == "__main__":
    sys.exit(main_ode())
