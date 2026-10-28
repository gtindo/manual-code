# A01 — LRU cache

★★ · ~1h · stacks: python

## Goal
Build a fixed-capacity cache that evicts the **least recently used** entry when it is full.
`get` and `put` must both run in **O(1)** time. Reading *or* writing a key makes it the most recently used.

## Spec (python)
Edit `python/solution.py`. Implement a class `LRUCache`:

| Member | Behaviour |
|---|---|
| `LRUCache(capacity: int)` | `capacity` must be an `int >= 1`, otherwise raise `ValueError`. |
| `get(key)` | Return the stored value, or `None` if the key is absent. A hit makes `key` the most recently used. |
| `put(key, value)` | Insert or update. Either way `key` becomes the most recently used. If this adds a new key and the cache would exceed `capacity`, evict the least recently used key first. Updating an existing key never evicts anything. |
| `len(cache)` | Number of entries currently stored. |
| `key in cache` | `True` if the key is stored. Must **not** change recency. |
| `cache.keys()` | `list` of stored keys ordered from **most** to **least** recently used. Must **not** change recency. |

Keys are any hashable. Values are anything, including `None`, `0`, `""` — a stored falsy value is still a hit
(use `in` to tell a stored `None` from a missing key).

## Examples
```python
c = LRUCache(2)
c.put("a", 1); c.put("b", 2)
c.get("a")          # 1      -> order is now a, b   (a is most recent)
c.put("c", 3)       # evicts "b"
c.get("b")          # None
c.keys()            # ["c", "a"]

c.put("a", 10)      # update: refreshes "a", nothing evicted
c.keys()            # ["a", "c"]
len(c)              # 2
"c" in c            # True, and recency unchanged
LRUCache(0)         # ValueError
```

## Constraints
- O(1) `get` / `put` (a hash map plus a doubly linked list is the classic answer).
- Don't use `collections.OrderedDict`, `functools.lru_cache` or `cachetools` — implementing the recency tracking is the exercise.
- Standard library only, single file.

## Done when
```
scripts/t A01 python        # or: .venv/bin/pytest problems/A01-lru-cache/python
```

## Stretch
- Add `delete(key)` and `peek(key)` (read without refreshing).
- Add an optional per-entry TTL with an injectable clock.
