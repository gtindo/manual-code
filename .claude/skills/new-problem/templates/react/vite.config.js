import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// Only used for `npx vite problems/<id>/react` (visual check). Tests use the root vitest.config.js.
export default defineConfig({ plugins: [react()] })
