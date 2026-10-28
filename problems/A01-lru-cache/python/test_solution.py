import random
import time
from collections import OrderedDict

import pytest

from solution import LRUCache


def test_get_missing_returns_none():
    c = LRUCache(2)
    assert c.get("nope") is None
    assert len(c) == 0


def test_put_then_get():
    c = LRUCache(2)
    c.put("a", 1)
    assert c.get("a") == 1
    assert len(c) == 1


def test_readme_example():
    c = LRUCache(2)
    c.put("a", 1)
    c.put("b", 2)
    assert c.get("a") == 1
    c.put("c", 3)  # evicts "b"
    assert c.get("b") is None
    assert c.keys() == ["c", "a"]
    c.put("a", 10)
    assert c.keys() == ["a", "c"]
    assert len(c) == 2
    assert "c" in c
    assert c.keys() == ["a", "c"]


def test_evicts_least_recently_inserted_when_untouched():
    c = LRUCache(3)
    for i, k in enumerate("abc"):
        c.put(k, i)
    c.put("d", 3)
    assert "a" not in c
    assert c.keys() == ["d", "c", "b"]


def test_get_refreshes_recency():
    c = LRUCache(2)
    c.put("a", 1)
    c.put("b", 2)
    c.get("a")
    c.put("c", 3)
    assert "a" in c and "c" in c and "b" not in c


def test_put_existing_updates_value_refreshes_and_does_not_evict():
    c = LRUCache(2)
    c.put("a", 1)
    c.put("b", 2)
    c.put("a", 99)
    assert len(c) == 2
    assert c.get("a") == 99
    assert c.keys() == ["a", "b"]
    c.put("c", 3)  # "b" is now the LRU
    assert "b" not in c and "a" in c


def test_capacity_one():
    c = LRUCache(1)
    c.put("a", 1)
    c.put("b", 2)
    assert c.get("a") is None
    assert c.get("b") == 2
    c.put("b", 3)
    assert c.get("b") == 3
    assert len(c) == 1


@pytest.mark.parametrize("bad", [0, -1, -100])
def test_invalid_capacity_raises(bad):
    with pytest.raises(ValueError):
        LRUCache(bad)


def test_contains_and_keys_do_not_change_recency():
    c = LRUCache(2)
    c.put("a", 1)
    c.put("b", 2)
    assert "a" in c
    assert c.keys() == ["b", "a"]
    c.put("c", 3)  # "a" must still be the LRU
    assert "a" not in c
    assert c.keys() == ["c", "b"]


def test_keys_returns_a_copy():
    c = LRUCache(2)
    c.put("a", 1)
    ks = c.keys()
    ks.append("zzz")
    assert c.keys() == ["a"]


def test_falsy_values_are_real_hits():
    c = LRUCache(3)
    c.put("zero", 0)
    c.put("empty", "")
    c.put("none", None)
    assert c.get("zero") == 0
    assert c.get("empty") == ""
    assert c.get("none") is None
    assert "none" in c
    assert len(c) == 3


def test_non_string_hashable_keys():
    c = LRUCache(3)
    c.put(1, "int")
    c.put((1, 2), "tuple")
    c.put(None, "none-key")
    assert c.get(1) == "int"
    assert c.get((1, 2)) == "tuple"
    assert c.get(None) == "none-key"


def test_matches_reference_model_on_random_ops():
    rng = random.Random(1234)
    for capacity in (1, 2, 5, 17):
        c = LRUCache(capacity)
        model = OrderedDict()  # most recent at the end
        for _ in range(3000):
            k = rng.randrange(capacity * 2)
            if rng.random() < 0.5:
                v = rng.randrange(1000)
                c.put(k, v)
                model[k] = v
                model.move_to_end(k)
                if len(model) > capacity:
                    model.popitem(last=False)
            else:
                expected = model.get(k)
                if k in model:
                    model.move_to_end(k)
                assert c.get(k) == expected
            assert len(c) == len(model)
            assert c.keys() == list(reversed(model))


def test_large_workload_is_fast_enough_for_o1():
    n = 200_000
    c = LRUCache(50_000)
    start = time.perf_counter()
    for i in range(n):
        c.put(i, i)
    for i in range(n - 50_000, n):
        assert c.get(i) == i
    assert c.get(0) is None
    assert len(c) == 50_000
    # an O(n) get/put would need ~1e10 steps; generous bound so slow machines don't flake
    assert time.perf_counter() - start < 5.0
