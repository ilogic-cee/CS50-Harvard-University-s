const App = () => {
  return (
    React.createElement('div', null,
      React.createElement('nav', { className: 'navbar fixed-top navbar-expand-sm navbar-light bg-light' },
        React.createElement('div', { className: 'container-fluid' },
          React.createElement('a', { className: 'navbar-brand', href: 'index.html' }, 'CS50ogle'),
          React.createElement('button', { className: 'navbar-toggler', type: 'button', 'data-bs-toggle': 'collapse', 'data-bs-target': '#navbarNav', 'aria-controls': 'navbarNav', 'aria-expanded': 'false', 'aria-label': 'Toggle navigation' },
            React.createElement('span', { className: 'navbar-toggler-icon' })
          ),
          React.createElement('div', { className: 'collapse navbar-collapse', id: 'navbarNav' },
            React.createElement('ul', { className: 'navbar-nav ms-auto' },
              React.createElement('li', { className: 'nav-item ms-auto' },
                React.createElement('a', { className: 'nav-link', href: 'index.html' }, 'Search')
              ),
              React.createElement('li', { className: 'nav-item ms-auto' },
                React.createElement('a', { className: 'nav-link', href: 'images.html' }, 'Image Search')
              ),
              React.createElement('li', { className: 'nav-item ms-auto' },
                React.createElement('a', { className: 'nav-link', href: 'advanced.html' }, 'Advanced Search')
              ),
              React.createElement('li', { className: 'nav-item ms-auto' },
                React.createElement('a', { className: 'nav-link', href: 'https://www.linkedin.com/in/ross-coron/' }, 'About')
              )
            )
          )
        )
      ),
      // The rest of your existing code...
    )
  );
};

ReactDOM.render(React.createElement(App), document.getElementById('root'));

function myFunction() {
  var msgElement = document.getElementById('searchterm');
  msgElement.value = '\\' + msgElement.value;
  return true;
}
