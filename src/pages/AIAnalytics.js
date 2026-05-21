import React, { useEffect, useState } from "react";

function AIAnalytics() {
  const [products, setProducts] = useState([]);
  const [khataList, setKhataList] = useState([]);

  const loadAIData = async () => {
    const productRes = await fetch("http://127.0.0.1:5000/api/products/");
    const productData = await productRes.json();

    const khataRes = await fetch("http://127.0.0.1:5000/api/khata/");
    const khataData = await khataRes.json();

    setProducts(productData.products || []);
    setKhataList(khataData.khata || []);
  };

  useEffect(() => {
    loadAIData();
  }, []);

  const lowStockProducts = products.filter((p) => Number(p.stock || 0) <= 5);
  const pendingKhata = khataList.reduce(
    (sum, item) => sum + Number(item.amount || 0),
    0
  );

  return (
    <div className="page">
      <h1>AI Analytics</h1>

      <button onClick={loadAIData}>Refresh AI Analytics</button>

      <div className="cards">
        <div className="card">
          <h3>AI Sales Suggestion</h3>
          <p>Top selling products ko stock me ready rakho.</p>
        </div>

        <div className="card">
          <h3>Low Stock Alert</h3>
          <p>{lowStockProducts.length} products low stock me hain.</p>
        </div>

        <div className="card">
          <h3>Customer Credit Alert</h3>
          <p>Total pending khata: ₹{pendingKhata}</p>
        </div>

        <div className="card">
          <h3>Business Growth Tips</h3>
          <p>Daily reports check karo aur high-demand products par focus karo.</p>
        </div>
      </div>
    </div>
  );
}

export default AIAnalytics;