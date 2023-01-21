import React from 'react';
import { HashRouter, Route, Link, Switch, Redirect, BrowserRouter, Router } from 'react-router-dom';
import logo from './logo.svg';
import './App.css';
import AuthorList from './components/Author.js';
import BookList from './components/Books.js';
import AuthorBookList from './components/AuthorBook';
import axios from 'axios';

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

    // заглушка чтобы не поднимать бекэнд
    const author1 = { id: 1, first_name: 'Александр', last_name: 'Грин', birthday_year: 1880 }
    const author2 = { id: 2, first_name: 'Александр', last_name: 'Пушкин', birthday_year: 1799 }
    const author3 = { id: 3, first_name: 'Алексей', last_name: 'Беляев', birthday_year: 1900 }
    const authors = [author1, author2, author3]

    const book1 = { id: 1, name: 'Алые паруса', author: author1 }
    const book2 = { id: 2, name: 'Золотая цепь', author: author1 }
    const book3 = { id: 3, name: 'Пиковая дама', author: author2 }
    const book4 = { id: 4, name: 'Капитанская дочка', author: author2 }
    const book5 = { id: 5, name: 'Ихтиандр', author: author3 }
    const books = [book1, book2, book3, book4, book5]
    ///-----------------------------


    this.state = {
      'authors': authors,
      'books': books
    }
  }
  //здесь обращаемся на бэк
  // componentDidMount() {
  //   axios.get('http://127.0.0.1:8000/api/authors')
  //     .then(response => {
  //       const authors = response.data
  //       this.setState(
  //         {
  //           'authors': authors
  //         }
  //       )
  //     }).catch(error => console.log(error))
  //}




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
            </ul>
          </nav>
          <Switch>
            <Route exact path='/' component={() => <AuthorList authors={this.state.authors} />} />
            <Route exact path='/books' component={() => <BookList items={this.state.books} />} />
            <Route exact path='/author/:first_name' component={() => <AuthorBookList items={this.state.books} />} />
            <Redirect from='/authors' to='/' />
            <Route component={NotFound404} />

          </Switch>
        </BrowserRouter>

      </div >
    )
  }
}

export default App;