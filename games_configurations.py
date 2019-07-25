import networks
import models
import tr_helpers



"""
LR_SCHEDULE: 'ADAPTIVE', 'EXP_DECAY', 'LINEAR_DECAY', 'NONE'
"""

halfcheetah_lstm_config_v2 = {
    'NETWORK' : models.ModelA2CContinuous(networks.simple_a2c_lstm_network_separated),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(scale_value = 1.0 / 10.0),
    'NORMALIZE_ADVANTAGE' : True,
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'LEARNING_RATE' : 1e-4,
    'NAME' : 'robo1',
    'SCORE_TO_WIN' : 2700,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.000,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'RoboschoolHalfCheetah-v1',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'CLIP_VALUE' : True,
    'NUM_ACTORS' : 16,
    'STEPS_NUM' : 256,
    'MINIBATCH_SIZE' : 1024,
    'MINI_EPOCHS' : 4,
    'CRITIC_COEF' : 1,
    'LR_SCHEDULE' : 'ADAPTIVE',
    'LR_THRESHOLD' : 0.02,
    'NORMALIZE_INPUT' : True,
    'SEQ_LEN' : 16,
    'MAX_EPOCHS' : 10000
    }

roboschoolant_config = {
    'NETWORK' : models.ModelA2CContinuous(networks.simple_a2c_network_separated),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(scale_value = 1.0 / 10.0),
    'NORMALIZE_ADVANTAGE' : True,
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'LEARNING_RATE' : 2.5*1e-4,
    'NAME' : 'robo1',
    'SCORE_TO_WIN' : 1800,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.000,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'RoboschoolAnt-v1',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'NUM_ACTORS' : 16,
    'STEPS_NUM' : 256,
    'MINIBATCH_SIZE' : 1024,
    'MINI_EPOCHS' : 4,
    'CRITIC_COEF' : 1,
    'CLIP_VALUE' : True,
    'LR_SCHEDULE' : 'ADAPTIVE',
    'LR_THRESHOLD' : 0.02,
    'NORMALIZE_INPUT' : False,
    'SEQ_LEN' : 16
}


roboschoolhumanoid_config = {
    'NETWORK' : models.ModelA2CContinuous(networks.default_a2c_network_separated),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(scale_value = 1.0 / 10.0),
    'NORMALIZE_ADVANTAGE' : True,
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'LEARNING_RATE' : 1e-4,
    'NAME' : 'robo1',
    'SCORE_TO_WIN' : 5000,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.000,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'RoboschoolHumanoid-v1',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'NUM_ACTORS' : 16,
    'STEPS_NUM' : 256,
    'MINIBATCH_SIZE' : 1024,
    'MINI_EPOCHS' : 4,
    'CRITIC_COEF' : 1,
    'CLIP_VALUE' : True,
    'NORMALIZE_INPUT' : True,
    'LR_SCHEDULE' : 'ADAPTIVE',
    'LR_THRESHOLD' : 0.04,
    'SEQ_LEN' : 8
}

roboschoolhumanoid_lstm_config = {
    'NETWORK' : models.LSTMModelA2CContinuous(networks.default_a2c_lstm_network_separated),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(scale_value = 1.0 / 10.0),
    'NORMALIZE_ADVANTAGE' : True,
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'LEARNING_RATE' : 1e-4,
    'NAME' : 'robo1',
    'SCORE_TO_WIN' : 5000,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.000,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'RoboschoolHumanoid-v1',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'NUM_ACTORS' : 16,
    'STEPS_NUM' : 128,
    'MINIBATCH_SIZE' : 512,
    'MINI_EPOCHS' : 4,
    'CRITIC_COEF' : 1,
    'CLIP_VALUE' : True,
    'LR_SCHEDULE' : 'NONE',
    'NORMALIZE_INPUT' : True,
    'SEQ_LEN' : 8,
}

flagrun_lstm_config = {
    'NETWORK' : models.ModelA2CContinuous(networks.default_a2c_network_separated),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(scale_value = 1.0 / 100.0),
    'NORMALIZE_ADVANTAGE' : True,
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'LEARNING_RATE' : 1e-4,
    'NAME' : 'robo1',
    'SCORE_TO_WIN' : 5000,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.000,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'RoboschoolHumanoidFlagrun-v1',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'NUM_ACTORS' : 16,
    'STEPS_NUM' : 512,
    'MINIBATCH_SIZE' : 1024 * 2,
    'MINI_EPOCHS' : 4,
    'CRITIC_COEF' : 1,
    'CLIP_VALUE' : True,
    'LR_SCHEDULE' : 'NONE',
    'NORMALIZE_INPUT' : True,
    'SEQ_LEN' : 16
}

