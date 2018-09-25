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
# learn PointToTarget-v0. A2C, CNN, 800000 steps, approx 1 hours by GPU.
time python -m baselines.run --alg=a2c  --env=PointToTarget-v0 --network=cnn  --num_timesteps=800000 --save_path=./save_model/ptt.only.a2c.cnn.800000.pkl

# learn PointToTargetRetina-v0. A2C, CNN, 800000 steps, approx 1.5 hours by GPU.
time python -m baselines.run --alg=a2c --env=PointToTargetRetina-v0 --network=cnn --num_timesteps=800000 --save_path=./save_model/ptt.retina.a2c.cnn.800000.pkl

# learn OddOneOutSkip-v0. A2C, CNN, 3200000 steps, approx 4.5 hours by GPU.
time python -m baselines.run --alg=a2c --env=OddOneOutSkip-v0 --network=cnn --num_timesteps=3200000 --save_path=./save_model/ooo.skip.a2c.cnn.3200000.pkl
```

### `PointToTarget-v0` results

```
timesteps  800000, total rewards 2073, target 54.6%, lure 45.4%, steps 8.05
timesteps 1600000, total rewards 2600, target 98.5%, lure  1.5%, steps 8.24
timesteps 2400000, total rewards 2620, target 97.1%, lure  2.9%, steps 8.12
timesteps 3200000, total rewards 2649, target 94.1%, lure  5.9%, steps 7.91
```

### `PointToTargetRetina-v0` results

```
timesteps  800000, non convergence
timesteps 1600000, total rewards 2506, target 77.2%, lure 22.8%, steps 7.64
timesteps 2400000, total rewards 2616, target 85.8%, lure 14.2%, steps 7.67
timesteps 3200000, total rewards 2618, target 85.7%, lure 14.3%, steps 7.65
```

### `PointToTargetD2-v0` results (difficulty=2)

```
timesteps 3200000, total rewards 2368, target 89.0%, lure 11.0%, steps 8.61
```

### `PointToTargetRetinaD2-v0` results (difficulty=2)

```
timesteps 3200000, total rewards 2352, target 74.1%, lure 25.9%, steps 7.99
```


### Logs

```
time python -m baselines.run --alg=a2c  --env=PointToTarget-v0 --network=cnn  --num_timesteps=0 --play --load_path=./save_model/ptt.only.a2c.cnn.800000.pkl
10800 [ 2073 10799] [1.5459 8.0529]
[[  1.     609.       0.4541]
 [  2.     732.       0.5459]]

time python -m baselines.run --alg=a2c  --env=PointToTarget-v0 --network=cnn  --num_timesteps=0 --play --load_path=./save_model/ptt.only.a2c.cnn.1600000.pkl
10800 [ 2600 10799] [1.9847 8.2435]
[[   1.       20.        0.0153]
 [   2.     1290.        0.9847]]

time python -m baselines.run --alg=a2c  --env=PointToTarget-v0 --network=cnn  --num_timesteps=0 --play --load_path=./save_model/ptt.only.a2c.cnn.2400000.pkl
10800 [ 2620 10796] [1.9714 8.1234]
[[   1.       38.        0.0286]
 [   2.     1291.        0.9714]]

time python -m baselines.run --alg=a2c  --env=PointToTarget-v0 --network=cnn  --num_timesteps=0 --play --load_path=./save_model/ptt.only.a2c.cnn.3200000.pkl
10800 [ 2649 10794] [1.9407 7.9077]
[[   1.       81.        0.0593]
 [   2.     1284.        0.9407]]


time python -m baselines.run --alg=a2c  --env=PointToTargetRetina-v0 --network=cnn  --num_timesteps=0  --play --load_path=./save_model/ptt.retina.a2c.cnn.800000.pkl
10800 [   14 10776] [   1.5556 1197.3333]
[[1.     4.     0.4444]
 [2.     5.     0.5556]]

time python -m baselines.run --alg=a2c  --env=PointToTargetRetina-v0 --network=cnn  --num_timesteps=0  --play --load_path=./save_model/ptt.retina.a2c.cnn.1600000.pkl
10800 [ 2506 10796] [1.7723 7.6351]
[[   1.      322.        0.2277]
 [   2.     1092.        0.7723]]

time python -m baselines.run --alg=a2c  --env=PointToTargetRetina-v0 --network=cnn  --num_timesteps=0  --play --load_path=./save_model/ptt.retina.a2c.cnn.2400000.pkl
10800 [ 2616 10793] [1.858  7.6655]
[[   1.     200.       0.142]
 [   2.    1208.       0.858]]

time python -m baselines.run --alg=a2c  --env=PointToTargetRetina-v0 --network=cnn  --num_timesteps=0  --play --load_path=./save_model/ptt.retina.a2c.cnn.3200000.pkl
10800 [ 2618 10792] [1.8567 7.6539]
[[   1.      202.        0.1433]
 [   2.     1208.        0.8567]]


time python -m baselines.run --alg=a2c --env=PointToTargetD2-v0 --network=cnn --num_timesteps=0 --play --load_path=./save_model/ptt.only.a2c.cnn.3200000.pkl
10800 [ 2368 10794] [1.8899 8.6145]
[[   1.      138.        0.1101]
 [   2.     1115.        0.8899]]


time python -m baselines.run --alg=a2c --env=PointToTargetRetinaD2-v0 --network=cnn --num_timesteps=0 --play --load_path=./save_model/ptt.retina.a2c.cnn.3200000.pkl
10800 [ 2352 10793] [1.7409 7.9889]
[[   1.      350.        0.2591]
 [   2.     1001.        0.7409]]
```


## Available Environments

```
PointToTarget-v0
PointToTargetRetina-v0
PointToTargetSkip-v0
PointToTargetRetinaSkip-v0
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

`Retina` versions simulate human eye's retina images instead of clear images. I copied retina image generation functions from WBAI's oculomotor framework. See this page.

https://github.com/wbap/oculomotor/blob/master/application/functions/retina.py

`RedCursor-v0` is a special environment of "move to red cross cursor" part.

See https://github.com/susumuota/gym-oculoenv/blob/master/gym_oculoenv/__init__.py for more details.

You can add custom environments. See these pages.

https://github.com/openai/gym/blob/master/gym/envs/README.md
https://github.com/openai/gym/blob/master/gym/envs/__init__.py


## Author

Susumu OTA  susumu dot ota at g mail dot com

