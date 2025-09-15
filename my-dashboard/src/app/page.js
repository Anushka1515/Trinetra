export default function DashboardPage() {
  return (
    <div>
      <h1 style={{ fontSize: "24px", marginBottom: "20px" }}>
        Dashboard Overview
      </h1>

      <div
        style={{
          display: "grid",
          gap: "20px",
          gridTemplateColumns: "repeat(auto-fit, minmax(250px, 1fr))",
        }}
      >
        <div
          style={{
            background: "#fff",
            padding: "20px",
            borderRadius: "10px",
            boxShadow: "0 2px 5px rgba(0,0,0,0.1)",
          }}
        >
          <h2>Users</h2>
          <p>1,245 active users</p>
        </div>
        <div
          style={{
            background: "#fff",
            padding: "20px",
            borderRadius: "10px",
            boxShadow: "0 2px 5px rgba(0,0,0,0.1)",
          }}
        >
          <h2>Revenue</h2>
          <p>$56,320 this month</p>
        </div>
        <div
          style={{
            background: "#fff",
            padding: "20px",
            borderRadius: "10px",
            boxShadow: "0 2px 5px rgba(0,0,0,0.1)",
          }}
        >
          <h2>System Health</h2>
          <p>All systems operational ✅</p>
        </div>
      </div>
    </div>
  );
}