carracing_config = {
    'NETWORK' : models.ModelA2CContinuous(networks.simple_a2c_network),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(scale_value = 1.0 / 100.0),
    'NORMALIZE_ADVANTAGE' : True,
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'LEARNING_RATE' : 2.5*1e-4,
    'NAME' : 'robo1',
    'SCORE_TO_WIN' : 5000,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.000,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'CarRacing-v0',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'NUM_ACTORS' : 16,
    'STEPS_NUM' : 1024,
    'MINIBATCH_SIZE' : 2048,
    'MINI_EPOCHS' : 8,
    'CRITIC_COEF' : 1,
    'CLIP_VALUE' : True,
    'LR_SCHEDULE' : 'NONE'
}


quadrupped_config = {
    'NETWORK' : models.ModelA2CContinuous(networks.simple_a2c_network),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(scale_value = 1.0 / 100.0),
    'NORMALIZE_ADVANTAGE' : True,
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'LEARNING_RATE' : 1e-4,
    'NAME' : 'robo2',
    'SCORE_TO_WIN' : 450000,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.000,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'QuadruppedWalk-v1',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'NUM_ACTORS' : 16,
    'STEPS_NUM' : 256,
    'MINIBATCH_SIZE' : 1024,
    'MINI_EPOCHS' : 4,
    'CRITIC_COEF' : 1,
    'CLIP_VALUE' : True,
    'LR_SCHEDULE' : 'NONE',
    'NORMALIZE_INPUT' : False,
    'SEQ_LEN' : 16
}


quadrupped_lstm_config = {
    'NETWORK' : models.LSTMModelA2CContinuous(networks.default_a2c_lstm_network),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(scale_value = 1.0 / 100.0),
    'NORMALIZE_ADVANTAGE' : True,
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'LEARNING_RATE' : 1e-4,
    'NAME' : 'robo2',
    'SCORE_TO_WIN' : 450000,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.000,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'QuadruppedWalk-v1',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'NUM_ACTORS' : 16,
    'STEPS_NUM' : 256,
    'MINIBATCH_SIZE' : 1024,
    'MINI_EPOCHS' : 4,
    'CRITIC_COEF' : 1,
    'CLIP_VALUE' : True,
    'LR_SCHEDULE' : 'NONE',
    'NORMALIZE_INPUT' : False,
    'SEQ_LEN' : 8
}

bipedalwalker_config = {
    'NETWORK' : models.ModelA2CContinuous(networks.simple_a2c_network_separated),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(scale_value = 1.0 / 10.0),
    'NORMALIZE_ADVANTAGE' : True,
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'LEARNING_RATE' : 1e-4,
    'NAME' : 'robo1',
    'SCORE_TO_WIN' : 300,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.000,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'BipedalWalker-v2',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'CLIP_VALUE' : True,
    'NUM_ACTORS' : 16,
    'STEPS_NUM' : 16,
    'MINIBATCH_SIZE' : 64,
    'MINI_EPOCHS' : 4,
    'CRITIC_COEF' : 1,
    'LR_SCHEDULE' : 'NONE',
    'MAX_EPOCHS' : 10000,
    'LR_THRESHOLD' : 0.01,
    'NORMALIZE_INPUT' : True,
    'SEQ_LEN' : 16
}

bipedalwalker_lstm_config = {
    'NETWORK' : models.LSTMModelA2CContinuous(networks.default_a2c_lstm_network_separated),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(scale_value = 1.0 / 10.0),
    'NORMALIZE_ADVANTAGE' : True,
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'LEARNING_RATE' : 1e-4,
    'NAME' : 'robo1',
    'SCORE_TO_WIN' : 320,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : -0.000,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'BipedalWalker-v2',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'CLIP_VALUE' : True,
    'NUM_ACTORS' : 16,
    'STEPS_NUM' : 128,
    'MINIBATCH_SIZE' : 512,
    'MINI_EPOCHS' : 4,
    'CRITIC_COEF' : 1,
    'LR_SCHEDULE' : 'ADAPTIVE',
    'LR_THRESHOLD' : 0.08,
    'NORMALIZE_INPUT' : True,
    'SEQ_LEN' : 8
}

bipedalwalkerhardcore_lstm_config = {
    'NETWORK' : models.LSTMModelA2CContinuous(networks.default_a2c_lstm_network_separated),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(scale_value = 1.0 / 10.0),
    'NORMALIZE_ADVANTAGE' : True,
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'LEARNING_RATE' : 1e-4,
    'NAME' : 'robo1',
    'SCORE_TO_WIN' : 320,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.000,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'BipedalWalkerHardcore-v2',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'CLIP_VALUE' : True,
    'NUM_ACTORS' : 24,
    'STEPS_NUM' : 128,
    'MINIBATCH_SIZE' : 1024,
    'MINI_EPOCHS' : 4,
    'CRITIC_COEF' : 1,
    'LR_SCHEDULE' : 'NONE',
    'LR_THRESHOLD' : 0.04,
    'NORMALIZE_INPUT' : True,
    'SEQ_LEN' : 8
}

