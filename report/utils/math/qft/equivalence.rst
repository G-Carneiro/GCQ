.. math::

    \begin{array}{lll}
    \ket{j} &→& \displaystyle\dfrac{1}{2^{n/2}} \sum_{k=0}^{2^n-1} e^{2πijk/2^n} \ket{k} \\ \\
    &=& \displaystyle\dfrac{1}{2^{n/2}} \sum_{k_1=0}^{1} \dots \sum_{k_n=0}^{1} e^{2πij \left( \sum_{l=1}^{n}k_l2^{-l} \right)} \ket{k_1 \dots k_n} \\ \\
    &=& \displaystyle\dfrac{1}{2^{n/2}} \sum_{k_1=0}^{1} \dots \sum_{k_n=0}^{1} \bigotimes_{l=1}^{n} e^{2πij k_l 2^{-l}} \ket{k_l} \\ \\
    &=& \displaystyle\dfrac{1}{2^{n/2}} \bigotimes_{l=1}^{n} \left[ \sum_{k_l=0}^{1} e^{2πij k_l 2^{-l}} \ket{k_l} \right] \\ \\
    &=& \displaystyle\dfrac{1}{2^{n/2}} \bigotimes_{l=1}^{n} \left[ \ket{0} + e^{2πij 2^{-l}} \ket{1} \right] \\ \\
    &=& \dfrac{\left( \ket{0} + e^{2πi 0.j_n} \ket{1} \right) \left( \ket{0} + e^{2πi 0.j_{n-1}j_n} \ket{1} \right) \dots \left( \ket{0} + e^{2πi 0.j_1 j_2 \dots j_n} \ket{1} \right)}{2^{n/2}}
    \end{array}
