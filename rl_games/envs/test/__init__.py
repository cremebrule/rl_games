import gym

gym.envs.register(
     id='TestRnnEnv-v0',
     entry_point='rl_games.envs.test.rnn_env:TestRNNEnv',
     max_episode_steps=50,
)