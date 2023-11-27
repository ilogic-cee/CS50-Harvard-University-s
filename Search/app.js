// app.js
const App = () => {
    return (
      React.createElement('div', null,
        React.createElement('nav', { className: 'navbar fixed-top navbar-expand-sm navbar-light bg-light' },
          // ... your existing navbar code ...
        ),

        React.createElement('div', { className: 'container d-flex align-items-center vh-100' },
          React.createElement('div', { className: 'container mt-5' },
            React.createElement('div', { className: 'd-flex p-2 justify-content-center' },
              React.createElement('img', { src: 'CS50ogle.png', width: '400', alt: 'CS50ogle Logo' })
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
        )
      )
    );
  };

  ReactDOM.render(React.createElement(App), document.getElementById('root'));

  function myFunction() {
    var msgElement = document.getElementById('searchterm');
    msgElement.value = '\\' + msgElement.value;
    // alert();
    return true;
  }
