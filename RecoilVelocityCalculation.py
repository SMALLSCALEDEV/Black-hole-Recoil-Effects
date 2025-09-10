 def calculate_recoil_velocity(m1, m2, chi1, chi2, theta1, phi1, theta2, phi2):
 """
 Calculate GW recoil using empirical numerical relativity formulas
 Parameters:----------
m1, m2 : float
 Black hole masses in solar masses
 chi1, chi2 : float
 Dimensionless spin magnitudes
 theta1, theta2 : float
 Spin polar angles relative to orbital angular momentum
 phi1, phi2 : float
 Spin azimuthal angles
 Returns:-------
V_recoil : float
 Total recoil velocity in km/s
 V_components : tuple
 (V_mass, V_perp, V_parallel) components
 """
 # Calculate mass ratio parameters
 q = min(m1, m2) / max(m1, m2) # Ensure q <= 1
 eta = m1 * m2 / (m1 + m2)**2 # Symmetric mass ratio
 # Mass-ratio recoil component
A = 1.2e4 # km/s
 B =-0.93
 V_mass = A * eta**2 * (1- q)/(1 + q) * (1 + B * eta)
 # Convert spins to Cartesian coordinates
 chi1_vec = chi1 * np.array([np.sin(theta1)*np.cos(phi1),
 np.sin(theta1)*np.sin(phi1),
 np.cos(theta1)])
 chi2_vec = chi2 * np.array([np.sin(theta2)*np.cos(phi2),
 np.sin(theta2)*np.sin(phi2),
 np.cos(theta2)])
 # In-plane component (perpendicular to L)
 chi_perp = chi1_vec + chi2_vec
 chi_perp[2] = 0 # Remove z-component
 H = 6.9e3 # km/s
 V_perp = H * eta**2 * np.linalg.norm(chi_perp)
 # Out-of-plane component (parallel to L)
 chi_parallel = (chi1_vec- q * chi2_vec)[2] # z-component only
 K = 6.0e4 # km/s
 V_parallel = K * eta**2 * abs(chi_parallel)
 # Total recoil velocity
 V_recoil = np.sqrt(V_mass**2 + V_perp**2 + V_parallel**2)
 return V_recoil, (V_mass, V_perp, V_parallel)
