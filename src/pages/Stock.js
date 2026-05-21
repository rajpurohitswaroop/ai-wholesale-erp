import React, { useEffect, useState } from "react";

function Stock() {
  const [products, setProducts] = useState([]);
  const [name, setName] = useState("");
  const [price, setPrice] = useState("");
  const [stock, setStock] = useState("");

  const loadProducts = async () => {
    const res = await fetch("http://127.0.0.1:5000/api/products/");
    const data = await res.json();
    setProducts(data.products || []);
  };

  const addProduct = async () => {
    if (!name || !price || !stock) {
      alert("Please fill all fields");
      return;
    }

    await fetch("http://127.0.0.1:5000/api/products/add", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        name: name,
        price: price,
        stock: stock,
      }),
    });

    setName("");
    setPrice("");
    setStock("");
    loadProducts();
  };

  useEffect(() => {
    loadProducts();
  }, []);

  return (
    <div className="page">
      <h1>Stock Management</h1>

      <input
        placeholder="Product Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />

      <input
        placeholder="Price"
        type="number"
        value={price}
        onChange={(e) => setPrice(e.target.value)}
      />

      <input
        placeholder="Stock Quantity"
        type="number"
        value={stock}
        onChange={(e) => setStock(e.target.value)}
      />

      <button onClick={addProduct}>Add Product</button>
      <button onClick={loadProducts}>Refresh Products</button>

      <div className="cards">
        {products.length === 0 ? (
          <div className="card">No products found</div>
        ) : (
          products.map((p) => (
            <div className="card" key={p.id || p.name}>
              <h3>{p.name}</h3>
              <p>Price: ₹{p.price}</p>
              <p>Stock: {p.stock}</p>
            </div>
          ))
        )}
      </div>
    </div>
  );
}

export default Stock;