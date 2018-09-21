# -*- coding: utf-8 -*-

import time
import numpy as np
import gym
import gym.spaces
import gym_oculoenv
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--env', type=str, default='PointToTarget-v0', help='gym environment name. ex) PointToTarget-v0')
    parser.add_argument('--render', action='store_true', help='rendering to display or not.')
    parser.add_argument('--num-episodes', type=int, default=10, help='number of episodes. ex) 10')
    parser.add_argument('--wait', type=int, default=0, help='wait seconds. ex) 0')
    args = parser.parse_args()

    env = gym.make(args.env)
    obs = env.reset()
    total_reward = 0

    for episode in range(1, args.num_episodes+1):
        while True:
            if args.wait > 0:
                time.sleep(args.wait)
            action = env.action_space.sample()
            obs, reward, done, info = env.step(action)
            total_reward += reward
            if args.render:
                env.render()
            if done:
                obs = env.reset()
                print(episode, total_reward, total_reward / episode)
                break

    env.close()

if __name__ == '__main__':
    main()
