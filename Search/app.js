const App = () => {
  return (
    React.createElement('div', null,
      React.createElement('nav', { className: 'navbar fixed-top navbar-expand-sm navbar-light bg-light' },
        React.createElement('div', { className: 'container-fluid' },
          React.createElement('a', { className: 'navbar-brand', href: 'index.html' }, 'Google'),
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
                React.createElement('a', { className: 'nav-link', href: 'https://www.linkedin.com/in/junior-motsoko-970a311b4' }, 'About')
              )
            )
          )
        )
      ),

      React.createElement('div', { className: 'container d-flex align-items-center vh-100' },
        React.createElement('div', { className: 'container mt-5' },
          React.createElement('div', { className: 'd-flex p-2 justify-content-center' },
            React.createElement('img', { src: 'CS50ogle.png', width: '400', alt: 'Googlephoto' })
          ),

          React.createElement('div', { className: 'd-flex justify-content-center' },
            React.createElement('div', { className: 'col-md-6 justify-content-center' },
              React.createElement('div', { className: 'form' },
                React.createElement('form', { action: 'https://google.com/search', autoComplete: 'off', id: 'searchbar' },
                  React.createElement('i', { className: 'fa fa-search' }),
                  React.createElement('input', { type: 'text', name: 'q', id: 'searchterm', className: 'form-control form-input', placeholder: 'Search' }),
                  React.createElement('span', { className: 'left-pan' }, React.createElement('i', { className: 'fa fa-microphone' }))
                )
              ),

              React.createElement('div', { className: 'd-flex justify-content-center my-4' },
                React.createElement('button', { type: 'submit', form: 'searchbar', formAction: 'https://google.com/search', className: 'btn btn-secondary mx-3' }, 'CS50ogle Search'),
                React.createElement('button', { onClick: myFunction, type: 'submit', form: 'searchbar', formAction: 'https://duckduckgo.com/', className: 'btn btn-secondary mx-3' }, "I'm Feeling Lucky")
              )
            )
          )
        )
      ),

      // Additional container for Google Image Search
      React.createElement('div', { className: 'd-flex justify-content-center mt-4' },
        React.createElement('form', { action: 'https://www.google.com/search', autoComplete: 'off', id: 'imageSearchBar' },



        )
      )
    )
  );
};

ReactDOM.render(React.createElement(App), document.getElementById('root'));

function myFunction() {
  var msgElement = document.getElementById('searchterm');
  msgElement.value = '\\' + msgElement.value;
  return true;
}
