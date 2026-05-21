"use strict";

let billItems = [];

function addBillItem(name, qty, rate, gst = 0) {
  if (!name || qty <= 0 || rate <= 0) {
    alert("Product, quantity aur rate sahi bharein");
    return;
  }

  const subtotal = Number(qty) * Number(rate);
  const gstAmount = subtotal * Number(gst) / 100;
  const total = subtotal + gstAmount;

  billItems.push({
    name,
    qty: Number(qty),
    rate: Number(rate),
    gst: Number(gst),
    total
  });

  renderBillItems();
}

function renderBillItems() {
  const box = document.getElementById("billItems");
  if (!box) return;

  box.innerHTML = billItems.map((item, index) => `
    <tr>
      <td>${index + 1}</td>
      <td>${item.name}</td>
      <td>${item.qty}</td>
      <td>₹${item.rate}</td>
      <td>${item.gst}%</td>
      <td>₹${item.total.toFixed(2)}</td>
    </tr>
  `).join("");

  calculateBillTotal();
}

function calculateBillTotal() {
  const total = billItems.reduce((sum, item) => sum + item.total, 0);
  const totalBox = document.getElementById("billTotal");

  if (totalBox) {
    totalBox.textContent = `₹${total.toFixed(2)}`;
  }

  return total;
}

function clearBill() {
  billItems = [];
  renderBillItems();
}