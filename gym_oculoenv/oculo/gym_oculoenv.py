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

from collections import Counter
import numpy as np
import gym
import oculoenv

class GymOculoEnv(gym.Env):
    '''see https://github.com/openai/gym/blob/master/gym/core.py'''

    metadata = {'render.modes': ['human']}

    # move 3.33 degrees per step. TODO: too high?
    ACTION_RATE = 3.333333333333333 / 180.0 * np.pi # == 0.05817764173314431
    # from https://github.com/wbap/oculomotor/blob/master/application/agent/__init__.py
    # ACTION_RATE = 0.02

    # move directions
    # NOOP, UP, RIGHT, LEFT, DOWN, UPRIGHT, UPLEFT, DOWNRIGHT, DOWNLEFT
    # 0.7071067811865476 == np.sqrt(2.0) * 0.5
    # see https://github.com/openai/gym/blob/master/gym/envs/atari/atari_env.py
    ACTION_DIRECTIONS = np.array([[0, 0], [0, -1], [-1, 0], [1, 0], [0, 1],
                                  [-0.7071067811865476, -0.7071067811865476],
                                  [ 0.7071067811865476, -0.7071067811865476],
                                  [-0.7071067811865476,  0.7071067811865476],
                                  [ 0.7071067811865476,  0.7071067811865476]
    ])

    def __init__(self, content=None, action_rate=ACTION_RATE, action_directions=ACTION_DIRECTIONS, skip_red_cursor=False, retina=False):
        print(content.__class__.__name__, action_rate, len(action_directions), skip_red_cursor, retina)
        self.env = oculoenv.Environment(content, on_buffer_width=128, skip_red_cursor=skip_red_cursor, retina=retina) if content is not None else oculoenv.RedCursorEnvironment(None, on_buffer_width=128, retina=retina)
        self.actions = action_rate * action_directions
        self.action_space = gym.spaces.Discrete(len(self.actions))
        self.observation_space = gym.spaces.Box(low=0, high=255, shape=(128, 128, 3), dtype=np.uint8)
        self.reward_range = (0, 2)
        self.result_history = []
        np.set_printoptions(suppress=True, precision=4) # TODO

    def step(self, action):
        obs, reward, done, info = self.env.step(self.actions[action])
        info['angle'] = obs['angle']
        if 'result' in info:
            self.result_history.append([reward, info['reaction_step'], 1 if info['result'] == 'success' else 0])
        return obs['screen'], reward, done, info

    def reset(self):
        self._print_status(self.env, self.result_history)
        obs = self.env.reset()
        self.result_history = []
        return obs['screen']

    def render(self, mode='human', close=False):
        return self.env.render(mode, close)

    def seed(self, seed=None):
        '''TODO: seeding'''
        np.random.seed(seed)
        return [seed]

    def _print_status(self, env, result_history):
        l = len(result_history)
        if l > 0:
            history = np.array(result_history)
            total = np.sum(history, axis=0)
            print(env.content.step_count, total, total / l)
            reward_stats = [[reward, count, count / l] for reward, count in sorted(Counter(history[:,0]).items())]
            print(np.array(reward_stats))
