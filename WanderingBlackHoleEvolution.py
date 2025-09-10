 class WanderingBlackHole:
 """Track evolution of partially ejected black holes"""
 def __init__(self, mass, velocity, halo_properties, ejection_redshift):
 self.mass = mass
 self.velocity = velocity
 self.halo_mass = halo_properties[’mass’]
 self.position = self.sample_initial_position()
 self.redshift = ejection_redshift
 def evolve_timestep(self, dt, halo_evolution):
 """Evolve wandering BH over time step dt"""
 # Update orbital motion
 self.update_orbit(dt, halo_evolution)
 # Apply dynamical friction
 self.apply_dynamical_friction(dt, halo_evolution)
 # Limited gas accretion
 accretion_rate = self.calculate_wanderer_accretion(halo_evolution)
 self.mass += accretion_rate * dt
 # Check for return to center
 if self.distance_from_center() < 0.1 * self.virial_radius():
 return ’RECOALESCED’
 return ’WANDERING’
 def apply_dynamical_friction(self, dt, halo_evolution):
"""Chandrasekhar dynamical friction"""
 # Local dark matter density
 rho_dm = self.local_dm_density()
 # Coulomb logarithm
 ln_Lambda = np.log(halo_evolution[’virial_mass’] / self.mass)
 # Friction force
 G = 4.301e-6 # km^2/s^2 * kpc/Msun
 friction_coeff = 4*np.pi * G**2 * self.mass * rho_dm * ln_Lambda
 # Velocity decay
 velocity_decay = friction_coeff * dt / self.velocity
 self.velocity = max(0.1, self.velocity- velocity_decay)
