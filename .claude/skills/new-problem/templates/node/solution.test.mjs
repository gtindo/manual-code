import { test } from 'node:test'
import assert from 'node:assert/strict'
import { solve } from './solution.mjs'

const cases = [
  // { name: 'README example', args: [], expected: undefined },
]

for (const { name, args, expected } of cases) {
  test(name, () => {
    assert.deepEqual(solve(...args), expected)
  })
}
