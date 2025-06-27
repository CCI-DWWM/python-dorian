import user

# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    assert inc(4) == 5

    def test_prime():
        assert user.est_premier(5)
        assert not user.est_premier(6)
        assert user.est_premier(7)
        assert not user.est_premier(8)
        assert not user.est_premier(9)
        assert not user.est_premier(33333333333333)
        assert not user.est_premier(10000000000)
        assert user.est_premier(9576890767)