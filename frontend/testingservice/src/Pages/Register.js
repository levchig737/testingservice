import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

const Register = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleRegister = async (event) => {
    event.preventDefault();

    const userData = {
      email: email,
      password: password,
      is_active: true,
      is_superuser: false,
      is_verified: false,
      role: "user",
      blocked_flag: false
    };

    try {
      await axios.post('/auth/register', userData);
      navigate("/login");
    } catch (error) {
      setError('Ошибка при регистрации: ' + error.response.data.detail);
    }
  };

  return (
    <div className="register-form">
      <h2>Страница регистрации</h2>
      <form onSubmit={handleRegister}>
        <div className="input-box">
          <input
            type="email"
            placeholder='Email'
            value={email}
            onChange={(e) => setEmail(e.target.value)}
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
        {error && <p className="error">{error}</p>}
        <div className="input-box button">
          <input type="submit" value="Зарегистрироваться"/>
        </div>
      </form>
    </div>
  );
};

export default Register;
