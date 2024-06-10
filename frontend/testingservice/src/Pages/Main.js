import React, { Component } from 'react';
import axios from 'axios';
import TestList from '../components/TestList'; // компонент для отображения списка тестов

export class Main extends Component {
  state = {
    tests: [], // состояние для хранения тестов
    themes: [], // состояние для хранения уникальных тем
    selectedTheme: 'all', // выбранная тема для фильтрации
    sortOrder: 'asc', // порядок сортировки
    searchQuery: '', // поисковый запрос
    userBlocked: false, // статус блокировки пользователя
    errorMessage: '' // сообщение об ошибке
  };

  componentDidMount() {
    this.fetchTests();
    this.checkUserBlocked();
  }

  fetchTests = () => {
    axios.get('/test', { withCredentials: true })
      .then(response => {
        const tests = response.data;
        const themes = [...new Set(tests.map(test => test.theme))];
        this.setState({ tests, themes });
      })
      .catch(error => {
        console.error('Ошибка при запросе к эндпоинту /test:', error);
        if (error.response && error.response.data && error.response.data.detail === 'USER_BLOCKED') {
          this.setState({ userBlocked: true, errorMessage: 'Ваш аккаунт заблокирован. Вы не можете просматривать тесты.' });
        } else {
          this.setState({ errorMessage: 'Ошибка при загрузке тестов. Пожалуйста, попробуйте еще раз.' });
        }
      });
  }

  checkUserBlocked = () => {
    axios.get('/users/me')
      .then(response => {
        const userBlocked = response.data.blocked_flag;
        if (userBlocked) {
          this.setState({ userBlocked: true, errorMessage: 'Ваш аккаунт заблокирован. Вы не можете просматривать тесты.' });
        }
      })
      .catch(error => {
        console.error('Ошибка при проверке статуса пользователя:', error);
      });
  }

  handleThemeChange = (event) => {
    this.setState({ selectedTheme: event.target.value });
  }

  handleSortOrderChange = (event) => {
    this.setState({ sortOrder: event.target.value });
  }

  handleSearchChange = (event) => {
    this.setState({ searchQuery: event.target.value });
  }

  getFilteredSortedTests = () => {
    const { tests, selectedTheme, sortOrder, searchQuery, userBlocked } = this.state;
    const filteredTests = tests.filter(test => 
      (selectedTheme === 'all' || test.theme === selectedTheme) && 
      test.name.toLowerCase().includes(searchQuery.toLowerCase())
    );

    if (userBlocked) {
      return [];
    }

    return filteredTests.sort((a, b) => {
      if (sortOrder === 'asc') {
        return a.name.localeCompare(b.name);
      } else {
        return b.name.localeCompare(a.name);
      }
    });
  }

  render() {
    const { themes, selectedTheme, sortOrder, searchQuery, errorMessage } = this.state;
    const filteredSortedTests = this.getFilteredSortedTests();

    return (
      <div>
        {errorMessage && <div>{errorMessage}</div>}
        <div className="filter-sort-container">
          <select value={selectedTheme} onChange={this.handleThemeChange}>
            <option value="all">Все темы</option>
            {themes.map((theme, index) => (
              <option key={index} value={theme}>{theme}</option>
            ))}
          </select>
          <select value={sortOrder} onChange={this.handleSortOrderChange}>
            <option value="asc">По возрастанию</option>
            <option value="desc">По убыванию</option>
          </select>
          <input 
            type="text" 
            placeholder="Поиск по названию..." 
            value={searchQuery} 
            onChange={this.handleSearchChange} 
          />
        </div>
        <TestList tests={filteredSortedTests} />
      </div>
    );
  }
}

export default Main;
