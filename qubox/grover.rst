Algoritmo de Busca de Grover
============================

Aqui será abordado como criar um algoritmo quântico para resolver o problema de Grover, o qual é mais eficiente que as soluções clássicas propostas até o momento.

Problema
--------

O problema pode ser resumido em encontrar um determinado elemento dado uma lista de tamanho :math:`2^n`.
Para isso, deve ser criada uma função booleana :math:`f: \{0, 1\}^n \to \{0, 1\}`, a qual só sinalize '1' para o elemento desejado.

.. math::

    f(x) =  \begin{cases}
                0, x \ne x_0 \\
                1, x = 0
            \end{cases}


Oráculo
-------

Um oráculo faz justamente o mesmo que a função booleana descrita anteriormente.
Existem dois tipos de oráculos, XOR e os de fase, nesse problema será utilizado o de fase.

Oráculo de Fase
^^^^^^^^^^^^^^^

O oráculo de fase introduzirá uma fase de :math:`\pi` em :math:`f(x = x_0)`, ou seja, multiplicará por :math:`-1`.

- Exemplo: dado :math:`\left| \psi \right\rangle = \dfrac{1}{\sqrt{2}}\left( \left| 0 \right\rangle + \left| 1 \right\rangle\right)`. Se o oráculo for usado para marcar o estado :math:`\left| 1 \right\rangle`, o resultado será :math:`O(\left| \psi \right\rangle) = \dfrac{1}{\sqrt{2}}\left( \left| 0 \right\rangle - \left| 1 \right\rangle\right)`.

Algoritmo
---------

O primeiro passo é aplicar a porta de Hadamard em todos os qubits, para conseguir uma superposição com pesos iguais.

.. math::
    H^{\otimes n}\left|0\right\rangle^{\otimes n}

Após isso aplicamos :math:`G` (operador de Grover) :math:`k` vezes.
Onde :math:`G` representa a seguinte sequência de passos.

1. Aplicar o oráculo de fase para o estado desejado.
2. Aplicar a porta de Hadamard em todos os qubits.
3. Aplicar :math:`2 \left| 0 \right\rangle \left\langle 0 \right| - I`.
4. Aplicar a porta de Hadamard em todos os qubits.

Notação Auxiliar
^^^^^^^^^^^^^^^^

.. math::
    \begin{matrix}
        \mathbb{B}_n: \text{conjunto de todas as palavras de n bits}. \\
        \mathbb{M}: \text{conjunto de todos itens desejados}. \\
        N = 2^n
        \begin{cases}
            n: \text{número de qubits}. \\
            N: \text{número de itens}.
        \end{cases} \\
        M: \text{número de itens desejados} (usaremos M = 1). \\
        \left| \alpha \right\rangle := \sum_{\substack{x \in \mathbb{B}_n \\ x \notin \mathbb{M}}} \frac{\left| x \right\rangle}{\sqrt{N - M}} \\
        \left| \beta \right\rangle := \sum_{x_0 \in \mathbb{M}} \dfrac{\left| x_0 \right\rangle}{\sqrt{M}} : \text{itens desejados}. \\
        S := \text{span}_\mathbb{R}\{\left| \alpha \right\rangle, \left| \beta \right\rangle \} : \text{espaço vetorial gerado por \left| \alpha \right\rangle e \left| \beta \right\rangle}.
    \end{matrix}

Difusor
^^^^^^^

.. math::
    \begin{matrix}
        2 \left| 0 \right\rangle \left\langle 0 \right| - I &=& 2 \cdot
        \begin{bmatrix}
            1       \\
            0       \\
            \vdots  \\
            0
        \end{bmatrix}_{n \times 1}
        \begin{bmatrix}
            1 & 0 & \cdots & 0
        \end{bmatrix}_{1 \times n} -
        \begin{bmatrix}
            1 & 0 & \cdots & 0 \\
            0 & 1 & \cdots & 0 \\
            \vdots & \vdots & \ddots & 0 \\
            0 & 0 & \cdots & 1
        \end{bmatrix}_{n \times n}
        \\
        &=&
        \begin{bmatrix}
            2 & 0 & \cdots & 0 \\
            0 & 0 & \cdots & 0 \\
            \vdots & \vdots & \ddots & 0 \\
            0 & 0 & \cdots & 0
        \end{bmatrix}_{n \times n} -
        \begin{bmatrix}
            1 & 0 & \cdots & 0 \\
            0 & 1 & \cdots & 0 \\
            \vdots & \vdots & \ddots & 0 \\
            0 & 0 & \cdots & 1
        \end{bmatrix}_{n \times n}
        \\
        &=&
        \begin{bmatrix}
            1 & 0 & \cdots & 0\\
            0 & -1 & \cdots & 0 \\
            \vdots & \vdots & \ddots & 0 \\
            0 & 0 & \cdots & -1
        \end{bmatrix}_{n \times n}
        \\
        &=& \left| 0\dots 0 \right\rangle \left\langle 0 \dots 0 \right| - \left| 0 \dots 1 \right\rangle \left\langle 0 \dots 1 \right| -\dots - \left| 1 \dots 1\right\rangle \left\langle 1 \dots 1 \right|
    \end{matrix}


