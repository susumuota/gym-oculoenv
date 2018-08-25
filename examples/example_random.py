# -*- coding: utf-8 -*-

import numpy as np
import gym
import gym_oculoenv
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--env', type=str, default='PointToTarget-v0', help='gym environment name. ex) PointToTarget-v0')
    parser.add_argument('--render', action='store_true', help='rendering to display or not.')
    parser.add_argument('--num-episodes', type=int, default=10000, help='number of episodes. ex) 10000')
    args = parser.parse_args()

    env = gym.make(args.env)
    obs = env.reset()
    total_reward = 0

    for episode in range(1, args.num_episodes+1):
        while True:
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
