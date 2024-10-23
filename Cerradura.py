# plantillaMain.py - Control simplificado de cerraduras electromecánicas
import sys
import time

# Variables iniciales de las cerraduras
A1 = True
B1 = True
C1 = False

A2 = True
B2 = False
C2 = False

msg = "Implementa la solución para las cerraduras electromecánicas:"

def foo():
    print(f"{msg} Control lógico basado en entradas A, B, C, y D")

def horaActual():
    return time.ctime()

def neg(p: bool) -> bool:
    """Negación de una proposición"""
    return not p

def y(p: bool, q: bool) -> bool:
    """Conjunción lógica"""
    return p and q

def o(p: bool, q: bool) -> bool:
    """Disyunción lógica"""
    return p or q

def controlar_primera_cerradura(A: bool, B: bool, C: bool, estado_segunda: bool) -> bool:
    """Control lógico de la primera cerradura
       Se desbloquea si se cumple alguna de las condiciones:
       - A y B son verdaderos.
       - C es falso y A y B son verdaderos.
       - estado_segunda es verdadero y A, B y C son verdaderos.
    """
    A_y_B = y(A, B)
    C_negado = neg(C)
    C_negado_y_A_y_B = y(C_negado, A_y_B)
    estado_segunda_y_A_y_B_y_C = y(estado_segunda, A_y_B and C)

    return o(A_y_B, o(C_negado_y_A_y_B, estado_segunda_y_A_y_B_y_C))

def controlar_segunda_cerradura(A: bool, B: bool, C: bool) -> bool:
    """Control lógico de la segunda cerradura
       Se desbloquea si A es verdadero, B es falso y C es falso.
    """
    B_negado = neg(B)
    C_negado = neg(C)
    A_y_B_negado_y_C_negado = y(A, y(B_negado, C_negado))

    return A_y_B_negado_y_C_negado

def mostrar_mensaje_primera_cerradura(estado: bool):
    """Muestra un mensaje dependiendo del estado de la primera cerradura"""
    if estado:
        print("UN4 LL4V3 QU3 48R3 CU4LQU13R C4ND4D0 35 UN4 LL4V3 M4357R4, P3R0 CU4ND0 353 C4ND4D0 L0 48R3 CU4LQU13R LL4V3, 53 D353CH4.")
    else:
        print("Se bloquea el pasador/picaporte de la primer cerradura electromecánica.")

def main() -> int:
    """Función principal, ejecuta el control de las cerraduras"""
    foo()
    print(f"Hora actual: {horaActual()}")

    # Control de la segunda cerradura
    estado_segunda_cerradura = controlar_segunda_cerradura(A2, B2, C2)
    print(f"Segunda cerradura: {'Desbloqueada' if estado_segunda_cerradura else 'Bloqueada'}")

    # Control de la primera cerradura utilizando el estado de la segunda cerradura
    estado_primera_cerradura = controlar_primera_cerradura(A1, B1, C1, estado_segunda_cerradura)
    print(f"Primera cerradura: {'Desbloqueada' if estado_primera_cerradura else 'Bloqueada'}")
    mostrar_mensaje_primera_cerradura(estado_primera_cerradura)

    return 0

if __name__ == "__main__":
    sys.exit(main())