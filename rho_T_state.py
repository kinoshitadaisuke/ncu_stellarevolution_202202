#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/05/17 01:13:37 (CST) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# output file name
file_eps = 'rho_T_state.eps'
file_png = 'rho_T_state.png'
file_pdf = 'rho_T_state.pdf'
file_ps  = 'rho_T_state.ps'

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
ideal_rad_logx = numpy.linspace (7.0, 10.0, n)
ideal_rad_logy = 3.0 * ideal_rad_logx - 20.73

# making objects "fig" and "ax"
fig = matplotlib.figure.Figure ()
matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax = fig.add_subplot (111)

# axes
ax.set_xlabel (r"$\log (T_c)$")
ax.set_ylabel (r"$\log (\rho_c)$")

# plotting data
ax.plot (ideal_deg_logx, ideal_deg_logy, '-', label=r"$P_{ideal}=P_{deg}$")
ax.plot (ideal_rdeg_logx, ideal_rdeg_logy, '-', label=r"$P_{ideal}=P_{r-deg}$")
ax.plot (deg_rdeg_logx, deg_rdeg_logy, '-', label=r"$P_{deg}=P_{r-deg}$")
ax.plot (ideal_rad_logx, ideal_rad_logy, '-', label=r"$P_{ideal}=10 P_{rad}$")
ax.text (6.0, 3.0, "ideal gas")
ax.text (5.5, 7.0, "degenerate gas")
ax.text (7.0, 11.0, "relativistic degenerate gas")
ax.text (8.5, 4.0, "radiation pressure")
ax.set_title (r"$\rho$-$T$ diagram")
ax.legend ()

# saving file
fig.savefig (file_eps, dpi=450)
fig.savefig (file_pdf, dpi=450)
fig.savefig (file_png, dpi=450)
fig.savefig (file_ps, dpi=450)
