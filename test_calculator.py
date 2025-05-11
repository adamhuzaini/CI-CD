import calculator

def test_tambah():
    assert calculator.tambah(3, 2) == 5

def test_kurang():
    assert calculator.kurang(5, 2) == 3

def test_kali():
    assert calculator.kali(4, 3) == 12

def test_bagi():
    assert calculator.bagi(10, 2) == 5.0

def test_bagi_dengan_nol():
    try:
        calculator.bagi(10, 0)
    except ValueError as e:
        assert str(e) == "Tidak bisa dibagi dengan nol."