pendulum_lstm_config = {
    'NETWORK' : models.LSTMModelA2CContinuous(networks.simple_a2c_lstm_network_separated),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(scale_value = 1.0 / 100.0),
    'NORMALIZE_ADVANTAGE' : True,
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'LEARNING_RATE' : 2.5e-5,
    'NAME' : 'robo1',
    'SCORE_TO_WIN' : 0,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.00,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'Pendulum-v0',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'NUM_ACTORS' : 16,
    'STEPS_NUM' : 64,
    'MINIBATCH_SIZE' : 256,
    'MINI_EPOCHS' : 4,
    'CRITIC_COEF' : 1,
    'CLIP_VALUE' : True,
    'LR_SCHEDULE' : 'NONE',
    'LR_THRESHOLD' : 0.75,
    'NORMALIZE_INPUT' : False
}


bipedalwalkerhardcore_config = {
    'NETWORK' : models.ModelA2CContinuous(networks.simple_a2c_network_separated),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(scale_value = 1.0 / 10.0),
    'NORMALIZE_ADVANTAGE' : True,
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'LEARNING_RATE' : 1e-4,
    'NAME' : 'robo1',
    'SCORE_TO_WIN' : 300,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.000,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'BipedalWalkerHardcore-v2',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'CLIP_VALUE' : True,
    'NUM_ACTORS' : 16,
    'STEPS_NUM' : 256,
    'MINIBATCH_SIZE' : 1024,
    'MINI_EPOCHS' : 4,
    'CRITIC_COEF' : 1,
    'LR_SCHEDULE' : 'NONE',
    'LR_THRESHOLD' : 0.008,
    'NORMALIZE_INPUT' : True
}

loonar_config = {
    'NETWORK' : models.ModelA2CContinuous(networks.default_a2c_network),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(scale_value = 1.0 / 10.0),
    'NORMALIZE_ADVANTAGE' : True,
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'LEARNING_RATE' : 1e-4,
    'NAME' : 'robo1',
    'SCORE_TO_WIN' : 5000,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.000,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'LunarLanderContinuous-v2',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'NUM_ACTORS' : 8,
    'STEPS_NUM' : 128,
    'MINIBATCH_SIZE' : 256,
    'MINI_EPOCHS' : 4,
    'CRITIC_COEF' : 1,
    'CLIP_VALUE' : False,
    'LR_SCHEDULE' : 'NONE'
}

mountain_car_cont_config = {
    'NETWORK' : models.ModelA2CContinuous(networks.simple_a2c_network),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(),
    'NORMALIZE_ADVANTAGE' : True,
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'LEARNING_RATE' : 1e-4,
    'NAME' : 'robo1',
    'SCORE_TO_WIN' : 5000,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.001,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'MountainCarContinuous-v0',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'NUM_ACTORS' : 16,
    'STEPS_NUM' : 64,
    'MINIBATCH_SIZE' : 256,
    'MINI_EPOCHS' : 4,
    'CRITIC_COEF' : 1,
    'CLIP_VALUE' : True,
    'LR_SCHEDULE' : 'NONE'
}

pendulum_config = {
    'NETWORK' : models.ModelA2CContinuous(networks.simple_a2c_network),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(scale_value = 1.0 / 100.0),
    'NORMALIZE_ADVANTAGE' : True,
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'LEARNING_RATE' : 1e-4,
    'NAME' : 'robo1',
    'SCORE_TO_WIN' : 0,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.00,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'Pendulum-v0',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'NUM_ACTORS' : 16,
    'STEPS_NUM' : 64,
    'MINIBATCH_SIZE' : 256,
    'MINI_EPOCHS' : 4,
    'CRITIC_COEF' : 1,
    'CLIP_VALUE' : True,
    'LR_SCHEDULE' : 'NONE',
    'LR_THRESHOLD' : 0.75,
    'NORMALIZE_INPUT' : False
}

mountain_car_config = {
    'NETWORK' : models.ModelA2C(networks.simple_a2c_network),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(),
    'NORMALIZE_ADVANTAGE' : True,
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'LEARNING_RATE' : 1e-4,
    'NAME' : 'robo1',
    'SCORE_TO_WIN' : 5000,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.01,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'MountainCar-v0',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'NUM_ACTORS' : 16,
    'STEPS_NUM' : 16,
    'MINIBATCH_SIZE' : 64,
    'MINI_EPOCHS' : 4,
    'CRITIC_COEF' : 1,
    'CLIP_VALUE' : True,
    'LR_SCHEDULE' : 'NONE'
}

