from app import sumar

def test_suma():
    # Verifica varias combinaciones de números
    assert sumar(2, 3) == 5
    assert sumar(-1, 1) == 0
    assert sumar(0, 0) == 0
    assert sumar(2.5, 3.5) == 6.0
