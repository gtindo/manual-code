import { defineConfig } from 'vitest/config'
import react from '@vitejs/plugin-react'

// Shared config for the web / webcomponent / react stacks. Plain-node problems use `node --test` instead.
export default defineConfig({
  plugins: [react()],
  test: {
    environment: 'jsdom',
    globals: true,
    include: ['problems/*/{web,webcomponent,react}/**/*.test.{js,jsx}'],
    setupFiles: ['./vitest.setup.js'],
  },
})
