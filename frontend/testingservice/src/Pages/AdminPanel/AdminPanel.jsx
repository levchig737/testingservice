import React, { useEffect, useState } from "react";
import axios from "axios";
import { Link, useNavigate } from "react-router-dom";

const AdminPanel = () => {
  const [tests, setTests] = useState([]);


  useEffect(() => {
    const fetchAllTests = async () => {
      try {
        const res = await axios.get("/test/");
        setTests(res.data);
      } catch (err) {
        console.log(err);
      }
    };
    fetchAllTests();

   
  }, []);

  const handleDeleteTest = async (id) => {
    try {
      await axios.delete(`/test/${id}/`);
      setTests(tests.filter(test => test.id !== id));
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <div className="admin-panel-container">
    <h1>Admin Panel</h1>
    <div className="admin-panel">
      <div className="admin-btn">
        <button>
          <Link to="/admin/test/add" style={{ color: "inherit", textDecoration: "none" }}>
            Add Test
          </Link>
        </button>
      </div>
      <div className="admin-btn">
        <button>
          <Link to="/users" style={{ color: "inherit", textDecoration: "none" }}>
            Manage Users
          </Link>
        </button>
      </div>
    </div>
      <div className="tests">
        <h2>Tests</h2>
        {tests.map((test) => (
          <div key={test.id} className="test">
            <h3>{test.name}</h3>
            <p>{test.description}</p>
            <button className="delete" onClick={() => handleDeleteTest(test.id)}>Delete</button>
            <button className="update">
              <Link to={`/tests/update/${test.id}`} style={{ color: "inherit", textDecoration: "none" }}>
                Update
              </Link>
            </button>
          </div>
        ))}
      </div>
     
    </div>
  );
};

export default AdminPanel;
