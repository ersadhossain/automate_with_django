import Link from "next/link";

export default function Home() {
  return (
    <main style={{ padding: 40 }}>
      <h1>Dashboard</h1>
      <ul style={{ fontSize: "20px", marginTop: "20px" }}>
        <li>
          <Link href="/export-data">Export Data</Link>
        </li>
        <li style={{ marginTop: "10px" }}>
          <Link href="/import-data">Import Data</Link>
        </li>
      </ul>
    </main>
  );
}
