import React, { useEffect, useState } from "react";
import axios from "axios";
import { useNavigate, useParams } from "react-router-dom";

const UpdateTest = () => {
  const [test, setTest] = useState({
    name: "",
    description: "",
    theme: ""
  });
  const [error, setError] = useState(false);

  const { id } = useParams(); // Получаем значение id из строки маршрута
  const navigate = useNavigate();

  useEffect(() => {
    const fetchTest = async () => {
      try {
        const res = await axios.get(`/test/without_questions/${id}/`);
        setTest(res.data);
      } catch (err) {
        console.log(err);
      }
    };
    fetchTest();
  }, [id]);

  const handleChange = (e) => {
    setTest((prev) => ({ ...prev, [e.target.name]: e.target.value }));
  };

  const handleClick = async (e) => {
    e.preventDefault();
    try {
      await axios.patch(`/test/${id}/`, test);
      navigate("/admin");
    } catch (err) {
      console.log(err);
      setError(true);
    }
  };

  return (
    <div className="add-test-container">
      <h1>Update Test</h1>
      <form onSubmit={handleClick}>
        <input
          type="text"
          placeholder="Test Name"
          name="name"
          value={test.name}
          onChange={handleChange}
        />
        <textarea
          placeholder="Description"
          name="description"
          value={test.description}
          onChange={handleChange}
        />
        <input
          type="text"
          placeholder="Theme"
          name="theme"
          value={test.theme}
          onChange={handleChange}
        />
        <button type="submit">Update</button>
        {error && "Something went wrong!"}
      </form>
    </div>
  );
};

export default UpdateTest;
