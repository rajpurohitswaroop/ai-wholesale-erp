"use strict";

function selectPayment(type) {
  const statusBox = document.getElementById("paymentStatus");

  if (!statusBox) return;

  const statuses = {
    cash: "STATUS: CASH RECEIVED ✅",
    upi: "STATUS: UPI PAYMENT RECEIVED ✅",
    qr: "STATUS: QR PAYMENT RECEIVED ✅",
    pending: "STATUS: PAYMENT PENDING ⏳"
  };

  statusBox.textContent = statuses[type] || "STATUS: NOT SELECTED";
}

function generateReceipt(customerName, amount) {
  if (!customerName || !amount) {
    alert("Customer name aur amount required hai");
    return;
  }

  alert(`Receipt generated for ${customerName}: ₹${amount}`);
}