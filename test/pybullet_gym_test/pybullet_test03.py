from gasimulator import GAPhysicsSimulator

sim = GAPhysicsSimulator(display=True)

sim.reset()
#g = [1.1223398342179305, -0.07098984190180832, 0.934183460116191, 0.07233773178762537, 0.8591756086192088, 0.04210142789066196, 0.94796135125632, 0.21589436846535714]
g = [1.2899472369677893, -0.07098984190180832, 1.1287358199087467, -0.008265321543718437, -0.034035529553375035, 0.04210142789066196, 1.0420296798328845, 0.21589436846535714]
f = sim.run_trial(g, time_sec=6000)

sim.finish()