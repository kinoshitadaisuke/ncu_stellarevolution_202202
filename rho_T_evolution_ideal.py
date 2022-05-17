#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/05/17 11:44:59 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.constants

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# constants
G  = scipy.constants.G
pi = scipy.pi
K0 = 1.36 * 10**4 # for solar composition
Bn = 0.206       # for n=1.5
Ms = 1.99 * 10**30

# output file name
file_eps = 'rho_T_evo_ideal.eps'
file_png = 'rho_T_evo_ideal.png'
file_pdf = 'rho_T_evo_ideal.pdf'
file_ps  = 'rho_T_evo_ideal.ps'

# number of data points
n = 1000

# border of ideal gas and degenerate gas
ideal_deg_logx = numpy.linspace (5.0, 9.0, n)
ideal_deg_logy = 1.5 * ideal_deg_logx - 4.13

# border of ideal gas and relativistic degenerate gas
ideal_rdeg_logx = numpy.linspace (9.0, 10.0, n)
ideal_rdeg_logy = 3.0 * ideal_rdeg_logx - 17.60

# border of degenerate gas and relativistic degenerate gas
deg_rdeg_logx = numpy.linspace (5.0, 9.0, n)
deg_rdeg_logy = numpy.array ([9.34] * n)

# border of ideal gas and radiation
ideal_rad_logx = numpy.linspace (5.5, 10.0, n)
ideal_rad_logy = 3.0 * ideal_rad_logx - 20.73

# evolutionary track of 0.1 solar mass star
M = 0.1 * Ms
evo_m1_logx = numpy.linspace (5.0, 7.0, n)
evo_m1_logy = 3.0 * evo_m1_logx - 2.0 * numpy.log10 (M) \
    + numpy.log10 (K0**3 / (4.0 * pi * Bn**3 * G**3) )

# evolutionary track of 1 solar mass star
M = 1.0 * Ms
evo_p0_logx = numpy.linspace (5.0, 8.3, n)
evo_p0_logy = 3.0 * evo_p0_logx - 2.0 * numpy.log10 (M) \
    + numpy.log10 (K0**3 / (4.0 * pi * Bn**3 * G**3) )

# evolutionary track of 10 solar mass star
M = 10.0 * Ms
evo_p1_logx = numpy.linspace (5.0, 9.5, n)
evo_p1_logy = 3.0 * evo_p1_logx - 2.0 * numpy.log10 (M) \
    + numpy.log10 (K0**3 / (4.0 * pi * Bn**3 * G**3) )

# evolutionary track of 30 solar mass star
M = 30.0 * Ms
evo_30_logx = numpy.linspace (5.0, 9.5, n)
evo_30_logy = 3.0 * evo_30_logx - 2.0 * numpy.log10 (M) \
    + numpy.log10 (K0**3 / (4.0 * pi * Bn**3 * G**3) )

# making objects "fig" and "ax"
fig = matplotlib.figure.Figure ()
matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax = fig.add_subplot (111)

# axes
ax.set_xlabel (r"$\log (T_c)$")
ax.set_ylabel (r"$\log (\rho_c)$")
ax.set_xlim (6.0, 10.0)
ax.set_ylim (0.0, 13.0)
ax.set_box_aspect (1)

# plotting data
ax.plot (ideal_deg_logx, ideal_deg_logy, '--', label=r"$P_{ideal}=P_{deg}$")
ax.plot (ideal_rdeg_logx, ideal_rdeg_logy, '--', label=r"$P_{ideal}=P_{r-deg}$")
ax.plot (deg_rdeg_logx, deg_rdeg_logy, '--', label=r"$P_{deg}=P_{r-deg}$")
ax.plot (ideal_rad_logx, ideal_rad_logy, '--', label=r"$P_{ideal}=10 P_{rad}$")
ax.plot (evo_m1_logx, evo_m1_logy, '-', label=r"0.1 $M_\odot$ star", lw=3)
ax.plot (evo_p0_logx, evo_p0_logy, '-', label=r"1 $M_\odot$ star", lw=3)
ax.plot (evo_p1_logx, evo_p1_logy, '-', label=r"10 $M_\odot$ star", lw=3)
ax.plot (evo_30_logx, evo_30_logy, '-', label=r"30 $M_\odot$ star", lw=3)
ax.text (7.0, 4.0, "ideal gas")
ax.text (6.5, 8.0, "degenerate gas")
ax.text (7.0, 11.0, "relativistic degenerate gas")
ax.text (8.0, 2.0, "radiation pressure")
ax.set_title (r"evolutionary track on $T$-$\rho$ plane")
ax.legend (bbox_to_anchor=(0.9, 0.5))

# saving file
fig.savefig (file_eps, dpi=450)
fig.savefig (file_pdf, dpi=450)
fig.savefig (file_png, dpi=450)
fig.savefig (file_ps, dpi=450)
