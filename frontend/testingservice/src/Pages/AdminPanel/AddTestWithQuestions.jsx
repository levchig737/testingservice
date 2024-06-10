import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const AddTestWithQuestions = () => {
  const [test, setTest] = useState({ name: "", owner: "", theme: "" });
  const [questions, setQuestions] = useState([{ question: "", min_score: 0, max_score: 0 }]);
  const [answers, setAnswers] = useState(Array.from({ length: 10 }, () => ""));
  const [correctAnswers, setCorrectAnswers] = useState(Array.from({ length: 10 }, () => false));
  const [error, setError] = useState(false);
  const navigate = useNavigate();

  const handleTestChange = (e) => {
    setTest({ ...test, [e.target.name]: e.target.value });
  };

  const handleQuestionChange = (index, e) => {
    const updatedQuestions = [...questions];
    updatedQuestions[index][e.target.name] = e.target.value;
    setQuestions(updatedQuestions);
  };

  const handleAddQuestion = () => {
    setQuestions([...questions, { question: "", min_score: 0, max_score: 0 }]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Создать тест
      const testResponse = await axios.post("/test/", test);
      const testId = testResponse.data.id;

      for (const [index, question] of questions.entries()) {
        // Создать вопрос
        const countAnswers = answers.filter(answer => answer.trim() !== "").length; // Количество ответов
        const questionResponse = await axios.post("/question/", { ...question, test_id: testId, count_answers: countAnswers });

        const questionId = questionResponse.data.id;

        // Создать ответы
        const formattedAnswers = answers.reduce((acc, curr, idx) => {
          acc[`answer${idx + 1}`] = curr.trim() !== "" ? curr : null;
          return acc;
        }, { question_id: questionId });
        console.log(formattedAnswers)
        await axios.post("/answer/", formattedAnswers);

        // Создать правильные ответы
        const formattedCorrectAnswers = correctAnswers.reduce((acc, curr, idx) => {
          acc[`answer${idx + 1}`] = curr;
          return acc;
        }, { question_id: questionId });
        console.log(formattedCorrectAnswers)
        await axios.post("/right_answer/", formattedCorrectAnswers);
      }

      navigate("/admin");
    } catch (err) {
      setError(true);
    }
  };

  const handleAnswerChange = (index, e) => {
    const updatedAnswers = [...answers];
    updatedAnswers[index] = e.target.value;
    setAnswers(updatedAnswers);
  };

  const handleCorrectAnswerChange = (index, e) => {
    const updatedCorrectAnswers = [...correctAnswers];
    updatedCorrectAnswers[index] = e.target.checked;
    setCorrectAnswers(updatedCorrectAnswers);
  };

  return (
    <div className="add-test-container">
      <h1>Add New Test with Questions</h1>
      <form onSubmit={handleSubmit}>
        <input type="text" placeholder="Test Name" name="name" onChange={handleTestChange} />
        <textarea placeholder="Owner" name="owner" onChange={handleTestChange} />
        <input type="text" placeholder="Test Theme" name="theme" onChange={handleTestChange} />

        {questions.map((question, qIndex) => (
          <div key={qIndex}>
            <input type="text" placeholder="Question Text" name="question" onChange={(e) => handleQuestionChange(qIndex, e)} />
            <input type="number" placeholder="Min Score" name="min_score" onChange={(e) => handleQuestionChange(qIndex, e)} />
            <input type="number" placeholder="Max Score" name="max_score" onChange={(e) => handleQuestionChange(qIndex, e)} />

            {answers.map((answer, aIndex) => (
              <div key={aIndex}>
                <input type="text" placeholder={`Answer ${aIndex + 1}`} onChange={(e) => handleAnswerChange(aIndex, e)} />
                <label>
                  Correct
                  <input type="checkbox" checked={correctAnswers[aIndex]} onChange={(e) => handleCorrectAnswerChange(aIndex, e)} />
                </label>
              </div>
            ))}
          </div>
        ))}

        <button type="button" onClick={handleAddQuestion}>Add Question</button>
        <button type="submit">Add Test</button>
        {error && "Something went wrong!"}
      </form>
    </div>
  );
};

export default AddTestWithQuestions;
