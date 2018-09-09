from gym.envs.registration import register
from oculoenv import PointToTargetContent, ChangeDetectionContent, OddOneOutContent, VisualSearchContent, MultipleObjectTrackingContent, RandomDotMotionDiscriminationContent

# see https://github.com/wbap/oculoenv/blob/master/examples/example_display.py

# PointToTarget
register(
    id='PointToTarget-v0',
    entry_point='gym_oculoenv.oculo:GymOculoEnv',
    kwargs={'content': PointToTargetContent()}
)

register(
    id='PointToTargetSkip-v0',
    entry_point='gym_oculoenv.oculo:GymOculoEnv',
    kwargs={'content': PointToTargetContent(), 'skip_fixation_point': True}
)

# ChangeDetection
register(
    id='ChangeDetection-v0',
    entry_point='gym_oculoenv.oculo:GymOculoEnv',
    kwargs={'content': ChangeDetectionContent()}
)

register(
    id='ChangeDetectionSkip-v0',
    entry_point='gym_oculoenv.oculo:GymOculoEnv',
    kwargs={'content': ChangeDetectionContent(), 'skip_fixation_point': True}
)

# OddOneOut
register(
    id='OddOneOut-v0',
    entry_point='gym_oculoenv.oculo:GymOculoEnv',
    kwargs={'content': OddOneOutContent()}
)

register(
    id='OddOneOutSkip-v0',
    entry_point='gym_oculoenv.oculo:GymOculoEnv',
    kwargs={'content': OddOneOutContent(), 'skip_fixation_point': True}
)

# VisualSearch
register(
    id='VisualSearch-v0',
    entry_point='gym_oculoenv.oculo:GymOculoEnv',
    kwargs={'content': VisualSearchContent()}
)

register(
    id='VisualSearchSkip-v0',
    entry_point='gym_oculoenv.oculo:GymOculoEnv',
    kwargs={'content': VisualSearchContent(), 'skip_fixation_point': True}
)

# MultipleObjectTracking
register(
    id='MultipleObjectTracking-v0',
    entry_point='gym_oculoenv.oculo:GymOculoEnv',
    kwargs={'content': MultipleObjectTrackingContent()}
)

register(
    id='MultipleObjectTrackingSkip-v0',
    entry_point='gym_oculoenv.oculo:GymOculoEnv',
    kwargs={'content': MultipleObjectTrackingContent(), 'skip_fixation_point': True}
)

# RandomDotMotionDiscrimination
register(
    id='RandomDotMotionDiscrimination-v0',
    entry_point='gym_oculoenv.oculo:GymOculoEnv',
    kwargs={'content': RandomDotMotionDiscriminationContent()}
)

register(
    id='RandomDotMotionDiscriminationSkip-v0',
    entry_point='gym_oculoenv.oculo:GymOculoEnv',
    kwargs={'content': RandomDotMotionDiscriminationContent(), 'skip_fixation_point': True}
)

# RedCursorEnvironment
register(
    id='RedCursor-v0',
    entry_point='gym_oculoenv.oculo:GymOculoEnv',
    kwargs={'content': None}
)