cartpole_config = {
    'NETWORK' : models.ModelA2C(networks.simple_a2c_network),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(),
    'NORMALIZE_ADVANTAGE' : True,
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'LEARNING_RATE' : 1e-4,
    'NAME' : 'robo1',
    'SCORE_TO_WIN' : 5000,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.01,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'CartPole-v1',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'NUM_ACTORS' : 16,
    'STEPS_NUM' : 16,
    'MINIBATCH_SIZE' : 64,
    'MINI_EPOCHS' : 4,
    'CRITIC_COEF' : 1,
    'CLIP_VALUE' : True,
    'LR_SCHEDULE' : 'NONE'
}

car_config = {
    'NETWORK' : models.ModelA2CContinuous(networks.atari_a2c_network),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(),
    'NORMALIZE_ADVANTAGE' : True,
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'LEARNING_RATE' : 1e-3,
    'NAME' : 'robo1',
    'SCORE_TO_WIN' : 5000,
    'EPISODES_TO_LOG' : 20, 
    'LIVES_REWARD' : 5,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.000,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'MountainCarContinuous-v0',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'NUM_ACTORS' : 8,
    'STEPS_NUM' : 256,
    'MINIBATCH_SIZE' : 1024,
    'MINI_EPOCHS' : 4,
    'CRITIC_COEF' : 1.0,
    'CLIP_VALUE' : True,
    'LR_SCHEDULE' : 'NONE'
}

atari_pong_config = {
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'NETWORK' : models.ModelA2C(networks.atari_a2c_network),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(),
    'NORMALIZE_ADVANTAGE' : True,
    'LEARNING_RATE' : 1e-4,
    'NAME' : 'pong',
    'SCORE_TO_WIN' : 20,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.01,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'PongNoFrameskip-v4',
    'PPO' : True,
    'E_CLIP' : 0.1,
    'NUM_ACTORS' : 8,
    'STEPS_NUM' : 128,
    'MINIBATCH_SIZE' : 256,
    'MINI_EPOCHS' : 3,
    'CRITIC_COEF' : 1.0,
    'CLIP_VALUE' : True,
    'LR_SCHEDULE' : 'NONE',
    'NORMALIZE_INPUT' : False,
    'SEQ_LEN' : 16
}

atari_pong_config_lstm = {
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'NETWORK' : models.LSTMModelA2C(networks.atari_a2c_network_lstm),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(),
    'NORMALIZE_ADVANTAGE' : True,
    'LEARNING_RATE' : 1e-4,
    'NAME' : 'pong',
    'SCORE_TO_WIN' : 20,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.01,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'PongNoFrameskip-v4',
    'PPO' : True,
    'E_CLIP' : 0.1,
    'NUM_ACTORS' : 8,
    'STEPS_NUM' : 128,
    'MINIBATCH_SIZE' : 256,
    'MINI_EPOCHS' : 3,
    'CRITIC_COEF' : 1.0,
    'CLIP_VALUE' : True,
    'LR_SCHEDULE' : 'NONE',
    'NORMALIZE_INPUT' : False,
    'SEQ_LEN' : 8
}

mario_config_lstm = {
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'NETWORK' : models.LSTMModelA2C(networks.atari_a2c_network_lstm),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(scale_value = 1.0 / 100.0),
    'NORMALIZE_ADVANTAGE' : True,
    'LEARNING_RATE' : 1e-4,
    'NAME' : 'pong',
    'SCORE_TO_WIN' : 100500,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.005,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'SuperMarioBros-v1',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'NUM_ACTORS' : 8,
    'STEPS_NUM' : 128,
    'MINIBATCH_SIZE' : 256,
    'MINI_EPOCHS' : 3,
    'CRITIC_COEF' : 1.0,
    'CLIP_VALUE' : True,
    'LR_SCHEDULE' : 'NONE',
    'NORMALIZE_INPUT' : False,
    'SEQ_LEN' : 8
}

mario_random_config_lstm = {
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'NETWORK' : models.LSTMModelA2C(networks.atari_a2c_network_lstm),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(scale_value = 1.0 / 100.0),
    'NORMALIZE_ADVANTAGE' : True,
    'LEARNING_RATE' : 1e-4,
    'NAME' : 'pong',
    'SCORE_TO_WIN' : 100500,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.005,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'SuperMarioBrosRandomStages-v1',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'NUM_ACTORS' : 16,
    'STEPS_NUM' : 128,
    'MINIBATCH_SIZE' : 1024,
    'MINI_EPOCHS' : 3,
    'CRITIC_COEF' : 1.0,
    'CLIP_VALUE' : True,
    'LR_SCHEDULE' : 'NONE',
    'NORMALIZE_INPUT' : False,
    'SEQ_LEN' : 8
}