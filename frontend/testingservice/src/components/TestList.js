import React from 'react';
import { Link } from 'react-router-dom';

const TestList = ({ tests }) => {
  return (
    <div>
      <h2>Список тестов</h2>
      <ul className="test-list">
        {tests.map(test => (
          <li key={test.id} className="test-item">
            <h3>{test.name}</h3>
            <p>Тематика: {test.theme}</p>
            <p>Минимальный балл: {test.min_score}</p>
            <p>Максимальный балл: {test.max_score}</p>
            <p>Количество вопросов: {test.questions ? test.questions.length : 0}</p>
            <Link to={`/test/${test.id}`}>
              <button>Пройти</button>
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default TestList;
