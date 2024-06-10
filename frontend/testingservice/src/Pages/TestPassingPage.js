import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

const TestPassingPage = () => {
  const { id } = useParams();
  const [test, setTest] = useState(null);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [score, setScore] = useState(0);
  const [completed, setCompleted] = useState(false);
  const [averageResult, setAverageResult] = useState(null);
  const [error, setError] = useState('');

  useEffect(() => {
    axios.get(`/test/with_questions/${id}/`, { withCredentials: true })
      .then(response => {
        setTest(response.data);
      })
      .catch(error => {
        console.error('Ошибка при получении теста с вопросами:', error);
        setError('Ошибка при загрузке теста. Пожалуйста, попробуйте еще раз.');
      });
  }, [id]);

  useEffect(() => {
    if (completed) {
      axios.get(`/test/average_result/${id}/`)
        .then(response => {
          setAverageResult(response.data.average_result);
        })
        .catch(error => {
          console.error('Ошибка при получении среднего балла:', error);
        });
    }
  }, [completed, id]);

  const handleAnswer = (answerIndex) => {
    const currentQuestion = test.questions[currentQuestionIndex];
    const correctAnswerIndex = Object.values(currentQuestion.right_answer).findIndex(answer => answer === true);

    const answerScore = answerIndex === correctAnswerIndex ? currentQuestion.max_score : currentQuestion.min_score;
    setScore(score + answerScore);

    if (currentQuestionIndex + 1 < test.questions.length) {
      setCurrentQuestionIndex(currentQuestionIndex + 1);
    } else {
      setCompleted(true);
      axios.post('/completed_test', { test_id: id, user_id: 1, scores: score + answerScore }, { withCredentials: true })
        .then(response => {
          console.log('Тест завершен', response.data);
        })
        .catch(error => {
          if (error.response.data.detail === 'USER_BLOCKED') {
            setError('Вы заблокированы и не можете завершить тест.');
          } else {
            console.error('Ошибка при завершении теста:', error);
            setError('Ошибка при завершении теста. Пожалуйста, попробуйте еще раз.');
          }
        });
    }
  };

  if (error) {
    return <div className="test-container error">{error}</div>;
  }

  if (completed) {
    return (
      <div className="test-container completed">
        <p>Тест завершен! Ваши баллы: {score}</p>
        {averageResult && <p>Средний балл среди пользователей: {averageResult}</p>}
      </div>
    );
  }

  if (!test) {
    return <div className="test-container loading">Загрузка теста...</div>;
  }

  const currentQuestion = test.questions[currentQuestionIndex];
  const answersArray = Object.values(currentQuestion.answer).filter(answer => answer !== null);

  return (
    <div className="test-container">
      <h2>{currentQuestion.question}</h2>
      {answersArray.map((answer, index) => (
        <button key={index} onClick={() => handleAnswer(index)}>
          {answer}
        </button>
      ))}
    </div>
  );
};

export default TestPassingPage;
