# -*- coding: utf-8 -*-
# programa de comisiones
# hecho por kevin, no tocar, ya funciona

COMISION_ALTA = 0.08
COMISION_BAJA = 0.05
META_COMISION = 30000
META_BONO = 50000
BONO = 500

vendedores = [
    ("María López", 45000.00),
    ("Carlos Pérez", 28500.00),
    ("Ana García", 61200.00),
    ("José Ramírez", 15800.00),
    ("Lucía Morales", 33400.00),
]


def calcular_comisiones():
    total_pagar = 0

    print("=" * 44)
    print("    COMISIONES DEL MES - LA COMERCIAL")
    print("=" * 44)

    for nombre, ventas in vendedores:

        if ventas > META_COMISION:

            comision = ventas * COMISION_ALTA
            comision = round(comision, 2)

            if ventas > META_BONO:
                bono = BONO
            else:
                bono = 0

            pago = round(comision + bono, 2)

            total_pagar += pago

            print(nombre + ": Q " + str(pago))

        else:

            comision = ventas * COMISION_BAJA
            comision = round(comision, 2)

            bono = 0

            pago = round(comision + bono, 2)

            total_pagar += pago

            print(nombre + ": Q " + str(pago))

    print("-" * 44)
    print("Total a pagar: Q " + str(round(total_pagar, 2)))


calcular_comisiones()