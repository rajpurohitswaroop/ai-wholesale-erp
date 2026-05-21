"use strict";

let products = JSON.parse(localStorage.getItem("products")) || [];

function saveProducts() {
  localStorage.setItem("products", JSON.stringify(products));
}

function addProduct(name, stock, rate, gst = 0) {
  if (!name || stock < 0 || rate <= 0) {
    alert("Product details sahi bharein");
    return;
  }

  products.push({
    name,
    stock: Number(stock),
    rate: Number(rate),
    gst: Number(gst)
  });

  saveProducts();
  renderProducts();
}

function renderProducts() {
  const box = document.getElementById("productList");
  if (!box) return;

  box.innerHTML = products.map((product, index) => `
    <tr>
      <td>${index + 1}</td>
      <td>${product.name}</td>
      <td>${product.stock}</td>
      <td>₹${product.rate}</td>
      <td>${product.gst}%</td>
      <td>${product.stock <= 10 ? "Low Stock" : "Available"}</td>
    </tr>
  `).join("");
}

function updateStock(index, qty) {
  if (!products[index]) return;

  products[index].stock += Number(qty);
  saveProducts();
  renderProducts();
}