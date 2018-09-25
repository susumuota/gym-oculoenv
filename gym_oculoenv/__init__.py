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
    id='PointToTargetRetina-v0',
    entry_point='gym_oculoenv.oculo:GymOculoEnv',
    kwargs={'content': PointToTargetContent(), 'retina': True}
)

register(
    id='PointToTargetSkip-v0',
    entry_point='gym_oculoenv.oculo:GymOculoEnv',
    kwargs={'content': PointToTargetContent(), 'skip_red_cursor': True}
)

register(
    id='PointToTargetRetinaSkip-v0',
    entry_point='gym_oculoenv.oculo:GymOculoEnv',
    kwargs={'content': PointToTargetContent(), 'skip_red_cursor': True, 'retina': True}
)

register(
    id='PointToTargetD0-v0',
    entry_point='gym_oculoenv.oculo:GymOculoEnv',
    kwargs={'content': PointToTargetContent(difficulty=0)}
)

register(
    id='PointToTargetD1-v0',
    entry_point='gym_oculoenv.oculo:GymOculoEnv',
    kwargs={'content': PointToTargetContent(difficulty=1)}
)

register(
    id='PointToTargetD2-v0',
    entry_point='gym_oculoenv.oculo:GymOculoEnv',
    kwargs={'content': PointToTargetContent(difficulty=2)}
)

register(
    id='PointToTargetRetinaD0-v0',
    entry_point='gym_oculoenv.oculo:GymOculoEnv',
    kwargs={'content': PointToTargetContent(difficulty=0), 'retina': True}
)

register(
    id='PointToTargetRetinaD1-v0',
    entry_point='gym_oculoenv.oculo:GymOculoEnv',
    kwargs={'content': PointToTargetContent(difficulty=1), 'retina': True}
)

register(
    id='PointToTargetRetinaD2-v0',
    entry_point='gym_oculoenv.oculo:GymOculoEnv',
    kwargs={'content': PointToTargetContent(difficulty=2), 'retina': True}
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
    kwargs={'content': ChangeDetectionContent(), 'skip_red_cursor': True}
)

register(
    id='ChangeDetectionRetina-v0',
    entry_point='gym_oculoenv.oculo:GymOculoEnv',
    kwargs={'content': ChangeDetectionContent(), 'retina': True}
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
    kwargs={'content': OddOneOutContent(), 'skip_red_cursor': True}
)

register(
    id='OddOneOutRetina-v0',
    entry_point='gym_oculoenv.oculo:GymOculoEnv',
    kwargs={'content': OddOneOutContent(), 'retina': True}
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
    kwargs={'content': VisualSearchContent(), 'skip_red_cursor': True}
)

register(
    id='VisualSearchRetina-v0',
    entry_point='gym_oculoenv.oculo:GymOculoEnv',
    kwargs={'content': VisualSearchContent(), 'retina': True}
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
    kwargs={'content': MultipleObjectTrackingContent(), 'skip_red_cursor': True}
)

register(
    id='MultipleObjectTrackingRetina-v0',
    entry_point='gym_oculoenv.oculo:GymOculoEnv',
    kwargs={'content': MultipleObjectTrackingContent(), 'retina': True}
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
    kwargs={'content': RandomDotMotionDiscriminationContent(), 'skip_red_cursor': True}
)

register(
    id='RandomDotMotionDiscriminationRetina-v0',
    entry_point='gym_oculoenv.oculo:GymOculoEnv',
    kwargs={'content': RandomDotMotionDiscriminationContent(), 'retina': True}
)

# RedCursorEnvironment
register(
    id='RedCursor-v0',
    entry_point='gym_oculoenv.oculo:GymOculoEnv',
    kwargs={'content': None}
)

register(
    id='RedCursorRetina-v0',
    entry_point='gym_oculoenv.oculo:GymOculoEnv',
    kwargs={'content': None, 'retina': True}
)

