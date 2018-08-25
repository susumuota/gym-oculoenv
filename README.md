# gym-oculoenv

Gym environment class and examples for oculoenv (Oculomotor task environments).


# Links

- OpenAI Gym

https://github.com/openai/gym

- OpenAI Baselines

https://github.com/openai/baselines

- oculoenv by WBAI

https://github.com/wbap/oculoenv


# Install

```
pip install oculoenv

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

# learn. A2C, CNN, 400000 steps, approx 2 hours by CPU.
time python -m baselines.run --alg=a2c --env=PointToTargetSkip-v0 --network=cnn --num_timesteps=400000 --save_path=./ptt.skip.a2c.cnn.400000

# play
time python -m baselines.run --alg=a2c --env=PointToTargetSkip-v0 --network=cnn --num_timesteps=0 --load_path=./ptt.skip.a2c.cnn.400000 --play
```

See https://github.com/openai/baselines#saving-loading-and-visualizing-models


## Available Environments

```
PointToTarget-v0
PointToTargetSkip-v0
PointToTargetSkipNoLureSmall-v0
PointToTargetSkipNoLureLarge-v0
ChangeDetectionContent-v0
ChangeDetectionContentSkip-v0
OddOneOutContent-v0
OddOneOutContentSkip-v0
VisualSearchContent-v0
VisualSearchContentSkip-v0
MultipleObjectTracking-v0
MultipleObjectTrackingSkip-v0
RandomDotMotionDiscrimination-v0
RandomDotMotionDiscriminationSkip-v0
```

`Skip` version of environments may reduce learning time. They skip "move to red cross cursor" part in the experiments.

See https://github.com/susumuota/gym-oculoenv/blob/master/gym_oculoenv/__init__.py for more details.

You can add custom environments. See these pages.

https://github.com/openai/gym/blob/master/gym/envs/README.md
https://github.com/openai/gym/blob/master/gym/envs/__init__.py


## Author

Susumu OTA  susumu dot ota at g mail dot com

