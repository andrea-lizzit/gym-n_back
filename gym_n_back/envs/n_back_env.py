import gym
from gym import error, spaces, utils
from collections import deque

import numpy as np
class NBackEnv(gym.Env):
	metadata = {'render.modes': ['human']}
	def __init__(self):
		self.num_actions = 4
		self.n = 2
		# self.observation_space = spaces.Tuple((spaces.Discrete(self.num_actions),))
		self.observation_space = spaces.Box(0, self.num_actions, shape=(1,), dtype=np.float32)
		self.action_space = spaces.Discrete(self.num_actions)
		self.time = 0
		self.max_time = 100
		self.reset()
	def step(self, action):
		self.action = action
		reward = self._get_reward()
		self.history.append(self.observation_space.sample())
		self.time += 1
		episode_over = self.time >= self.max_time
		return self.history[-1], reward, episode_over, {}
	def _get_reward(self):
		""" reward is weighed in order for the expected value to be 0 for a random policy. """
		if self.action == int(self.history[0]):
			return self.num_actions - 1
		else:
			return -1
	def _reset(self):
		self.history = deque([], self.n)
		for x in range(self.n):
			self.history.append(self.observation_space.sample())
		self.time = 0
		return self.history[-1]
	def reset(self):
		return self._reset()
	def render(self, mode='human'):
		pass
	def close(self):
		pass
