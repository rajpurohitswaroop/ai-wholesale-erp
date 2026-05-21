import React, { useEffect, useState } from "react";

function Reports() {
  const [products, setProducts] = useState([]);
  const [khataList, setKhataList] = useState([]);

  const loadReports = async () => {
    const productRes = await fetch("http://127.0.0.1:5000/api/products/");
    const productData = await productRes.json();

    const khataRes = await fetch("http://127.0.0.1:5000/api/khata/");
    const khataData = await khataRes.json();

    setProducts(productData.products || []);
    setKhataList(khataData.khata || []);
  };

  useEffect(() => {
    loadReports();
  }, []);

  const totalProducts = products.length;
  const lowStock = products.filter((p) => Number(p.stock || 0) <= 5).length;
  const totalPending = khataList.reduce(
    (sum, item) => sum + Number(item.amount || 0),
    0
  );

  return (
    <div className="page">
      <h1>Reports</h1>

      <button onClick={loadReports}>Refresh Reports</button>

      <div className="cards">
        <div className="card">Total Products: {totalProducts}</div>
        <div className="card">Low Stock Products: {lowStock}</div>
        <div className="card">Total Khata Pending: ₹{totalPending}</div>
        <div className="card">Today Sales: ₹0</div>
      </div>
    </div>
  );
}

export default Reports;