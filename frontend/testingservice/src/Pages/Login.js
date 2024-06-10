import React, { useState, useContext } from "react";
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { AuthContext } from '../AuthContext';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();
  const { setIsLoggedIn } = useContext(AuthContext);

  const handleLogin = async (event) => {
    event.preventDefault();

    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);

    try {
      const response = await axios.post('/auth/login', formData);
      localStorage.setItem('token', response.data.access_token);
      setIsLoggedIn(true);
      navigate("/");
    } catch (error) {
      console.error('Ошибка при авторизации:', error);
    }
  };

  return (
    <div className="login-form">
      <h2>Страница авторизации</h2>
      <form action="#" onSubmit={handleLogin}>
        <div className="input-box">
          <input
            type="text"
            placeholder='Логин'
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </div>
        <div className="input-box">
          <input
            type="password"
            placeholder='Пароль'
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>
        <div className="input-box button">
          <input type="submit" value="Войти"/>
        </div>
      </form>
    </div>
  );
};

export default Login;