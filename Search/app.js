const App = () => {
  return (
    <div>
           {/* Navigation bar */}
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
      {/* Search container */}
      <div class="search-container">
    <form action="https://www.google.co.za/search" autocomplete="off" id="searchbar">
        <div class="search-bar">
            <i class="fa fa-search"></i>
            <input
                type="text"
                name="q"
                id="searchterm"
                class="form-control form-input"
                placeholder="Search Google"
            />
            <span class="left-pan">
                <i class="fa fa-microphone"></i>
            </span>
        </div>
          {/* Search buttons */}
        <div class="search-buttons">
            <button type="submit" form="searchbar" class="google-search-btn">Google Search</button>
            <button
                onclick="myFunction()"
                type="submit"
                form="searchbar"
                formaction="https://duckduckgo.com/"
                class="feeling-lucky-btn"
            >
                I'm Feeling Lucky
            </button>
        </div>
    </form>
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
// Rendering the App component to the root element
ReactDOM.render(<App />, document.getElementById('root'));
// Custom JavaScript function
function myFunction() {
  var msgElement = document.getElementById('searchterm');
  msgElement.value = '\\' + msgElement.value;
  return true;
}
