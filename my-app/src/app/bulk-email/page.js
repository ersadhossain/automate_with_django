'use client'
import { useState, useEffect } from "react";

export default function BulkEmailPage() {
  const [subject, setSubject] = useState("");
  const [emailList, setEmailList] = useState("");
  const [body, setBody] = useState("");
  const [attachment, setAttachment] = useState(null);
  const [listOptions, setListOptions] = useState([]);

  // -------------------------
  // FETCH email list from backend API
  // -------------------------
  useEffect(() => {
    fetch("http://localhost:8000/send_email/")
      .then((res) => res.json())
      .then((data) => {
        setListOptions(data.email_lists);  // example: ["List1", "List2"]
      })
      .catch((err) => console.error(err));
  }, []);

  // -------------------------
  // HANDLE FORM SUBMISSION
  // -------------------------
  const handleSubmit = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append("Email-List", emailList);
    formData.append("subject", subject);
    formData.append("body", body);

    if (attachment) {
      formData.append("Attachment", attachment);
    }

    const res = await fetch("http://localhost:8000/send_email/", {
      method: "POST",
      body: formData
    });

    const data = await res.json();
    alert(data.message);
  };

  return (
    <div className="bulk-container">
      <h1 className="bulk-title">Send Emails</h1>

      <div className="bulk-card">
        <form className="bulk-form" onSubmit={handleSubmit}>

          <label>Email List</label>
          <select value={emailList} onChange={(e) => setEmailList(e.target.value)}> 
            <option value="">Select List</option>
            {listOptions.map((list, index) => (
              <option key={index} value={list}>{list}</option>
            ))}
          </select>

          <label>Email Subject</label>
          <input
            type="text"
            value={subject}
            onChange={(e) => setSubject(e.target.value)}
          />

          <label>Email Body</label>
          <textarea
            rows="6"
            value={body}
            onChange={(e) => setBody(e.target.value)}
          ></textarea>

          <label>Attachment</label>
          <input
            type="file"
            onChange={(e) => setAttachment(e.target.files[0])}
          />

          <button type="submit" className="bulk-btn">Send Email</button>
        </form>
      </div>
    </div>
  );
}
