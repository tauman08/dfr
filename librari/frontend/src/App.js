import React from 'react';
import { HashRouter, Route, Link, Switch, Redirect, BrowserRouter, Router } from 'react-router-dom';
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Author.js';
import BookList from './components/Books.js';
import AuthorBookList from './components/AuthorBook';
import axios from 'axios';
import LoginForm from './components/Auth.js';
import Cookies from 'universal-cookie';

const NotFound404 = ({ location }) => {
  return (
    <div>
      <h1> Страница по адресу `{location.pathname}` не найдена </h1>
    </div>
  )
}

class App extends React.Component {
  constructor(props) {
    super(props)

    this.state = {
      'authors': [],
      'books': [],
      'token': ''
    }
  }

  set_token(token) {
    const cookies = new Cookies()
    cookies.set('token', token)
    localStorage.setItem('token': token)
    this.setState({ 'token': token }, () => this.load_data())
  }

  is_authenticated() {
    return this.state.token != ''
  }

  logout() {
    this.set_token('')
  }

  get_token_from_storage() {
    const cookies = new Cookies
    const token = cookies.get('token')
    //получим из локального хранилища браузера ( менее безопасно чем куки )
    //const token = localStorage.getItem('token')

    this.setState({ 'token': token }, () => this.load_data())
  }

  get_token(login, password) {
    axios.post('http://127.0.0.1:8000/api-token-auth/', { username: login, password: password })
      .then(response => {
        this.set_token(response.data['token'])
      }).catch(error => alert('неверный пароль'))
  }

  get_headers() {
    let headers = {
      'Content-Type': 'application/json',
    }
    if (this.is_authenticated()) {
      headers['Authorization'] = 'Token' + this.state.token
    }
    return headers
  }

  load_data() {
    const headers = this.get_headers()
    axios.get('http://127.0.0.1:8000/api/authors', { headers })
      .then(response => {
        const authors = response.data
        this.setState(
          {
            'authors': authors['results']
          }
        )
      }).catch(error => console.log(error))

    axios.get('http://127.0.0.1:8000/api/books', { headers })
      .then(response => {
        const books = response.data
        this.setState(
          {
            'books': books['results']
          }
        )
      }).catch(error => console.log(error))
  }


  //здесь обращаемся на бэк
  componentDidMount() {
    this.get_token_from_storage()

  }


  render() {
    return (
      <div className='App'>

        <BrowserRouter>
          <nav>
            <ul>
              <li>
                <Link to='/'>Authors</Link>
              </li>
              <li>
                <Link to='/books'>Books</Link>
              </li>
              <li>
                {this.is_authenticated() ? <button onClick={() => this.logout}>Logout</button> : <Link to='/login'>Login</Link>}

              </li>
            </ul>
          </nav>
          <Switch>
            <Route exact path='/' component={() => <AuthorList authors={this.state.authors} />} />
            <Route exact path='/books' component={() => <BookList items={this.state.books} />} />
            <Route exact path='/author/:first_name' component={() => <AuthorBookList items={this.state.books} />} />
            <Route exact path='/login' component={() => <LoginForm get_token={(login, password) => this.get_token(login, password)} />} />
            <Redirect from='/authors' to='/' />
            <Route component={NotFound404} />

          </Switch>
        </BrowserRouter>

      </div >
    )
  }
}

export default App;