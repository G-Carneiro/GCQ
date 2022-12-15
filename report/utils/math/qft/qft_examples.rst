.. math::

    \begin{array}{ccl}
    \ket{0} &→& \dfrac{1}{\sqrt{2}} \left( e^{πi·0·0} \ket{0} + e^{πi·0·1} \ket{1}\right) \\
    &=& \dfrac{1}{\sqrt{2}} \left( \ket{0} + \ket{1}\right) \\ \\
    \ket{1} &→& \dfrac{1}{\sqrt{2}} \left( e^{πi·1·0} \ket{0} + e^{πi·1·1} \ket{1}\right) \\
    &=& \dfrac{1}{\sqrt{2}} \left( \ket{0} - \ket{1}\right) \\ \\
    \ket{0 \dots 0} &→& \dfrac{1}{\sqrt{N}} \left( \ket{0 \dots 0} +  \ket{0 \dots 1} + \dots + \ket{1 \dots 1}\right) \\
    &=& \dfrac{1}{\sqrt{N}} \left( \ket{0 \dots 0} + \ket{0 \dots 1} + \dots + \ket{1 \dots 1} \right) \\ \\
    \ket{1 \dots 1} &→& \dfrac{1}{\sqrt{N}} \left( \ket{0 \dots 0} + e^{2πi(N-1)/N} \ket{0 \dots 1} + \dots + e^{2πi(N-1)(N-1)/N} \ket{1 \dots 1}\right) \\
    &=& \dfrac{1}{\sqrt{N}} \left( \ket{0 \dots 0} + e^{2πi(N-1)/N} \ket{0 \dots 1} + \dots + e^{2πi(N^2-2N+1)/N} \ket{1 \dots 1} \right)
    \end{array}
