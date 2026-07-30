# -*- coding: utf-8 -*-
"""Programa para generar el cierre de caja diario."""

IVA = 0.12
COMISION_POS = 0.05

ventas = [
    ("EF", 150.00),
    ("TJ", 89.50),
    ("EF", 45.25),
    ("TJ", 210.00),
    ("EF", 78.00),
    ("TJ", 156.75),
    ("EF", 92.50),
    ("EF", 34.00),
    ("TJ", 67.25),
    ("EF", 125.00),
]


def calcular_iva(total):
    """Calcula el IVA incluido en un monto."""
    return round(total - (total / (1 + IVA)), 2)


def generar_cierre():
    """Calcula y muestra el resumen del cierre de caja."""

    total_efectivo = 0
    total_tarjeta = 0

    # Acumula las ventas según el método de pago.
    for metodo_pago, monto in ventas:
        if metodo_pago == "EF":
            total_efectivo += monto
        else:
            total_tarjeta += monto

    iva_efectivo = calcular_iva(total_efectivo)
    iva_tarjeta = calcular_iva(total_tarjeta)
    comision = round(total_tarjeta * COMISION_POS, 2)

    total_dia = round(total_efectivo + total_tarjeta, 2)
    deposito_neto = round(total_dia - comision, 2)

    print("=" * 42)
    print("      CIERRE DE CAJA - LA COMERCIAL")
    print("=" * 42)
    print(f"Ventas en efectivo:      Q {total_efectivo:.2f}")
    print(f"IVA incluido (efectivo): Q {iva_efectivo:.2f}")
    print(f"Ventas con tarjeta:      Q {total_tarjeta:.2f}")
    print(f"IVA incluido (tarjeta):  Q {iva_tarjeta:.2f}")
    print(f"Comisión del POS:        Q {comision:.2f}")
    print("-" * 42)
    print(f"Total del día:           Q {total_dia:.2f}")
    print(f"Depósito neto:           Q {deposito_neto:.2f}")


generar_cierre()