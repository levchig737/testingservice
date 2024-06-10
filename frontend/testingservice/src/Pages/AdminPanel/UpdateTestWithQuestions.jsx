import React, { useState, useEffect } from "react";
import axios from "axios";
import { useNavigate, useParams } from "react-router-dom";

const UpdateTestWithQuestions = () => {
  const [test, setTest] = useState({ name: "", description: "", theme: "" });
  const [questions, setQuestions] = useState([]);
  const [error, setError] = useState(false);
  const { id } = useParams();
  const navigate = useNavigate();

  useEffect(() => {
    const fetchTest = async () => {
      try {
        const testResponse = await axios.get(`/tests/${id}/`);
        setTest(testResponse.data);

        const questionsResponse = await axios.get(`/questions/test/${id}/`);
        setQuestions(questionsResponse.data);
      } catch (err) {
        console.log(err);
      }
    };
    fetchTest();
  }, [id]);

  const handleTestChange = (e) => {
    setTest({ ...test, [e.target.name]: e.target.value });
  };

  const handleQuestionChange = (index, e) => {
    const updatedQuestions = questions.map((question, qIndex) => 
      qIndex === index ? { ...question, [e.target.name]: e.target.value } : question
    );
    setQuestions(updatedQuestions);
  };

  const handleAnswerChange = (qIndex, aIndex, e) => {
    const updatedQuestions = questions.map((question, questionIndex) => 
      questionIndex === qIndex ? {
        ...question,
        answers: question.answers.map((answer, answerIndex) => 
          answerIndex === aIndex ? { ...answer, [e.target.name]: e.target.value } : answer
        )
      } : question
    );
    setQuestions(updatedQuestions);
  };

  const handleAddQuestion = () => {
    setQuestions([...questions, { text: "", answers: [{ text: "", is_correct: false }] }]);
  };

  const handleAddAnswer = (qIndex) => {
    const updatedQuestions = questions.map((question, index) => 
      index === qIndex ? { ...question, answers: [...question.answers, { text: "", is_correct: false }] } : question
    );
    setQuestions(updatedQuestions);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.patch(`/tests/${id}/`, test);

      for (const question of questions) {
        if (question.id) {
          await axios.patch(`/questions/${question.id}/`, question);
        } else {
          const questionResponse = await axios.post("/questions/", { ...question, test_id: id });
          const questionId = questionResponse.data.id;

          for (const answer of question.answers) {
            await axios.post("/answers/", { ...answer, question_id: questionId });
          }
        }
      }

      navigate("/admin");
    } catch (err) {
      setError(true);
    }
  };

  return (
    <div>
      <h1>Update Test with Questions</h1>
      <form onSubmit={handleSubmit}>
        <input type="text" placeholder="Test Name" name="name" value={test.name} onChange={handleTestChange} />
        <textarea placeholder="Test Description" name="description" value={test.description} onChange={handleTestChange} />
        <input type="text" placeholder="Test Theme" name="theme" value={test.theme} onChange={handleTestChange} />

        {questions.map((question, qIndex) => (
          <div key={qIndex}>
            <input type="text" placeholder="Question Text" name="text" value={question.text} onChange={(e) => handleQuestionChange(qIndex, e)} />
            {question.answers.map((answer, aIndex) => (
              <div key={aIndex}>
                <input type="text" placeholder="Answer Text" name="text" value={answer.text} onChange={(e) => handleAnswerChange(qIndex, aIndex, e)} />
                <label>
                  Correct
                  <input type="checkbox" name="is_correct" checked={answer.is_correct} onChange={(e) => handleAnswerChange(qIndex, aIndex, e)} />
                </label>
              </div>
            ))}
            <button type="button" onClick={() => handleAddAnswer(qIndex)}>Add Answer</button>
          </div>
        ))}
        <button type="button" onClick={handleAddQuestion}>Add Question</button>
        <button type="submit">Update Test</button>
        {error && "Something went wrong!"}
      </form>
    </div>
  );
};

export default UpdateTestWithQuestions;
