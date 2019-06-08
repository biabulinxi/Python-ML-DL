# -*- coding: utf-8 -*-
# @Project:AID1810
# @Author:biabu
# @Date:2019/4/19 15:05
# @File_name:01_gridWorld.py
# @IDE:PyCharm

"""格子世界，强化学习迭代案例"""

import numpy as np
from gridworld import GridworldEnv

env = GridworldEnv()


def value_iteration(env, theta=0.0001, discount_factor=1.0):
    def one_step_lookahead(state, v):
        A = np.zeros(env.nA)
        for a in range(env.nA):
            for prob, next_state, reword, done in env.P[state][a]:
                A[a] += prob * (reword + discount_factor * v[next_state])  # bellman方程
        return A

    v = np.zeros(env.nS)
    delta = 0
    while delta > theta:
        for s in range(env.nS):
            A = one_step_lookahead(s, v)
            best_action_value = np.max(A)
            delta = max(delta, np.abs(best_action_value - v[s]))
            v[s] = best_action_value

    policy = np.zeros([env.nS, env.nA])

    for s in range(env.nS):
        A = one_step_lookahead(s, v)
        best_action = np.argmax(A)
        policy[s, best_action] = 1.0

    return policy, v


if __name__ == '__main__':
    policy, v = value_iteration(env)
    print("Policy Probability Distribution:")
    print(policy)
    print("")

    print("Reshaped Grid Policy (0=up, 1=right, 2=down, 3=left):")
    print(np.reshape(np.argmax(policy, axis=1), env.shape))
    print("")