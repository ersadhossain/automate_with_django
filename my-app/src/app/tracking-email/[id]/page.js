export default async function EmailStats(props) {
  const { params } = props; // now params will work!
  const resolved = await params; // unwrap it
  // console.log(resolved)
  const id = resolved.id;

  // const [email, setEmail] = useState(null);

  const res = await fetch(`http://127.0.0.1:8000/tracking_email/${id}/`);

  const data = await res.json();
  const result = data.data;
 

  // if (!result) return <h2>Loading...</h2>;

  return (
    <div className="container">
      <h2 className="title">Email Statistics</h2>

      <div className="stats-wrapper">
        <div className="card left-card">
          <h4>Total Emails Sent: {result.total_sent}</h4>
          <p>Sent at: {result.sent_at}</p>
          <hr />
          <div>
            <h3 className="quote">{result.subject}</h3>
          </div>
          <div>
            <small>{result.body}</small>
          </div>
          {result.attachment ? (
            <a href={result.attachment}>
              Download
            </a>
          ) : (
            "result.attachment"
          )}
        </div>

        <div className="card right-card">
          <h4>Opened: {result.open_rate}%</h4>
          <h4>Clicked: {result.click_rate}%</h4>
        </div>
      </div>
    </div>
  );
}
