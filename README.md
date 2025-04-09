# ippo-mappo-on-smac

A simple try for multi-agent algorithm on SMAC, the StarCraft environment.

## Preparations

need torch, smac enviroment.(see as [samc](https://zhuanlan.zhihu.com/p/595500237))

## Run an experiment

python3 main.py --map=3m --alg=ippo

## Saving models and results

You can set the `model_dir` and `result_dir`, which can be found in `./common/arguments.py`. By default, all of the results and models are saved in `./model`.

## Replay

If you want to see the replay, make sure the `replay_dir` is an absolute path, which can be set in `./common/arguments.py.` Then the replays of each evaluation will be saved, you can find them in your path.
