import React, { useState } from "react";

function Settings() {
  const [shopName, setShopName] = useState("");
  const [ownerName, setOwnerName] = useState("");
  const [phone, setPhone] = useState("");
  const [gst, setGst] = useState("");
  const [saved, setSaved] = useState(null);

  const saveSettings = () => {
    const data = {
      shopName,
      ownerName,
      phone,
      gst,
    };

    setSaved(data);
    alert("Settings saved successfully");
  };

  return (
    <div className="page">
      <h1>Settings</h1>

      <input
        placeholder="Shop Name"
        value={shopName}
        onChange={(e) => setShopName(e.target.value)}
      />

      <input
        placeholder="Owner Name"
        value={ownerName}
        onChange={(e) => setOwnerName(e.target.value)}
      />

      <input
        placeholder="Phone Number"
        value={phone}
        onChange={(e) => setPhone(e.target.value)}
      />

      <input
        placeholder="GST Number"
        value={gst}
        onChange={(e) => setGst(e.target.value)}
      />

      <button onClick={saveSettings}>Save Settings</button>

      {saved && (
        <div className="card" style={{ marginTop: "20px", maxWidth: "420px" }}>
          <h3>Saved Shop Details</h3>
          <p>Shop: {saved.shopName}</p>
          <p>Owner: {saved.ownerName}</p>
          <p>Phone: {saved.phone}</p>
          <p>GST: {saved.gst}</p>
        </div>
      )}
    </div>
  );
}

export default Settings;