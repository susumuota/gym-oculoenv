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

    def __init__(self, content=None, delta=DELTA, actions=ACTIONS, skip_red_cursor=False):
        print(content.__class__.__name__, delta, len(actions), skip_red_cursor)
        self.env = oculoenv.Environment(content, skip_red_cursor=skip_red_cursor) if content is not None else oculoenv.RedCursorEnvironment(None)
        self.delta_actions = delta * actions
        self.action_space = gym.spaces.Discrete(len(self.delta_actions))
        self.observation_space = gym.spaces.Box(low=0, high=255, shape=(128, 128, 3), dtype=np.uint8)
        self.reward_range = (0, 2)

    def step(self, action):
        obs, reward, done, info = self.env.step(self.delta_actions[action])
        return obs['screen'], reward, done, { 'angle': obs['angle'] }

    def reset(self):
        obs = self.env.reset()
        return obs['screen']

    def render(self, mode='human', close=False):
        return self.env.render(mode, close)

    def seed(self, seed=None):
        '''TODO: seeding'''
        np.random.seed(seed)
        return [seed]
