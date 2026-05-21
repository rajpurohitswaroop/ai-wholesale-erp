import React, { useEffect, useState } from "react";

function Billing() {
  const [products, setProducts] = useState([]);
  const [customerName, setCustomerName] = useState("");
  const [selectedProduct, setSelectedProduct] = useState("");
  const [quantity, setQuantity] = useState("");
  const [bill, setBill] = useState(null);

  const loadProducts = async () => {
    const res = await fetch("http://127.0.0.1:5000/api/products/");
    const data = await res.json();
    setProducts(data.products || []);
  };

  useEffect(() => {
    loadProducts();
  }, []);

  const createBill = async () => {
    if (!customerName || !selectedProduct || !quantity) {
      alert("Please fill all fields");
      return;
    }

    const product = products.find((p) => p.name === selectedProduct);

    if (!product) {
      alert("Product not found");
      return;
    }

    const total = Number(product.price || 0) * Number(quantity);

    const newBill = {
      customer_name: customerName,
      product_name: product.name,
      price: product.price,
      quantity: Number(quantity),
      total_amount: total,
    };

    setBill(newBill);

    try {
      await fetch("http://127.0.0.1:5000/api/billing/create", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(newBill),
      });
    } catch (error) {
      console.log("Billing API not connected yet", error);
    }
  };

  return (
    <div className="page">
      <h1>Billing Page</h1>

      <input
        placeholder="Customer Name"
        value={customerName}
        onChange={(e) => setCustomerName(e.target.value)}
      />

      <select
        value={selectedProduct}
        onChange={(e) => setSelectedProduct(e.target.value)}
        style={{
          display: "block",
          width: "100%",
          maxWidth: "420px",
          padding: "12px",
          margin: "12px 0",
          border: "1px solid #ccc",
          borderRadius: "8px",
        }}
      >
        <option value="">Select Product</option>
        {products.map((p) => (
          <option key={p.id || p.name} value={p.name}>
            {p.name} - ₹{p.price} - Stock {p.stock}
          </option>
        ))}
      </select>

      <input
        placeholder="Quantity"
        type="number"
        value={quantity}
        onChange={(e) => setQuantity(e.target.value)}
      />

      <button onClick={createBill}>Create Bill</button>

      {bill && (
        <div className="card" style={{ marginTop: "20px", maxWidth: "420px" }}>
          <h3>Bill Preview</h3>
          <p>Customer: {bill.customer_name}</p>
          <p>Product: {bill.product_name}</p>
          <p>Price: ₹{bill.price}</p>
          <p>Quantity: {bill.quantity}</p>
          <h3>Total: ₹{bill.total_amount}</h3>
        </div>
      )}
    </div>
  );
}

export default Billing;