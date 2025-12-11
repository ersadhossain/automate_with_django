"use client";
import { useEffect, useState } from "react";

export default function EmailTracking() {
  const [emails, setEmails] = useState([]);

  useEffect(() => {
    fetch(`http://127.0.0.1:8000/tracking_email/`)
      .then((res) => res.json())
      .then((result) => setEmails(result.data))
      .catch((err) => console.log(err));
  }, []);

  return (
    <div className="container">
      <h1>Email Engagement Tracking</h1>

      <table className="styled-table">
        <thead>
          <tr>
            <th>#</th>
            <th>Subject</th>
            <th>List</th>
            <th>Body</th>
            <th>Attachment</th>
            <th>Sent At</th>
            <th>Total-send</th>
            <th>Event</th>
          </tr>
        </thead>

        <tbody>
          {emails.map((email, index) => (
            <tr key={email.id}>
              <td>{index + 1}</td>
              <td>
                <a
                  href={`/tracking-email/${email.id}`}
                  style={{
                    color: "#2563eb",
                    fontWeight: "600",
                    textDecoration: "none",
                  }}
                >
                  {email.subject}
                </a>
              </td>

              <td>{email.list_name}</td>
              <td>{email.body}</td>

              <td>
                {email.attachment ? (
                  <a href={email.attachment} target="_blank">
                    Download
                  </a>
                ) : (
                  "No file"
                )}
              </td>

              <td>{email.sent_at}</td>
              <td>{email.total_sent}</td>
              <td>
                <div>{email.open_rate}% opened</div>
                <div>{email.click_rate}% click</div>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
