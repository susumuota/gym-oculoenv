from gym.envs.registration import register
from oculoenv import PointToTargetContent, ChangeDetectionContent, OddOneOutContent, VisualSearchContent, MultipleObjectTrackingContent, RandomDotMotionDiscriminationContent

# see https://github.com/wbap/oculoenv/blob/master/examples/example_display.py

# PointToTarget
register(
    id='PointToTarget-v0',
    entry_point='gym_oculoenv.oculo:GymOculoEnv',
    kwargs={'content': PointToTargetContent(target_size='small', use_lure=True, lure_size='large')}
)

register(
    id='PointToTargetSkip-v0',
    entry_point='gym_oculoenv.oculo:GymOculoEnv',
    kwargs={'content': PointToTargetContent(target_size='small', use_lure=True, lure_size='large'), 'skip_fixation_point': True}
)

register(
    id='PointToTargetSkipNoLureSmall-v0',
    entry_point='gym_oculoenv.oculo:GymOculoEnv',
    kwargs={'content': PointToTargetContent(target_size='small', use_lure=False, lure_size='large'), 'skip_fixation_point': True}
)

register(
    id='PointToTargetSkipNoLureLarge-v0',
    entry_point='gym_oculoenv.oculo:GymOculoEnv',
    kwargs={'content': PointToTargetContent(target_size='large', use_lure=False, lure_size='large'), 'skip_fixation_point': True}
)

# ChangeDetection
register(
    id='ChangeDetection-v0',
    entry_point='gym_oculoenv.oculo:GymOculoEnv',
    kwargs={'content': ChangeDetectionContent(target_number=2, max_learning_count=20, max_interval_count=10)}
)

register(
    id='ChangeDetectionSkip-v0',
    entry_point='gym_oculoenv.oculo:GymOculoEnv',
    kwargs={'content': ChangeDetectionContent(target_number=2, max_learning_count=20, max_interval_count=10), 'skip_fixation_point': True}
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

