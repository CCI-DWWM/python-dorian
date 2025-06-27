# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    assert inc(4) == 5

    def test_prime():
        assert prime.est_premier(5)
        assert not prime.est_premier(6)
        assert prime.est_premier(7)
        assert not prime.est_premier(8)
        assert not prime.est_premier(9)
        assert not prime.est_premier(33333333333333)
        assert not prime.est_premier(10000000000)
        assert prime.est_premier(9576890767)