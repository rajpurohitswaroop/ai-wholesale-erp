import React from "react";

function Login() {
  return (
    <div className="login-page">
      <div className="login-box">
        <h1>AI Wholesale ERP</h1>
        <input placeholder="Username" />
        <input placeholder="Password" type="password" />
        <button>Login</button>
      </div>
    </div>
  );
}

export default Login;