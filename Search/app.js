const App = () => {
  return (
    <div>
      <nav className="navbar fixed-top navbar-expand-sm navbar-light bg-light">
        <div className="container-fluid">
          <a className="navbar-brand" href="index.html"></a>
          <button
            className="navbar-toggler"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#navbarNav"
            aria-controls="navbarNav"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <div className="collapse navbar-collapse" id="navbarNav">
            <ul className="navbar-nav ms-auto">
              <li className="nav-item ms-auto">
                <a className="nav-link" href="index.html">
                  Search
                </a>
              </li>
              <li className="nav-item ms-auto">
                <a className="nav-link" href="images.html">
                  Image Search
                </a>
              </li>
              <li className="nav-item ms-auto">
                <a className="nav-link" href="advanced.html">
                  Advanced Search
                </a>
              </li>
              <li className="nav-item ms-auto">
                <a
                  className="nav-link"
                  href="https://www.linkedin.com/in/junior-motsoko-970a311b4"
                >
                  About
                </a>
              </li>
            </ul>
          </div>
        </div>
      </nav>

      <div className="container d-flex align-items-center vh-100">
        <div className="container mt-5">
          <div className="d-flex p-2 justify-content-center">
            <img src="gooogle.png" width="200" alt="Googlephoto" />
          </div>

          <div className="d-flex justify-content-center">
            <div className="col-md-6 justify-content-center">
              <div className="form">
                <form
                  action="https://google.com/search"
                  autoComplete="off"
                  id="searchbar"
                >
                  <i className="fa fa-search"></i>
                  <input
                    type="text"
                    name="q"
                    id="searchterm"
                    className="form-control form-input"
                    placeholder="Search"
                  />
                  <span className="left-pan">
                    <i className="fa fa-microphone"></i>
                  </span>
                </form>
              </div>

              <div className="d-flex justify-content-center my-4">
                <button
                  type="submit"
                  form="searchbar"
                  formAction="https://google.com/search"
                  className="btn btn-secondary mx-3"
                >
                  CS50ogle Search
                </button>
                <button
                  onClick={myFunction}
                  type="submit"
                  form="searchbar"
                  formAction="https://duckduckgo.com/"
                  className="btn btn-secondary mx-3"
                >
                  I'm Feeling Lucky
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Additional container for Google Image Search */}
      <div className="d-flex justify-content-center mt-4">
        <form
          action="https://www.google.com/search"
          autoComplete="off"
          id="imageSearchBar"
        ></form>
      </div>
    </div>
  );
};

ReactDOM.render(<App />, document.getElementById('root'));

function myFunction() {
  var msgElement = document.getElementById('searchterm');
  msgElement.value = '\\' + msgElement.value;
  return true;
}
