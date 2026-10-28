import { describe, it, expect, beforeEach } from 'vitest'
import { mount } from './app.js'

describe('__TITLE__', () => {
  let root
  beforeEach(() => {
    document.body.innerHTML = '<div id="app"></div>'
    root = document.getElementById('app')
  })

  it('renders something on mount', () => {
    mount(root)
    expect(root.children.length).toBeGreaterThan(0)
  })
})
