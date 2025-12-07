"use client";

import { useState, useEffect } from "react";

export default function ExportData() {
  const [models, setModels] = useState([]);
  const [modelName, setModelName] = useState("");

  // ✅ Fetch models on load (correct endpoint)
  useEffect(() => {
    fetch("http://localhost:8000/export_data/")
      .then((res) => res.json())
      .then((data) => setModels(data.data || []))
      .catch(() => alert("Failed to load models."));
  }, []);

  // Submit export request
  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!modelName) {
      alert("Please select a model first!");
      return;
    }

    try {
      const formData = new FormData();
      formData.append("models_name", modelName);

      const res = await fetch("http://localhost:8000/export_data/", {
        method: "POST",
        body: formData,
      });

      const data = await res.json();

      if (!res.ok) {
        alert("Error: " + data.error);
        return;
      }

      alert("Export started successfully!");
    } catch (err) {
      alert("Something went wrong.");
    }
  };

  return (
    <main style={{ padding: 40 }}>
      <h1>Export Data</h1>

      <form onSubmit={handleSubmit} style={{ marginTop: 20 }}>
        
        {/* Model Dropdown */}
        <label style={{ display: "block", marginBottom: 10, fontSize: 18 }}>
          Select Model:
        </label>

        <select
          value={modelName}
          onChange={(e) => setModelName(e.target.value)}
          style={{ width: "100%", padding: "8px", marginBottom: "15px" }}
        >
          <option value="">-- Choose Model --</option>

          {models.map((m) => (
            <option key={m} value={m}>
              {m}
            </option>
          ))}
        </select>

        {/* Submit */}
        <button
          type="submit"
          style={{
            padding: "10px 20px",
            fontSize: 16,
            cursor: "pointer",
          }}
        >
          Export
        </button>
      </form>
    </main>
  );
}
