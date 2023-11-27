// app.js
const App = () => {
    return (
      <div>
        <nav className="navbar fixed-top navbar-expand-sm navbar-light bg-light">
          {/* ... your existing navbar code ... */}
        </nav>

        <div className="container d-flex align-items-center vh-100">
          <div className="container mt-5">
            <div className="d-flex p-2 justify-content-center">
              <img src="CS50ogle.png" width="400" alt="CS50ogle Logo" />
            </div>
            <div className="d-flex justify-content-center">
              <div className="col-md-6 justify-content-center">
                <div className="form">
                  <form action="https://google.com/search" autoComplete="off" id="searchbar">
                    <i className="fa fa-search"></i>
                    <input type="text" name="q" id="searchterm" className="form-control form-input" placeholder="Search" />
                    <span className="left-pan"><i className="fa fa-microphone"></i></span>
                  </form>
                </div>

                <div className="d-flex justify-content-center my-4">
                  <button type="submit" form="searchbar" formAction="https://google.com/search" className="btn btn-secondary mx-3">CS50ogle Search</button>
                  <button onClick={myFunction} type="submit" form="searchbar" formAction="https://duckduckgo.com/" className="btn btn-secondary mx-3">I'm Feeling Lucky</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  };

  ReactDOM.render(<App />, document.getElementById('root'));

  function myFunction() {
    var msgElement = document.getElementById("searchterm");
    msgElement.value = '\\' + msgElement.value;
    // alert();
    return true;
  }
