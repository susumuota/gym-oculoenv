# gym-oculoenv

Gym environment class and examples for oculoenv (Oculomotor task environments).


# Links

- OpenAI Gym
https://github.com/openai/gym

- oculoenv by WBAI
https://github.com/wbap/oculoenv

- Psychlab
https://arxiv.org/abs/1801.08116

- OpenAI Baselines
https://github.com/openai/baselines


# Install

```
git clone https://github.com/susumuota/oculoenv.git # not wbap's
cd oculoenv
pip install -e .
cd ..

pip install gym

git clone https://github.com/openai/baselines.git
cd baselines
pip install -e .
cd ..

git clone https://github.com/susumuota/gym-oculoenv.git
cd gym-oculoenv
pip install -e .
cd ..
```


# Uninstall

```
pip uninstall gym-oculoenv
pip uninstall baselines
pip uninstall gym
pip uninstall oculoenv
```


# Example

## simplest random sampling example (no learning)

```python
import gym
import gym.spaces
import gym_oculoenv

def main():
    env = gym.make('PointToTarget-v0')
    obs = env.reset()
    while True:
        action = env.action_space.sample()
        obs, reward, done, info = env.step(action)
        env.render()
        if done:
            obs = env.reset()
            break
    env.close()

if __name__ == '__main__':
    main()
```

## random sampling example (no learning)

```
cd examples
python example_random.py -h
python example_random.py --env=PointToTargetSkip-v0 --render --num_episodes=100
```

## OpenAI Baselines example

```
cd baselines/baselines
cp -p run.py run.py.bak
cp -p ../../gym-oculoenv/examples/example_baselines_run.py run.py
diff -u run.py.bak run.py # or git diff

# learn. A2C, CNN, 400000 steps, approx 2 hours by CPU. 15 minutes by GPU.
time python -m baselines.run --alg=a2c --env=PointToTargetSkip-v0 --network=cnn --num_timesteps=400000 --save_path=./ptt.skip.a2c.cnn.400000.pkl

# play
time python -m baselines.run --alg=a2c --env=PointToTargetSkip-v0 --network=cnn --num_timesteps=0 --load_path=./ptt.skip.a2c.cnn.400000.pkl --play
```

See https://github.com/openai/baselines#saving-loading-and-visualizing-models

## oculoenv example

```
# learn. A2C, CNN, 800000 steps, approx 4 hours by CPU. 30 minutes by GPU.
time python -m baselines.run --alg=a2c  --env=PointToTarget-v0 --network=cnn  --num_timesteps=800000 --save_path=./save_model/ptt.only.a2c.cnn.800000.pkl
```

I added 3 pre-trained models for PointToTarget environment.

```
timesteps  800000, total rewards 2104, target 56.7%, lure 43.3%.
timesteps 1600000, total rewards 2603, target 98.1%, lure  1.9%.
timesteps 2400000, total rewards 2658, target 96.0%, lure  4.0%.
```

```
time python -m baselines.run --alg=a2c  --env=PointToTarget-v0 --network=cnn  --num_timesteps=0 --play --load_path=./save_model/ptt.only.a2c.cnn.800000.pkl
[(1, 582, 0.43335815338793743), (2, 761, 0.5666418466120625)]
1 2104.0 2104.0

time python -m baselines.run --alg=a2c  --env=PointToTarget-v0 --network=cnn  --num_timesteps=0 --play --load_path=./save_model/ptt.only.a2c.cnn.1600000.pkl
[(1, 25, 0.01902587519025875), (2, 1289, 0.9809741248097412)]
1 2603.0 2603.0

time python -m baselines.run --alg=a2c  --env=PointToTarget-v0 --network=cnn  --num_timesteps=0 --play --load_path=./save_model/ptt.only.a2c.cnn.2400000.pkl
[(1, 54, 0.03982300884955752), (2, 1302, 0.9601769911504425)]
1 2658.0 2658.0
```


## Available Environments

```
PointToTarget-v0
PointToTargetRetina-v0
PointToTargetSkip-v0
PointToTargetD0-v0
PointToTargetD1-v0
PointToTargetD2-v0
ChangeDetection-v0
ChangeDetectionSkip-v0
ChangeDetectionRetina-v0
OddOneOut-v0
OddOneOutSkip-v0
OddOneOutRetina-v0
VisualSearch-v0
VisualSearchSkip-v0
VisualSearchRetina-v0
MultipleObjectTracking-v0
MultipleObjectTrackingSkip-v0
MultipleObjectTrackingRetina-v0
RandomDotMotionDiscrimination-v0
RandomDotMotionDiscriminationSkip-v0
RandomDotMotionDiscriminationRetina-v0
RedCursor-v0
RedCursorRetina-v0
```

`Skip` versions of environments may reduce learning time. They skip "move to red cross cursor" part in the experiments.

`Retina` versions simulate human eye's retina images instead of clear images. I copied retina generation functions from WBAI's oculomotor framework. See this page.

https://github.com/wbap/oculomotor/blob/master/application/functions/retina.py

`RedCursor-v0` is a special environment of "move to red cross cursor" part.

See https://github.com/susumuota/gym-oculoenv/blob/master/gym_oculoenv/__init__.py for more details.

You can add custom environments. See these pages.

https://github.com/openai/gym/blob/master/gym/envs/README.md
https://github.com/openai/gym/blob/master/gym/envs/__init__.py


## Author

Susumu OTA  susumu dot ota at g mail dot com