Usando o conceito de fase global, é possível escrever o resultado de outra forma, sendo ela:

.. math::
    -\left| 0\dots 0 \right\rangle \left\langle 0 \dots 0 \right| + \left| 0 \dots 1 \right\rangle \left\langle 0 \dots 1 \right| + \dots + \left| 1 \dots 1\right\rangle \left\langle 1 \dots 1 \right|



Para obter esse resultado, basta usar o oráculo de fase visto anteriormente e usá-lo para marcar o estado :math:`\left| 0 \right\rangle`.

Primeira Aplicação de :math:`G`
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Antes de fazer as aplicações, temos:

.. math::
    \begin{matrix}
        \left| \psi_0 \right\rangle &=& \left| + \right\rangle^{\otimes n} \\
        &=& \sum_{x \in \mathbb{B}_n} \dfrac{\left| x \right\rangle}{\sqrt{N}} \\
        &=& \sum_{\substack{x \in \mathbb{B}_n \\ x \ne x_0}}\dfrac{\left| x \right\rangle}{\sqrt{N}} + \dfrac{\left| x_0 \right\rangle}{\sqrt{N}} \\
        &=& \dfrac{\sqrt{N - 1}}{\sqrt{N}}\sum_{\substack{x \in \mathbb{B}_n \\ x \ne x_0}}\dfrac{\left| x \right\rangle}{\sqrt{N - 1}} + \dfrac{\left| x_0 \right\rangle}{\sqrt{N}} \\
        &=& \dfrac{\sqrt{N - 1}}{\sqrt{N}} \left| \alpha \right\rangle + \dfrac{1}{\sqrt{N}} \left| \beta \right\rangle
    \end{matrix}

Após a aplicação do oráculo:

.. math::
    \begin{matrix}
        \left| \psi_1 \right\rangle &=& O_F \left| \psi_0 \right\rangle \\
        &=& \dfrac{\sqrt{N - 1}}{\sqrt{N}} \left| \alpha \right\rangle - \dfrac{1}{\sqrt{N}} \left| \beta \right\rangle
    \end{matrix}

.. TODO: adicionar imagem do oráculo

Após a aplicação de :math:`2\left| \psi \right\rangle \left\langle \psi \right| - I`:

.. math::
    \begin{matrix}
        \left| \psi_2 \right\rangle &=& (2\left| \psi \right\rangle \left\langle \psi \right| - I) \left| \psi_1 \right\rangle \\
        &=& 2\left| \psi \right\rangle \left\langle \psi \right| \left| \psi_1 \right\rangle - \left| \psi_1 \right\rangle
    \end{matrix}

.. TODO: imagem do difusor

Com isso, obtemos o seguinte resultado:

.. TODO: imagem do plano alpha-beta após a aplicação de G.

Aplicações Sucessivas de :math:`G`
----------------------------------

A cada aplicação teremos uma rotação no sentido anti-horário, logo, o vetor estará se afastando de :math:`\left| \alpha\right\rangle` e se aproximando de :math:`\left| \beta \right\rangle` (item desejado).

.. TODO: imagem operador G aplicado k vezes.

Número de Aplicações
^^^^^^^^^^^^^^^^^^^^

O número de aplicações necessárias é dado por:

.. math::
    k = \dfrac{\pi}{4} \cdot \sqrt{\dfrac{N}{M}}

.. TODO: adicionar referência para livro Quantum Computation and Quantum Information
