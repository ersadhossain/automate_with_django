import Link from "next/link";

export default function Home() {
  const items = [
    { title: "Import Data", desc: "Imports data from CSV files to any table", color: "#cce5ff", url: "/import-data" },
    { title: "Export Data", desc: "Exports data to a CSV file", color: "#d4edda", url: "/export-data" },
    { title: "Compress Images", desc: "Compresses image files and reduces size", color: "#f5c6cb" },
    { title: "Bulk Emails", desc: "Sends bulk emails to users", color: "#f8d7da" },
    { title: "Email Tracking", desc: "Tracks email open and click rate", color: "#fff3cd" },
    { title: "Web Scraping", desc: "Scrapes websites for useful information", color: "#e2d9f3" },
  ];

  return (
    <div className="container">
      <h1 className="title">Automate The Boring Stuff With Django</h1>

      <div className="grid">
        {items.map((item, index) => (
          <Link href={item.url || "#"} key={index} className="card-link">
            <div className="card" style={{ backgroundColor: item.color }}>
              <h2>{item.title}</h2>
              <p>{item.desc}</p>
            </div>
          </Link>
        ))}
      </div>
    </div>
  );
}
