import { describe, it, expect, beforeEach } from 'vitest'
import './element.js'

describe('<__TAG__>', () => {
  beforeEach(() => {
    document.body.innerHTML = ''
  })

  it('upgrades and renders', () => {
    const el = document.createElement('__TAG__')
    document.body.append(el)
    expect(el.shadowRoot ?? el).toBeTruthy()
  })
})
