import gymnasium as gym

gym.register(
    id="Unitree-G1-29dof-Velocity",
    entry_point="isaaclab.envs:ManagerBasedRLEnv",
    disable_env_checker=True,
    kwargs={
        "env_cfg_entry_point": f"{__name__}.g1:G1EnvCfg",
        "play_env_cfg_entry_point": f"{__name__}.g1:G1PlayEnvCfg",
        "rsl_rl_cfg_entry_point": f"talab.source.envs.agents.rsl_rl_ppo_cfg:GerneralPPORunnerCfg",
    },
)
