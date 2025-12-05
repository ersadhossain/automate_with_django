"use client";

import { useEffect, useState } from "react";

export default function Home() {
  const [models, setModels] = useState([]);
  const [responseMsg, setResponseMsg] = useState("");
  const [formData, setFormData] = useState({
    model: "",
    file: null,
  });
  // console.log(models,"hello")

  // Fetch models on page load
  useEffect(() => {
    fetch("http://127.0.0.1:8000/data_entry_view/")
      .then((res) => res.json())
      .then((data) => {
        // console.log("Models from Django:", data.data);
        setModels(data.data); // assuming Django sends { data: ["Model1", "Model2"] }
      })
      .catch((err) => console.error("Fetch error:", err));
  }, []);

  const handleChange = (e) => {
    const { name, value, files } = e.target;
    console.log(name, value, files);

    if (name === "file") {
      setFormData((prev) => ({
        ...prev,
        file: files && files[0],
      }));
    } else {
      setFormData((prev) => ({
        ...prev,
        [name]: value,
      }));
    }
  };

  // Submit file + model via POST
  const handleSubmit = async () => {
    if (!formData.model || !formData.file) {
      setResponseMsg("Please select a model and upload a file.");
      return;
    }

    // Use FormData for file upload
    const body = new FormData();
    body.append("model", formData.model);
    body.append("file", formData.file);

try {
  const res = await fetch("http://127.0.0.1:8000/data_entry_view/", {
    method: "POST",
    body,
  });

  const data = await res.json();
  setResponseMsg(data.message );

  // Reset form fields
  setFormData({
    model: "",
    file: null,
  });

  // Also reset file input manually (React cannot reset file inputs automatically)
  document.getElementById("fileInput").value = "";
  
} catch (err) {
  console.error(err);
  setResponseMsg("Upload failed.");
}
  }

  return (
    <div style={{ padding: "30px" }}>
      <h1>Django + Next.js File Upload</h1>

      {/* Dropdown */}
      <label>Select Model:</label>
      <select
        name="model"
        value={formData.model}
        onChange={handleChange}
        style={{ padding: "10px", marginBottom: "20px", display: "block" }}
      >
        <option value="">-- Choose Model --</option>
          {models.map((model, index) => (
          <option key={index} value={model}>
            {model}
          </option>
        ))}

      </select>

      {/* File Upload */}
      <label>Upload File:</label>
    <input
  type="file"
  id="fileInput"
  name="file"
  onChange={handleChange}
  style={{ display: "block", marginBottom: "20px" }}
/>


      {/* POST Button */}
      <button
        onClick={handleSubmit}
        style={{
          padding: "10px 20px",
          background: "black",
          color: "white",
          cursor: "pointer",
        }}
      >
        Submit
      </button>

      {/* Response Message */}
      {responseMsg && (
        <p style={{ marginTop: "20px", fontWeight: "bold" }}>{responseMsg}</p>
      )}
    </div>
  );
}
