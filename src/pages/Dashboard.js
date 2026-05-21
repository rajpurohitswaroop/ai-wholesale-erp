import React, { useEffect, useState } from "react";

function Dashboard() {
  const [products, setProducts] = useState([]);
  const [khataList, setKhataList] = useState([]);

  const loadDashboardData = async () => {
    try {
      const productRes = await fetch("http://127.0.0.1:5000/api/products/");
      const productData = await productRes.json();
      setProducts(productData.products || []);

      const khataRes = await fetch("http://127.0.0.1:5000/api/khata/");
      const khataData = await khataRes.json();
      setKhataList(khataData.khata || []);
    } catch (error) {
      console.log("Dashboard API Error:", error);
    }
  };

  useEffect(() => {
    loadDashboardData();
  }, []);

  const totalProducts = products.length;

  const lowStock = products.filter(
    (item) => Number(item.stock || 0) <= 5
  ).length;

  const pendingKhata = khataList.reduce(
    (total, item) => total + Number(item.amount || 0),
    0
  );

  const todaySales = 0;

  return (
    <div className="page">
      <h1>Dashboard</h1>

      <button onClick={loadDashboardData}>Refresh Dashboard</button>

      <div className="cards">
        <div className="card">Today Sales: ₹{todaySales}</div>
        <div className="card">Total Products: {totalProducts}</div>
        <div className="card">Pending Khata: ₹{pendingKhata}</div>
        <div className="card">Low Stock: {lowStock}</div>
      </div>
    </div>
  );
}

export default Dashboard;