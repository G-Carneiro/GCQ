- Feita a partir da redução do problema da fatoração para “busca em ordem” (pág 260/233).
- Dividido em dois passos básicos (Seção A4.3 do Apêndice 4 - Quantum Computation and Quantum Information).

    #. Mostrar que é possível computar um fator para :math:`N` se encontrar uma solução :math:`x ≠ ± 1 (\mod N)` para a equação :math:`x^2 = 1 (\mod N)`.

    #. Mostrar que um co-primo :math:`y` escolhido aleatoriamente para :math:`N` é muito provável ter uma ordem :math:`r` par e que :math:`y^{r / 2} ≠ ± 1 (\mod N)`, assim :math:`x ≡ y^{r / 2} (\mod N)` é uma solução não trivial para :math:`x^2 = 1 (\mod N)`.

Transformada de Fourier Quântica
================================

Transformada em um base ortonormal
----------------------------------

.. math::

    \ket{j} → \dfrac{1}{\sqrt{N}} \sum_{k=0}^{N-1} e^{2 π i jk /N} \ket{k}


**Exemplos**

.. math::

    \ket{0} &→& \dfrac{1}{\sqrt{2}} \left( e^{πi·0·0} \ket{0} + e^{πi·0·1} \ket{1}\right) \\
    &=& \dfrac{1}{\sqrt{2}} \left( \ket{0} + \ket{1}\right) \\
    \ket{1} &→& \dfrac{1}{\sqrt{2}} \left( e^{πi·1·0} \ket{0} + e^{πi·1·1} \ket{1}\right) \\
    &=& \dfrac{1}{\sqrt{2}} \left( \ket{0} - \ket{1}\right) \\
    \ket{0 \dots 0} &→& \dfrac{1}{\sqrt{N}} \left( \ket{0 \dots 0} +  \ket{0 \dots 1} + \dots + \ket{1 \dots 1}\right) \\
    &=& \dfrac{1}{\sqrt{N}} \left( \ket{0 \dots 0} + \ket{0 \dots 1} + \dots + \ket{1 \dots 1} \right) \\
    \ket{1 \dots 1} &→& \dfrac{1}{\sqrt{N}} \left( \ket{0 \dots 0} + e^{2πi(N-1)/N} \ket{0 \dots 1} + \dots + e^{2πi(N-1)(N-1)/N} \ket{1 \dots 1}\right) \\
    &=& \dfrac{1}{\sqrt{N}} \left( \ket{0 \dots 0} + e^{2πi(N-1)/N} \ket{0 \dots 1} + \dots + e^{2πi(N^2-2N+1)/N} \ket{1 \dots 1} \right) \\


**Conclusão**

A transformada atribui mais “peso” quando :math:`k` se aproxima de :math:`N-1`.

Ação sobre estado arbitrário
----------------------------

.. math::

    \sum_{j=0}^{N-1} x_j \ket{j} &→& \sum_{k=0}^{N-1} y_k \ket{k} \\

.. TODO: criar exemplos

.. qft(\ket{0} + \ket{1}) = qft(\ket{0}) + qft(\ket{1}) ?

Representação de Produto
------------------------

.. math::

    \ket{j_1 \dots j_n} \to \dfrac{1}{\sqrt{2^n}} \left( \ket{0} + e^{2 πi 0.j_n}\ket{1} \right) \left( \ket{0} + e^{2 πi 0.j_{n-1}j_n}\ket{1} \right) \dots \left( \ket{0} + e^{2 πi 0.j_1 \dots j_n}\ket{1} \right)

**Exemplos**

