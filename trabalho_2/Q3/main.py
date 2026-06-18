import pandas as pd
from pathlib import Path

from euler import Euler
from runge_kutta import RungeKutta

RESULTADOS = Path(__file__).parent / "resultados_Q3"
RESULTADOS.mkdir(parents=True, exist_ok=True)

# Parâmetros da simulação
A = 1.0
q_in = 0.10
h_ref = 1.0

t_f = 50
Delta_t = 0.01

h_0 = 0.5
z_0 = 0


def calcular_derivadas(h, z, Kp, Ki):
    dh_dt = (1 / A) * (q_in - Kp * (h - h_ref) - Ki * z)
    dz_dt = h - h_ref
    return dh_dt, dz_dt


# Caso 1: controle P com Euler
p_euler = Euler(calcular_derivadas, h_0, z_0, t_f, Delta_t, Kp=0.20, Ki=0.00)
p_euler.calcular()
p_euler.imprimir()
p_euler.exportar(RESULTADOS / "p_euler.tex")
h_p_euler = p_euler.resultado[1][-1]

# Caso 2: controle P com RK2
p_rk2 = RungeKutta(calcular_derivadas, h_0, z_0, t_f, Delta_t, Kp=0.20, Ki=0.00)
p_rk2.calcular()
p_rk2.imprimir()
p_rk2.exportar(RESULTADOS / "p_rk2.tex")
h_p_rk2 = p_rk2.resultado[1][-1]

# Caso 3: controle PI com Euler
pi_euler = Euler(calcular_derivadas, h_0, z_0, t_f, Delta_t, Kp=0.20, Ki=0.10)
pi_euler.calcular()
pi_euler.imprimir()
pi_euler.exportar(RESULTADOS / "pi_euler.tex")
h_pi_euler = pi_euler.resultado[1][-1]

# Caso 4: controle PI com RK2
pi_rk2 = RungeKutta(calcular_derivadas, h_0, z_0, t_f, Delta_t, Kp=0.20, Ki=0.10)
pi_rk2.calcular()
pi_rk2.imprimir()
pi_rk2.exportar(RESULTADOS / "pi_rk2.tex")
h_pi_rk2 = pi_rk2.resultado[1][-1]

# Tabela de resultados finais
tabela = pd.DataFrame(
    {
        "Controle": ["P", "P", "PI", "PI"],
        "Método": ["Euler", "RK2", "Euler", "RK2"],
        "h(t_f)": [h_p_euler, h_p_rk2, h_pi_euler, h_pi_rk2],
        "e_f": [
            h_p_euler - h_ref,
            h_p_rk2 - h_ref,
            h_pi_euler - h_ref,
            h_pi_rk2 - h_ref,
        ],
    }
)
tabela.index.name = "caso"

print(tabela)
print("\n")
print("--------------------------------")
print("\n")

tabela.to_latex(
    RESULTADOS / "tabela_resultados.tex",
    index=True,
    float_format="%.6f",
)
