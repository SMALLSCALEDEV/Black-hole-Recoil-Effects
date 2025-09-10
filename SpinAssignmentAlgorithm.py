def assign_black_hole_spins(seed_type, formation_environment):
 """
 Assign spin magnitude and orientation based on formation channel
 Parameters:----------
seed_type : str
 ’light’, ’medium’, or ’heavy’ seed classification
 formation_environment : dict
 Halo properties, metallicity, LW flux
 Returns:-------
chi : float
 Dimensionless spin magnitude [0,1]
 theta : float
 Polar angle relative to accretion disk
 phi : float
 Azimuthal angle
 """
 if seed_type == ’light’:
 # Pop III remnants: moderate spins from stellar evolution
 chi = np.random.normal(0.3, 0.2)
 chi = np.clip(chi, 0, 0.98)
 # Random orientation initially
 theta = np.arccos(1- 2*np.random.random())
 phi = 2*np.pi*np.random.random()
elif seed_type == ’heavy’:
 # Direct collapse: low spins from rapid accretion
 chi = np.random.normal(0.1, 0.05)
 chi = np.clip(chi, 0, 0.3)
 # Tend to align with gas inflow
 alignment_factor = calculate_gas_alignment(formation_environment)
 theta = np.random.normal(0, np.pi/4 * (1-alignment_factor))
 phi = 2*np.pi*np.random.random()
 elif seed_type == ’medium’:
 # Stellar collisions: variable spins
 chi = np.random.uniform(0.1, 0.7)
 # Cluster dynamics create random orientations
 theta = np.arccos(1- 2*np.random.random())
 phi = 2*np.pi*np.random.random()
 return chi, theta, phi
