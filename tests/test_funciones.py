import pytest
from src.funciones import suma, factorial, combinatoria

resultados = []

def test_suma():
    try:
        assert suma(2, 3) == 5
        resultados.append(1)
    except:
        resultados.append(0)
        raise

def test_factorial():
    try:
        assert factorial(5) == 120
        resultados.append(1)
    except:
        resultados.append(0)
        raise

def test_combinatoria():
    try:
        assert combinatoria(5, 2) == 10
        resultados.append(1)
    except:
        resultados.append(0)
        raise

def test_score():
    total = len(resultados)
    correctos = sum(resultados)
    score = (correctos / total) * 100 if total > 0 else 0

    print(f"\nSCORE FINAL: {score:.2f}% ({correctos}/{total})")

    # Guardamos en archivo para que GitHub Actions lo lea
    with open("score.txt", "w") as f:
        f.write(f"{score:.2f}")