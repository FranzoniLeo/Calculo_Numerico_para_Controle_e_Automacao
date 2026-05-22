from m_jacobiana import Jacobiana


Q = [10, 5, 5, 2, 7, 3]

Fq = [[Q[0] - 10],
      [Q[0] - Q[1] - Q[2]],
      [Q[1] - Q[3] - Q[5]],
      [Q[2] + Q[3] - Q[4]],
      [Q[1]**2 + Q[3]**2 - 4*Q[2]**2],
      [Q[3]**2 + Q[4]**2 - 4*Q[5]**2]]

jacobi = Jacobiana(Fq, Q)
jacobi.resolver()
jacobi.imprimir()
jacobi.exportar()