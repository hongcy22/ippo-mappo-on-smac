from runner import Runner
from smac.env import StarCraft2Env
from common.arguments import get_mixer_args, get_common_args
import os

if __name__ == '__main__':
    os.environ['CUDA_VISIBLE_DEVICES'] = '0'

    args = get_common_args()
    args = get_mixer_args(args)
    env = StarCraft2Env(map_name=args.map,
                        step_mul=args.step_mul,
                        difficulty=args.difficulty,
                        game_version=args.game_version,
                        replay_dir=args.replay_dir)
    env_info = env.get_env_info()
    args.n_actions = env_info["n_actions"]
    args.n_agents = env_info["n_agents"]
    args.state_shape = env_info["state_shape"]
    args.obs_shape = env_info["obs_shape"]
    args.episode_limit = env_info["episode_limit"]
    args.last_action = bool(args.last_action)
    args.reuse_network = bool(args.reuse_network)
    args.learn = bool(args.learn)

    runner = Runner(env, args)
    if args.learn:
        runner.run()  # add num=0 means the different time to run
    else:
        win_rate, _ = runner.evaluate()
        print('The win rate of {} is  {}'.format(args.alg, win_rate))
    env.close()