.. math::

    \ket{0} &→& \dfrac{1}{\sqrt{2}} \left( \ket{0} + e^{2πi0.0_{\text{bin}}} \ket{1} \right) \\
    &=& \dfrac{1}{\sqrt{2}} \left( \ket{0} + \ket{1} \right) \\
    \ket{1} &→& \dfrac{1}{\sqrt{2}} \left( \ket{0} + e^{2πi0.1_{\text{bin}}} \ket{1} \right) \\
    \ket{1} &→& \dfrac{1}{\sqrt{2}} \left( \ket{0} + e^{2πi/2} \ket{1} \right) \\
    &=& \dfrac{1}{\sqrt{2}} \left( \ket{0} - \ket{1} \right) \\
    \ket{00} &→& \dfrac{1}{\sqrt{4}} \left( \ket{0} + e^{2πi0.0_{\text{bin}}} \ket{1} \right) \left( \ket{0} + e^{2πi0.00_{\text{bin}}} \ket{1} \right) \\
    &=& \dfrac{1}{\sqrt{4}} \left( \ket{0} + \ket{1} \right) \left( \ket{0} + \ket{1} \right) \\
    &=& \dfrac{1}{\sqrt{4}} \left( \ket{00} + \ket{01} + \ket{10} + \ket{11} \right) \\
    \ket{11} &→& \dfrac{1}{\sqrt{4}} \left( \ket{0} + e^{2πi0.1_{\text{bin}}} \ket{1} \right) \left( \ket{0} + e^{2πi0.11_{\text{bin}}} \ket{1} \right) \\
    &=& \dfrac{1}{\sqrt{4}} \left( \ket{0} + e^{2πi/2} \ket{1} \right) \left( \ket{0} + e^{2πi·0.75} \ket{1} \right) \\
    &=& \dfrac{1}{\sqrt{4}} \left( \ket{0} - \ket{1} \right) \left( \ket{0} - i\ket{1} \right) \\
    &=& \dfrac{1}{\sqrt{4}} \left( \ket{00} - i\ket{01} - \ket{10} + i\ket{11} \right) \\

Equivalência
------------

.. math::

    \begin{array}{lll}
    \ket{j} &→& \displaystyle\dfrac{1}{2^{n/2}} \sum_{k=0}^{2^n-1} e^{2πijk/2^n} \ket{k} \\ \\
    &=& \displaystyle\dfrac{1}{2^{n/2}} \sum_{k_1=0}^{1} \dots \sum_{k_n=0}^{1} e^{2πij \left( \sum_{l=1}^{n}k_l2^{-l} \right)} \ket{k_1 \dots k_n} \\ \\
    &=& \displaystyle\dfrac{1}{2^{n/2}} \sum_{k_1=0}^{1} \dots \sum_{k_n=0}^{1} \bigotimes_{l=1}^{n} e^{2πij k_l 2^{-l}} \ket{k_l} \\ \\
    &=& \displaystyle\dfrac{1}{2^{n/2}} \bigotimes_{l=1}^{n} \left[ \sum_{k_l=0}^{1} e^{2πij k_l 2^{-l}} \ket{k_l} \right] \\ \\
    &=& \displaystyle\dfrac{1}{2^{n/2}} \bigotimes_{l=1}^{n} \left[ \ket{0} + e^{2πij 2^{-l}} \ket{1} \right] \\ \\
    &=& \dfrac{\left( \ket{0} + e^{2πi 0.j_n} \ket{1} \right) \left( \ket{0} + e^{2πi 0.j_{n-1}j_n} \ket{1} \right) \dots \left( \ket{0} + e^{2πi 0.j_1 j_2 \dots j_n} \ket{1} \right)}{2^{n/2}}
    \end{array}

**Provando notação**

.. math::

    \dfrac{k}{2^n} &=& \sum_{l=1}^{n} \dfrac{k_l}{2^l} \\
    &=& \dfrac{k_1}{2^1} + \dfrac{k_2}{2^2} + \dots + \dfrac{k_n}{2^n} \\
    &=& \dfrac{k_1·2^{n-1}}{2^n} + \dfrac{k_2·2^{n-2}}{2^n} + \dots + \dfrac{k_n}{2^n} \\
    &=& \dfrac{1}{2^n} \left( k_1·2^{n-1} + k_2·2^{n-2} + \dots + k_n \right)
