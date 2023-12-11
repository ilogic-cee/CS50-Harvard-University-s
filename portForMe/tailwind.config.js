module.exports = {
    content: [
      './src/**/*.html',
      './src/**/*.js',
      // Add other file paths that contain your HTML/JS code
    ],
    theme: {
      extend: {
        colors: {
          // Add custom colors here
          myBlue: '#3490dc',
        },
      },
    },
    plugins: [
      // Add any Tailwind CSS plugins you want to use
      // For example, 'tailwindcss-animatecss' or 'tailwindcss-typography'
    ],
  };
