import femm
import numpy as np


def main():
    n_pontos = 40
    polos = 7
    deg_mec = np.linspace(0, 360, n_pontos)
    deg_ele = deg_mec / polos

    a_flux = np.zeros(n_pontos)
    b_flux = np.zeros(n_pontos)
    c_flux = np.zeros(n_pontos)
    print(a_flux)

    for i in range(n_pontos):
        femm.mi_modifyboundprop("Sliding", 11, deg_ele[i])
        femm.mi_analyse()
        femm.mi_loadsolution()

        a_flux[i] = femm.mo_getcircuitproperties("A")[2]
        b_flux[i] = femm.mo_getcircuitproperties("A")[2]
        c_flux[i] = femm.mo_getcircuitproperties("A")[2]

    flux_1n = np.zeros(n_pontos)
    for i in range(n_pontos):
        femm.mi_modifyboundprop("Sliding", 11, deg_ele[i])
        femm.mi_analyse()
        femm.mi_loadsolution()

        femm.mo_selectblock(1.5, 8.6)
        flux_1n[i] = femm.mo_blockintegral(1) / femm.mo_blockintegral(5)
        femm.mo_clearblock()

    ap = 10e-3 * (10.86 + 10.96) * 1e-3 * np.pi / 14
    bt = flux_1n / ap / 4


if __name__ == '__main__':
    main()
