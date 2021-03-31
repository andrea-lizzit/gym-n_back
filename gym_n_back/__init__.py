from gym.envs.registration import register

register(
	id='2back-v0',
	entry_point='gym_n_back.envs:NBackEnv',
)
register(
	id='nback_hard-v0',
	entry_point='gym_n_back.envs:NBackEnv',
)
