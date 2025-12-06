'use client'
import { useEffect, useState, useRef } from "react";

export default function DataEntryPage() {
  const [models, setModels] = useState([]);
  const [modelName, setModelName] = useState("");
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");

  const fileInputRef = useRef(null); // For clearing file input

  // -----------------------------------------
  // AUTO-HIDE MESSAGE AFTER 5 SECONDS
  // -----------------------------------------
  useEffect(() => {
    if (message) {
      const timer = setTimeout(() => {
        setMessage("");
      }, 5000);

      return () => clearTimeout(timer);
    }
  }, [message]);

  // Fetch list of models
  useEffect(() => {
    fetch("http://localhost:8000/data_entry_view/")
      .then((res) => res.json())
      .then((data) => setModels(data.data || []))
      .catch(() => setMessage("Failed to load models"));
  }, []);

  // Submit form
  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!modelName || !file) {
      setMessage("Please select a model and upload a file.");
      return;
    }

    const formData = new FormData();
    formData.append("model", modelName);
    formData.append("file", file);

    try {
      const res = await fetch("http://localhost:8000/data_entry_view/", {
        method: "POST",
        body: formData,
      });

      const data = await res.json();

      if (!res.ok) {
        setMessage("Error: " + data.error);
      } else {
        setMessage(data.message);

        // CLEAR ALL FIELDS AFTER SUCCESS
        setModelName("");
        setFile(null);
        fileInputRef.current.value = "";
      }
    } catch (error) {
      setMessage("Something went wrong!");
    }
  };

  return (
    <div style={{ maxWidth: "500px", margin: "40px auto", fontFamily: "Arial" }}>
      <h2>Data Entry Upload</h2>

      {message && (
        <p
          style={{
            padding: "10px",
            background: "black",
            color: "white",
            borderRadius: "5px",
            marginBottom: "15px",
            transition: "opacity 0.3s ease"
          }}
        >
          {message}
        </p>
      )}

      <form onSubmit={handleSubmit}>
        {/* Select Model */}
        <label>Select Model:</label>
        <br />
        <select
          value={modelName}
          onChange={(e) => setModelName(e.target.value)}
          style={{ width: "100%", padding: "8px", margin: "10px 0" }}
        >
          <option value="">-- Choose Model --</option>
          {models.map((m, i) => (
            <option key={i} value={m}>
              {m}
            </option>
          ))}
        </select>

        {/* Upload File */}
        <label>Upload CSV File:</label>
        <br />
        <input
          type="file"
          accept=".csv"
          onChange={(e) => setFile(e.target.files[0])}
          ref={fileInputRef}
          style={{ margin: "10px 0" }}
        />

        <button
          type="submit"
          style={{
            padding: "10px 20px",
            background: "brown",
            color: "white",
            border: "none",
            cursor: "pointer",
            marginTop: "10px",
          }}
        >
          Submit
        </button>
      </form>
    </div>
  );
}
