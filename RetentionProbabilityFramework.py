 def calculate_retention_probability(V_recoil, halo_mass, halo_redshift,
 merger_location=’random’):
 """
 Determine retention probability based on recoil vs escape velocity
 Parameters:----------
V_recoil : float
 Recoil velocity in km/s
 halo_mass : float
 Host halo virial mass in solar masses
 halo_redshift : float
 Redshift of merger event
 merger_location : str or float
 ’random’, ’center’, or specific radius in kpc
 Returns:-------
P_retention : float
Probability of black hole retention [0,1]
 merger_radius : float
 Actual merger radius used in calculation
 """
 # Calculate halo properties
 R_vir = virial_radius(halo_mass, halo_redshift)
 # Sample merger location
 if merger_location == ’random’:
 # Assume mergers occur preferentially in inner regions
 r_merger = R_vir * np.random.beta(2, 5) # Peaked at small radii
 elif merger_location == ’center’:
 r_merger = 0.01 * R_vir # Very central
 else:
 r_merger = float(merger_location)
 # Calculate escape velocity at merger location
 # Use NFW profile for dark matter + gas
 V_escape = escape_velocity_NFW(halo_mass, r_merger, halo_redshift)
 # Determine retention probability
 velocity_ratio = V_recoil / V_escape
 if velocity_ratio < 0.5:
 P_retention = 1.0 # Definitely retained
 elif velocity_ratio > 2.0:
 P_retention = 0.0 # Definitely ejected
 else:
 # Smooth transition accounting for orbital mechanics uncertainty
 P_retention = 0.5 * (1 + np.cos(np.pi * (velocity_ratio- 0.5) / 1.5))
 return P_retention, r_merger
 def escape_velocity_NFW(M_vir, r, z):
 """Calculate escape velocity using NFW profile"""
 # Concentration parameter
 c = concentration_parameter(M_vir, z)
 # Characteristic density and radius
 rho_s = M_vir / (4*np.pi * R_s**3 * (np.log(1+c)- c/(1+c)))
 R_s = R_vir / c
 # Enclosed mass within radius r
 x = r / R_s
 M_enc = 4*np.pi * rho_s * R_s**3 * (np.log(1+x)- x/(1+x))
 # Escape velocity
 G = 4.301e-6 # km^2/s^2 * kpc/Msun
 V_escape = np.sqrt(2 * G * M_enc / r)
return V_escape
