 def enhanced_merger_treatment(bh1_mass, bh1_spins, bh2_mass, bh2_spins,
 halo_properties, merger_type):
 """
 Enhanced merger treatment including GW recoil effects
 Original assumption: All major mergers result in retained BHs
 Enhanced treatment: Account for recoil and retention physics
 """
 if merger_type == ’major’: # mu >= 1/4
 # Calculate recoil velocity
 V_recoil, components = calculate_recoil_velocity(
 bh1_mass, bh2_mass,
 bh1_spins[’chi’], bh2_spins[’chi’],
 bh1_spins[’theta’], bh2_spins[’theta’],
 bh1_spins[’phi’], bh2_spins[’phi’]
 )
 # Determine retention
 P_ret, r_merger = calculate_retention_probability(
 V_recoil, halo_properties[’mass’], halo_properties[’redshift’]
 )
 # Stochastic retention decision
 if np.random.random() < P_ret:
 # Retained: BH remains in nucleus
 final_mass = bh1_mass + bh2_mass
 final_spins = merger_remnant_spin(bh1_mass, bh1_spins,
 bh2_mass, bh2_spins)
 return {
 ’status’: ’retained’,
 ’mass’: final_mass,
 ’spins’: final_spins,
 ’recoil_velocity’: V_recoil,
 ’location’: ’nucleus’
 }
 else:
 # Ejected: becomes wandering BH or leaves system entirely
 wandering_velocity = V_recoil- V_escape
 if wandering_velocity < galaxy_escape_velocity(halo_properties):
 return {
 ’status’: ’wandering’,
’mass’: bh1_mass + bh2_mass,
 ’velocity’: wandering_velocity,
 ’location’: ’halo_outskirts’
 }
 else:
 return {
 }
 ’status’: ’ejected’,
 ’mass’: bh1_mass + bh2_mass,
 ’velocity’: V_recoil,
 ’location’: ’intergalactic_medium’
 elif merger_type == ’minor’: # mu < 1/4
 # Original treatment: only most massive BH retained
 # Enhanced: smaller BH could still affect main BH if close approach
 return original_minor_merger_treatment(bh1_mass, bh2_mass, halo_properties)
