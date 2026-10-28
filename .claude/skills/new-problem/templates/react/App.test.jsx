import { describe, it, expect } from 'vitest'
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import App from './App.jsx'

describe('__TITLE__', () => {
  it('renders', () => {
    render(<App />)
    // expect(screen.getByRole(...)).toBeInTheDocument()
  })
})
