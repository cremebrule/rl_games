import networks
import tr_helpers

roboschoolant_config = {
    'NETWORK' : networks.ModelA2CContinuous(networks.default_a2c_network),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(),
    'NORMALIZE_ADVANTAGE' : True,
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'LEARNING_RATE' : 1e-4,
    'NAME' : 'robo1',
    'SCORE_TO_WIN' : 5000,
    'EPISODES_TO_LOG' : 20, 
    'LIVES_REWARD' : 5,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.000,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'RoboschoolAnt-v1',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'NUM_ACTORS' : 16,
    'STEPS_NUM' : 128,
    'MINIBATCH_SIZE' : 512,
    'MINI_EPOCHS' : 4,
    'CRITIC_COEF' : 1,
}


bipedalwalker_config = {
    'NETWORK' : networks.ModelA2CContinuous(networks.default_a2c_network),
    'REWARD_SHAPER' : tr_helpers.DefaultRewardsShaper(),
    'NORMALIZE_ADVANTAGE' : True,
    'GAMMA' : 0.99,
    'TAU' : 0.9,
    'LEARNING_RATE' : 2.5 * 1e-4,
    'NAME' : 'robo1',
    'SCORE_TO_WIN' : 5000,
    'EPISODES_TO_LOG' : 20, 
    'LIVES_REWARD' : 5,
    'GRAD_NORM' : 0.5,
    'ENTROPY_COEF' : 0.000,
    'TRUNCATE_GRADS' : True,
    'ENV_NAME' : 'BipedalWalker-v2',
    'PPO' : True,
    'E_CLIP' : 0.2,
    'NUM_ACTORS' : 16,
    'STEPS_NUM' : 512,
    'MINIBATCH_SIZE' : 2048,
    'MINI_EPOCHS' : 4,
    'CRITIC_COEF' : 1,
}