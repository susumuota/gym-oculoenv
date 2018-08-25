# -*- coding: utf-8 -*-

# Copyright 2018 Susumu OTA
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np
import gym
import oculoenv

class GymOculoEnv(gym.Env):
    '''see https://github.com/openai/gym/blob/master/gym/core.py'''

    metadata = {'render.modes': ['human']}

    # move 3.33 degrees per step. TODO: too high?
    DELTA = 3.333333333333333 / 180.0 * np.pi

    # move directions
    # NOOP, UP, RIGHT, LEFT, DOWN, UPRIGHT, UPLEFT, DOWNRIGHT, DOWNLEFT
    # 0.7071067811865476 == np.sqrt(2.0) * 0.5
    # see https://github.com/openai/gym/blob/master/gym/envs/atari/atari_env.py
    ACTIONS = np.array([[0, 0], [0, -1], [-1, 0], [1, 0], [0, 1],
                        [-0.7071067811865476, -0.7071067811865476],
                        [ 0.7071067811865476, -0.7071067811865476],
                        [-0.7071067811865476,  0.7071067811865476],
                        [ 0.7071067811865476,  0.7071067811865476]
    ])

    def __init__(self, content=None, delta=DELTA, actions=ACTIONS, skip_fixation_point=False):
        print(content.__class__.__name__, delta, len(actions), skip_fixation_point)
        self.env = oculoenv.Environment(content)
        self.delta_actions = delta * actions
        self.skip_fixation_point = skip_fixation_point
        self.action_space = gym.spaces.Discrete(len(self.delta_actions))
        self.observation_space = gym.spaces.Box(low=0, high=255, shape=(128, 128, 3), dtype=np.uint8)
        self.reward_range = (0, 2)
        self.last_reward_step = 0
        self.reward_history = []

    def step(self, action):
        obs, reward, done, info = self.env.step(self.delta_actions[action])
        if reward != 0:
            self.reward_history.append([reward, self.env.content.step_count - self.last_reward_step])
            self.last_reward_step = self.env.content.step_count
        if self.skip_fixation_point and self._is_start_phase(self.env):
            obs, _, done, info = self._step_to_center(self.env, obs) # skip!!! don't update reward!
        return obs['screen'], reward, done, { 'angle': obs['angle'] }

    def reset(self):
        self._print_status(self.env, self.reward_history)
        obs = self.env.reset()
        self.last_reward_step = 0
        self.reward_history = []
        if self.skip_fixation_point and self._is_start_phase(self.env):
            obs, reward, done, info = self._step_to_center(self.env, obs) # skip!!!
        return obs['screen']

    def render(self, mode='human', close=False):
        return self.env.render(mode, close)

    def seed(self, seed=None):
        '''TODO: seeding'''
        np.random.seed(seed)
        return [seed]

    def _step_to_center(self, env, obs):
        '''this is a cheat code.'''
        return env.step([-obs['angle'][0], -obs['angle'][1]])

    def _is_start_phase(self, env):
        if type(env.content) is oculoenv.ChangeDetectionContent:
            return env.content.current_phase == env.content.start_phase
        else:
            return env.content.phase == 0 # PHASE_START == 0

    def _print_status(self, env, reward_history):
        reward_history_len = len(reward_history)
        if reward_history_len > 0:
            total = np.sum(np.array(reward_history), axis=0)
            print(env.content.step_count, reward_history_len, total, total / reward_history_len)
