# Reinforcement Learning homework

The aim of this project is to answer the questions of the Reinforcement Learning homework by completing the following tasks:
1. Implement efficiently the Fibonacci computation using recursion :white_check_mark:
3. Solve the Arsène Lupin problem with dynamic programming :white_check_mark:
4. Implement Puissance 4 game through Q-learning :white_check_mark:

## Dynamic programming

Prove that:

$$V_\pi(s) = \mathbb{E}_\pi[R(s, \pi(s)] + \sum_{s^\prime \in S} P(s^\prime| s, \pi(s))V_\pi(s^\prime)$$

Let us define the following notations:

* $s$ : a state
* $a$ : an action
* $S_{t}$ : state at time t
* $R(S_{t})$ : reward at time t that depends on $S_{t}$
* $\pi(a|s)$ : probability of choosing the action $a$ in the state $s$ under the stochastic policy $\pi$
* $\mathbb{P}(s',r| s,a)$ : probability of going to state $s'$ with a reward $r$ from $s$ and $a$

$$
\begin{align}
  V_{\pi}(s)  &=\mathbb{E}_{\pi}\left(\sum_{t \geqq 0} R(S_{t}|S_{0} = s)\right) \\
        &= \mathbb{E}_{\pi}\left[R(S_{0}) + \sum_{t \geqq 0} R(S_{t+1})|S_{0} = s\right] \\
            &= \sum_{a}\pi(a|s) \sum_{s'}\sum_{r}\mathbb{P}(s',r| s,a) \left[r + \mathbb{E}_{\pi}\left(\sum_{t \geqq 0} R(S_{t+1}|S_{1} = s'\right)\right] \\
            &= \sum_{a}\pi(a|s) \sum_{s'}\sum_{r}\mathbb{P}(s',r| s,a) [r + V_{\pi}(s')]
\end{align}
$$

(4) is equivalent to:

$$V_{\pi}(s) = \mathbb{E}_{\pi}[R(s,\pi(s))] + \sum_{s'}\mathbb{P}(s'| s,\pi(s))V_{\pi}(s')$$

as it is only a reformulation of the problem.

## Contributors

* Alanna DEVLIN-GENIN
* Clément DIGOIN
* Camille LE POTIER
* Hélène MOGENET