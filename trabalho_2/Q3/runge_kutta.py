import numpy as np
import pandas as pd


class RungeKutta:

    def __init__(self, derivadas, h0, z0, t_f, dt, Kp, Ki):
        self.derivadas = derivadas
        self.h0 = h0
        self.z0 = z0
        self.t_f = t_f
        self.dt = dt
        self.Kp = Kp
        self.Ki = Ki
        self.resultado = None

    def calcular(self):
        n = int(round(self.t_f / self.dt))
        t = np.arange(n + 1) * self.dt
        h = np.zeros(n + 1)
        z = np.zeros(n + 1)
        h[0] = self.h0
        z[0] = self.z0

        for i in range(n):
            dh1, dz1 = self.derivadas(h[i], z[i], self.Kp, self.Ki)
            h_pred = h[i] + self.dt * dh1
            z_pred = z[i] + self.dt * dz1
            dh2, dz2 = self.derivadas(h_pred, z_pred, self.Kp, self.Ki)

            h[i + 1] = h[i] + (self.dt / 2) * (dh1 + dh2)
            z[i + 1] = z[i] + (self.dt / 2) * (dz1 + dz2)

        self.resultado = (t, h, z)
        return self.resultado

    def imprimir(self):
        if self.resultado is None:
            self.calcular()

        t, h, _ = self.resultado
        tabela = pd.DataFrame(
            {
                "t [s]": t[::50],
                "h [m]": h[::50],
            }
        )
        print(tabela)
        print("\n")
        print("--------------------------------")
        print("\n")

    def exportar(self, caminho):
        if self.resultado is None:
            self.calcular()

        t, h, _ = self.resultado
        tabela = pd.DataFrame(
            {
                "t [s]": t,
                "h [m]": h,
            }
        )
        tabela.to_latex(caminho, index=False, float_format="%.6f")
