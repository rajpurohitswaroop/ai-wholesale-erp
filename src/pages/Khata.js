import React, { useState, useEffect } from "react";

function Khata() {
  const [customer, setCustomer] = useState("");
  const [amount, setAmount] = useState("");
  const [dueDate, setDueDate] = useState("");

  const [khataList, setKhataList] = useState([]);

  const loadKhata = async () => {
    try {
      const response = await fetch("http://127.0.0.1:5000/api/khata/");
      const data = await response.json();

      if (data.khata) {
        setKhataList(data.khata);
      }
    } catch (error) {
      console.log(error);
    }
  };

  useEffect(() => {
    loadKhata();
  }, []);

  const addKhata = async () => {
    if (!customer || !amount) {
      alert("Fill all fields");
      return;
    }

    try {
      await fetch("http://127.0.0.1:5000/api/khata/add", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          customer_name: customer,
          amount: amount,
          due_date: dueDate,
        }),
      });

      setCustomer("");
      setAmount("");
      setDueDate("");

      loadKhata();
    } catch (error) {
      console.log(error);
    }
  };

  const totalPending = khataList.reduce(
    (total, item) => total + Number(item.amount),
    0
  );

  return (
    <div>
      <h1>Khata Management</h1>

      <input
        placeholder="Customer Name"
        value={customer}
        onChange={(e) => setCustomer(e.target.value)}
      />

      <input
        placeholder="Pending Amount"
        type="number"
        value={amount}
        onChange={(e) => setAmount(e.target.value)}
      />

      <input
        type="date"
        value={dueDate}
        onChange={(e) => setDueDate(e.target.value)}
      />

      <br />
      <br />

      <button onClick={addKhata}>Add Khata</button>

      <button
        onClick={loadKhata}
        style={{ marginLeft: "10px" }}
      >
        Refresh
      </button>

      <div className="card" style={{ marginTop: "20px" }}>
        <h3>Total Pending: ₹{totalPending}</h3>
      </div>

      {khataList.map((item, index) => (
        <div
          key={index}
          className="card"
          style={{ marginTop: "20px", maxWidth: "400px" }}
        >
          <h3>{item.customer_name}</h3>

          <p>Amount: ₹{item.amount}</p>

          <p>Due Date: {item.due_date}</p>
        </div>
      ))}
    </div>
  );
}

export default Khata;