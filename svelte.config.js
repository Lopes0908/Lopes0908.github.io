// svelte.config.js
export default {
  kit: {
    prerender: {
      handleHttpError: ({ status, path }) => {
        if (status === 404) return 'warn'; // or 'ignore'
      }
    }
  }
}