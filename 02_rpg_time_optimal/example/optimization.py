import sys
import os
BASEPATH = os.path.abspath(__file__).split('rpg_time_optimal', 1)[0]+'rpg_time_optimal/'
sys.path += [BASEPATH + 'src']
from src.track import Track
from src.quad import Quad
from src.integrator import RungeKutta4
from src.planner import Planner
from src.trajectory import Trajectory
from src.plot import CallbackPlot

track = Track("./tracks/track.yaml")
quad = Quad("./quads/quad.yaml")

cp = CallbackPlot(pos='xy', vel='xya', ori='xyzw', rate='xyz', inputs='u', prog='mn')
planner = Planner(quad, track, RungeKutta4, {'tolerance': 0.3, 'nodes_per_gate': 40, 'vel_guess': 3.0})
planner.setup()
planner.set_iteration_callback(cp)
x = planner.solve()

traj = Trajectory(x, NPW=planner.NPW, wp=planner.wp)
traj.save('./example/result_cpc_format.csv', False)
traj.save('./example/result.csv', True)
