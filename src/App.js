import React, { useState } from "react";
import "./styles.css";

import Dashboard from "./pages/Dashboard";
import Billing from "./pages/Billing";
import Stock from "./pages/Stock";
import Khata from "./pages/Khata";
import Customers from "./pages/Customers";
import Reports from "./pages/Reports";
import Settings from "./pages/setting";
import AIAnalytics from "./pages/AIAnalytics";
import Login from "./pages/Login";

function App() {
  const [page, setPage] = useState("dashboard");
  const [loggedIn, setLoggedIn] = useState(true);

  if (!loggedIn) {
    return <Login onLogin={() => setLoggedIn(true)} />;
  }

  const renderPage = () => {
    if (page === "dashboard") return <Dashboard />;
    if (page === "billing") return <Billing />;
    if (page === "stock") return <Stock />;
    if (page === "khata") return <Khata />;
    if (page === "customers") return <Customers />;
    if (page === "reports") return <Reports />;
    if (page === "settings") return <Settings />;
    if (page === "ai") return <AIAnalytics />;
    return <Dashboard />;
  };

  return (
    <div className="app">
      <aside className="sidebar">
        <h2>AI ERP</h2>

        <button onClick={() => setPage("dashboard")}>Dashboard</button>
        <button onClick={() => setPage("billing")}>Billing</button>
        <button onClick={() => setPage("stock")}>Stock</button>
        <button onClick={() => setPage("khata")}>Khata</button>
        <button onClick={() => setPage("customers")}>Customers</button>
        <button onClick={() => setPage("reports")}>Reports</button>
        <button onClick={() => setPage("ai")}>AI Analytics</button>
        <button onClick={() => setPage("settings")}>Settings</button>

        <button className="logout" onClick={() => setLoggedIn(false)}>
          Logout
        </button>
      </aside>

      <main className="main">
        <div className="topbar">
          <h1>AI Wholesale ERP</h1>
          <span>Owner Panel</span>
        </div>

        {renderPage()}
      </main>
    </div>
  );
}

export default App;