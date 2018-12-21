# -*- coding: utf-8 -*-

import gym
import gym.spaces
import gym_oculoenv

def main():
    env = gym.make('RandomDotMotionDiscriminationAcc-v0')
    obs = env.reset()
    while True:
        action = env.action_space.sample()
        obs, reward, done, info = env.step(action)
        print(obs)
        if 'result' in info:
            print("result={}".format(info['result']))
            print("reward = {}".format(reward))
            print("reaction step={}".format(info['reaction_step']))
        env.render()
        if done:
            obs = env.reset()
            break
    env.close()

if __name__ == '__main__':
    main()
