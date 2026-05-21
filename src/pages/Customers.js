import React, { useState } from "react";

function Customers() {
  const [customers, setCustomers] = useState([]);
  const [name, setName] = useState("");
  const [phone, setPhone] = useState("");
  const [address, setAddress] = useState("");

  const addCustomer = () => {
    if (!name || !phone) {
      alert("Customer name and phone required");
      return;
    }

    const newCustomer = {
      id: customers.length + 1,
      name,
      phone,
      address,
    };

    setCustomers([...customers, newCustomer]);
    setName("");
    setPhone("");
    setAddress("");
  };

  return (
    <div className="page">
      <h1>Customer List</h1>

      <input
        placeholder="Customer Name"
        value={name}
        onChange={(e) => setName(e.target.value)}
      />

      <input
        placeholder="Phone Number"
        value={phone}
        onChange={(e) => setPhone(e.target.value)}
      />

      <input
        placeholder="Address"
        value={address}
        onChange={(e) => setAddress(e.target.value)}
      />

      <button onClick={addCustomer}>Add Customer</button>

      <div className="cards">
        {customers.length === 0 ? (
          <div className="card">No customers found</div>
        ) : (
          customers.map((c) => (
            <div className="card" key={c.id}>
              <h3>{c.name}</h3>
              <p>Phone: {c.phone}</p>
              <p>Address: {c.address}</p>
            </div>
          ))
        )}
      </div>
    </div>
  );
}

export default Customers;